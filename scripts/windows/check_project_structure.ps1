param(
    [int]$Port = 8765
)

$ErrorActionPreference = 'Stop'
$base = "http://127.0.0.1:$Port"
$fail = $false

try {
    $health = Invoke-RestMethod -Uri "$base/healthz" -Method Get
    if (-not ($health.ok -eq $true)) { $fail = $true }
}
catch {
    $fail = $true
}

try {
    $tree = Invoke-RestMethod -Uri "$base/api/project-tree" -Method Get
    if (-not $tree.name -or -not $tree.type) { $fail = $true }
}
catch {
    $fail = $true
}

try {
    $page = Invoke-WebRequest -UseBasicParsing -Uri "$base/project-structure/" -Method Get
    if ($page.StatusCode -ne 200 -or $page.Content -notmatch 'OpenScript Agent Lab') { $fail = $true }
}
catch {
    $fail = $true
}

if ($fail) {
    Write-Host 'FAIL'
    exit 1
}

Write-Host 'PASS'
