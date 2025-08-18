#!/usr/bin/env python3
"""
🚀⚡💎 GEMMA 3 SETUP WIZARD 💎⚡🚀
🌟 HYPERFOCUS ZONE EMPIRE AI DEPLOYMENT ACTIVATOR 🌟

Quick setup script for Google Gemma 3 270M integration
"""

import os
import subprocess
import sys

def print_banner():
    """🎯 Display setup banner"""
    banner = """
    🚀⚡💎═══════════════════════════════════════════════════════════════💎⚡🚀
    ║                                                                     ║
    ║        🌟 GEMMA 3 SETUP WIZARD v1.0 🌟                            ║
    ║           HYPERFOCUS ZONE EMPIRE AI ACTIVATION                     ║
    ║                                                                     ║
    ║  🧠 Setting up Google Gemma 3 270M for Peak Performance 🧠        ║
    ║                                                                     ║
    🚀⚡💎═══════════════════════════════════════════════════════════════💎⚡🚀
    """
    print(banner)

def check_python_version():
    """✅ Check Python version compatibility"""
    print("🐍 Checking Python version...")

    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ is required for Gemma 3 270M")
        print(f"   Current version: {sys.version}")
        return False
    else:
        print(f"✅ Python {sys.version.split()[0]} is compatible")
        return True

def check_hf_token():
    """🔑 Check Hugging Face token"""
    print("\n🔑 Checking Hugging Face authentication...")

    # Check environment files
    env_files = [
        "h:\\HyperBeast\\empire.env",
        ".env",
        "empire.env"
    ]

    hf_token = None

    for env_file in env_files:
        if os.path.exists(env_file):
            print(f"📄 Found environment file: {env_file}")
            try:
                with open(env_file, 'r') as f:
                    content = f.read()
                    for line in content.split('\n'):
                        if line.startswith('HF_TOKEN=') or line.startswith('HUGGINGFACE_TOKEN='):
                            hf_token = line.split('=', 1)[1].strip()
                            print("✅ Hugging Face token found!")
                            break
            except Exception as e:
                print(f"⚠️ Error reading {env_file}: {e}")

    if not hf_token:
        print("❌ No Hugging Face token found!")
        print("\n📝 To set up your token:")
        print("1. Go to https://huggingface.co/settings/tokens")
        print("2. Create a new token with 'Read' access")
        print("3. Add to your empire.env file: HF_TOKEN=your_token_here")
        return False

    return True

def install_packages():
    """📦 Install required packages"""
    print("\n📦 Installing required AI packages...")

    packages = [
        "torch",
        "transformers>=4.36.0",
        "accelerate",
        "python-dotenv",
        "psutil",
        "requests",
        "ping3"
    ]

    for package in packages:
        print(f"📥 Installing {package}...")
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", package, "--upgrade"
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"✅ {package} installed successfully")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install {package}: {e}")
            return False

    return True

def test_model_access():
    """🧪 Test Gemma 3 270M model access"""
    print("\n🧪 Testing Gemma 3 270M model access...")

    try:
        from transformers import AutoTokenizer
        from dotenv import load_dotenv

        # Load environment
        load_dotenv('h:\\HyperBeast\\empire.env')
        hf_token = os.getenv("HF_TOKEN") or os.getenv("HUGGINGFACE_TOKEN")

        if not hf_token:
            print("❌ No token available for testing")
            return False

        print("🔍 Attempting to access google/gemma-3-270m...")

        # Try to load tokenizer (lightweight test)
        tokenizer = AutoTokenizer.from_pretrained(
            "google/gemma-3-270m",
            token=hf_token,
            trust_remote_code=True
        )

        print("✅ Model access successful!")
        print(f"📊 Vocabulary size: {len(tokenizer)}")
        return True

    except Exception as e:
        error_str = str(e).lower()

        if "repository not found" in error_str or "401" in error_str:
            print("🔒 Model access requires approval!")
            print("\n📝 To request access:")
            print("1. Go to https://huggingface.co/google/gemma-3-270m")
            print("2. Click 'Request Access'")
            print("3. Accept the license terms")
            print("4. Wait for approval (usually within minutes)")
            return False
        else:
            print(f"❌ Error testing model access: {e}")
            return False

def create_test_script():
    """📝 Create a simple test script"""
    print("\n📝 Creating test script...")

    test_script = '''#!/usr/bin/env python3
"""
🧪 Quick Gemma 3 270M Test Script
"""

import os
from dotenv import load_dotenv

# Load environment
load_dotenv('h:\\\\HyperBeast\\\\empire.env')

def test_gemma():
    """Test Gemma 3 270M functionality"""
    try:
        from transformers import AutoTokenizer, AutoModelForCausalLM
        import torch

        hf_token = os.getenv("HF_TOKEN") or os.getenv("HUGGINGFACE_TOKEN")

        print("🧠 Loading Gemma 3 270M...")

        tokenizer = AutoTokenizer.from_pretrained(
            "google/gemma-3-270m",
            token=hf_token,
            trust_remote_code=True
        )

        model = AutoModelForCausalLM.from_pretrained(
            "google/gemma-3-270m",
            token=hf_token,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            device_map="auto" if torch.cuda.is_available() else None,
            trust_remote_code=True,
            low_cpu_mem_usage=True
        )

        # Add padding token
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token

        print("✅ Model loaded successfully!")

        # Test generation
        prompt = "The HyperFocus Zone Empire network status is"
        inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=50,
                temperature=0.7,
                do_sample=True,
                pad_token_id=tokenizer.eos_token_id
            )

        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(f"\\n🎯 Test generation:\\n{response}")

        return True

    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

if __name__ == "__main__":
    test_gemma()
'''

    try:
        with open("test_gemma.py", "w") as f:
            f.write(test_script)
        print("✅ Test script created: test_gemma.py")
        return True
    except Exception as e:
        print(f"❌ Failed to create test script: {e}")
        return False

def create_quick_start_guide():
    """📖 Create quick start guide"""
    print("\n📖 Creating quick start guide...")

    guide = """# 🚀 Gemma 3 270M Quick Start Guide

## 🎯 HyperFocus Zone Empire AI Integration

### ✅ Prerequisites Completed
- Python 3.8+ installed
- Required packages installed
- Hugging Face token configured

### 🚀 Quick Start Steps

#### 1. Test Model Access
```bash
python test_gemma.py
```

#### 2. Run AI-Enhanced Scanner
```bash
python "⚡💎🧠_GEMMA3_INTELLIGENCE_SCANNER_🧠💎⚡.py"
```

#### 3. Check Your Results
- Look for `empire_ai_health_report_*.json` files
- Review `empire_summary_*.md` for ADHD-friendly summaries

### 🧠 AI Features Available

#### System Analysis
- Intelligent performance insights
- ADHD/neurodivergent optimizations
- Security recommendations
- Network optimization suggestions

#### HyperFocus Integration
- 25-minute focused task suggestions
- Color-coded priority levels
- Automated alert recommendations
- Cognitive load management tips

### 🔧 Troubleshooting

#### Model Access Issues
1. Check token at: https://huggingface.co/settings/tokens
2. Request access: https://huggingface.co/google/gemma-3-270m
3. Verify token in empire.env file

#### Performance Issues
- Model runs on CPU by default (safe but slower)
- GPU acceleration available if CUDA installed
- Memory usage: ~1-2GB for 270M model

### 🌟 Empire Integration Points

#### Current Scanners
- Enhance `ULTRA_THINKING_BOARDROOM_SCANNER.py`
- Integrate with health monitoring systems
- Add to automated workflows

#### Future Enhancements
- Real-time monitoring with AI insights
- Predictive maintenance recommendations
- Automated optimization suggestions
- Natural language query interface

### 💡 ADHD-Friendly Tips

#### Focus Sessions
- Use AI for 25-minute analysis bursts
- Schedule during peak mental energy
- Break complex tasks into AI-assisted chunks

#### Cognitive Load Management
- Let AI handle pattern recognition
- Use visual dashboards for quick status
- Automate routine analysis tasks

---
*Generated by HyperFocus Zone Empire AI Setup Wizard*
*Powered by Google Gemma 3 270M*
"""

    try:
        with open("GEMMA3_QUICK_START.md", "w") as f:
            f.write(guide)
        print("✅ Quick start guide created: GEMMA3_QUICK_START.md")
        return True
    except Exception as e:
        print(f"❌ Failed to create guide: {e}")
        return False

def main():
    """🚀 Main setup function"""
    print_banner()

    print("🌟 Welcome to the Gemma 3 270M Setup Wizard!")
    print("🎯 Setting up AI intelligence for your HyperFocus Zone Empire")
    print()

    # Step 1: Check Python version
    if not check_python_version():
        print("\n❌ Setup cannot continue with incompatible Python version")
        return False

    # Step 2: Check Hugging Face token
    if not check_hf_token():
        print("\n⚠️ Setup can continue, but model access will require token configuration")

    # Step 3: Install packages
    if not install_packages():
        print("\n❌ Package installation failed")
        return False

    # Step 4: Test model access
    model_access = test_model_access()

    # Step 5: Create helper files
    create_test_script()
    create_quick_start_guide()

    # Final status
    print("\n" + "=" * 70)
    print("🎉 GEMMA 3 SETUP COMPLETE!")
    print("=" * 70)

    if model_access:
        print("✅ Model Access: READY")
        print("🚀 Next Step: Run the AI-enhanced scanner!")
        print('   python "⚡💎🧠_GEMMA3_INTELLIGENCE_SCANNER_🧠💎⚡.py"')
    else:
        print("⚠️ Model Access: NEEDS APPROVAL")
        print("🔑 Next Step: Request access at https://huggingface.co/google/gemma-3-270m")
        print("📝 Then run: python test_gemma.py")

    print("\n📖 Quick Start Guide: GEMMA3_QUICK_START.md")
    print("🧪 Test Script: test_gemma.py")
    print("\n🌟 Your HyperFocus Zone Empire is ready for AI enhancement!")

    return True

if __name__ == "__main__":
    main()
