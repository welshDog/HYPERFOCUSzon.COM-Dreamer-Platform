#!/bin/bash
# 🚀💎⚡ LEGENDARY DASHBOARD DEPLOYMENT AUTOMATION SCRIPT ⚡💎🚀
# =====================================================================
#
# Automated deployment of cost management dashboard to welshdog.grafana.net
# Author: Chief Lyndz Empire
# Date: August 3, 2025
# Purpose: One-click deployment of 38.8KB cost management dashboard

set -e  # Exit on any error

# Colors for legendary output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;96m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Legendary banner
echo -e "${PURPLE}${BOLD}"
echo "🚀💎⚡ LEGENDARY GRAFANA DASHBOARD DEPLOYER ⚡💎🚀"
echo "====================================================="
echo -e "${NC}"

# Configuration
GRAFANA_URL="https://welshdog.grafana.net"
DASHBOARD_PATH="h:/grafana-by-example/cost-management/dashboard-final.json"
DEPLOYER_SCRIPT="h:/🚀💎⚡_LEGENDARY_GRAFANA_DASHBOARD_DEPLOYER_⚡💎🚀.py"
PYTHON_CMD="python"

# Check if Python is available
if ! command -v python &> /dev/null; then
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
    else
        echo -e "${RED}❌ Python not found! Please install Python 3.7+ ${NC}"
        exit 1
    fi
fi

echo -e "${CYAN}🔍 Environment Check:${NC}"
echo -e "   Python: ${GREEN}$(${PYTHON_CMD} --version)${NC}"
echo -e "   Dashboard: ${GREEN}${DASHBOARD_PATH}${NC}"
echo -e "   Target: ${GREEN}${GRAFANA_URL}${NC}"
echo ""

# Check if dashboard file exists
if [ ! -f "${DASHBOARD_PATH}" ]; then
    echo -e "${RED}❌ Dashboard file not found: ${DASHBOARD_PATH}${NC}"
    echo -e "${YELLOW}💡 Make sure you're running from the correct directory${NC}"
    exit 1
fi

# Check if deployer script exists
if [ ! -f "${DEPLOYER_SCRIPT}" ]; then
    echo -e "${RED}❌ Deployer script not found: ${DEPLOYER_SCRIPT}${NC}"
    exit 1
fi

# Check for service account token
if [ -z "${GRAFANA_SERVICE_ACCOUNT_TOKEN}" ]; then
    echo -e "${YELLOW}⚠️  No GRAFANA_SERVICE_ACCOUNT_TOKEN environment variable found${NC}"
    echo -e "${CYAN}🔑 Please set your Grafana service account token:${NC}"
    echo -e "   ${BOLD}export GRAFANA_SERVICE_ACCOUNT_TOKEN=glsa_your_token_here${NC}"
    echo ""
    read -p "Enter your Grafana service account token: " GRAFANA_TOKEN
    if [ -z "${GRAFANA_TOKEN}" ]; then
        echo -e "${RED}❌ No token provided. Aborting deployment.${NC}"
        exit 1
    fi
    export GRAFANA_SERVICE_ACCOUNT_TOKEN="${GRAFANA_TOKEN}"
fi

# Install required Python packages
echo -e "${CYAN}📦 Installing required Python packages...${NC}"
${PYTHON_CMD} -m pip install requests --quiet

# Get dashboard file size
DASHBOARD_SIZE=$(stat -f%z "${DASHBOARD_PATH}" 2>/dev/null || stat -c%s "${DASHBOARD_PATH}" 2>/dev/null)
DASHBOARD_SIZE_KB=$((DASHBOARD_SIZE / 1024))

echo -e "${CYAN}📊 Dashboard Information:${NC}"
echo -e "   Size: ${GREEN}${DASHBOARD_SIZE_KB} KB${NC}"
echo -e "   Type: ${GREEN}Cost Management Dashboard${NC}"
echo -e "   Features: ${GREEN}Billable series tracking, cost analysis, environment comparison${NC}"
echo ""

# Confirmation prompt
echo -e "${YELLOW}🎯 Ready to deploy dashboard to ${GRAFANA_URL}${NC}"
echo -e "${BOLD}This will upload the cost management dashboard to your Grafana Cloud instance.${NC}"
echo ""
read -p "Continue with deployment? (y/N): " CONFIRM

if [[ ! "${CONFIRM}" =~ ^[Yy]$ ]]; then
    echo -e "${YELLOW}⚠️  Deployment cancelled by user${NC}"
    exit 0
fi

echo ""
echo -e "${PURPLE}${BOLD}🚀 INITIATING LEGENDARY DEPLOYMENT...${NC}"
echo ""

# Run the Python deployer
${PYTHON_CMD} "${DEPLOYER_SCRIPT}" \
    --dashboard "${DASHBOARD_PATH}" \
    --url "${GRAFANA_URL}"

DEPLOYMENT_STATUS=$?

if [ ${DEPLOYMENT_STATUS} -eq 0 ]; then
    echo ""
    echo -e "${GREEN}${BOLD}🎊💎⚡ LEGENDARY DEPLOYMENT COMPLETE! ⚡💎🎊${NC}"
    echo -e "${GREEN}=====================================${NC}"
    echo ""
    echo -e "${CYAN}🏛️ Empire Cost Management Dashboard is now LIVE!${NC}"
    echo -e "${CYAN}🌐 Access your dashboard: ${GRAFANA_URL}/dashboards${NC}"
    echo -e "${CYAN}📊 Monitor your $8,750+ empire economy in real-time${NC}"
    echo -e "${CYAN}💎 Track 677+ agent monitoring costs efficiently${NC}"
    echo ""
    echo -e "${PURPLE}Next Phase: Advanced Cost Optimization & Alerts${NC}"
else
    echo ""
    echo -e "${RED}${BOLD}❌ DEPLOYMENT FAILED${NC}"
    echo -e "${YELLOW}🔧 Check the error messages above and try again${NC}"
    exit 1
fi
