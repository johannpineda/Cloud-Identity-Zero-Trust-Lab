# RBAC and Privileged Identity Management

Roles map to job functions and use the narrowest available permission set. Global Administrator is reserved for emergency recovery; routine work uses purpose-built roles.

| Function | Role | Assignment model |
|---|---|---|
| User and group administration | User Administrator | Eligible, 4-hour maximum |
| Authentication support | Authentication Administrator | Eligible, 2-hour maximum |
| Conditional Access | Conditional Access Administrator | Eligible, approval required |
| Security investigation | Security Reader | Group-based active assignment |
| Emergency recovery | Global Administrator | Two monitored emergency identities |

Activation requires MFA, justification, expiration, and audit logging. Quarterly reviews remove unused eligibility.
