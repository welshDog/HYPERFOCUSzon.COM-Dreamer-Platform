# Test HyperFocus Zone AI Assistant
# Verify all endpoints are working correctly

Write-Host "🧪 TESTING HYPERFOCUS ZONE AI ASSISTANT 🧪" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Yellow

$baseUrl = "http://localhost:8888"
$testsPassed = 0
$totalTests = 6

function Test-Endpoint {
    param(
        [string]$Name,
        [string]$Url,
        [string]$Method = "GET",
        [hashtable]$Body = $null
    )

    Write-Host "`n$Name" -ForegroundColor Yellow
    Write-Host ("=" * $Name.Length) -ForegroundColor Gray

    try {
        if ($Method -eq "POST" -and $Body) {
            $jsonBody = $Body | ConvertTo-Json
            $response = Invoke-RestMethod -Uri $Url -Method $Method -Body $jsonBody -ContentType "application/json" -TimeoutSec 15
        } else {
            $response = Invoke-RestMethod -Uri $Url -Method $Method -TimeoutSec 15
        }

        Write-Host "✅ SUCCESS" -ForegroundColor Green

        # Pretty print response
        if ($response -is [PSCustomObject]) {
            $response | Format-List | Out-String | Write-Host -ForegroundColor Cyan
        } else {
            Write-Host $response -ForegroundColor Cyan
        }

        return $true
    } catch {
        Write-Host "❌ FAILED: $($_.Exception.Message)" -ForegroundColor Red
        return $false
    }
}

# Test 1: Health Check
if (Test-Endpoint "1. Health Check" "$baseUrl/health") { $testsPassed++ }

# Test 2: Welcome Page
if (Test-Endpoint "2. Welcome Page" "$baseUrl/") { $testsPassed++ }

# Test 3: Techniques List
if (Test-Endpoint "3. Techniques List" "$baseUrl/techniques") { $testsPassed++ }

# Test 4: Specific Technique
if (Test-Endpoint "4. Modified Pomodoro Technique" "$baseUrl/techniques/1") { $testsPassed++ }

# Test 5: ADHD Chat Test
$adhdMessage = @{ message = "I have ADHD and need help focusing on this boring task" }
if (Test-Endpoint "5. ADHD Chat Test" "$baseUrl/chat" "POST" $adhdMessage) { $testsPassed++ }

# Test 6: Autism Support Test
$autismMessage = @{ message = "I am autistic and feeling overwhelmed by sensory input" }
if (Test-Endpoint "6. Autism Support Test" "$baseUrl/chat" "POST" $autismMessage) { $testsPassed++ }

# Summary
Write-Host "`n" ("=" * 50) -ForegroundColor Yellow
Write-Host "TEST SUMMARY" -ForegroundColor Cyan
Write-Host ("=" * 50) -ForegroundColor Yellow

Write-Host "Tests Passed: $testsPassed / $totalTests" -ForegroundColor $(if ($testsPassed -eq $totalTests) { "Green" } else { "Yellow" })

if ($testsPassed -eq $totalTests) {
    Write-Host "🎉 ALL TESTS PASSED!" -ForegroundColor Green
    Write-Host "Your HyperFocus Zone AI Assistant is ready to help neurodivergent individuals! 🚀" -ForegroundColor Cyan
} elseif ($testsPassed -gt 0) {
    Write-Host "⚠️ Some tests passed, but there may be issues." -ForegroundColor Yellow
    Write-Host "Check the logs with: docker-compose logs hyperfocus-ai" -ForegroundColor Gray
} else {
    Write-Host "❌ All tests failed. Service may not be running." -ForegroundColor Red
    Write-Host "Try: docker-compose ps" -ForegroundColor Gray
    Write-Host "Or check logs: docker-compose logs" -ForegroundColor Gray
}

Write-Host "`n🌐 ACCESS URLS:" -ForegroundColor Cyan
Write-Host "Local: http://localhost:8888" -ForegroundColor White
Write-Host "Server: http://212.227.127.144:8888" -ForegroundColor White
Write-Host "SSL (when configured): https://support.hyperfocuszone.com" -ForegroundColor White

Write-Host "`n💎 EMPIRE STATUS: LEGENDARY! 💎" -ForegroundColor Magenta
