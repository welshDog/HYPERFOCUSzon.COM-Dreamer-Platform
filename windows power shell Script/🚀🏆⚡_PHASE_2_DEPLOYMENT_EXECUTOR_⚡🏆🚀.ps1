# 🚀🏆⚡ PHASE 2 DEPLOYMENT EXECUTOR ⚡🏆🚀
# Execute the ubuntu1_deployment_commands.sh script on the remote server

Write-Host "🚀🏆⚡ PHASE 2 DEPLOYMENT EXECUTOR ⚡🏆🚀" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# Read the deployment script
$deploymentScript = Get-Content "ubuntu1_deployment_commands.sh" -Raw

Write-Host "📋 DEPLOYMENT SCRIPT LOADED:" -ForegroundColor Green
Write-Host "   Size: $($deploymentScript.Length) characters" -ForegroundColor Yellow
Write-Host "   Target: ubuntu-1 (100.71.69.16)" -ForegroundColor Yellow
Write-Host ""

# Test connectivity first
Write-Host "🔍 Testing connectivity to ubuntu-1..." -ForegroundColor Cyan
$connection = Test-NetConnection -ComputerName 100.71.69.16 -Port 22 -InformationLevel Quiet

if ($connection.TcpTestSucceeded) {
    Write-Host "✅ CONNECTION SUCCESS!" -ForegroundColor Green
    Write-Host ""
    
    Write-Host "🎯 DEPLOYMENT EXECUTION OPTIONS:" -ForegroundColor Magenta
    Write-Host ""
    Write-Host "OPTION 1 - Manual SSH Execution (RECOMMENDED):" -ForegroundColor Yellow
    Write-Host "   1. Open new terminal/command prompt" -ForegroundColor White
    Write-Host "   2. Run: ssh root@100.71.69.16" -ForegroundColor White
    Write-Host "   3. Copy and paste the deployment commands" -ForegroundColor White
    Write-Host "   4. Or upload ubuntu1_deployment_commands.sh and run it" -ForegroundColor White
    Write-Host ""
    
    Write-Host "OPTION 2 - PowerShell Remote Execution:" -ForegroundColor Yellow
    Write-Host "   Note: Requires SSH key authentication setup" -ForegroundColor Red
    Write-Host ""
    
    # Create a simplified command list for manual execution
    Write-Host "📋 KEY COMMANDS TO RUN ON ubuntu-1:" -ForegroundColor Cyan
    Write-Host "-----------------------------------" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "# 1. Clean environment" -ForegroundColor Green
    Write-Host "sudo kubeadm reset --force" -ForegroundColor White
    Write-Host "sudo systemctl stop kubelet containerd" -ForegroundColor White
    Write-Host ""
    Write-Host "# 2. Start services" -ForegroundColor Green  
    Write-Host "sudo systemctl start containerd kubelet" -ForegroundColor White
    Write-Host "sudo systemctl enable containerd kubelet" -ForegroundColor White
    Write-Host ""
    Write-Host "# 3. Initialize Kubernetes" -ForegroundColor Green
    Write-Host "sudo kubeadm init --apiserver-advertise-address=100.71.69.16 --pod-network-cidr=10.244.0.0/16 --ignore-preflight-errors=all" -ForegroundColor White
    Write-Host ""
    Write-Host "# 4. Configure kubectl" -ForegroundColor Green
    Write-Host "export KUBECONFIG=/etc/kubernetes/admin.conf" -ForegroundColor White
    Write-Host "echo 'export KUBECONFIG=/etc/kubernetes/admin.conf' >> ~/.bashrc" -ForegroundColor White
    Write-Host ""
    Write-Host "# 5. Install network" -ForegroundColor Green
    Write-Host "kubectl apply -f https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml" -ForegroundColor White
    Write-Host ""
    Write-Host "# 6. Deploy empire containers (use the full YAML from ubuntu1_deployment_commands.sh)" -ForegroundColor Green
    Write-Host ""
    
    Write-Host "🎮 READY TO EXECUTE!" -ForegroundColor Magenta
    Write-Host "Choose your preferred method above and let's deploy! 🚀" -ForegroundColor Yellow
    
} else {
    Write-Host "❌ CONNECTION FAILED!" -ForegroundColor Red
    Write-Host "Cannot reach ubuntu-1 on port 22" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "🏆 DEPLOYMENT EXECUTOR READY 🏆" -ForegroundColor Magenta
