#!/usr/bin/env python3
"""
Quick syntax checker for the Discord bot
"""
import ast
import sys

def check_syntax(filename):
    """Check Python file for syntax errors"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Try to parse the file
        ast.parse(content)
        print(f"✅ {filename} - No syntax errors found!")
        return True
        
    except SyntaxError as e:
        print(f"❌ Syntax Error in {filename}:")
        print(f"   Line {e.lineno}: {e.text.strip() if e.text else 'Unknown'}")
        print(f"   Error: {e.msg}")
        return False
        
    except Exception as e:
        print(f"❌ Error checking {filename}: {e}")
        return False

if __name__ == "__main__":
    filename = "🤖👑💎⚡_ULTIMATE_LEGENDARY_DISCORD_BOT_COMMAND_SYSTEM_⚡💎👑🤖.py"
    
    print("🔍 Checking Discord bot syntax...")
    print("=" * 50)
    
    if check_syntax(filename):
        print("🎊 Bot file is ready to run!")
    else:
        print("⚠️ Please fix syntax errors before running the bot.")
    
    print("=" * 50)
