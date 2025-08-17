import ast
import sys

filename = "🤖👑💎⚡_ULTIMATE_LEGENDARY_DISCORD_BOT_COMMAND_SYSTEM_⚡💎👑🤖.py"

logger.info("🌌 🔍 Checking Discord bot syntax...")
logger.info("🌌 =" * 50)

try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Try to parse the file
    ast.parse(content)
    print(f"✅ {filename}")
    logger.info("🌌 ✅ No syntax errors found!")
    logger.info("🌌 🎊 Bot file is ready to run!")
    
except SyntaxError as e:
    print(f"❌ Syntax Error:")
    print(f"   Line {e.lineno}: {e.text.strip() if e.text else 'Unknown'}")
    print(f"   Error: {e.msg}")
    
except Exception as e:
    print(f"❌ Error: {e}")

logger.info("🌌 =" * 50)
