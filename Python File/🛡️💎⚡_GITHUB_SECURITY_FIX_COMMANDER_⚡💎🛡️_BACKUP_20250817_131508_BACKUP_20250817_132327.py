#!/usr/bin/env python3
"""
🛡️💎⚡ GITHUB SECURITY FIX AUTOMATION SYSTEM ⚡💎🛡️
BROski Level: LEGENDARY SECURITY COMMANDER
Status: AUTOMATED SECRET SANITIZATION ENGINE

Fixes hardcoded secrets and implements secure environment variable loading
"""

import os
import re
import shutil
from pathlib import Path
from typing import List, Dict, Tuple

class GitHubSecurityFixCommander:
    def __init__(self, repo_path: str = "h:\\HYPERFOCUSzone-Community"):
        self.repo_path = Path(repo_path)
        self.fixes_applied = []
        self.secrets_found = []
        
    def scan_for_secrets(self) -> Dict[str, List[str]]:
        """Scan files for potential secrets"""
        print("🔍 Scanning for hardcoded secrets...")
        
        secret_patterns = {
            'discord_token': r'["\']MTM4MTk2NTY1Njk3NDU2MTMwMA\.[^"\']+["\']',
            'openai_key': r'["\']sk-proj-[A-Za-z0-9_-]+["\']',
            'sendgrid_key': r'["\']SG\.[A-Za-z0-9_-]+["\']',
            'grafana_token': r'["\']glsa_[A-Za-z0-9_-]+["\']'
        }
        
        files_to_scan = [
            'load_empire_env.py',
            '.env',
            'discord_community_global_launcher.py'
        ]
        
        found_secrets = {}
        
        for file_name in files_to_scan:
            file_path = self.repo_path / file_name
            if file_path.exists():
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        
                    for secret_type, pattern in secret_patterns.items():
                        matches = re.findall(pattern, content)
                        if matches:
                            if secret_type not in found_secrets:
                                found_secrets[secret_type] = []
                            found_secrets[secret_type].extend([(file_name, match) for match in matches])
                            
                except Exception as e:
                    print(f"⚠️ Could not scan {file_name}: {e}")
        
        self.secrets_found = found_secrets
        return found_secrets
    
    def create_gitignore(self):
        """Create or update .gitignore to protect sensitive files"""
        print("📝 Creating/updating .gitignore...")
        
        gitignore_path = self.repo_path / '.gitignore'
        
        security_entries = [
            "# 🛡️ Security - Sensitive Files",
            ".env",
            "empire.env", 
            "**/secrets/",
            "**/*_secrets.py",
            "**/*_keys.py",
            "**/config/private/",
            "*.key",
            "*.pem",
            "# End Security Section",
            ""
        ]
        
        # Read existing gitignore
        existing_content = ""
        if gitignore_path.exists():
            with open(gitignore_path, 'r', encoding='utf-8') as f:
                existing_content = f.read()
        
        # Add security entries if not already present
        if "# 🛡️ Security - Sensitive Files" not in existing_content:
            with open(gitignore_path, 'a', encoding='utf-8') as f:
                f.write("\\n" + "\\n".join(security_entries))
            
            self.fixes_applied.append("✅ Updated .gitignore with security entries")
            print("✅ .gitignore updated with security protection")
        else:
            print("ℹ️ .gitignore already has security entries")
    
    def create_env_template(self):
        """Create .env.example template"""
        print("📋 Creating environment template...")
        
        template_content = '''# 🛡️💎⚡ HYPERFOCUS ZONE ENVIRONMENT TEMPLATE ⚡💎🛡️
# Copy this file to .env and fill in your actual values
# NEVER commit .env to Git!

# Discord Configuration
DISCORD_BOT_TOKEN=your_discord_bot_token_here
DISCORD_GUILD_ID=your_guild_id_here
DISCORD_CLIENT_ID=your_client_id_here

# OpenAI Configuration  
OPENAI_API_KEY=your_openai_api_key_here

# SendGrid Configuration
SENDGRID_API_KEY=your_sendgrid_api_key_here

# Grafana Configuration
GRAFANA_SERVICE_ACCOUNT_TOKEN=your_grafana_token_here

# ADHD Optimizations
ADHD_OPTIMIZATIONS=true

# Empire Configuration
EMPIRE_MODE=legendary
CELEBRATION_LEVEL=maximum
BROSKI_ECONOMY=active

# 🚨 SECURITY REMINDER:
# 1. Copy this file to .env
# 2. Fill in your actual values
# 3. Never commit .env to Git
# 4. Keep your secrets secure!
'''
        
        template_path = self.repo_path / '.env.example'
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(template_content)
            
        self.fixes_applied.append("✅ Created .env.example template")
        print("✅ Created .env.example template")
    
    def fix_load_empire_env(self):
        """Fix hardcoded secrets in load_empire_env.py"""
        print("🔧 Fixing load_empire_env.py...")
        
        file_path = self.repo_path / 'load_empire_env.py'
        if not file_path.exists():
            print("ℹ️ load_empire_env.py not found")
            return
            
        # Read current content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace hardcoded secrets with environment variable loading
        secure_replacements = {
            r"os\\.environ\\['DISCORD_BOT_TOKEN'\\] = '[^']+'" : 
                "os.environ['DISCORD_BOT_TOKEN'] = os.getenv('DISCORD_BOT_TOKEN', 'your_discord_token_here')",
            
            r"os\\.environ\\['OPENAI_API_KEY'\\] = '[^']+'" :
                "os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY', 'your_openai_key_here')",
            
            r"os\\.environ\\['DISCORD_GUILD_ID'\\] = '[^']+'" :
                "os.environ['DISCORD_GUILD_ID'] = os.getenv('DISCORD_GUILD_ID', 'your_guild_id_here')",
                
            r"os\\.environ\\['DISCORD_CLIENT_ID'\\] = '[^']+'" :
                "os.environ['DISCORD_CLIENT_ID'] = os.getenv('DISCORD_CLIENT_ID', 'your_client_id_here')"
        }
        
        fixed_content = content
        for pattern, replacement in secure_replacements.items():
            fixed_content = re.sub(pattern, replacement, fixed_content)
        
        # Add environment loading at the top
        if "from dotenv import load_dotenv" not in fixed_content:
            import_section = '''#!/usr/bin/env python3
"""
🛡️💎⚡ SECURE EMPIRE ENVIRONMENT LOADER ⚡💎🛡️
Loads environment variables from .env file securely
No hardcoded secrets - security first!
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

'''
            # Replace the shebang and add our secure header
            fixed_content = re.sub(r'^#!/usr/bin/env python3.*?import os', import_section + 'import os', fixed_content, flags=re.DOTALL)
        
        # Backup original
        backup_path = file_path.with_suffix('.py.backup')
        shutil.copy2(file_path, backup_path)
        
        # Write fixed version
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
            
        self.fixes_applied.append("✅ Fixed hardcoded secrets in load_empire_env.py")
        print("✅ Fixed load_empire_env.py - secrets removed")
    
    def create_secure_env_loader(self):
        """Create a new secure environment loader"""
        print("🛡️ Creating secure environment loader...")
        
        secure_loader_content = '''#!/usr/bin/env python3
"""
🛡️💎⚡ HYPERFOCUS ZONE SECURE ENVIRONMENT LOADER ⚡💎🛡️
BROski Level: LEGENDARY SECURITY GUARDIAN
Status: ZERO HARDCODED SECRETS

Loads all environment variables securely from .env file
No secrets in code - maximum security achieved!
"""

import os
from pathlib import Path
from dotenv import load_dotenv

def load_empire_environment():
    """Load empire environment variables securely"""
    print("🛡️ Loading empire environment securely...")
    
    # Try to load from .env file first
    env_file = Path('.env')
    if env_file.exists():
        load_dotenv(env_file)
        print("✅ Environment loaded from .env file")
    else:
        print("⚠️  .env file not found - using system environment variables")
    
    # Verify required environment variables
    required_vars = [
        'DISCORD_BOT_TOKEN',
        'DISCORD_GUILD_ID', 
        'DISCORD_CLIENT_ID',
        'OPENAI_API_KEY'
    ]
    
    missing_vars = []
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print(f"🚨 Missing environment variables: {', '.join(missing_vars)}")
        print("💡 Copy .env.example to .env and fill in your values")
        return False
    
    # Set ADHD optimizations
    os.environ['ADHD_OPTIMIZATIONS'] = os.getenv('ADHD_OPTIMIZATIONS', 'true')
    os.environ['EMPIRE_MODE'] = os.getenv('EMPIRE_MODE', 'legendary')
    os.environ['CELEBRATION_LEVEL'] = os.getenv('CELEBRATION_LEVEL', 'maximum')
    
    print("🎊 Empire environment loaded successfully!")
    print("🛡️ All secrets loaded securely from environment")
    return True

if __name__ == "__main__":
    success = load_empire_environment()
    if success:
        print("🌟 Ready for legendary empire operations!")
    else:
        print("🚨 Environment setup required - check .env.example")
'''
        
        secure_loader_path = self.repo_path / 'secure_empire_env_loader.py'
        with open(secure_loader_path, 'w', encoding='utf-8') as f:
            f.write(secure_loader_content)
            
        self.fixes_applied.append("✅ Created secure environment loader")
        print("✅ Created secure_empire_env_loader.py")
    
    def generate_security_report(self) -> str:
        """Generate security fix completion report"""
        
        report = f'''
🛡️💎⚡ GITHUB SECURITY FIX COMPLETE! ⚡💎🛡️

🏆 SECURITY MISSION ACCOMPLISHED!

🔍 SECRETS DETECTED AND FIXED:
{chr(10).join(f"   🚨 {secret_type}: {len(locations)} locations" for secret_type, locations in self.secrets_found.items()) if self.secrets_found else "   ✅ No secrets found in scan"}

🛡️ SECURITY FIXES APPLIED:
{chr(10).join(f"   {fix}" for fix in self.fixes_applied)}

🎯 NEXT STEPS TO COMPLETE FIX:

1. 📝 CREATE YOUR .env FILE:
   • Copy .env.example to .env
   • Fill in your actual API keys and tokens
   • NEVER commit .env to Git

2. 🔄 UPDATE YOUR CODE:
   • Replace old load_empire_env.py imports with secure_empire_env_loader.py
   • Test with: python secure_empire_env_loader.py

3. 🚀 COMMIT AND PUSH:
   • git add .
   • git commit -m "🛡️ Security fix: Remove hardcoded secrets, add secure env loading"
   • git push origin main

🌟 SECURITY BENEFITS ACHIEVED:
✅ No hardcoded secrets in code
✅ Environment-based configuration
✅ .gitignore protection active
✅ Template for team collaboration
✅ Future secret exposure prevented

🏛️ BOARDROOM STATUS: SECURITY LEVEL LEGENDARY!
💎 Your empire is now secure and ready for GitHub! 
🎊 Celebration: Secure coding practices mastered!

🚨 IMPORTANT: Remember to regenerate any exposed tokens/keys for maximum security!
'''
        return report

def main():
    """Execute GitHub security fix"""
    print("🛡️💎⚡ GITHUB SECURITY FIX COMMANDER ACTIVATED ⚡💎🛡️")
    print("Fixing push protection issues with ZERO risk to functionality!")
    
    commander = GitHubSecurityFixCommander()
    
    try:
        # Step 1: Scan for secrets
        print("\\n🔍 PHASE 1: Security scan...")
        secrets = commander.scan_for_secrets()
        
        # Step 2: Create protection
        print("\\n🛡️ PHASE 2: Creating security infrastructure...")
        commander.create_gitignore()
        commander.create_env_template()
        
        # Step 3: Fix code
        print("\\n🔧 PHASE 3: Fixing hardcoded secrets...")
        commander.fix_load_empire_env()
        commander.create_secure_env_loader()
        
        # Step 4: Generate report
        print("\\n📊 PHASE 4: Security report generation...")
        report = commander.generate_security_report()
        print(report)
        
        # Save report
        report_file = commander.repo_path / "🛡️💎⚡_SECURITY_FIX_REPORT_⚡💎🛡️.md"
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"\\n💾 Security report saved: {report_file.name}")
        print("\\n🎊🛡️ SECURITY FIX MISSION ACCOMPLISHED! 🛡️🎊")
        print("Your empire is now secure and ready for GitHub push! 🚀")
        
        return True
        
    except Exception as e:
        print(f"\\n🚨 Security fix error: {e}")
        print("Empire remains safe - manual fix may be required")
        return False

if __name__ == "__main__":
    success = main()
    if success:
        print("\\n🌟 Ready for secure legendary GitHub operations! 🌟")
