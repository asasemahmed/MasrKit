param(
  [switch]$All,
  [string[]]$Skill,
  [ValidateSet('codex','claude','cursor','gemini')][string]$Target,
  [string]$Dest,
  [switch]$DryRun
)
$arguments = @()
if ($All) { $arguments += '--all' }
foreach ($name in $Skill) { $arguments += @('--skill', $name) }
if ($Target) { $arguments += @('--target', $Target) }
if ($Dest) { $arguments += @('--dest', $Dest) }
if ($DryRun) { $arguments += '--dry-run' }
python (Join-Path $PSScriptRoot 'install.py') @arguments
exit $LASTEXITCODE
