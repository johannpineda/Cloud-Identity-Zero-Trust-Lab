# Zero Trust Model

## Verify explicitly

Access decisions evaluate identity, MFA status, device compliance, application, location, and sign-in risk. Legacy authentication is blocked because it cannot satisfy modern controls.

## Use least privilege

Administrative roles are separated from daily-use identities. Privileged roles are eligible rather than permanent, activated for a limited duration, and reviewed on a recurring schedule.

## Assume breach

Risk signals, audit events, application consent, and privileged changes are monitored. Emergency access is tightly scoped, excluded from dependency-causing policies, and protected by alerting and review.

| Signal | Response |
|---|---|
| Unfamiliar or risky sign-in | Require stronger authentication or block |
| Noncompliant device | Block protected applications |
| Privileged role request | Require approval, MFA, justification, and expiration |
| Suspicious application consent | Revoke consent, disable principal, investigate activity |
