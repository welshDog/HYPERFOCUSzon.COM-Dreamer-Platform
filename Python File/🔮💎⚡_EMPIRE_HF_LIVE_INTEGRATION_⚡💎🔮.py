#!/usr/bin/env python3
# 🔮💎⚡ EMPIRE ORACLE HF INTEGRATION LIVE DEMO ⚡💎🔮

"""
🚀 LIVE HF INTEGRATION WITH EMPIRE TOKEN 🚀
============================================
Uses the confirmed HF token from empire.env
Ready for immediate empire deployment!
"""

print("🔮💎⚡ EMPIRE ORACLE HF INTEGRATION STARTING ⚡💎🔮")
print("=" * 60)

try:
    from pathlib import Path

    from huggingface_hub import login, InferenceClient
    print("✅ Hugging Face Hub imported successfully")

    # Read HF token from empire.env
    def get_empire_hf_token():
        """Get HF token from empire.env file"""

        # Check multiple possible locations
        env_files = [
            "empire.env",
            "HyperBeast/empire.env",
            Path("h:/HyperBeast/empire.env"),
            Path("h:/empire.env")
        ]

        for env_file in env_files:
            env_path = Path(env_file)
            if env_path.exists():
                print(f"📁 Reading: {env_path}")
                try:
                    with open(env_path, 'r') as f:
                        for line in f:
                            # Look for the exact token format from empire.env
                            if line.startswith('Hugging_Face_Token='):
                                token = line.split('=', 1)[1].strip()
                                print(f"🔑 HF Token found: {token[:10]}...{token[-10:]}")
                                return token
                            elif line.startswith('HF_TOKEN='):
                                token = line.split('=', 1)[1].strip()
                                print(f"🔑 HF Token found: {token[:10]}...{token[-10:]}")
                                return token
                except Exception as e:
                    print(f"⚠️ Error reading {env_file}: {e}")
            else:
                print(f"❌ Not found: {env_file}")

        return None

    # Get the empire HF token
    print("🔍 Searching for empire HF token...")
    hf_token = get_empire_hf_token()

    if hf_token:
        print("🚀 Initializing HF client with empire token...")

        # Create InferenceClient with empire token
        client = InferenceClient(token=hf_token)

        print("🧪 Testing empire query with HF models...")

        # Empire-specific prompt
        empire_prompt = """You are the Empire Oracle, an ADHD-friendly AI assistant for a legendary monitoring empire.

Empire Status:
- Monitoring: Grafana V12.1 with custom dashboards
- Infrastructure: 30+ Docker containers running smoothly
- AI Coordination: 677+ agents working in harmony
- Performance: 99.9% uptime achieved
- Empire Mode: LEGENDARY

User Question: How is my legendary empire performing today?

Respond with enthusiasm, emojis, and actionable empire insights:"""

        # Test different models
        test_models = [
            "microsoft/DialoGPT-medium",
            "microsoft/DialoGPT-large",
            "facebook/blenderbot-400M-distill"
        ]

        successful_tests = 0

        for model in test_models:
            print(f"\n🤖 Testing model: {model}")
            try:
                response = client.text_generation(
                    prompt=empire_prompt,
                    model=model,
                    max_new_tokens=120,
                    temperature=0.7
                )

                print(f"✅ SUCCESS! Model response:")
                print(f"   📝 {response[:200]}...")
                successful_tests += 1

                # Save the working model for later use
                if successful_tests == 1:
                    working_model = model
                    working_response = response

            except Exception as e:
                print(f"❌ Model {model} failed: {str(e)[:100]}...")

        # Results summary
        print(f"\n🎊 EMPIRE HF INTEGRATION TEST RESULTS:")
        print("=" * 45)
        print(f"🔑 Token Status: ✅ ACTIVE")
        print(f"🤖 Models Tested: {len(test_models)}")
        print(f"✅ Successful Tests: {successful_tests}")

        if successful_tests > 0:
            print(f"\n🏆 WORKING MODEL: {working_model}")
            print(f"🌟 SAMPLE RESPONSE:")
            print(f"   {working_response}")
            print(f"\n🎊💎⚡ EMPIRE HF INTEGRATION: LEGENDARY SUCCESS! ⚡💎🎊")

            # Create quick integration guide
            print(f"\n📋 NEXT STEPS FOR FULL INTEGRATION:")
            print("   1. Replace Empire Oracle static responses with HF")
            print("   2. Integrate with agent army coordination")
            print("   3. Add to Grafana dashboard queries")
            print("   4. Deploy to empire production systems")

        else:
            print("⚠️ No models responded successfully - may need API permissions")

    else:
        print("❌ Could not find HF token in empire files")
        print("💡 Expected format: Hugging_Face_Token=hf_...")

except ImportError as e:
    print(f"❌ Import error: {e}")
    print("💡 Run: pip install huggingface_hub")
except Exception as e:
    print(f"❌ Unexpected error: {e}")

print("\n🌟 Empire HF Integration Demo Complete! 🌟")
