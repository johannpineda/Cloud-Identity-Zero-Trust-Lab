# Monitoring and Troubleshooting

## Monitored telemetry

- Interactive and non-interactive sign-in logs
- Directory audit events and role changes
- Conditional Access outcomes and failure reasons
- Risk detections, application consent, and service-principal changes
- Lifecycle automation output and policy validation results

## Investigation sequence

1. Confirm the affected identity, time window, application, and correlation ID.
2. Review authentication details, Conditional Access evaluation, device state, IP, location, and risk.
3. Correlate directory changes and privileged activity.
4. Contain by revoking sessions, resetting credentials, disabling the identity, or blocking the application as warranted.
5. Document root cause, evidence, remediation, and validation.

Common access failures are resolved by reading the policy evaluation details instead of weakening the policy globally.
