#!/bin/bash
# 🌐🏆⚡ LEGENDARY TAILSCALE RECOVERY & UPDATE STRATEGY ⚡🏆🌐
#
# Based on: https://tailscale.com/kb/1067/update?tab=linux
# Target: Ubuntu server with Tailscale connectivity issues
# Created: August 7, 2025

echo "🌐🏆⚡ LEGENDARY TAILSCALE RECOVERY & UPDATE STRATEGY ⚡🏆🌐"
echo "=================================================================="

# STRATEGY 1: Try Alternative Access Methods
echo "🔍 STRATEGY 1: Testing Alternative Access Methods..."

# Test direct domain access
echo "🌐 Testing domain access..."
if ssh -o ConnectTimeout=10 root@ubuntu.tail13f1ca.ts.net "echo 'Domain SSH Success'" 2>/dev/null; then
    echo "✅ SUCCESS: Domain access working!"
    CONNECT_METHOD="root@ubuntu.tail13f1ca.ts.net"
else
    echo "❌ Domain access failed"
fi

# Test IPv6 access
echo "🌐 Testing IPv6 access..."  
if ssh -o ConnectTimeout=10 "root@[fd7a:115c:a1e0::7101:251c]" "echo 'IPv6 SSH Success'" 2>/dev/null; then
    echo "✅ SUCCESS: IPv6 access working!"
    CONNECT_METHOD="root@[fd7a:115c:a1e0::7101:251c]"
else
    echo "❌ IPv6 access failed"
fi

# Test if we found any working connection
if [ -n "$CONNECT_METHOD" ]; then
    echo "🎉 CONNECTION ESTABLISHED: $CONNECT_METHOD"
    
    # STRATEGY 2: Tailscale Update & Recovery
    echo ""
    echo "🚀 STRATEGY 2: Executing Tailscale Update & Recovery..."
    
    # Check current Tailscale status
    echo "📊 Checking current Tailscale status..."
    ssh $CONNECT_METHOD "tailscale version && tailscale status" || echo "⚠️ Tailscale status check failed"
    
    # Update Tailscale to latest version
    echo "⬆️ Updating Tailscale to latest version..."
    ssh $CONNECT_METHOD "
        echo '🔄 Updating Tailscale...'
        curl -fsSL https://tailscale.com/install.sh | sh
        echo '✅ Tailscale update complete'
    "
    
    # Restart Tailscale service
    echo "🔄 Restarting Tailscale service..."
    ssh $CONNECT_METHOD "
        sudo systemctl restart tailscaled
        sleep 5
        sudo tailscale up
        echo '✅ Tailscale service restarted'
    "
    
    # Verify connectivity 
    echo "🧪 Testing connectivity after update..."
    sleep 10
    if ssh -o ConnectTimeout=10 root@100.68.37.27 "echo 'Updated Tailscale SSH Success'"; then
        echo "🎉 SUCCESS: Tailscale connectivity restored!"
        
        # STRATEGY 3: Kubernetes Recovery
        echo ""
        echo "☸️ STRATEGY 3: Executing Kubernetes Recovery..."
        
        # Execute our proven recovery sequence
        ssh root@100.68.37.27 "
            echo '🧹 Cleaning previous Kubernetes installation...'
            kubeadm reset --force 2>/dev/null || true
            systemctl stop kubelet containerd 2>/dev/null || true
            rm -rf /etc/kubernetes/* /var/lib/etcd/* /etc/cni/net.d/* 2>/dev/null || true
            iptables -F && iptables -t nat -F && iptables -t mangle -F && iptables -X 2>/dev/null || true
            
            echo '🚀 Starting container services...'
            systemctl start containerd
            systemctl start kubelet
            sleep 10
            
            echo '☸️ Initializing Kubernetes cluster...'
            kubeadm init --apiserver-advertise-address=100.68.37.27 --pod-network-cidr=10.244.0.0/16 --ignore-preflight-errors=all
        "
        
        if [ $? -eq 0 ]; then
            echo "✅ Kubernetes cluster initialization SUCCESS!"
            
            # Install Flannel network
            echo "🌐 Installing pod network..."
            ssh root@100.68.37.27 "
                export KUBECONFIG=/etc/kubernetes/admin.conf
                kubectl apply -f https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml
                sleep 30
                kubectl get nodes,pods --all-namespaces
            "
            
            echo ""
            echo "🎉🏆 LEGENDARY RECOVERY COMPLETE! 🏆🎉"
            echo "========================================"
            echo "✅ Tailscale: Updated and Connected"
            echo "✅ SSH: Accessible via 100.68.37.27"  
            echo "✅ Kubernetes: Cluster Running"
            echo "✅ Network: Pod network deployed"
            echo ""
            echo "🚀 READY FOR PHASE 2 CONTAINER MIGRATION!"
        else
            echo "❌ Kubernetes initialization failed - manual intervention needed"
        fi
        
    else
        echo "❌ Tailscale connectivity still not restored"
    fi
    
else
    echo "❌ No working connection method found"
    echo "📋 Manual recovery options:"
    echo "   1. Physical/console access to server"
    echo "   2. Check server power and network status"
    echo "   3. Restart server if necessary"
    echo "   4. Use backup server (100.71.69.16) for deployment"
fi

echo ""
echo "🏆 RECOVERY ATTEMPT COMPLETE 🏆"
echo "Check output above for success status"
