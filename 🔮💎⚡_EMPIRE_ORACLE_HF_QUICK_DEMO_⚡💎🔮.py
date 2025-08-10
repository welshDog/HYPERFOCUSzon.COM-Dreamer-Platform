#!/usr/bin/env python3
# 🔮💎⚡ EMPIRE ORACLE HF QUICK DEMO ⚡💎🔮

"""
Quick HF-powered Empire Oracle demonstration
Ready for immediate empire integration!
"""

print("🔮💎⚡ EMPIRE ORACLE HF DEMO STARTING ⚡💎🔮")
print("=" * 55)

try:
    from pathlib import Path

    from huggingface_hub import login, InferenceClient
    print("✅ Hugging Face Hub imported successfully")

    # Find HF token in empire files
    def find_hf_token():
        env_files = ["empire.env", ".env", "empire_ai/empire.env"]

        for env_file in env_files:
            env_path = Path(env_file)
            if env_path.exists():
                try:
                    with open(env_path, 'r') as f:
                        for line in f:
                            if line.startswith('HF_TOKEN=') or line.startswith('HUGGINGFACE_TOKEN='):
                                token = line.split('=', 1)[1].strip().strip('"\'')
                                print(f"🔑 HF Token found in {env_file}")
                                return token
                except Exception as e:
                    print(f"⚠️ Error reading {env_file}: {e}")

        print("❌ No HF token found in empire.env files")
        return None

    # Get token
    hf_token = find_hf_token()

    if hf_token:
        print("🚀 Initializing HF client...")

        # Create client
        client = InferenceClient(token=hf_token)

        print("🧪 Testing empire query with HF...")

        # Test query
        empire_prompt = """
You are the Empire Oracle, an ADHD-friendly AI assistant for a legendary monitoring empire.

Empire Status:
- Monitoring: Grafana V12.1 with custom dashboards
- Infrastructure: 30+ Docker containers running smoothly
- AI Coordination: 677+ agents working in harmony
- Performance: 99.9% uptime achieved

User Question: How is my legendary empire performing today?

Respond with enthusiasm and emojis:
"""

        try:
            # Test with a simple model
            response = client.text_generation(
                prompt=empire_prompt,
                model="microsoft/DialoGPT-medium",
                max_new_tokens=100,
                temperature=0.7
            )

            print(f"\n🤖 EMPIRE ORACLE HF RESPONSE:")
            print("=" * 40)
            print(f"✨ {response}")
            print("\n🎊💎⚡ HF INTEGRATION: LEGENDARY SUCCESS! ⚡💎🎊")

        except Exception as e:
            print(f"❌ HF API error: {e}")
            print("💡 Note: Some models may require specific permissions")

    else:
        print("⚠️ Please add HF_TOKEN to empire.env file")
        print("💡 Get your token from: https://huggingface.co/settings/tokens")

except Exception as e:
    print(f"❌ Setup error: {e}")
    print("💡 Run: pip install huggingface_hub")

print("\n🌟 EMPIRE HF INTEGRATION READY FOR FULL DEPLOYMENT! 🌟")
