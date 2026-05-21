param(
    [Alias('Host')]
    [string]$ListenHost = '127.0.0.1',
    [int]$Port = 8765,
    [string]$Root
)

$ErrorActionPreference = 'Stop'

if (-not $Root) {
    $Root = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
}
else {
    $Root = (Resolve-Path $Root).Path
}

$bundledPython = Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
$pythonPath = $null

if (Test-Path $bundledPython) {
    $pythonPath = $bundledPython
}
else {
    $pythonCandidates = @(
        (Get-Command python -ErrorAction SilentlyContinue),
        (Get-Command py -ErrorAction SilentlyContinue)
    ) | Where-Object { $_ }

    foreach ($candidate in $pythonCandidates) {
        if ($candidate.Source -and $candidate.Source -notmatch '\\WindowsApps\\') {
            $pythonPath = $candidate.Source
            break
        }
    }
}

if (-not $pythonPath) {
    throw 'python or py was not found'
}

& $pythonPath -m project_structure.server --host $ListenHost --port $Port --root $Root
