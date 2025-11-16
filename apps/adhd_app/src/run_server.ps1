# PowerShell script to run ADHD Assistant API Server

Write-Host "🚀 Starting ADHD Assistant API Server..." -ForegroundColor Green

# Set PYTHONPATH to workspace root
$workspaceRoot = (Get-Item -Path "..\..\..").FullName
$env:PYTHONPATH = $workspaceRoot

Write-Host "PYTHONPATH set to: $env:PYTHONPATH" -ForegroundColor Cyan

# Run the Flask server
python api_server.py
