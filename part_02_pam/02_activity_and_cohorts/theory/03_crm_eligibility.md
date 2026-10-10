# CRM eligibility

A churn score or a bonus recommendation is not a send list. PAM already refuses some marketing.

Remove a player from a CRM population when either of these is true:

- `status` is not `active` (the shared sample uses `self_excluded` and `closed`)
- `marketing_email_allowed` is 0

Self-excluded players can still have historical rounds and deposits. Those rows stay in GGR and NGR. They leave the contact set. On the shared sample the eligible cids are 101, 102, and 104. Cid 103 is self-excluded. Cid 105 is closed.

The live communications service also checks an advertising-permission gate (OASIS for the German regime) at send time, and it fails closed. A warehouse flag is the daily approximation of that gate, not a bypass. If the flag says no, the campaign does not include the player.

Account status is a filter. It is not a feature to maximise.

## Key takeaway

Compute revenue on the full player base. Compute contact rates on the eligible base. Mixing them makes a suppressed player look like a failed campaign.
