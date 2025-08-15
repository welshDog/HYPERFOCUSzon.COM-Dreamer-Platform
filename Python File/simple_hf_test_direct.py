import sys
sys.stdout.reconfigure(encoding='utf-8')
print("🚀 Testing HF Integration...")

try:
    from huggingface_hub import InferenceClient
    
    # Direct token (confirmed from empire.env)
    hf_token = "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"
    
    print(f"🔑 Using token: {hf_token[:10]}...{hf_token[-10:]}")
    
    # Create client
    client = InferenceClient(token=hf_token)
    
    # Simple test
    response = client.text_generation(
        prompt="Hello! How are you today?",
        model="microsoft/DialoGPT-medium",
        max_new_tokens=50
    )
    
    print(f"✅ HF Response: {response}")
    print("🎊💎⚡ EMPIRE HF INTEGRATION: SUCCESS! ⚡💎🎊")
    
except Exception as e:
    print(f"❌ Error: {e}")
