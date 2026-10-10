# From an RGS stream to PAM

Chapter 1 starts from a gameplay event: `player_id`, `session_id`, `game_id`, `round_id`, `bet_amount`, `win_amount`. That grain is still the right grain for GGR. The platform that holds it is different.

PAM is a NestJS monorepo. Domain services talk over NATS and store MySQL, one schema per service. The HTTP edge is `service-gateway`. Casino providers, including Diger RGS, call that edge on every bet and win. This is a **seamless wallet**: PAM, not the game server, is the source of truth for the player's balance.

Two facts follow for analytics:

1. A provider round is not, by itself, the money record. `service-casino` stores `game_sessions` and `game_rounds`. `service-wallet` moves the money and writes `transactions`.
2. Diger RGS is one adapter. Pragmatic, Ezugi (live games fronted for Evolution, NetEnt, and Red Tiger), and O2A are others. A warehouse built only from one provider's feed misses the rest of the catalogue.

Redis pub/sub carries events such as balance updates. Delivery is at-most-once. Use it for product push, not as the feed that fills the warehouse. Replicate the MySQL facts.

## Key takeaway

Chapter 1's GGR formula does not change. The durable copy of a round and of the cash behind it now lives in PAM tables, not in an external RGS dump.
