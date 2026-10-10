"""Copy course markdown into flet_app/assets/course for offline Android builds."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

FLET_APP_DIR = Path(__file__).resolve().parent
REPO_ROOT = FLET_APP_DIR.parent
COURSE_NAV_SRC = REPO_ROOT / "course_nav"
COURSE_NAV_DEST = FLET_APP_DIR / "course_nav"
ASSETS_COURSE = FLET_APP_DIR / "assets" / "course"
MODULE_PATTERN = re.compile(r"^(\d{2})_.+$")
PART_PATTERN = re.compile(r"^part_(\d{2})_.+$")


def _copy_markdown(src: Path, dst: Path) -> None:
    if src.is_file() and src.suffix.lower() == ".md":
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)


def _sync_course_nav() -> None:
    if COURSE_NAV_DEST.exists():
        shutil.rmtree(COURSE_NAV_DEST)
    shutil.copytree(COURSE_NAV_SRC, COURSE_NAV_DEST)


def _copy_module_markdown(module_dir: Path, dest_module: Path) -> None:
    readme = module_dir / "README.md"
    if readme.is_file():
        _copy_markdown(readme, dest_module / "README.md")

    theory_dir = module_dir / "theory"
    if theory_dir.is_dir():
        for path in sorted(theory_dir.glob("*.md")):
            _copy_markdown(path, dest_module / "theory" / path.name)

    quizzes_dir = module_dir / "quizzes"
    if quizzes_dir.is_dir():
        for path in sorted(quizzes_dir.glob("*.md")):
            _copy_markdown(path, dest_module / "quizzes" / path.name)


def prepare_assets() -> None:
    _sync_course_nav()

    if ASSETS_COURSE.exists():
        shutil.rmtree(ASSETS_COURSE)
    ASSETS_COURSE.mkdir(parents=True)

    root_readme = REPO_ROOT / "README.md"
    if root_readme.is_file():
        _copy_markdown(root_readme, ASSETS_COURSE / "README.md")

    for module_dir in sorted(REPO_ROOT.iterdir()):
        if not module_dir.is_dir() or not MODULE_PATTERN.match(module_dir.name):
            continue
        rel = module_dir.relative_to(REPO_ROOT)
        _copy_module_markdown(module_dir, ASSETS_COURSE / rel)

    for part_dir in sorted(REPO_ROOT.iterdir()):
        if not part_dir.is_dir() or not PART_PATTERN.match(part_dir.name):
            continue
        part_readme = part_dir / "README.md"
        if part_readme.is_file():
            _copy_markdown(part_readme, ASSETS_COURSE / part_dir.name / "README.md")
        for module_dir in sorted(part_dir.iterdir()):
            if not module_dir.is_dir() or not MODULE_PATTERN.match(module_dir.name):
                continue
            dest = ASSETS_COURSE / part_dir.name / module_dir.name
            _copy_module_markdown(module_dir, dest)

    print(f"Course assets prepared at {ASSETS_COURSE}")
    print(f"Shared modules copied to {COURSE_NAV_DEST}")


if __name__ == "__main__":
    prepare_assets()
