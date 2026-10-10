"""Discover course modules and content from the filesystem."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

COURSE_ROOT = Path(__file__).resolve().parent.parent
MODULE_PATTERN = re.compile(r"^(\d{2})_(.+)$")
PART_PATTERN = re.compile(r"^part_(\d{2})_(.+)$")
CHAPTER_01_TITLE = "Chapter 1: RGS analytics"


@dataclass
class ContentItem:
    title: str
    path: Path
    kind: str  # readme | theory | quiz | challenge


@dataclass
class CourseModule:
    module_id: str
    number: int
    slug: str
    title: str
    readme: ContentItem | None
    theory: list[ContentItem] = field(default_factory=list)
    quizzes: list[ContentItem] = field(default_factory=list)
    challenges: list[ContentItem] = field(default_factory=list)
    part_number: int = 1
    part_id: str = "chapter_01"
    part_title: str = CHAPTER_01_TITLE
    part_readme: Path | None = None


def _title_from_markdown(path: Path, fallback: str) -> str:
    try:
        first_line = path.read_text(encoding="utf-8").splitlines()[0].strip()
    except (OSError, IndexError):
        return fallback
    if first_line.startswith("#"):
        return first_line.lstrip("#").strip()
    return fallback


def _title_from_filename(path: Path) -> str:
    stem = re.sub(r"^\d{2}_", "", path.stem)
    return stem.replace("_", " ").title()


def _discover_quizzes(module_dir: Path) -> list[ContentItem]:
    items: list[ContentItem] = []
    quiz_dirs = [module_dir / "quizzes", module_dir / "theory"]
    seen: set[Path] = set()
    for quiz_dir in quiz_dirs:
        if not quiz_dir.is_dir():
            continue
        for path in sorted(quiz_dir.glob("*.md")):
            if "quiz" not in path.stem.lower():
                continue
            if path in seen:
                continue
            seen.add(path)
            items.append(
                ContentItem(
                    title=_title_from_filename(path),
                    path=path,
                    kind="quiz",
                )
            )
    return items


def _module_from_dir(
    module_dir: Path,
    *,
    module_id: str,
    part_number: int,
    part_id: str,
    part_title: str,
    part_readme: Path | None,
) -> CourseModule | None:
    match = MODULE_PATTERN.match(module_dir.name)
    if not match or not module_dir.is_dir():
        return None

    number = int(match.group(1))
    slug = match.group(2)
    readme_path = module_dir / "README.md"
    readme_item = None
    if readme_path.is_file():
        readme_item = ContentItem(
            title="Module Overview",
            path=readme_path,
            kind="readme",
        )
        title = _title_from_markdown(readme_path, slug.replace("_", " ").title())
    else:
        title = slug.replace("_", " ").title()

    theory_dir = module_dir / "theory"
    theory_items: list[ContentItem] = []
    if theory_dir.is_dir():
        for path in sorted(theory_dir.glob("*.md")):
            if "quiz" in path.stem.lower():
                continue
            theory_items.append(
                ContentItem(
                    title=_title_from_markdown(path, _title_from_filename(path)),
                    path=path,
                    kind="theory",
                )
            )

    challenge_dir = module_dir / "challenges"
    challenge_items: list[ContentItem] = []
    if challenge_dir.is_dir():
        for path in sorted(challenge_dir.glob("*.py")):
            challenge_items.append(
                ContentItem(
                    title=_title_from_filename(path),
                    path=path,
                    kind="challenge",
                )
            )

    return CourseModule(
        module_id=module_id,
        number=number,
        slug=slug,
        title=title,
        readme=readme_item,
        theory=theory_items,
        quizzes=_discover_quizzes(module_dir),
        challenges=challenge_items,
        part_number=part_number,
        part_id=part_id,
        part_title=part_title,
        part_readme=part_readme,
    )


def _part_title(part_dir: Path, number: int, slug: str) -> tuple[str, Path | None]:
    readme = part_dir / "README.md"
    fallback = f"Chapter {number}: {slug.replace('_', ' ')}"
    if readme.is_file():
        return _title_from_markdown(readme, fallback), readme
    return fallback, None


def discover_modules(root: Path | None = None) -> list[CourseModule]:
    root = root or COURSE_ROOT
    modules: list[CourseModule] = []

    for module_dir in sorted(root.iterdir()):
        if not module_dir.is_dir() or not MODULE_PATTERN.match(module_dir.name):
            continue
        loaded = _module_from_dir(
            module_dir,
            module_id=module_dir.name,
            part_number=1,
            part_id="chapter_01",
            part_title=CHAPTER_01_TITLE,
            part_readme=None,
        )
        if loaded is not None:
            modules.append(loaded)

    for part_dir in sorted(root.iterdir()):
        if not part_dir.is_dir():
            continue
        part_match = PART_PATTERN.match(part_dir.name)
        if not part_match:
            continue
        part_number = int(part_match.group(1))
        part_slug = part_match.group(2)
        part_title, part_readme = _part_title(part_dir, part_number, part_slug)
        for module_dir in sorted(part_dir.iterdir()):
            loaded = _module_from_dir(
                module_dir,
                module_id=f"{part_dir.name}/{module_dir.name}",
                part_number=part_number,
                part_id=part_dir.name,
                part_title=part_title,
                part_readme=part_readme,
            )
            if loaded is not None:
                modules.append(loaded)

    return modules


def group_modules(modules: list[CourseModule]) -> list[tuple[str, list[CourseModule]]]:
    """Group modules by chapter, preserving discovery order."""
    groups: list[tuple[str, list[CourseModule]]] = []
    for module in modules:
        if not groups or groups[-1][0] != module.part_title:
            groups.append((module.part_title, [module]))
        else:
            groups[-1][1].append(module)
    return groups


def read_markdown(path: Path) -> str:
    return path.read_text(encoding="utf-8")
