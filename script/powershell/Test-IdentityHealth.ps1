[CmdletBinding()]
param(
    [Parameter(Mandatory)]
    [ValidateScript({ Test-Path $_ -PathType Leaf })]
    [string]$InputPath
)

$report = Get-Content -LiteralPath $InputPath -Raw | ConvertFrom-Json
$checks = @(
    [pscustomobject]@{ Name = 'MFA registration'; Passed = $report.metrics.mfaRegistrationPercent -ge 95; Value = $report.metrics.mfaRegistrationPercent }
    [pscustomobject]@{ Name = 'Conditional Access success'; Passed = $report.metrics.conditionalAccessSuccessPercent -ge 99; Value = $report.metrics.conditionalAccessSuccessPercent }
    [pscustomobject]@{ Name = 'Compliant devices'; Passed = $report.metrics.compliantDevicesPercent -ge 90; Value = $report.metrics.compliantDevicesPercent }
    [pscustomobject]@{ Name = 'Permanent Global Administrators'; Passed = $report.metrics.permanentGlobalAdministrators -eq 0; Value = $report.metrics.permanentGlobalAdministrators }
    [pscustomobject]@{ Name = 'Risky users'; Passed = $report.metrics.riskyUsers -eq 0; Value = $report.metrics.riskyUsers }
)

$checks | Format-Table Name, Passed, Value -AutoSize
if ($checks.Passed -contains $false) { exit 1 }
Write-Host 'Overall status: HEALTHY' -ForegroundColor Green
