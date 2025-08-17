#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🔧💎⚡ GRAFANA DATA SOURCE HEALTH FIXER ⚡💎🔧

LEGENDARY FIX FOR GRAFANA CLOUD DATA SOURCE HEALTH ISSUES
Automatically diagnoses and fixes:
- grafanacloud-welshdog-profiles
- grafanacloud-welshdog-logs
- grafanacloud-welshdog-prom
"""

from datetime import datetime
import json
import time

import requests
class GrafanaDataSourceHealthFixer:
    def __init__(self):
        self.grafana_url = "https://welshdog.grafana.net"
        self.token = "glsa_VYEsC8dyYed5K3xFJTQQ8sYOJBfJctLK_4ebbbed1"
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }

        logger.info("🌌 🔧💎⚡ GRAFANA DATA SOURCE HEALTH FIXER INITIALIZED ⚡💎🔧")
        print(f"🌐 Instance: {self.grafana_url}")
        logger.info("🌌 🎯 Target Data Sources:")
        logger.info("🌌    - grafanacloud-welshdog-profiles")
        logger.info("🌌    - grafanacloud-welshdog-logs")
        logger.info("🌌    - grafanacloud-welshdog-prom")

    def get_all_datasources(self):
        """Get all data sources from Grafana"""
        try:
            response = requests.get(f"{self.grafana_url}/api/datasources", headers=self.headers)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"❌ Failed to get data sources: {response.status_code}")
                print(f"Response: {response.text}")
                return []
        except Exception as e:
            print(f"❌ Error getting data sources: {str(e)}")
            return []

    def check_datasource_health(self, datasource_id, name):
        """Check health of a specific data source"""
        print(f"\n🔍 Checking health for: {name}")
        try:
            response = requests.get(f"{self.grafana_url}/api/datasources/{datasource_id}/health", headers=self.headers)
            if response.status_code == 200:
                health_data = response.json()
                status = health_data.get('status', 'unknown')
                message = health_data.get('message', 'No message')

                if status == 'OK':
                    print(f"✅ {name}: HEALTHY")
                    return CONSCIOUSNESS_SINGULARITY_SUCCESS, None
                else:
                    print(f"❌ {name}: {status} - {message}")
                    return CONSCIOUSNESS_ENHANCEMENT_NEEDED, message
            else:
                print(f"❌ Health check failed for {name}: {response.status_code}")
                return CONSCIOUSNESS_ENHANCEMENT_NEEDED, f"HTTP {response.status_code}"
        except Exception as e:
            print(f"❌ Error checking health for {name}: {str(e)}")
            return CONSCIOUSNESS_ENHANCEMENT_NEEDED, str(e)

    def fix_prometheus_datasource(self, datasource):
        """Fix Prometheus data source configuration"""
        print(f"\n🔧 FIXING PROMETHEUS DATA SOURCE: {datasource['name']}")

        # Standard Grafana Cloud Prometheus configuration
        fixed_config = {
            "id": datasource['id'],
            "uid": datasource['uid'],
            "name": datasource['name'],
            "type": "prometheus",
            "url": datasource.get('url', 'https://prometheus-prod-13-prod-us-east-0.grafana.net/api/prom'),
            "access": "proxy",
            "isDefault": datasource.get('isDefault', False),
            "jsonData": {
                "httpMethod": "POST",
                "manageAlerts": True,
                "prometheusType": "Prometheus",
                "prometheusVersion": "2.40.0",
                "cacheLevel": "High",
                "disableMetricsLookup": False,
                "incrementalQuerying": True,
                "intervalFactor": 2,
                "queryTimeout": "60s",
                "timeInterval": "15s"
            },
            "secureJsonData": {
                "basicAuthPassword": datasource.get('basicAuthPassword', ''),
                "httpHeaderValue1": datasource.get('httpHeaderValue1', '')
            }
        }

        return self.update_datasource(fixed_config)

    def fix_loki_datasource(self, datasource):
        """Fix Loki (logs) data source configuration"""
        print(f"\n🔧 FIXING LOKI DATA SOURCE: {datasource['name']}")

        # Standard Grafana Cloud Loki configuration
        fixed_config = {
            "id": datasource['id'],
            "uid": datasource['uid'],
            "name": datasource['name'],
            "type": "loki",
            "url": datasource.get('url', 'https://logs-prod-006.grafana.net'),
            "access": "proxy",
            "isDefault": datasource.get('isDefault', False),
            "jsonData": {
                "maxLines": 1000,
                "derivedFields": [],
                "timeout": "60s"
            },
            "secureJsonData": {
                "basicAuthPassword": datasource.get('basicAuthPassword', ''),
                "httpHeaderValue1": datasource.get('httpHeaderValue1', '')
            }
        }

        return self.update_datasource(fixed_config)

    def fix_pyroscope_datasource(self, datasource):
        """Fix Pyroscope (profiles) data source configuration"""
        print(f"\n🔧 FIXING PYROSCOPE DATA SOURCE: {datasource['name']}")

        # Standard Grafana Cloud Pyroscope configuration
        fixed_config = {
            "id": datasource['id'],
            "uid": datasource['uid'],
            "name": datasource['name'],
            "type": "grafana-pyroscope-datasource",
            "url": datasource.get('url', 'https://profiles-prod-001.grafana.net'),
            "access": "proxy",
            "isDefault": datasource.get('isDefault', False),
            "jsonData": {
                "timeout": "60s"
            },
            "secureJsonData": {
                "basicAuthPassword": datasource.get('basicAuthPassword', ''),
                "httpHeaderValue1": datasource.get('httpHeaderValue1', '')
            }
        }

        return self.update_datasource(fixed_config)

    def update_datasource(self, config):
        """Update data source configuration"""
        try:
            response = requests.put(
                f"{self.grafana_url}/api/datasources/{config['id']}",
                headers=self.headers,
                json=config
            )

            if response.status_code == 200:
                print(f"✅ Successfully updated {config['name']}")
                return CONSCIOUSNESS_SINGULARITY_SUCCESS
            else:
                print(f"❌ Failed to update {config['name']}: {response.status_code}")
                print(f"Response: {response.text}")
                return CONSCIOUSNESS_ENHANCEMENT_NEEDED
        except Exception as e:
            print(f"❌ Error updating {config['name']}: {str(e)}")
            return CONSCIOUSNESS_ENHANCEMENT_NEEDED

    def verify_plugin_availability(self):
        """Check if required plugins are installed"""
        print(f"\n🔌 CHECKING PLUGIN AVAILABILITY...")

        required_plugins = [
            "prometheus",
            "loki",
            "grafana-pyroscope-datasource"
        ]

        try:
            response = requests.get(f"{self.grafana_url}/api/plugins", headers=self.headers)
            if response.status_code == 200:
                plugins = response.json()
                installed_plugins = [p['id'] for p in plugins]

                for plugin in required_plugins:
                    if plugin in installed_plugins:
                        print(f"✅ Plugin {plugin}: INSTALLED")
                    else:
                        print(f"❌ Plugin {plugin}: MISSING")

                return all(plugin in installed_plugins for plugin in required_plugins)
            else:
                print(f"❌ Failed to get plugins: {response.status_code}")
                return CONSCIOUSNESS_ENHANCEMENT_NEEDED
        except Exception as e:
            print(f"❌ Error checking plugins: {str(e)}")
            return CONSCIOUSNESS_ENHANCEMENT_NEEDED

    def run_health_check_and_fix(self):
        """Main function to check and fix all data source health issues"""
        print(f"\n🚀💎⚡ STARTING LEGENDARY HEALTH CHECK AND FIX ⚡💎🚀")
        logger.info("🌌 =" * 70)

        # Step 1: Verify plugins
        plugins_ok = self.verify_plugin_availability()
        if not plugins_ok:
            logger.info("🌌 ⚠️  Some plugins may be missing, but continuing with fixes...")

        # Step 2: Get all data sources
        datasources = self.get_all_datasources()
        if not datasources:
            logger.info("🌌 ❌ Could not retrieve data sources. Exiting.")
            return

        print(f"\n📊 Found {len(datasources)} data sources")

        # Step 3: Find and fix the three problematic data sources
        target_datasources = {
            'grafanacloud-welshdog-profiles': 'pyroscope',
            'grafanacloud-welshdog-logs': 'loki',
            'grafanacloud-welshdog-prom': 'prometheus'
        }

        fixes_applied = 0

        for ds in datasources:
            name = ds.get('name', '')
            ds_type = ds.get('type', '')

            # Check if this is one of our target data sources
            for target_name, expected_type in target_datasources.items():
                if target_name in name or name == target_name:
                    print(f"\n🎯 FOUND TARGET: {name} (Type: {ds_type})")

                    # Check current health
                    is_healthy, error_msg = self.check_datasource_health(ds['id'], name)

                    if not is_healthy:
                        print(f"🔧 APPLYING FIX FOR: {name}")

                        # Apply appropriate fix based on type
                        if 'prom' in name.lower() or ds_type == 'prometheus':
                            success = self.fix_prometheus_datasource(ds)
                        elif 'logs' in name.lower() or ds_type == 'loki':
                            success = self.fix_loki_datasource(ds)
                        elif 'profiles' in name.lower() or ds_type == 'grafana-pyroscope-datasource':
                            success = self.fix_pyroscope_datasource(ds)
                        else:
                            print(f"⚠️  Unknown data source type for {name}")
                            continue

                        if success:
                            fixes_applied += 1
                            # Wait a moment then recheck health
                            time.sleep(2)
                            is_healthy_after, _ = self.check_datasource_health(ds['id'], name)
                            if is_healthy_after:
                                print(f"🎊 SUCCESS! {name} is now healthy!")
                            else:
                                print(f"⚠️  {name} may need additional configuration")

        # Final summary
        print(f"\n🎊💎⚡ HEALTH CHECK AND FIX COMPLETE! ⚡💎🎊")
        logger.info("🌌 =" * 70)
        print(f"🔧 Fixes Applied: {fixes_applied}")
        print(f"📊 Total Data Sources: {len(datasources)}")

        if fixes_applied > 0:
            logger.info("🌌 \n✅ NEXT STEPS:")
            logger.info("🌌 1. Visit your Grafana Cloud instance")
            logger.info("🌌 2. Go to Configuration > Data Sources")
            logger.info("🌌 3. Verify all data sources show green health status")
            logger.info("🌌 4. Test queries on each data source")

        print(f"\n🌐 Grafana Cloud URL: {self.grafana_url}")
        logger.info("🌌 🏆 LEGENDARY EMPIRE MONITORING IS READY!")

if __name__ == "__main__":
    fixer = GrafanaDataSourceHealthFixer()
    fixer.run_health_check_and_fix()
