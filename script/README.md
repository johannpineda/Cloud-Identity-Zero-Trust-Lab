# Automation Scripts

The scripts support repeatable validation, analysis, evidence export, and lifecycle simulation. They contain no credentials and do not modify a tenant by default.

| Script | Purpose | Safe behavior |
|---|---|---|
| `powershell/Test-IdentityHealth.ps1` | Evaluate the health-report thresholds | Local read only |
| `powershell/Invoke-IdentityLifecycle.ps1` | Validate joiner/mover/leaver requests | Supports `-WhatIf`; simulation by default |
| `powershell/Export-IdentityEvidence.ps1` | Export sanitized local evidence | Local read/write only |
| `python/validate_policies.py` | Validate Conditional Access JSON | Local read only |
| `python/analyze_signins.py` | Summarize sign-in CSV data | Local read only |
| `python/generate_incident_report.py` | Render a Markdown incident report | Writes a requested local output |
| `python/render_identity_diagram.py` | Rebuild the architecture PNG | Writes the diagram asset |

## Examples

```powershell
./powershell/Test-IdentityHealth.ps1 -InputPath ../health-reports/identity-health-report.json
./powershell/Invoke-IdentityLifecycle.ps1 -CsvPath ./examples/users.csv -WhatIf
./powershell/Export-IdentityEvidence.ps1 -SourcePath ../health-reports/identity-health-report.json -OutputPath ../evidence/automation/exported-health.json
```

```bash
python3 python/validate_policies.py ../config/conditional-access
python3 python/analyze_signins.py examples/signins.csv
python3 python/generate_incident_report.py examples/incident-example.json --output /tmp/identity-incident.md
```

Live Microsoft Graph changes require an authenticated session, the minimum approved permissions, removal of simulation mode, and explicit operator confirmation. See `config/graph/required-permissions.md`.
