# Frontend Deployment Script untuk GitHub Pages
# Script ini akan push frontend files ke GitHub

Write-Host "===========================================" -ForegroundColor Cyan
Write-Host "  KPI Dashboard - Frontend Deployment" -ForegroundColor Cyan
Write-Host "===========================================" -ForegroundColor Cyan
Write-Host ""

# Check if git is installed
Write-Host "Checking Git installation..." -ForegroundColor Yellow
$gitInstalled = Get-Command git -ErrorAction SilentlyContinue
if (-not $gitInstalled) {
    Write-Host "ERROR: Git is not installed!" -ForegroundColor Red
    Write-Host "Please install Git from: https://git-scm.com/download/win" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host "✓ Git is installed" -ForegroundColor Green
Write-Host ""

# Check if we're in a git repository
Write-Host "Checking Git repository..." -ForegroundColor Yellow
$isGitRepo = Test-Path ".git"
if (-not $isGitRepo) {
    Write-Host "ERROR: Not a Git repository!" -ForegroundColor Red
    Write-Host "Please initialize Git first or run this script from the correct directory." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host "✓ Git repository detected" -ForegroundColor Green
Write-Host ""

# Check if files exist
Write-Host "Checking required files..." -ForegroundColor Yellow
$requiredFiles = @("index.html", "dashboard.html", "dashboard_4g.html")
$missingFiles = @()

foreach ($file in $requiredFiles) {
    if (-not (Test-Path $file)) {
        $missingFiles += $file
    }
}

if ($missingFiles.Count -gt 0) {
    Write-Host "ERROR: Missing files:" -ForegroundColor Red
    foreach ($file in $missingFiles) {
        Write-Host "  - $file" -ForegroundColor Red
    }
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host "✓ All required files found" -ForegroundColor Green
Write-Host ""

# Show current branch
Write-Host "Current Git branch:" -ForegroundColor Yellow
git branch --show-current
Write-Host ""

# Add files to git
Write-Host "Adding files to Git..." -ForegroundColor Yellow
git add index.html dashboard.html dashboard_4g.html

$gitStatus = git status --short
if ($gitStatus) {
    Write-Host "Files to be committed:" -ForegroundColor Cyan
    git status --short
} else {
    Write-Host "No changes to commit." -ForegroundColor Yellow
    Write-Host "Files are already up to date." -ForegroundColor Green
    Read-Host "Press Enter to exit"
    exit 0
}
Write-Host ""

# Commit changes
Write-Host "Committing changes..." -ForegroundColor Yellow
$commitMessage = "Deploy frontend: Update backend URL and add landing page"
git commit -m $commitMessage

if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to commit changes!" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host "✓ Changes committed" -ForegroundColor Green
Write-Host ""

# Push to GitHub
Write-Host "Pushing to GitHub..." -ForegroundColor Yellow
Write-Host "This may take a moment..." -ForegroundColor Cyan

git push origin main

if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to push to GitHub!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Possible issues:" -ForegroundColor Yellow
    Write-Host "  1. No internet connection" -ForegroundColor Yellow
    Write-Host "  2. Authentication required" -ForegroundColor Yellow
    Write-Host "  3. Branch name is different (try 'master' instead of 'main')" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "You can try pushing manually:" -ForegroundColor Cyan
    Write-Host "  git push origin main" -ForegroundColor White
    Write-Host "  or" -ForegroundColor White
    Write-Host "  git push origin master" -ForegroundColor White
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "===========================================" -ForegroundColor Green
Write-Host "  ✓ SUCCESS! Frontend Pushed to GitHub" -ForegroundColor Green
Write-Host "===========================================" -ForegroundColor Green
Write-Host ""

# Show next steps
Write-Host "NEXT STEPS:" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Go to your GitHub repository:" -ForegroundColor Yellow
Write-Host "   https://github.com/cashewwww14/Project-KPI" -ForegroundColor White
Write-Host ""
Write-Host "2. Click 'Settings' tab" -ForegroundColor Yellow
Write-Host ""
Write-Host "3. In sidebar, click 'Pages'" -ForegroundColor Yellow
Write-Host ""
Write-Host "4. Under 'Source':" -ForegroundColor Yellow
Write-Host "   - Branch: Select 'main'" -ForegroundColor White
Write-Host "   - Folder: Select '/ (root)'" -ForegroundColor White
Write-Host "   - Click 'Save'" -ForegroundColor White
Write-Host ""
Write-Host "5. Wait 1-2 minutes for deployment" -ForegroundColor Yellow
Write-Host ""
Write-Host "6. Your dashboard will be available at:" -ForegroundColor Yellow
Write-Host "   https://cashewwww14.github.io/Project-KPI/" -ForegroundColor Green
Write-Host ""
Write-Host "===========================================" -ForegroundColor Cyan

Read-Host "Press Enter to exit"
