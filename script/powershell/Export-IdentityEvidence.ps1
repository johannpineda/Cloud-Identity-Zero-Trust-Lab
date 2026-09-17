[CmdletBinding()]
param(
    [Parameter(Mandatory)][ValidateScript({ Test-Path $_ -PathType Leaf })][string]$SourcePath,
    [Parameter(Mandatory)][string]$OutputPath
)

$data = Get-Content -LiteralPath $SourcePath -Raw | ConvertFrom-Json
$evidence = [ordered]@{
    generatedAt = (Get-Date).ToUniversalTime().ToString('o')
    source = (Split-Path -Leaf $SourcePath)
    status = $data.status
    metrics = $data.metrics
    controls = $data.controls
}
$parent = Split-Path -Parent $OutputPath
if ($parent -and -not (Test-Path $parent)) { New-Item -ItemType Directory -Path $parent | Out-Null }
$evidence | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $OutputPath -Encoding utf8
Write-Host "Evidence exported to $OutputPath"
