# INC-2026-011 — Risky Sign-In Investigation

| Field | Value |
|---|---|
| Severity | Medium |
| Status | Closed — contained, no compromise found |
| Detected | 2026-08-24 02:14 UTC |
| Closed | 2026-08-24 03:06 UTC |

## Summary

Entra ID flagged an unfamiliar sign-in for `alex.p@contoso.example`. Conditional Access required MFA and prevented a session from being issued after the challenge was not completed.

## Investigation

Sign-in telemetry showed an unfamiliar IP and device with no successful MFA claim. No mailbox, application-consent, directory, or privileged-role activity followed the attempt. The user confirmed no travel or expected sign-in.

## Response and outcome

Active sessions were revoked, the password was reset, registered methods were reviewed, and the source indicator was retained for monitoring. Subsequent sign-ins originated from a compliant managed device and satisfied MFA. No evidence of account compromise was identified.

## Improvement

The event confirmed that the risk and MFA controls operated as designed. The incident pattern was added to the investigation runbook and access-review evidence set.
