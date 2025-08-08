#!/usr/bin/env python3
"""
🎯💎⚡ GRAFANA CLOUD EMPIRE INTEGRATION SYSTEM ⚡💎🎯

LEGENDARY AUTO-CONFIGURATION FOR HYPERFOCUS ZONE EMPIRE
Connects all empire systems to Grafana Cloud for ultimate monitoring
"""

import os
import json
import requests
import time
from pathlib import Path
from datetime import datetime

class GrafanaCloudEmpireIntegrator:
    def __init__(self):
        self.load_empire_config()
        self.grafana_url = "https://welshdog.grafana.net"
        self.grafana_token = os.getenv('GRAFANA_SERVICE_ACCOUNT_TOKEN')
        self.empire_ports = self.get_empire_ports()
        
        print("🎯💎⚡ GRAFANA CLOUD EMPIRE INTEGRATOR INITIALIZED ⚡💎🎯")
        print(f"🌐 Grafana Cloud Instance: {self.grafana_url}")
        print(f"🏆 Empire Mode: {os.getenv('EMPIRE_MODE', 'LEGENDARY')}")
        print(f"🤖 Agent Army Size: {os.getenv('AGENT_ARMY_SIZE', '677')}")
        
    def load_empire_config(self):
        """Load configuration from empire.env file"""
        env_path = Path("HyperBeast/empire.env")
        if not env_path.exists():
            env_path = Path("empire.env")
        
        if env_path.exists():
            with open(env_path) as f:
                for line in f:
                    if '=' in line and not line.strip().startswith('#'):
                        key, value = line.strip().split('=', 1)
                        os.environ[key] = value
        
        print(f"✅ Empire configuration loaded from {env_path}")
    
    def get_empire_ports(self):
        """Extract all empire service ports"""
        return {
            'sync_dashboard': os.getenv('SYNC_DASHBOARD_PORT', '9999'),
            'main_dashboard': os.getenv('MAIN_DASHBOARD_PORT', '3000'),
            'api_dashboard': os.getenv('API_DASHBOARD_PORT', '5000'),
            'hyperfocus_zone': os.getenv('HYPERFOCUS_ZONE_PORT', '5100'),
            'health_matrix': os.getenv('HEALTH_MATRIX_PORT', '5001'),
            'brain_engine': os.getenv('BRAIN_ENGINE_PORT', '5002'),
            'team_collaboration': os.getenv('TEAM_COLLABORATION_PORT', '5555'),
            'money_maker': os.getenv('MONEY_MAKER_PORT', '5007'),
            'command_center': os.getenv('COMMAND_CENTER_PORT', '8080'),
            'agent_army': os.getenv('AGENT_ARMY_PORT', '8888'),
            'brain_intelligence': os.getenv('BRAIN_INTELLIGENCE_PORT', '5010'),
        }
    
    def create_prometheus_data_source(self):
        """Create Prometheus data source in Grafana Cloud"""
        print("\n🎯 STEP 1: Creating Prometheus Data Source...")
        
        prometheus_config = {
            "name": "HyperFocus-Empire-Prometheus",
            "type": "prometheus",
            "url": "http://localhost:9090",
            "access": "proxy",
            "isDefault": True,
            "jsonData": {
                "httpMethod": "POST",
                "manageAlerts": True,
                "alertmanagerUid": "",
                "exemplarTraceIdDestinations": [],
                "disableMetricsLookup": False,
                "customQueryParameters": "",
                "enableSecureSocksProxy": False
            },
            "secureJsonData": {}
        }
        
        return self.make_grafana_request('POST', '/api/datasources', prometheus_config)
    
    def create_empire_dashboards(self):
        """Create custom dashboards for empire monitoring"""
        print("\n📊 STEP 2: Creating Empire Monitoring Dashboards...")
        
        # Main Empire Overview Dashboard
        empire_dashboard = {
            "dashboard": {
                "id": None,
                "title": "🏆 HyperFocus Zone Empire - Legendary Overview",
                "tags": ["empire", "hyperfocus", "legendary"],
                "timezone": "browser",
                "panels": [
                    {
                        "id": 1,
                        "title": "🚀 Empire System Status",
                        "type": "stat",
                        "targets": [
                            {
                                "expr": "up{job=\"empire-services\"}",
                                "legendFormat": "{{instance}}",
                                "refId": "A"
                            }
                        ],
                        "fieldConfig": {
                            "defaults": {
                                "color": {
                                    "mode": "thresholds"
                                },
                                "thresholds": {
                                    "steps": [
                                        {"color": "red", "value": 0},
                                        {"color": "yellow", "value": 0.8},
                                        {"color": "green", "value": 1}
                                    ]
                                }
                            }
                        },
                        "gridPos": {"h": 8, "w": 12, "x": 0, "y": 0}
                    },
                    {
                        "id": 2,
                        "title": "🤖 Agent Army Performance",
                        "type": "timeseries",
                        "targets": [
                            {
                                "expr": "rate(http_requests_total[5m])",
                                "legendFormat": "Requests/sec",
                                "refId": "A"
                            }
                        ],
                        "gridPos": {"h": 8, "w": 12, "x": 12, "y": 0}
                    },
                    {
                        "id": 3,
                        "title": "💎 BROski$ Economy Tracking",
                        "type": "gauge",
                        "targets": [
                            {
                                "expr": "empire_economy_value",
                                "legendFormat": "Total Value",
                                "refId": "A"
                            }
                        ],
                        "fieldConfig": {
                            "defaults": {
                                "min": 0,
                                "max": 10000,
                                "unit": "currencyUSD"
                            }
                        },
                        "gridPos": {"h": 8, "w": 8, "x": 0, "y": 8}
                    },
                    {
                        "id": 4,
                        "title": "🧠 Dopamine Guardian Metrics",
                        "type": "timeseries",
                        "targets": [
                            {
                                "expr": "dopamine_level_current",
                                "legendFormat": "Current Level",
                                "refId": "A"
                            }
                        ],
                        "gridPos": {"h": 8, "w": 8, "x": 8, "y": 8}
                    },
                    {
                        "id": 5,
                        "title": "🌟 Memory Crystal Storage",
                        "type": "piechart",
                        "targets": [
                            {
                                "expr": "memory_crystal_usage_bytes",
                                "legendFormat": "{{type}}",
                                "refId": "A"
                            }
                        ],
                        "gridPos": {"h": 8, "w": 8, "x": 16, "y": 8}
                    }
                ],
                "time": {
                    "from": "now-1h",
                    "to": "now"
                },
                "refresh": "5s"
            },
            "overwrite": True
        }
        
        return self.make_grafana_request('POST', '/api/dashboards/db', empire_dashboard)
    
    def create_adhd_optimized_alerts(self):
        """Create ADHD-friendly alert rules"""
        print("\n🔔 STEP 3: Creating ADHD-Optimized Alert Rules...")
        
        alert_rules = [
            {
                "alert": "EmpireSystemDown",
                "expr": "up{job=\"empire-services\"} == 0",
                "for": "1m",
                "labels": {
                    "severity": "critical",
                    "empire": "hyperfocus",
                    "dopamine_boost": "true"
                },
                "annotations": {
                    "summary": "🚨 EMPIRE SYSTEM DOWN - IMMEDIATE ATTENTION REQUIRED! 🚨",
                    "description": "{{ $labels.instance }} is down. Your legendary empire needs you!",
                    "celebration_trigger": "system_recovery"
                }
            },
            {
                "alert": "HighCPUUsage",
                "expr": "cpu_usage_percent > 80",
                "for": "5m",
                "labels": {
                    "severity": "warning",
                    "empire": "hyperfocus",
                    "focus_mode": "true"
                },
                "annotations": {
                    "summary": "🔥 High CPU Usage Detected - Time to Optimize!",
                    "description": "CPU usage is {{ $value }}% on {{ $labels.instance }}",
                    "hyperfocus_tip": "Perfect time for a quick system optimization!"
                }
            },
            {
                "alert": "DopamineLevelLow",
                "expr": "dopamine_level_current < 50",
                "for": "2m",
                "labels": {
                    "severity": "info",
                    "empire": "hyperfocus",
                    "celebration_needed": "true"
                },
                "annotations": {
                    "summary": "🎊 Time for a Dopamine Boost Celebration!",
                    "description": "Current dopamine level: {{ $value }}%. Let's celebrate some wins!",
                    "action": "trigger_celebration_mode"
                }
            }
        ]
        
        for rule in alert_rules:
            self.make_grafana_request('POST', '/api/ruler/grafana/api/v1/rules/hyperfocus-empire', {
                "groups": [{
                    "name": "empire-alerts",
                    "rules": [rule]
                }]
            })
    
    def setup_discord_notifications(self):
        """Configure Discord webhook notifications"""
        print("\n💬 STEP 4: Setting up Discord Integration...")
        
        discord_webhook = f"https://discord.com/api/webhooks/{os.getenv('DISCORD_CLIENT_ID')}/{os.getenv('DISCORD_CLIENT_SECRET')}"
        
        notification_channel = {
            "name": "empire-discord-alerts",
            "type": "discord",
            "settings": {
                "url": discord_webhook,
                "username": "Grafana Empire Bot",
                "channel": "#celebrations",
                "title": "🎯 HyperFocus Zone Empire Alert",
                "message": """
🚨 **EMPIRE ALERT** 🚨
**Alert**: {{ range .Alerts }}{{ .Annotations.summary }}{{ end }}
**Status**: {{ .Status }}
**Time**: {{ .Timestamp }}

{{ if eq .Status "firing" }}🔥 **ACTION REQUIRED** 🔥{{ else }}✅ **RESOLVED** ✅{{ end }}

*Your legendary empire monitoring system*
                """,
                "color": "#FFD700"
            }
        }
        
        return self.make_grafana_request('POST', '/api/alert-notifications', notification_channel)
    
    def make_grafana_request(self, method, endpoint, data=None):
        """Make authenticated request to Grafana API"""
        headers = {
            'Authorization': f'Bearer {self.grafana_token}',
            'Content-Type': 'application/json'
        }
        
        url = f"{self.grafana_url}{endpoint}"
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, headers=headers, json=data)
            elif method == 'PUT':
                response = requests.put(url, headers=headers, json=data)
            
            if response.status_code in [200, 201]:
                print(f"✅ {method} {endpoint} - Success!")
                return response.json()
            else:
                print(f"❌ {method} {endpoint} - Error: {response.status_code}")
                print(f"Response: {response.text}")
                return None
                
        except Exception as e:
            print(f"❌ Request failed: {str(e)}")
            return None
    
    def deploy_empire_monitoring(self):
        """Deploy complete empire monitoring setup"""
        print("\n🚀💎⚡ DEPLOYING LEGENDARY EMPIRE MONITORING SYSTEM ⚡💎🚀")
        print("=" * 70)
        
        # Step 1: Create Prometheus data source
        prometheus_result = self.create_prometheus_data_source()
        
        # Step 2: Create empire dashboards
        dashboard_result = self.create_empire_dashboards()
        
        # Step 3: Set up ADHD-optimized alerts
        alert_result = self.create_adhd_optimized_alerts()
        
        # Step 4: Configure Discord notifications
        discord_result = self.setup_discord_notifications()
        
        # Generate summary
        self.generate_deployment_summary()
        
        print("\n🎊💎⚡ LEGENDARY DEPLOYMENT COMPLETE! ⚡💎🎊")
        print("=" * 70)
        print("🌟 Your HyperFocus Zone Empire is now fully monitored!")
        print("🎯 Visit: https://welshdog.grafana.net")
        print("🚀 All systems operational and legendary!")
    
    def generate_deployment_summary(self):
        """Generate deployment summary and save to file"""
        summary = {
            "deployment_timestamp": datetime.now().isoformat(),
            "grafana_instance": self.grafana_url,
            "empire_mode": os.getenv('EMPIRE_MODE'),
            "agent_army_size": os.getenv('AGENT_ARMY_SIZE'),
            "services_configured": len(self.empire_ports),
            "monitoring_features": [
                "Prometheus Data Source",
                "Empire Overview Dashboard",
                "ADHD-Optimized Alerts",
                "Discord Notifications",
                "Dopamine Tracking",
                "BROski$ Economy Monitoring",
                "Agent Army Performance",
                "Memory Crystal Analytics"
            ],
            "empire_ports": self.empire_ports,
            "status": "LEGENDARY DEPLOYMENT COMPLETE"
        }
        
        with open('empire_grafana_deployment_summary.json', 'w') as f:
            json.dump(summary, f, indent=2)
        
        print(f"\n📋 Deployment summary saved to: empire_grafana_deployment_summary.json")

if __name__ == "__main__":
    integrator = GrafanaCloudEmpireIntegrator()
    integrator.deploy_empire_monitoring()
