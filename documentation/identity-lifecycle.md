# Identity Lifecycle

The lifecycle model covers joiners, movers, and leavers with one authoritative request, controlled group assignment, license allocation, and audit evidence.

| Stage | Automated action | Verification |
|---|---|---|
| Joiner | Create identity, set usage location, assign governed groups | Account enabled, manager and group state confirmed |
| Mover | Reconcile department and role-based groups | Unauthorized access removed before new access is granted |
| Leaver | Disable sign-in, revoke sessions, remove groups and licenses | Account disabled and active sessions invalidated |

The example workflow validates CSV input and emits deterministic status records. Live Graph modification requires explicit authentication, permissions, and operator confirmation.
