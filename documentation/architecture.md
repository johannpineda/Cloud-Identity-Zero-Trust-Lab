# Architecture

The lab uses Microsoft Entra ID as the policy decision point for users, administrators, devices, and service principals. Authentication signals, device state, application sensitivity, location, and risk feed Conditional Access. Approved sessions reach Microsoft 365 and enterprise applications; denied or challenged sessions are retained in sign-in telemetry.

## Trust boundaries

| Boundary | Control |
|---|---|
| User to identity provider | Modern authentication and MFA |
| Identity to application | Conditional Access and app assignment |
| Administrator to control plane | Separate admin identity, MFA, PIM, least privilege |
| Automation to Graph | Minimal application permissions and auditable execution |
| Telemetry to operations | Sign-in logs, audit logs, alerts, and health reports |

The reference diagram is maintained as `assets/diagrams/identity-architecture.png` and can be regenerated with `script/python/render_identity_diagram.py`.
