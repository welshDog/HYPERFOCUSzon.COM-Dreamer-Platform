# 🔧💎⚡ GRAFANA ACCESS DENIED - INSTANT FIX GUIDE ⚡💎🔧

## 🚨 PROBLEM IDENTIFIED: API Authentication Missing

Your Grafana Cloud instance needs proper authentication credentials!

## ⚡ SOLUTION 1: Create Service Account Token (RECOMMENDED)

### Step 1: Go to Grafana Cloud
1. Visit: https://welshdog.grafana.net
2. Go to **Administration** → **Service Accounts**
3. Click **Add Service Account**

### Step 2: Create Empire Service Account
```
Name: HyperFocus-Empire-Monitor
Display Name: Empire Monitoring System
Role: Admin (for full access)
```

### Step 3: Generate Token
1. Click on your new service account
2. Click **Add Service Account Token**
3. Name: `Empire-API-Token`
4. Copy the token immediately! (You won't see it again)

### Step 4: Set Environment Variable
```bash
# In PowerShell
$env:GRAFANA_SERVICE_ACCOUNT_TOKEN="your_token_here"

# Or add to your empire.env file
echo "GRAFANA_SERVICE_ACCOUNT_TOKEN=your_token_here" >> empire.env
```

## ⚡ SOLUTION 2: Use API Key (Alternative)

### Step 1: Create API Key
1. Visit: https://welshdog.grafana.net/org/apikeys
2. Click **Add API Key**
3. Name: `Empire-Monitoring-Key`
4. Role: **Admin**
5. Copy the key

### Step 2: Update Script
Replace the token line in the script with:
```python
self.grafana_token = os.getenv('GRAFANA_API_KEY')
```

## ⚡ SOLUTION 3: Manual Setup (Quick Start)

Since API is blocked, let's do it manually in the web interface:

### 1. Add Prometheus Data Source
1. Go to: https://welshdog.grafana.net/datasources
2. Click **Add data source**
3. Select **Prometheus**
4. Configure:
   - Name: `HyperFocus-Empire-Prometheus`
   - URL: `http://localhost:9090`
   - Access: `Server (default)`
5. Click **Save & Test**

### 2. Import Dashboard
1. Go to: https://welshdog.grafana.net/dashboard/import
2. Click **Upload JSON file**
3. Select: `h:\grafana-config\empire-dashboard-template.json`
4. Click **Import**

## 🎯 IMMEDIATE ACTION PLAN

### Option A: Quick Manual Fix (5 minutes)
1. Follow Solution 3 above
2. Your monitoring will be active immediately
3. No API tokens needed

### Option B: Full Automation Setup (10 minutes)
1. Create service account token (Solution 1)
2. Run the Python script again
3. Everything will auto-configure

## 🔥 TROUBLESHOOTING CHECKLIST

- [ ] Grafana Cloud instance accessible at welshdog.grafana.net
- [ ] Service account created with Admin permissions
- [ ] Token copied and set in environment
- [ ] Prometheus running on localhost:9090
- [ ] Empire services running on configured ports

## 🚀 NEXT STEPS

Choose your path:
1. **Quick & Manual**: Follow Solution 3 for immediate results
2. **Full Automation**: Follow Solution 1 for complete setup

Your legendary empire monitoring will be operational within minutes! 🎊💎⚡
