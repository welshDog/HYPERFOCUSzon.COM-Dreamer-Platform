logger.info("🌌 🚀 HYPER TEAM HF INTEGRATION STARTING...")

# Basic test
try:
    from huggingface_hub import login
    logger.info("🌌 ✅ HF import successful")
except Exception as e:
    print(f"❌ HF import failed: {e}")

logger.info("🌌 🎊 Test complete!")
