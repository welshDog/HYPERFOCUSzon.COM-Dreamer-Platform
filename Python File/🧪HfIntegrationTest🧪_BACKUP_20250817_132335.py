#!/usr/bin/env python3
# 🚀💎⚡ HYPER TEAM HF INTEGRATION TEST ⚡💎🚀

"""
Quick test to verify HF integration capabilities
"""

def test_hf_imports():
    """Test HF imports"""
    print("🧪 Testing Hugging Face imports...")
    
    try:
        from huggingface_hub import login, InferenceClient, HfApi
        print("✅ HF imports successful!")
        return True
    except Exception as e:
        print(f"❌ HF import error: {e}")
        return False

def test_empire_env():
    """Test empire.env file reading"""
    print("🧪 Testing empire.env access...")
    
    import os
    from pathlib import Path
    
    env_files = [
        "empire.env",
        ".env", 
        "empire_ai/empire.env"
    ]
    
    token_found = False
    
    for env_file in env_files:
        env_path = Path(env_file)
        if env_path.exists():
            print(f"📁 Found: {env_file}")
            try:
                with open(env_path, 'r') as f:
                    content = f.read()
                    if 'HF_TOKEN=' in content or 'HUGGINGFACE_TOKEN=' in content:
                        print(f"🔑 HF token found in {env_file}")
                        token_found = True
                        break
            except Exception as e:
                print(f"⚠️ Error reading {env_file}: {e}")
        else:
            print(f"❌ Not found: {env_file}")
    
    return token_found

def main():
    """Run integration tests"""
    print("🌟💎⚡ HYPER TEAM HF INTEGRATION TEST ⚡💎🌟")
    print("=" * 60)
    
    # Test 1: Imports
    imports_ok = test_hf_imports()
    
    # Test 2: Environment  
    env_ok = test_empire_env()
    
    # Summary
    print(f"\n🎊 TEST RESULTS:")
    print(f"  HF Imports: {'✅ PASS' if imports_ok else '❌ FAIL'}")
    print(f"  Empire ENV: {'✅ PASS' if env_ok else '❌ FAIL'}")
    
    if imports_ok and env_ok:
        print("\n🚀 READY FOR FULL HF INTEGRATION DEPLOYMENT!")
    else:
        print("\n⚠️ Fix issues before proceeding with integration")

if __name__ == "__main__":
    main()
