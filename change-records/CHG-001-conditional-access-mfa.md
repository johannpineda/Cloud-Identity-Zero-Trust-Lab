# CHG-001 — Enforce MFA with Conditional Access

| Field | Value |
|---|---|
| Status | Implemented and validated |
| Risk | Medium |
| Window | 2026-08-18 18:00–19:00 UTC |
| Owner | Cloud Identity Administration |

## Change

Enable CA002 for workforce identities after report-only validation. Exclude two monitored emergency-access identities and the lifecycle automation workload identity.

## Validation

Test users completed modern authentication with MFA; legacy authentication was blocked; excluded emergency access remained available and generated monitoring events. No unexpected service impact was observed.

## Backout

Disable CA002, preserve sign-in evidence, notify stakeholders, and return the policy to report-only while the failed condition is investigated. Backout was not required.
