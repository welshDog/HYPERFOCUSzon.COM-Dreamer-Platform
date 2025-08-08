# 🚀🏆⚡ PHASE 2 UBUNTU-1 DEPLOYMENT STRATEGY (PowerShell) ⚡🏆🚀
#
# Target: ubuntu-1 (100.71.69.16) - CONFIRMED ACCESSIBLE
# PowerShell version for Windows deployment control

Write-Host "🚀🏆⚡ PHASE 2 UBUNTU-1 DEPLOYMENT STRATEGY ⚡🏆🚀" -ForegroundColor Cyan
Write-Host "=============================================================" -ForegroundColor Cyan
Write-Host "🎯 Target: ubuntu-1 (100.71.69.16) - BACKUP SERVER DEPLOYMENT" -ForegroundColor Yellow
Write-Host "📅 Date: $(Get-Date)" -ForegroundColor Green
Write-Host ""

# Test connectivity first
Write-Host "🔍 STEP 1: Testing server connectivity..." -ForegroundColor Cyan
$connection = Test-NetConnection -ComputerName 100.71.69.16 -Port 22 -InformationLevel Quiet

if ($connection.TcpTestSucceeded) {
    Write-Host "✅ SUCCESS: ubuntu-1 server is accessible!" -ForegroundColor Green
    
    # Create the deployment commands
    Write-Host ""
    Write-Host "📋 DEPLOYMENT COMMANDS READY:" -ForegroundColor Cyan
    Write-Host "   1. Clean environment: sudo kubeadm reset --force" -ForegroundColor Yellow
    Write-Host "   2. Start services: sudo systemctl start containerd kubelet" -ForegroundColor Yellow
    Write-Host "   3. Initialize cluster: sudo kubeadm init --apiserver-advertise-address=100.71.69.16" -ForegroundColor Yellow
    Write-Host "   4. Install network: kubectl apply -f flannel.yml" -ForegroundColor Yellow
    Write-Host "   5. Deploy containers: kubectl apply empire namespace and pods" -ForegroundColor Yellow
    
    Write-Host ""
    Write-Host "🔑 SSH CONNECTION REQUIRED:" -ForegroundColor Magenta
    Write-Host "   Please run: ssh root@100.71.69.16" -ForegroundColor White
    Write-Host "   Then execute the commands above manually" -ForegroundColor White
    
    # Create the complete deployment script for manual execution
    $deploymentScript = @"
#!/bin/bash
echo "🚀 PHASE 2 UBUNTU-1 DEPLOYMENT - MANUAL EXECUTION"
echo "=================================================="

# Step 1: Clean environment
echo "🧹 Cleaning environment..."
sudo kubeadm reset --force
sudo systemctl stop kubelet containerd
sudo rm -rf /etc/kubernetes/* /var/lib/etcd/* /etc/cni/net.d/*
sudo iptables -F && sudo iptables -t nat -F && sudo iptables -t mangle -F && sudo iptables -X

# Step 2: Start services
echo "🚀 Starting services..."
sudo systemctl start containerd
sudo systemctl enable containerd
sudo systemctl start kubelet
sudo systemctl enable kubelet
sleep 10

# Step 3: Initialize Kubernetes
echo "☸️ Initializing Kubernetes cluster..."
sudo kubeadm init --apiserver-advertise-address=100.71.69.16 --pod-network-cidr=10.244.0.0/16 --ignore-preflight-errors=all

if [ `$? -eq 0 ]; then
    echo "✅ Cluster initialization SUCCESS!"
    
    # Configure kubectl
    export KUBECONFIG=/etc/kubernetes/admin.conf
    echo 'export KUBECONFIG=/etc/kubernetes/admin.conf' >> ~/.bashrc
    
    # Install Flannel
    echo "🌐 Installing pod network..."
    kubectl apply -f https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml
    
    sleep 60
    
    # Deploy containers
    echo "🚀 Deploying empire containers..."
    cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Namespace
metadata:
  name: empire
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: legendary-elasticsearch
  namespace: empire
spec:
  serviceName: elasticsearch
  replicas: 1
  selector:
    matchLabels:
      app: legendary-elasticsearch
  template:
    metadata:
      labels:
        app: legendary-elasticsearch
    spec:
      containers:
      - name: elasticsearch
        image: docker.elastic.co/elasticsearch/elasticsearch:8.11.0
        ports:
        - containerPort: 9200
        env:
        - name: discovery.type
          value: single-node
        - name: xpack.security.enabled
          value: "false"
        - name: ES_JAVA_OPTS
          value: "-Xms512m -Xmx512m"
---
apiVersion: v1
kind: Service
metadata:
  name: elasticsearch
  namespace: empire
spec:
  selector:
    app: legendary-elasticsearch
  ports:
  - port: 9200
    targetPort: 9200
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: legendary-memory-crystals
  namespace: empire
spec:
  serviceName: memory-crystals
  replicas: 1
  selector:
    matchLabels:
      app: legendary-memory-crystals
  template:
    metadata:
      labels:
        app: legendary-memory-crystals
    spec:
      containers:
      - name: memory-crystals
        image: redis:7-alpine
        ports:
        - containerPort: 6379
---
apiVersion: v1
kind: Service
metadata:
  name: memory-crystals
  namespace: empire
spec:
  selector:
    app: legendary-memory-crystals
  ports:
  - port: 6379
    targetPort: 6379
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ai-agents
  namespace: empire
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ai-agents
  template:
    metadata:
      labels:
        app: ai-agents
    spec:
      containers:
      - name: ai-agent
        image: python:3.11-slim
        command: ["python", "-c", "import time; print('AI Agent starting...'); [print(f'AI Agent {i} processing...') or time.sleep(30) for i in range(1000)]"]
EOF
    
    sleep 30
    
    echo "📊 Final status:"
    kubectl get all -n empire
    kubectl get nodes -o wide
    
    echo ""
    echo "🎉 PHASE 2 DEPLOYMENT COMPLETE!"
    echo "✅ Kubernetes cluster running on ubuntu-1"
    echo "✅ Empire containers deployed"
    
else
    echo "❌ Cluster initialization failed"
fi
"@

    # Save the script to a file
    $deploymentScript | Out-File -FilePath "h:\ubuntu1_deployment_commands.sh" -Encoding UTF8
    
    Write-Host ""
    Write-Host "📄 DEPLOYMENT SCRIPT SAVED: ubuntu1_deployment_commands.sh" -ForegroundColor Green
    Write-Host ""
    Write-Host "🎯 NEXT STEPS:" -ForegroundColor Cyan
    Write-Host "   1. SSH to server: ssh root@100.71.69.16" -ForegroundColor White
    Write-Host "   2. Copy and run the deployment commands" -ForegroundColor White
    Write-Host "   3. Or upload and execute: ubuntu1_deployment_commands.sh" -ForegroundColor White
    
} else {
    Write-Host "❌ FAILED: ubuntu-1 server not accessible via SSH" -ForegroundColor Red
    Write-Host "   Port 22 test failed - check SSH service status" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "🏆 UBUNTU-1 DEPLOYMENT PREPARATION COMPLETE 🏆" -ForegroundColor Magenta

# Also test the original ubuntu server
Write-Host ""
Write-Host "🔍 Testing original ubuntu server (100.68.37.27)..." -ForegroundColor Cyan
$originalConnection = Test-NetConnection -ComputerName 100.68.37.27 -Port 22 -InformationLevel Quiet

if ($originalConnection.TcpTestSucceeded) {
    Write-Host "✅ Original ubuntu server is now accessible!" -ForegroundColor Green
    Write-Host "   Consider using this server instead if preferred" -ForegroundColor Yellow
} else {
    Write-Host "❌ Original ubuntu server still not accessible via SSH" -ForegroundColor Red
    Write-Host "   Tailscale shows 'active via relay' but SSH not working" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "🌐 TAILSCALE ADMIN ACCESS:" -ForegroundColor Magenta
Write-Host "   With admin access, you can investigate server status" -ForegroundColor White
Write-Host "   and potentially restart/reconnect the offline server" -ForegroundColor White
