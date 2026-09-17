# CA002 Workforce MFA Validation

| Test | Expected | Result |
|---|---|---|
| Managed Windows device, modern client | MFA required, access granted after success | Passed |
| Unmanaged browser | MFA required | Passed |
| Legacy authentication | Access blocked | Passed |
| Emergency-access identity | Policy excluded, monitoring event created | Passed |
| Lifecycle automation identity | Explicit workload exclusion | Passed |
| User outside target group | Policy not applied | Passed |

Report-only evaluation was reviewed before enablement. Enabled-policy results matched the predicted outcomes and no rollback criteria were triggered.
