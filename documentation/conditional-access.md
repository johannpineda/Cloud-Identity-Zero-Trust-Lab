# Conditional Access

Policies are introduced in report-only mode, validated against test personas, reviewed for service dependencies, and then enabled through change control.

| Policy | Scope | Control |
|---|---|---|
| CA001 | Administrative roles | Require MFA every sign-in |
| CA002 | Workforce users | Require MFA for cloud applications |
| CA003 | All users | Block legacy authentication |
| CA004 | Protected applications | Require compliant device |
| CA005 | Elevated sign-in risk | Require MFA or block |

Two monitored emergency-access identities are excluded from policies that could lock out the tenant. Exclusions are documented, tested, and alerted on—not treated as routine administrator accounts.
