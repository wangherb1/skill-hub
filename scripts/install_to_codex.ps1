param(
    [string]$CodexSkillsRoot = "C:\Users\wang_\.codex\skills"
)

$ErrorActionPreference = "Stop"

$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$SkillsRoot = Join-Path $RepoRoot "skills"

if (-not (Test-Path $SkillsRoot)) {
    throw "Missing skills directory: $SkillsRoot"
}

New-Item -ItemType Directory -Force -Path $CodexSkillsRoot | Out-Null

$skills = Get-ChildItem -Path $SkillsRoot -Directory | Sort-Object Name
foreach ($skill in $skills) {
    $sourceSkill = $skill.FullName
    $sourceSkillFile = Join-Path $sourceSkill "SKILL.md"
    if (-not (Test-Path $sourceSkillFile)) {
        throw "Missing SKILL.md in $sourceSkill"
    }

    $destSkill = Join-Path $CodexSkillsRoot $skill.Name
    if (Test-Path $destSkill) {
        Remove-Item -LiteralPath $destSkill -Recurse -Force
    }

    Copy-Item -LiteralPath $sourceSkill -Destination $destSkill -Recurse -Force
    Write-Host "Installed $($skill.Name) -> $destSkill"
}

Write-Host "Done. Restart or reload Codex to discover updated skills."
