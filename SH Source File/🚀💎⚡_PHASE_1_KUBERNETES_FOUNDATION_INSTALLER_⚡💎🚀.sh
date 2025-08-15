#!/bin/bash

# 🏆💎⚡ KUBERNETES TRANSFORMATION PHASE 1 IMPLEMENTATION ⚡💎🏆
# Script: Phase 1 - Kubernetes Foundation Setup
# Target: Server 100.68.37.27 (ubuntu)
# Purpose: Transform Docker infrastructure to enterprise Kubernetes

set -e  # Exit on any error

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Logging function
log() {
    echo -e "${GREEN}[$(date '+%Y-%m-%d %H:%M:%S')] $1${NC}"
}

error() {
    echo -e "${RED}[ERROR $(date '+%Y-%m-%d %H:%M:%S')] $1${NC}"
}

warning() {
    echo -e "${YELLOW}[WARNING $(date '+%Y-%m-%d %H:%M:%S')] $1${NC}"
}

info() {
    echo -e "${BLUE}[INFO $(date '+%Y-%m-%d %H:%M:%S')] $1${NC}"
}

header() {
    echo -e "${PURPLE}================================${NC}"
    echo -e "${PURPLE}$1${NC}"  
    echo -e "${PURPLE}================================${NC}"
}

# Configuration variables
SERVER_IP="100.68.37.27"
SERVER_ACTUAL_IP="212.227.127.144"
HOSTNAME="ubuntu"
KUBE_VERSION="1.28.0"
CONTAINERD_VERSION="1.7.2"
TAILSCALE_OPERATOR_VERSION="v1.52.1"

# Verification functions
verify_prerequisites() {
    header "🔍 VERIFYING PREREQUISITES"
    
    # Check if running on target server
    CURRENT_IP=$(ip route get 8.8.8.8 | sed -n '/src/{s/.*src *\([^ ]*\).*/\1/p;q}')
    if [[ "$CURRENT_IP" != "$SERVER_ACTUAL_IP" ]] && [[ "$CURRENT_IP" != "$SERVER_IP" ]]; then
        error "This script must be run on server $SERVER_IP (ubuntu). Current IP: $CURRENT_IP"
        exit 1
    fi
    
    # Check if running as root or with sudo
    if [[ $EUID -ne 0 ]]; then
        error "This script must be run as root or with sudo"
        exit 1
    fi
    
    # Check system resources
    MEMORY_GB=$(free -g | awk '/^Mem:/{print $2}')
    CPU_CORES=$(nproc)
    
    if [[ $MEMORY_GB -lt 2 ]]; then
        error "Insufficient memory: ${MEMORY_GB}GB (minimum 2GB required)"
        exit 1
    fi
    
    if [[ $CPU_CORES -lt 2 ]]; then
        error "Insufficient CPU cores: ${CPU_CORES} (minimum 2 required)"
        exit 1
    fi
    
    log "✅ Prerequisites verified: ${MEMORY_GB}GB RAM, ${CPU_CORES} CPU cores"
    log "✅ Running on target server: ${SERVER_IP} (${HOSTNAME})"
}

# Backup current Docker configuration
backup_current_state() {
    header "💾 BACKING UP CURRENT DOCKER STATE"
    
    BACKUP_DIR="/opt/k8s-migration-backup-$(date +%Y%m%d_%H%M%S)"
    mkdir -p "$BACKUP_DIR"
    
    log "📦 Creating backup directory: $BACKUP_DIR"
    
    # Backup Docker containers
    if command -v docker &> /dev/null; then
        log "📋 Backing up Docker container list..."
        docker ps -a --format "table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}" > "$BACKUP_DIR/docker-containers.txt"
        
        log "📋 Backing up Docker images..."
        docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.ID}}\t{{.Size}}" > "$BACKUP_DIR/docker-images.txt"
        
        log "📋 Backing up Docker networks..."
        docker network ls > "$BACKUP_DIR/docker-networks.txt"
        
        log "📋 Backing up Docker volumes..."
        docker volume ls > "$BACKUP_DIR/docker-volumes.txt"
    fi
    
    # Backup Tailscale configuration
    if command -v tailscale &> /dev/null; then
        log "🌐 Backing up Tailscale status..."
        tailscale status > "$BACKUP_DIR/tailscale-status.txt" 2>/dev/null || true
        
        log "🌐 Backing up Tailscale IP..."
        tailscale ip > "$BACKUP_DIR/tailscale-ip.txt" 2>/dev/null || true
    fi
    
    # Backup network configuration
    log "🌐 Backing up network configuration..."
    ip addr show > "$BACKUP_DIR/network-interfaces.txt"
    ip route show > "$BACKUP_DIR/network-routes.txt"
    
    log "✅ Backup completed: $BACKUP_DIR"
    echo "$BACKUP_DIR" > /tmp/k8s-backup-location
}

# Install container runtime (containerd)
install_containerd() {
    header "🐳 INSTALLING CONTAINERD"
    
    # Remove existing Docker if present (we'll use containerd for K8s)
    if command -v docker &> /dev/null; then
        warning "Docker detected - will coexist with containerd"
    fi
    
    # Install containerd
    log "📦 Installing containerd..."
    apt-get update
    apt-get install -y containerd
    
    # Configure containerd
    log "⚙️ Configuring containerd for Kubernetes..."
    mkdir -p /etc/containerd
    containerd config default | sudo tee /etc/containerd/config.toml
    
    # Enable SystemdCgroup
    sed -i 's/SystemdCgroup \= false/SystemdCgroup \= true/g' /etc/containerd/config.toml
    
    # Restart containerd
    systemctl restart containerd
    systemctl enable containerd
    
    log "✅ Containerd installed and configured"
}

# Disable swap and configure kernel modules
configure_system() {
    header "⚙️ CONFIGURING SYSTEM FOR KUBERNETES"
    
    # Disable swap
    log "🔄 Disabling swap..."
    swapoff -a
    sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
    
    # Load kernel modules
    log "🔧 Configuring kernel modules..."
    cat <<EOF | tee /etc/modules-load.d/k8s.conf
br_netfilter
overlay
EOF
    
    modprobe br_netfilter
    modprobe overlay
    
    # Configure sysctl
    log "🔧 Configuring sysctl parameters..."
    cat <<EOF | tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables  = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward                 = 1
EOF
    
    sysctl --system
    
    log "✅ System configured for Kubernetes"
}

# Install Kubernetes components
install_kubernetes() {
    header "🚀 INSTALLING KUBERNETES COMPONENTS"
    
    # Add Kubernetes repository
    log "📦 Adding Kubernetes repository..."
    curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.28/deb/Release.key | gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
    echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.28/deb/ /' | tee /etc/apt/sources.list.d/kubernetes.list
    
    # Install Kubernetes components
    log "📦 Installing kubeadm, kubelet, and kubectl..."
    apt-get update
    apt-get install -y kubelet kubeadm kubectl
    apt-mark hold kubelet kubeadm kubectl
    
    log "✅ Kubernetes components installed"
    kubeadm version
    kubectl version --client
}

# Initialize Kubernetes cluster
initialize_cluster() {
    header "🏗️ INITIALIZING KUBERNETES CLUSTER"
    
    # Initialize the cluster
    log "🚀 Initializing Kubernetes cluster..."
    
    # Use Tailscale IP for API server
    TAILSCALE_IP=$(tailscale ip 2>/dev/null | head -n1 || echo "$SERVER_IP")
    
    kubeadm init \
        --apiserver-advertise-address="$TAILSCALE_IP" \
        --apiserver-cert-extra-sans="$TAILSCALE_IP,$SERVER_IP,localhost,127.0.0.1" \
        --node-name="$HOSTNAME" \
        --pod-network-cidr=10.244.0.0/16 \
        --service-cidr=10.96.0.0/12
    
    # Configure kubectl for root user
    log "⚙️ Configuring kubectl..."
    mkdir -p /root/.kube
    cp -i /etc/kubernetes/admin.conf /root/.kube/config
    chown root:root /root/.kube/config
    
    # Configure kubectl for regular users (if they exist)
    for user_home in /home/*; do
        if [[ -d "$user_home" ]]; then
            username=$(basename "$user_home")
            log "⚙️ Configuring kubectl for user: $username"
            sudo -u "$username" mkdir -p "$user_home/.kube"
            cp /etc/kubernetes/admin.conf "$user_home/.kube/config"
            chown "$username:$username" "$user_home/.kube/config"
        fi
    done
    
    log "✅ Kubernetes cluster initialized"
}

# Install Pod network (Flannel)
install_pod_network() {
    header "🌐 INSTALLING POD NETWORK (FLANNEL)"
    
    # Install Flannel
    log "🌐 Installing Flannel CNI..."
    kubectl apply -f https://github.com/flannel-io/flannel/releases/latest/download/kustomization.yaml
    
    # Wait for Flannel pods to be ready
    log "⏳ Waiting for Flannel pods to be ready..."
    kubectl wait --for=condition=ready pod -l app=flannel -n kube-flannel --timeout=300s
    
    log "✅ Pod network installed and ready"
}

# Remove taint from control plane (allow pods to be scheduled)
configure_single_node() {
    header "🎯 CONFIGURING SINGLE-NODE CLUSTER"
    
    log "🔧 Removing taint from control plane to allow pod scheduling..."
    kubectl taint nodes --all node-role.kubernetes.io/control-plane- || true
    
    log "✅ Single-node cluster configured"
}

# Create essential namespaces
create_namespaces() {
    header "📁 CREATING ESSENTIAL NAMESPACES"
    
    # Create namespaces
    cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Namespace
metadata:
  name: ai-agents
---
apiVersion: v1
kind: Namespace
metadata:
  name: monitoring
---
apiVersion: v1
kind: Namespace
metadata:
  name: storage
---
apiVersion: v1
kind: Namespace
metadata:
  name: tailscale
EOF
    
    log "✅ Essential namespaces created"
    kubectl get namespaces
}

# Install Tailscale operator
install_tailscale_operator() {
    header "🌐 INSTALLING TAILSCALE OPERATOR"
    
    # Check if Tailscale is installed on the host
    if ! command -v tailscale &> /dev/null; then
        error "Tailscale not found on host system. Please install Tailscale first."
        return 1
    fi
    
    log "🌐 Installing Tailscale Kubernetes Operator..."
    kubectl apply -f https://raw.githubusercontent.com/tailscale/tailscale/main/cmd/k8s-operator/deploy/manifests/operator.yaml
    
    # Wait for operator to be ready
    log "⏳ Waiting for Tailscale operator to be ready..."
    kubectl wait --for=condition=available deployment/tailscale-operator -n tailscale-system --timeout=300s
    
    log "✅ Tailscale operator installed"
}

# Install local path provisioner for storage
install_storage_provisioner() {
    header "💾 INSTALLING LOCAL PATH PROVISIONER"
    
    log "💾 Installing local-path-provisioner..."
    kubectl apply -f https://raw.githubusercontent.com/rancher/local-path-provisioner/v0.0.24/deploy/local-path-storage.yaml
    
    # Set as default storage class
    kubectl patch storageclass local-path -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
    
    log "✅ Local path provisioner installed and set as default"
}

# Verify cluster status
verify_cluster() {
    header "✅ VERIFYING CLUSTER STATUS"
    
    log "🔍 Checking node status..."
    kubectl get nodes -o wide
    
    log "🔍 Checking system pods..."
    kubectl get pods -A
    
    log "🔍 Checking cluster info..."
    kubectl cluster-info
    
    log "🔍 Checking storage classes..."
    kubectl get storageclass
    
    # Test pod creation
    log "🧪 Testing pod creation..."
    cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: test-pod
  namespace: default
spec:
  containers:
  - name: test
    image: nginx:alpine
    ports:
    - containerPort: 80
EOF
    
    # Wait for test pod to be ready
    kubectl wait --for=condition=ready pod/test-pod --timeout=120s
    
    log "🧪 Test pod status:"
    kubectl get pod test-pod -o wide
    
    # Clean up test pod
    kubectl delete pod test-pod
    
    log "✅ Cluster verification completed successfully"
}

# Generate summary report
generate_report() {
    header "📊 GENERATING PHASE 1 COMPLETION REPORT"
    
    REPORT_FILE="/opt/k8s-phase1-report-$(date +%Y%m%d_%H%M%S).txt"
    
    cat <<EOF > "$REPORT_FILE"
🏆💎⚡ KUBERNETES PHASE 1 IMPLEMENTATION REPORT ⚡💎🏆
================================================================

Implementation Date: $(date)
Server: $SERVER_IP ($HOSTNAME)
Phase: 1 - Kubernetes Foundation Setup

COMPONENTS INSTALLED:
✅ Containerd Runtime: $(containerd --version)
✅ Kubernetes Version: $(kubeadm version -o short)
✅ Pod Network: Flannel CNI
✅ Storage: Local Path Provisioner (default)
✅ Tailscale Operator: Installed
✅ Essential Namespaces: ai-agents, monitoring, storage, tailscale

CLUSTER STATUS:
$(kubectl get nodes -o wide)

SYSTEM PODS:
$(kubectl get pods -A)

STORAGE CLASSES:
$(kubectl get storageclass)

CLUSTER INFO:
$(kubectl cluster-info)

NEXT STEPS:
1. Proceed to Phase 2: AI Agent Container Migration
2. Begin container analysis and Kubernetes manifest creation
3. Test migration of non-critical containers first

BACKUP LOCATION:
$(cat /tmp/k8s-backup-location 2>/dev/null || echo "Backup location not found")

CONFIGURATION FILES:
- Kubeconfig: /root/.kube/config
- Containerd Config: /etc/containerd/config.toml
- Kubernetes Manifests: /etc/kubernetes/

PHASE 1 STATUS: ✅ COMPLETED SUCCESSFULLY
================================================================
EOF
    
    log "📊 Report generated: $REPORT_FILE"
    cat "$REPORT_FILE"
}

# Main execution function
main() {
    echo -e "${CYAN}"
    echo "🏆💎⚡ KUBERNETES ENTERPRISE TRANSFORMATION ⚡💎🏆"
    echo "Phase 1: Kubernetes Foundation Setup"
    echo "Server: $SERVER_IP ($HOSTNAME)"
    echo "$(date)"
    echo -e "${NC}"
    
    # Execute installation steps
    verify_prerequisites
    backup_current_state
    configure_system
    install_containerd
    install_kubernetes
    initialize_cluster
    install_pod_network
    configure_single_node
    create_namespaces
    install_storage_provisioner
    install_tailscale_operator
    verify_cluster
    generate_report
    
    header "🎉 PHASE 1 COMPLETED SUCCESSFULLY!"
    echo -e "${GREEN}"
    echo "✅ Kubernetes cluster is ready!"
    echo "✅ Foundation setup complete!"
    echo "✅ Ready for Phase 2: Container Migration"
    echo ""
    echo "🚀 Next Steps:"
    echo "1. Review the generated report"
    echo "2. Verify all services are operational" 
    echo "3. Begin Phase 2 implementation"
    echo -e "${NC}"
}

# Run main function
main "$@"
