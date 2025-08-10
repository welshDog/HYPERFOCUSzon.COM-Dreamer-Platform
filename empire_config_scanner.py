#!/usr/bin/env python3
"""
🔍💎⚡ EMPIRE CONFIGURATION SCANNER ⚡💎🔍

Scans existing empire setup and provides optimization recommendations
"""

from pathlib import Path
import os
def scan_empire_configuration():
    """🔍 Scan existing empire configuration"""
    print('🔍 SCANNING EXISTING EMPIRE CONFIGURATION...')
    print('=' * 50)

    # Check for existing empire.env
    empire_env_path = Path('HyperBeast/empire.env')
    if empire_env_path.exists():
        print('✅ Empire configuration found!')
        print('📍 Location: HyperBeast/empire.env')
        print(f'📏 File size: {empire_env_path.stat().st_size} bytes')

        try:
            # Read with UTF-8 encoding
            with open(empire_env_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except (ConnectionError, OSError):
            # Fallback to reading as binary and decoding
            with open(empire_env_path, 'rb') as f:
                content = f.read().decode('utf-8', errors='ignore')

        # Check key components
        checks = {
            'Discord Bot Token': 'DISCORD_BOT_TOKEN=' in content and len([line for line in content.split('\n') if line.startswith('DISCORD_BOT_TOKEN=')]) > 0,
            'Database Config': 'POSTGRES_PASSWORD=' in content,
            'OpenAI API': 'OPENAI_API_KEY=' in content,
            'HYPERFOCUS Mode': 'HYPERFOCUS_MODE=True' in content or 'HYPERFOCUS_MODE=true' in content,
            'Legendary Mode': 'LEGENDARY_MODE=true' in content,
            'Agent Army': 'AGENT_ARMY_SIZE=' in content,
            'Port Configuration': 'SYNC_DASHBOARD_PORT=9999' in content,
            'AI Enhancement': 'AI_BRAIN_AMPLIFIER_ACTIVE=true' in content
        }

        print('\n🏆 EMPIRE COMPONENT STATUS:')
        for component, status in checks.items():
            status_icon = '✅' if status else '⚠️'
            print(f'  {status_icon} {component}: {'CONFIGURED' if status else 'MISSING'}')

        active_count = sum(checks.values())
        readiness_percent = (active_count/len(checks))*100

        print(f'\n📊 Empire Configuration Readiness: {active_count}/{len(checks)} components ({readiness_percent:.1f}%)')

        # Status determination
        if readiness_percent >= 90:
            status = "🏆 LEGENDARY READY"
        elif readiness_percent >= 70:
            status = "🚀 DEPLOYMENT READY"
        else:
            status = "⚠️ NEEDS OPTIMIZATION"

        print(f'🎯 Empire Status: {status}')

        return active_count, len(checks), content

    else:
        print('⚠️ Empire configuration not found in HyperBeast/empire.env')
        return 0, 0, ""

def create_optimized_v2_launcher():
    """🚀 Create V2 launcher using existing empire configuration"""
    print('\n🚀 CREATING OPTIMIZED V2 DEPLOYMENT LAUNCHER...')
    print('=' * 50)

    # Enhanced V2 launcher that uses existing configuration
    launcher_content = '''#!/usr/bin/env python3
"""
🚀💎⚡ LEGENDARY V2 DEPLOYMENT WITH EMPIRE CONFIG ⚡💎🚀

Uses your existing empire.env configuration for full deployment
"""

import os
from pathlib import Path

def load_empire_config():
    """📋 Load configuration from empire.env"""
    empire_env_path = Path('HyperBeast/empire.env')
    config = {}

    if empire_env_path.exists():
        try:
            with open(empire_env_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    if '=' in line and not line.startswith('#'):
                        key, value = line.strip().split('=', 1)
                        config[key] = value
        except (socket.error, ConnectionError, requests.RequestException) as e:
            print(f"⚠️ Error reading empire config: {e}")

    return config

def start_v2_deployment():
    """🎯 Start V2 deployment with empire configuration"""
    print('🏆💎⚡ LEGENDARY V2 DEPLOYMENT ACTIVATOR ⚡💎🏆')
    print('=' * 60)

    config = load_empire_config()

    # Get ports from config or use defaults
    dashboard_port = config.get('SYNC_DASHBOARD_PORT', '9999')
    websocket_port = config.get('WEBSOCKET_PORT', '8765')

    print(f'📊 Analytics Dashboard Port: {dashboard_port}')
    print(f'🔌 WebSocket Server Port: {websocket_port}')
    print(f'🤖 Discord Bot: {'CONFIGURED' if config.get('DISCORD_BOT_TOKEN') else 'NOT CONFIGURED'}')
    print(f'💾 Database: {'CONFIGURED' if config.get('POSTGRES_PASSWORD') else 'NOT CONFIGURED'}')
    print(f'🧠 AI Enhancement: {'ACTIVE' if config.get('AI_BRAIN_AMPLIFIER_ACTIVE') == 'true' else 'INACTIVE'}')
    print(f'⚡ HYPERFOCUS Mode: {'ACTIVE' if config.get('HYPERFOCUS_MODE') == 'True' else 'INACTIVE'}')

    print('\\n🚀 STARTING V2 COMPONENTS...')

    # Start analytics dashboard
    print('📊 Starting Analytics Dashboard...')
    try:
        subprocess.Popen([
            sys.executable, 'v2_analytics_server.py'
        ], creationflags=subprocess.CREATE_NEW_CONSOLE if os.name == 'nt' else 0)
        print(f'✅ Dashboard starting on http://localhost:{dashboard_port}')
    except (socket.error, ConnectionError, requests.RequestException) as e:
        print(f'❌ Dashboard error: {e}')

    # Start WebSocket server
    print('🔌 Starting WebSocket Server...')
    try:
        subprocess.Popen([
            sys.executable, 'v2_websocket_server.py'
        ], creationflags=subprocess.CREATE_NEW_CONSOLE if os.name == 'nt' else 0)
        print(f'✅ WebSocket starting on ws://localhost:{websocket_port}')
    except (socket.error, ConnectionError, requests.RequestException) as e:
        print(f'❌ WebSocket error: {e}')

    print('\\n🏆 V2 DEPLOYMENT LAUNCH COMPLETE!')
    print('=' * 40)
    print(f'🌐 Dashboard: http://localhost:{dashboard_port}')
    print(f'🔌 WebSocket: ws://localhost:{websocket_port}')
    print('💡 Check the new console windows for server status')

    return True

if __name__ == "__main__":
    start_v2_deployment()
'''

    with open('legendary_v2_launcher.py', 'w') as f:
        f.write(launcher_content)

    print('✅ Created: legendary_v2_launcher.py')
    return True

if __name__ == "__main__":
    active, total, content = scan_empire_configuration()
    if active > 0:
        create_optimized_v2_launcher()
        print(f'\n🎯 READY TO ACTIVATE YOUR LEGENDARY EMPIRE!')
        print(f'📋 Run: H:/.venv/Scripts/python.exe legendary_v2_launcher.py')
    else:
        print(f'\n⚠️ Empire configuration needs setup first')
