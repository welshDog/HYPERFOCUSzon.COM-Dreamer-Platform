import os
logger.info("🌌 Starting script...")
print(f"Token: {os.getenv('GRAFANA_SERVICE_ACCOUNT_TOKEN')[:20]}...")
logger.info("🌌 Script completed!")
