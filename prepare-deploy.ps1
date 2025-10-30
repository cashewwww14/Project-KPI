# Deploy KPI Dashboard - Preparation Script

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  KPI Dashboard Deployment Preparation" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check current directory
Write-Host "[*] Current directory: $PWD" -ForegroundColor Yellow
Write-Host ""

# Step 1: Check required files
Write-Host "[1] Checking required files..." -ForegroundColor Green
$requiredFiles = @(
    "dashboard_backend.py",
    "dashboard.html",
    "dashboard_4g.html",
    "requirements_dashboard.txt",
    "runtime.txt",
    "Procfile",
    ".gitignore"
)

$allFilesExist = $true
foreach ($file in $requiredFiles) {
    if (Test-Path $file) {
        Write-Host "    [OK] $file" -ForegroundColor Green
    } else {
        Write-Host "    [MISSING] $file" -ForegroundColor Red
        $allFilesExist = $false
    }
}

if (-not $allFilesExist) {
    Write-Host ""
    Write-Host "[ERROR] Some required files are missing!" -ForegroundColor Red
    exit 1
}

Write-Host ""

# Step 2: Check Git status
Write-Host "[2] Checking Git status..." -ForegroundColor Green

$gitRemote = $null
if (Test-Path ".git") {
    Write-Host "    [OK] Git repository initialized" -ForegroundColor Green
    
    $gitStatus = git status --porcelain 2>$null
    if ($gitStatus) {
        Write-Host "    [INFO] You have uncommitted changes" -ForegroundColor Yellow
    } else {
        Write-Host "    [OK] Working directory clean" -ForegroundColor Green
    }
    
    $gitRemote = git remote -v 2>$null
    if ($gitRemote) {
        Write-Host "    [OK] Git remote configured" -ForegroundColor Green
    } else {
        Write-Host "    [INFO] No Git remote configured" -ForegroundColor Yellow
    }
} else {
    Write-Host "    [INFO] Git not initialized" -ForegroundColor Yellow
}

Write-Host ""

# Step 3: Database credentials
Write-Host "[3] Database Configuration" -ForegroundColor Green
Write-Host ""

$backendContent = Get-Content "dashboard_backend.py" -Raw
if ($backendContent -match "'host':\s*os\.getenv\('DB_HOST',\s*'([^']+)'") {
    Write-Host "    Host: $($matches[1])" -ForegroundColor White
}
if ($backendContent -match "'port':\s*os\.getenv\('DB_PORT',\s*'([^']+)'") {
    Write-Host "    Port: $($matches[1])" -ForegroundColor White
}
if ($backendContent -match "'dbname':\s*os\.getenv\('DB_NAME',\s*'([^']+)'") {
    Write-Host "    Database: $($matches[1])" -ForegroundColor White
}
if ($backendContent -match "'user':\s*os\.getenv\('DB_USER',\s*'([^']+)'") {
    Write-Host "    User: $($matches[1])" -ForegroundColor White
}

Write-Host ""
Write-Host "    [NOTE] Remember these for Render!" -ForegroundColor Yellow
Write-Host ""

# Step 4: Summary
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  PREPARATION SUMMARY" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

if ($allFilesExist) {
    Write-Host "[OK] All required files exist" -ForegroundColor Green
}

if (Test-Path ".git") {
    Write-Host "[OK] Git initialized" -ForegroundColor Green
} else {
    Write-Host "[TODO] Git not initialized" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  NEXT STEPS" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

if (-not (Test-Path ".git")) {
    Write-Host "[1] Initialize Git:" -ForegroundColor Yellow
    Write-Host "    git init" -ForegroundColor White
    Write-Host "    git branch -M main" -ForegroundColor White
    Write-Host ""
}

if (Test-Path ".git") {
    $gitStatus = git status --porcelain 2>$null
    if ($gitStatus) {
        Write-Host "[2] Commit changes:" -ForegroundColor Yellow
        Write-Host "    git add ." -ForegroundColor White
        Write-Host "    git commit -m 'Initial commit: KPI Dashboard'" -ForegroundColor White
        Write-Host ""
    }
}

if (-not $gitRemote) {
    Write-Host "[3] Add GitHub remote:" -ForegroundColor Yellow
    Write-Host "    - Create repo: https://github.com/new" -ForegroundColor White
    Write-Host "    - git remote add origin https://github.com/cashewwww14/kpi-dashboard.git" -ForegroundColor White
    Write-Host ""
    
    Write-Host "[4] Push to GitHub:" -ForegroundColor Yellow
    Write-Host "    git push -u origin main" -ForegroundColor White
    Write-Host ""
}

Write-Host "[5] When database online:" -ForegroundColor Yellow
Write-Host "    a. Deploy backend to Render" -ForegroundColor White
Write-Host "    b. Update HTML with backend URL" -ForegroundColor White
Write-Host "    c. Deploy frontend to Netlify" -ForegroundColor White
Write-Host ""

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  DOCUMENTATION" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Quick Start:  QUICKSTART.md" -ForegroundColor White
Write-Host "Full Guide:   DEPLOYMENT_GUIDE.md" -ForegroundColor White
Write-Host "Checklist:    DEPLOYMENT_CHECKLIST.md" -ForegroundColor White
Write-Host ""

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Ready to Deploy!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
