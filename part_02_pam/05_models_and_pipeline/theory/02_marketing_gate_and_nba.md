# The marketing gate and next best action

Next best action becomes concrete once offerings exist. The action is a plan the catalogue already has:

- `first_deposit` — the player has no approved deposit
- `no_deposit` — credit that does not require a deposit
- `retention_bonus` — a player who has deposited and gone quiet
- free spins — a game-level grant, still a bonus definition

The action is not a send. `crm_eligible` has to be 1, and the communications service will still apply the advertising-permission check at send time. A model that ranks self-excluded players for `retention_bonus` is a defect, even if their GGR was high.

Solitics is the CRM already wired into the backoffice. The analytics output is a predictions table (cid, brand, score, recommended plan, eligible flag) that a campaign can read. It is not a second email sender.

Game recommendations from Chapter 1 do not change source: they still read play history on `game_rounds`. Promotions are the new action type. Do not recommend a game by looking only at bonus claims.

## Key takeaway

Map the action to a real bonus plan. Drop anyone who fails the marketing gate before the list leaves the warehouse.
