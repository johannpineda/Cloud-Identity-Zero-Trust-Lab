[CmdletBinding(SupportsShouldProcess, ConfirmImpact = 'High')]
param(
    [Parameter(Mandatory)]
    [ValidateScript({ Test-Path $_ -PathType Leaf })]
    [string]$CsvPath,
    [switch]$Apply
)

$required = 'UserPrincipalName', 'DisplayName', 'Action', 'Department', 'Group'
$records = Import-Csv -LiteralPath $CsvPath
foreach ($row in $records) {
    foreach ($field in $required) {
        if ([string]::IsNullOrWhiteSpace($row.$field)) { throw "Missing $field for a lifecycle record." }
    }
    if ($row.Action -notin 'Joiner', 'Mover', 'Leaver') { throw "Unsupported action: $($row.Action)" }

    $summary = "$($row.Action): $($row.UserPrincipalName) [$($row.Group)]"
    if (-not $Apply) {
        [pscustomobject]@{ Identity = $row.UserPrincipalName; Action = $row.Action; Result = 'Validated'; Mode = 'Simulation' }
        continue
    }

    if ($PSCmdlet.ShouldProcess($row.UserPrincipalName, $summary)) {
        throw 'Live Graph mutation is intentionally not embedded. Connect using approved Graph authentication and implement the reviewed tenant-specific operation.'
    }
}
