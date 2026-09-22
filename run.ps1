<#
.SYNOPSIS
    Launches FluffyTails Pet Adoption System on Windows.
#>
$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $ScriptDir

Write-Host "===================================================" -ForegroundColor Cyan
Write-Host "     Starting FluffyTails Pet Adoption System      " -ForegroundColor Yellow
Write-Host "===================================================" -ForegroundColor Cyan

$PythonExe = Join-Path $ScriptDir "venv\Scripts\python.exe"

if (-not (Test-Path $PythonExe)) {
    Write-Host "[*] Windows virtual environment not detected. Creating one..." -ForegroundColor Cyan
    try {
        py -3.12 -m venv venv
    } catch {
        python -m venv venv
    }
    Write-Host "[*] Installing dependencies..." -ForegroundColor Cyan
    & (Join-Path $ScriptDir "venv\Scripts\pip.exe") install -r (Join-Path $ScriptDir "requirements.txt")
}

Write-Host "[*] Starting Flask server on http://127.0.0.1:5000 ..." -ForegroundColor Green
Write-Host "[*] Default Admin: admin@gmail.com / admin123" -ForegroundColor Magenta
Write-Host "[*] Press Ctrl+C to stop." -ForegroundColor Gray
& $PythonExe (Join-Path $ScriptDir "app.py")
