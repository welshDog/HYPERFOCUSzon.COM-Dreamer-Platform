print("🌟💎⚡ HYPERFOCUS EMPIRE HF QUICK TEST ⚡💎🌟")

# Test 1: Import check
try:
    from huggingface_hub import HfApi, InferenceClient

    print("✅ SUCCESS: Hugging Face Hub imported!")
    hf_available = True
except ImportError as e:
    print(f"❌ FAILED: {e}")
    hf_available = False

# Test 2: Token check
import os

token_found = False
env_file = "h:/HyperBeast/empire.env"
if os.path.exists(env_file):
    with open(env_file, "r") as f:
        content = f.read()
        if "HF_TOKEN=" in content:
            print("✅ SUCCESS: HF Token found in empire.env!")
            token_found = True
        else:
            print("⚠️ WARNING: No HF_TOKEN in empire.env")
else:
    print("⚠️ WARNING: empire.env not found")

# Summary
print("\n🎊 ACTIVATION SUMMARY:")
print(f"📦 HF Library: {'✅ READY' if hf_available else '❌ MISSING'}")
print(f"🔑 HF Token: {'✅ READY' if token_found else '❌ MISSING'}")

if hf_available and token_found:
    print("🚀 STATUS: READY FOR FULL HF EMPIRE INTEGRATION!")
elif hf_available:
    print("⚡ STATUS: READY FOR FREE-TIER HF FEATURES!")
else:
    print("🔧 STATUS: NEEDS SETUP")

print("🏆 EMPIRE HF TEST COMPLETE!")
