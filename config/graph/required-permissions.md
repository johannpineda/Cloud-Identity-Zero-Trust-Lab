# Microsoft Graph Permissions

| Workflow | Delegated permission | Rationale |
|---|---|---|
| Identity health | `Directory.Read.All`, `AuditLog.Read.All` | Read directory posture and sign-in/audit telemetry |
| Lifecycle validation | `User.Read.All`, `Group.Read.All` | Compare requested and current state |
| Approved lifecycle change | `User.ReadWrite.All`, `GroupMember.ReadWrite.All` | Explicitly create/update identities and memberships |

Write permissions are not required for policy validation or evidence analysis. Production use should prefer managed identities or certificate credentials, with admin consent and credential rotation governed separately.
