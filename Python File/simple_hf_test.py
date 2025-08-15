print("🚀 HYPER TEAM HF INTEGRATION STARTING...")

# Basic test
try:
    from huggingface_hub import login
    print("✅ HF import successful")
except Exception as e:
    print(f"❌ HF import failed: {e}")

print("🎊 Test complete!")
