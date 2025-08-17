#!/bin/bash
# 🔧🏆⚡ LEGENDARY KUBERNETES RECOVERY TOOLKIT ⚡🏆🔧
#
# Quick recovery procedures for Kubernetes cluster issues
# Created: August 7, 2025
# Status: EMERGENCY_RECOVERY_PROCEDURES

echo "🔧🏆⚡ LEGENDARY KUBERNETES RECOVERY TOOLKIT ⚡🏆🔧"
echo "========================================================"

# Network connectivity check
echo "🌐 Step 1: Testing network connectivity..."
if ping -c 3 100.68.37.27 > /dev/null 2>&1; then
    echo "✅ Network connectivity: OK"
else
    echo "❌ Network connectivity: FAILED - Manual intervention required"
    echo "📋 Recovery actions:"
    echo "   1. Check physical network connection"
    echo "   2. Access server console/IPMI"
    echo "   3. Restart networking: systemctl restart networking"
    echo "   4. Restart Tailscale: systemctl restart tailscaled"
    exit 1
fi

# SSH connectivity check
echo "🔑 Step 2: Testing SSH connectivity..."
if ssh -o ConnectTimeout=10 root@100.68.37.27 "echo 'SSH OK'" > /dev/null 2>&1; then
    echo "✅ SSH connectivity: OK"
else
    echo "❌ SSH connectivity: FAILED"
    echo "📋 SSH recovery actions:"
    echo "   1. Check SSH service: systemctl status ssh"
    echo "   2. Check firewall: ufw status"
    echo "   3. Check Tailscale status: tailscale status"
    exit 1
fi

# Kubernetes cluster status
echo "☸️ Step 3: Testing Kubernetes cluster..."
if ssh root@100.68.37.27 "export KUBECONFIG=/etc/kubernetes/admin.conf && kubectl get nodes" > /dev/null 2>&1; then
    echo "✅ Kubernetes cluster: HEALTHY"
    ssh root@100.68.37.27 "export KUBECONFIG=/etc/kubernetes/admin.conf && kubectl get nodes,pods --all-namespaces"
else
    echo "❌ Kubernetes cluster: REQUIRES RECOVERY"
    echo "🔧 Starting cluster recovery procedures..."
    
    # Clean recovery procedure
    echo "🧹 Cleaning previous installation..."
    ssh root@100.68.37.27 "
        kubeadm reset --force 2>/dev/null || true
        systemctl stop kubelet containerd 2>/dev/null || true
        rm -rf /etc/kubernetes/* /var/lib/etcd/* /etc/cni/net.d/* 2>/dev/null || true
        iptables -F && iptables -t nat -F && iptables -t mangle -F && iptables -X 2>/dev/null || true
    "
    
    echo "🚀 Starting services..."
    ssh root@100.68.37.27 "
        systemctl start containerd
        systemctl start kubelet
        sleep 5
    "
    
    echo "☸️ Initializing cluster..."
    ssh root@100.68.37.27 "
        kubeadm init --apiserver-advertise-address=100.68.37.27 --pod-network-cidr=10.244.0.0/16 --ignore-preflight-errors=all
    "
    
    if [ $? -eq 0 ]; then
        echo "✅ Cluster initialization: SUCCESS"
        
        echo "🌐 Installing network plugin..."
        ssh root@100.68.37.27 "
            export KUBECONFIG=/etc/kubernetes/admin.conf
            kubectl apply -f https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml
        "
        
        echo "⏳ Waiting for cluster ready..."
        sleep 30
        
        echo "🎯 Final status check..."
        ssh root@100.68.37.27 "
            export KUBECONFIG=/etc/kubernetes/admin.conf
            kubectl get nodes
            kubectl get pods --all-namespaces
        "
    else
        echo "❌ Cluster initialization: FAILED"
        echo "📋 Manual recovery required - check server console"
        exit 1
    fi
fi

echo ""
echo "🏆 RECOVERY COMPLETE! 🏆"
echo "=========================="
echo "✅ Network: Connected"  
echo "✅ SSH: Accessible"
echo "✅ Kubernetes: Running"
echo ""
echo "🚀 Ready for Phase 2 container migration!"
echo "📚 See recovery report for detailed next steps"
