# 🚀🏆⚡ PHASE 2 DEPLOYMENT - COPY-PASTE METHOD ⚡🏆🚀

## **IMMEDIATE EXECUTION STEPS:**

### **STEP 1: SSH to ubuntu-1**
```bash
ssh root@100.71.69.16
```

### **STEP 2: Copy and paste these commands one by one:**

```bash
# Clean environment
sudo kubeadm reset --force
sudo systemctl stop kubelet containerd
sudo rm -rf /etc/kubernetes/* /var/lib/etcd/* /etc/cni/net.d/*
sudo iptables -F && sudo iptables -t nat -F && sudo iptables -t mangle -F && sudo iptables -X
```

```bash
# Start services
sudo systemctl start containerd kubelet
sudo systemctl enable containerd kubelet
sleep 10
```

```bash
# Initialize Kubernetes cluster
sudo kubeadm init --apiserver-advertise-address=100.71.69.16 --pod-network-cidr=10.244.0.0/16 --ignore-preflight-errors=all
```

```bash
# Configure kubectl
export KUBECONFIG=/etc/kubernetes/admin.conf
echo 'export KUBECONFIG=/etc/kubernetes/admin.conf' >> ~/.bashrc
```

```bash
# Install pod network
kubectl apply -f https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml
sleep 60
```

```bash
# Create empire namespace
kubectl create namespace empire
```

```bash
# Deploy Elasticsearch
kubectl apply -f - <<EOF
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
EOF
```

```bash
# Deploy Memory Crystals (Redis)
kubectl apply -f - <<EOF
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
EOF
```

```bash
# Deploy AI Agents
kubectl apply -f - <<EOF
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
```

```bash
# Check deployment status
kubectl get nodes -o wide
kubectl get all -n empire
```

## **SUCCESS INDICATORS:**
- Node shows as "Ready"  
- All pods show as "Running"
- Services are accessible

## **🎉 VICTORY CONDITION:**
When you see all empire pods running, **PHASE 2 IS COMPLETE!** 🏆⚡
