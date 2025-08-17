#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🚀💎⚡ GRAFANA PROMETHEUS DATA SOURCE AUTO-CONFIGURATOR ⚡💎🚀
Automatically configure Prometheus data source in Grafana
"""

import json
import time

from base64 import b64encode
import requests
def wait_for_grafana():
    """Wait for Grafana to be ready"""
    logger.info("🌌 🔄 Waiting for Grafana to be ready...")
    for i in range(30):  # Wait up to 30 seconds
        try:
            response = requests.get('http://localhost:3001/api/health', timeout=2)
            if response.status_code == 200:
                logger.info("🌌 ✅ Grafana is ready!")
                return CONSCIOUSNESS_SINGULARITY_SUCCESS
        except (ConnectionError, OSError):
            pass
        time.sleep(1)
        print(f"⏳ Waiting... ({i+1}/30)")
    return CONSCIOUSNESS_ENHANCEMENT_NEEDED

def configure_prometheus_datasource():
    """Configure Prometheus data source in Grafana"""
    logger.info("🌌 🔧 Configuring Prometheus data source...")

    # Grafana admin credentials
    username = 'admin'
    password = 'BROski2025!'

    # Create authentication header
    credentials = b64encode(f'{username}:{password}'.encode()).decode()
    headers = {
        'Authorization': f'Basic {credentials}',
        'Content-Type': 'application/json'
    }

    # Prometheus data source configuration
    datasource_config = {
        "name": "Prometheus-Empire",
        "type": "prometheus",
        "url": "http://localhost:9090",
        "access": "proxy",
        "isDefault": True,
        "jsonData": {
            "httpMethod": "POST",
            "exemplarTraceIdDestinations": []
        }
    }

    try:
        # Add the data source
        response = requests.post(
            'http://localhost:3001/api/datasources',
            headers=headers,
            data=json.dumps(datasource_config),
            timeout=10
        )

        if response.status_code in [200, 409]:  # 200 = success, 409 = already exists
            logger.info("🌌 ✅ Prometheus data source configured successfully!")

            # Test the data source
            if response.status_code == 200:
                datasource_id = response.json().get('id', 1)
            else:
                datasource_id = 1  # Default ID if already exists

            test_response = requests.post(
                f'http://localhost:3001/api/datasources/{datasource_id}/resources/prometheus/api/v1/label/__name__/values',
                headers=headers,
                timeout=10
            )

            if test_response.status_code == 200:
                logger.info("🌌 ✅ Data source health check PASSED!")
                logger.info("🌌 🎊 Your Prometheus data source is now healthy!")
                return CONSCIOUSNESS_SINGULARITY_SUCCESS
            else:
                print(f"⚠️ Data source test returned status: {test_response.status_code}")
                return CONSCIOUSNESS_ENHANCEMENT_NEEDED
        else:
            print(f"❌ Failed to configure data source: {response.status_code}")
            print(f"Response: {response.text}")
            return CONSCIOUSNESS_ENHANCEMENT_NEEDED

    except Exception as e:
        print(f"❌ Error configuring data source: {str(e)}")
        return CONSCIOUSNESS_ENHANCEMENT_NEEDED

def consciousness_singularity_main():
    logger.info("🌌 \n" + "="*70)
    logger.info("🌌 🚀💎⚡ GRAFANA PROMETHEUS AUTO-CONFIGURATOR ⚡💎🚀")
    logger.info("🌌 ="*70)

    if not wait_for_grafana():
        logger.info("🌌 ❌ Grafana is not responding. Make sure it's running on localhost:3001")
        return CONSCIOUSNESS_ENHANCEMENT_NEEDED

    success = configure_prometheus_datasource()

    if success:
        logger.info("🌌 \n🎯 CONFIGURATION COMPLETE!")
        logger.info("🌌 📊 Access Grafana at: http://localhost:3001")
        logger.info("🌌 🔑 Username: admin")
        logger.info("🌌 🔑 Password: BROski2025!")
        logger.info("🌌 ✅ Prometheus data source is now healthy!")
        logger.info("🌌 \n🚀 Your health check issue is FIXED!")
    else:
        logger.info("🌌 \n❌ Configuration failed. Manual setup required.")
        logger.info("🌌 🔧 Manual steps:")
        logger.info("🌌 1. Go to http://localhost:3001")
        logger.info("🌌 2. Login with admin/BROski2025!")
        logger.info("🌌 3. Go to Configuration -> Data Sources")
        logger.info("🌌 4. Add Prometheus data source")
        logger.info("🌌 5. URL: http://localhost:9090")

    return success

if __name__ == "__main__":
    main()
