# Offline installer for the market-research skill (Windows PowerShell).
# Copies the skill (SKILL.md + scripts + schemas + templates + knowledge)
# into an agent's skills directory.
#
# Usage:
#   .\install.ps1                          # -> $HOME\.claude\skills\market-research
#   .\install.ps1 -Dest "$HOME\.config\opencode\skills"

param([string]$Dest)

$ErrorActionPreference = 'Stop'
$Src = Split-Path -Parent $MyInvocation.MyCommand.Path
$Name = 'market-research'
if (-not $Dest) { $Dest = Join-Path $HOME '.claude\skills' }
$Target = Join-Path $Dest $Name

if (Test-Path -LiteralPath $Target) { Remove-Item -Recurse -Force -LiteralPath $Target }
New-Item -ItemType Directory -Force -Path $Target | Out-Null

foreach ($f in 'SKILL.md', 'README.md', 'INSTALL.md', 'LICENSE', 'requirements.txt') {
    Copy-Item -LiteralPath (Join-Path $Src $f) -Destination $Target
}
foreach ($d in 'scripts', 'schemas', 'templates', 'knowledge') {
    Copy-Item -LiteralPath (Join-Path $Src $d) -Destination $Target -Recurse
}

Write-Host "Installed market-research -> $Target"
