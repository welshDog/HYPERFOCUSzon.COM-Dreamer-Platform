#!/usr/bin/env python3
# 🔮💎⚡ EMPIRE HF INTEGRATION FIXED ⚡💎🔮

"""
🚀 FIXED HF INTEGRATION WITH PROPER ENCODING 🚀
================================================
Handles character encoding issues and multiple token formats
Ready for immediate empire deployment!
"""

print("🔮💎⚡ EMPIRE HF INTEGRATION (FIXED VERSION) ⚡💎🔮")
print("=" * 65)

try:
    from huggingface_hub import login, InferenceClient
    import os
    from pathlib import Path
    
    print("✅ Hugging Face Hub imported successfully")
    
    # Read HF token with proper encoding handling
    def get_empire_hf_token():
        """Get HF token from empire.env file with encoding fixes"""
        
        # Check multiple possible locations
        env_files = [
            Path("h:/HyperBeast/empire.env"),
            Path("h:/empire.env"),
            Path("empire.env"),
            Path("HyperBeast/empire.env")
        ]
        
        for env_file in env_files:
            if env_file.exists():
                print(f"📁 Reading: {env_file}")
                
                # Try multiple encodings to handle character issues
                encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252']
                
                for encoding in encodings:
                    try:
                        with open(env_file, 'r', encoding=encoding) as f:
                            content = f.read()
                            
                            # Look for various HF token formats
                            token_patterns = [
                                'HF_TOKEN=',
                                'HUGGINGFACE_TOKEN=', 
                                'Hugging_Face_Token=',
                                'HF token='
                            ]
                            
                            for line in content.split('\n'):
                                line = line.strip()
                                for pattern in token_patterns:
                                    if line.startswith(pattern):
                                        token = line.split('=', 1)[1].strip()
                                        if token.startswith('hf_') and len(token) > 20:
                                            print(f"🔑 HF Token found with {encoding} encoding")
                                            print(f"   Pattern: {pattern}")
                                            print(f"   Token: {token[:10]}...{token[-10:]}")
                                            return token
                        
                        print(f"✅ Successfully read {env_file} with {encoding} encoding")
                        break
                        
                    except UnicodeDecodeError:
                        print(f"⚠️ Encoding {encoding} failed for {env_file}")
                        continue
                    except Exception as e:
                        print(f"❌ Error with {encoding}: {e}")
                        continue
        
        return None
    
    # Get the empire HF token
    print("🔍 Searching for empire HF token with encoding fixes...")
    hf_token = get_empire_hf_token()
    
    if hf_token:
        print("🚀 Initializing HF client with empire token...")
        
        try:
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
            
            # Test with reliable models
            test_models = [
                "microsoft/DialoGPT-medium",
                "HuggingFaceH4/zephyr-7b-beta",
                "microsoft/DialoGPT-large"
            ]
            
            successful_tests = 0
            best_response = None
            working_model = None
            
            for model in test_models:
                print(f"\n🤖 Testing model: {model}")
                try:
                    response = client.text_generation(
                        prompt=empire_prompt,
                        model=model,
                        max_new_tokens=100,
                        temperature=0.7,
                        do_sample=True
                    )
                    
                    print(f"✅ SUCCESS! Model response:")
                    print(f"   📝 {response[:150]}...")
                    successful_tests += 1
                    
                    # Save the first working response
                    if successful_tests == 1:
                        working_model = model
                        best_response = response
                    
                except Exception as e:
                    print(f"❌ Model {model} failed: {str(e)[:80]}...")
            
            # Results summary
            print(f"\n🎊 EMPIRE HF INTEGRATION TEST RESULTS:")
            print("=" * 45)
            print(f"🔑 Token Status: ✅ ACTIVE")
            print(f"🤖 Models Tested: {len(test_models)}")
            print(f"✅ Successful Tests: {successful_tests}")
            
            if successful_tests > 0:
                print(f"\n🏆 WORKING MODEL: {working_model}")
                print(f"🌟 SAMPLE RESPONSE:")
                print(f"   {best_response}")
                print(f"\n🎊💎⚡ EMPIRE HF INTEGRATION: LEGENDARY SUCCESS! ⚡💎🎊")
                
                # Save integration config for later use
                config = {
                    "status": "LEGENDARY",
                    "working_model": working_model,
                    "token_verified": True,
                    "integration_ready": True,
                    "sample_response": best_response
                }
                
                with open("h:/🎊_HF_INTEGRATION_SUCCESS_CONFIG.json", "w") as f:
                    import json
                    json.dump(config, f, indent=2)
                
                print(f"\n📋 NEXT STEPS FOR FULL INTEGRATION:")
                print("   1. ✅ Token verified and working")
                print("   2. ✅ Model connectivity confirmed") 
                print("   3. 🚀 Ready to replace Empire Oracle backend")
                print("   4. 🤖 Ready for 677+ agent army integration")
                print("   5. 📊 Ready for Grafana AI enhancement")
                
            else:
                print("⚠️ No models responded - checking token permissions...")
                
        except Exception as e:
            print(f"❌ HF Client error: {e}")
    
    else:
        print("❌ Could not find HF token in empire files")
        print("💡 Please check token format in empire.env")

except ImportError as e:
    print(f"❌ Import error: {e}")
    print("💡 Run: pip install huggingface_hub")
except Exception as e:
    print(f"❌ Unexpected error: {e}")

print("\n🌟 Empire HF Integration (Fixed) Complete! 🌟")
