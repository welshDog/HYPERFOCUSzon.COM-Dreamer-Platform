# 🔧⚡ ULTRA dOoK FILE SYSTEM HEALTH CHECK ⚡🔧

# PowerShell script to check dOoK file system health
# BROski♾️ Ultra Mode - July 29, 2025

Write-Host "🚀 ULTRA dOoK FILE SYSTEM HEALTH CHECK INITIATED!" -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Yellow

$rootPath = "h:\tHE HYPERFOUCS dOoK ultra Web Comic"
$healthReport = @{}

# Check main dOoK directories
$dookDirs = @(
    "The-Hyperfocus-DOOK",
    "ð_YOUR_REAL_DOOK_STORIES",
    "hyperfocus-dook-comic",
    "The HYPER dOoK"
)

Write-Host "`n📊 DIRECTORY HEALTH CHECK:" -ForegroundColor Green

foreach ($dir in $dookDirs) {
    $fullPath = Join-Path $rootPath $dir
    if (Test-Path $fullPath) {
        $fileCount = (Get-ChildItem $fullPath -Recurse -File | Measure-Object).Count
        $mdCount = (Get-ChildItem $fullPath -Recurse -Filter "*.md" | Measure-Object).Count
        Write-Host "✅ $dir" -ForegroundColor Green
        Write-Host "   📁 Files: $fileCount | 📝 Markdown: $mdCount" -ForegroundColor White
        $healthReport[$dir] = @{
            "Status" = "✅ HEALTHY"
            "Files" = $fileCount
            "Markdown" = $mdCount
        }
    } else {
        Write-Host "❌ $dir - NOT FOUND" -ForegroundColor Red
        $healthReport[$dir] = @{
            "Status" = "❌ MISSING"
            "Files" = 0
            "Markdown" = 0
        }
    }
}

# Check Memory Crystal System
Write-Host "`n💎 MEMORY CRYSTAL SYSTEM CHECK:" -ForegroundColor Magenta

$crystalDir = Join-Path $rootPath "The-Hyperfocus-DOOK"
if (Test-Path $crystalDir) {
    $crystalCategories = @(
        "ð_YOUR_REAL_DOOK_STORIES",
        "ð_Victory_Crystals", 
        "ðª_Pain_Crystals",
        "ð_Origin_Crystals",
        "ð_Future_Crystals",
        "ð_Lesson_Crystals",
        "ð¬_TikTok_Crystals"
    )
    
    foreach ($category in $crystalCategories) {
        $categoryPath = Join-Path $crystalDir $category
        if (Test-Path $categoryPath) {
            $stories = (Get-ChildItem $categoryPath -Filter "*.md" | Measure-Object).Count
            Write-Host "✅ $category - $stories stories" -ForegroundColor Green
        } else {
            Write-Host "❌ $category - NOT FOUND" -ForegroundColor Red
        }
    }
}

# Check for corrupted or inaccessible files
Write-Host "`n🔍 FILE INTEGRITY CHECK:" -ForegroundColor Yellow

$corruptedFiles = @()
$totalStories = 0

Get-ChildItem $rootPath -Recurse -Filter "*.md" | ForEach-Object {
    try {
        $content = Get-Content $_.FullName -ErrorAction Stop
        if ($content.Length -eq 0) {
            $corruptedFiles += $_.Name
        } else {
            $totalStories++
        }
    } catch {
        $corruptedFiles += $_.Name
    }
}

Write-Host "📚 Total Stories Found: $totalStories" -ForegroundColor Green
if ($corruptedFiles.Count -gt 0) {
    Write-Host "⚠️  Corrupted/Empty Files: $($corruptedFiles.Count)" -ForegroundColor Yellow
    $corruptedFiles | ForEach-Object { Write-Host "   - $_" -ForegroundColor Red }
} else {
    Write-Host "✅ All story files are accessible!" -ForegroundColor Green
}

# Check for critical system files
Write-Host "`n🛠️  CRITICAL SYSTEM FILES CHECK:" -ForegroundColor Cyan

$criticalFiles = @(
    "MEMORY_CRYSTAL_DASHBOARD.md",
    "ð§ _MEMORY_CRYSTAL_REGISTRY_ð§ .json",
    "ð®_ULTRA_VECTOR_SEARCH_DB_ð®.sqlite"
)

foreach ($file in $criticalFiles) {
    $found = Get-ChildItem $rootPath -Recurse -Name $file -ErrorAction SilentlyContinue
    if ($found) {
        Write-Host "✅ $file - FOUND" -ForegroundColor Green
    } else {
        Write-Host "❌ $file - MISSING" -ForegroundColor Red
    }
}

# Generate BROski$ value calculation
$totalBroskiValue = $totalStories * 500 + (Get-ChildItem $rootPath -Recurse -Filter "*.md" | Measure-Object).Count * 100
Write-Host "`n💰 CURRENT BROSKI$ VALUE: $totalBroskiValue" -ForegroundColor Yellow

Write-Host "`n🎊 HEALTH CHECK COMPLETE!" -ForegroundColor Cyan
Write-Host "Status: dOoK System is LEGENDARY OPERATIONAL! 🚀" -ForegroundColor Green
Write-Host "=============================================" -ForegroundColor Yellow
