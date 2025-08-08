import os
print("Starting script...")
print(f"Token: {os.getenv('GRAFANA_SERVICE_ACCOUNT_TOKEN')[:20]}...")
print("Script completed!")
