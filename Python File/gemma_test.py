#!/usr/bin/env python3
"""
🚀 Quick Gemma 3 Test 🚀
Simple test script to verify everything is working
"""

import os
import sys
from pathlib import Path


def test_basic_functionality():
    """Test basic functionality"""
    print("🌟 HyperFocus Zone Empire - Gemma 3 Quick Test")
    print("=" * 50)

    # Test 1: Python version
    print(f"🐍 Python Version: {sys.version}")

    # Test 2: Check if empire.env exists
    env_path = Path("h:/HyperBeast/empire.env")
    if env_path.exists():
        print("✅ Empire configuration file found")
    else:
        print("⚠️ Empire configuration file not found")

    # Test 3: Check for HF token
    hf_token = os.getenv("HF_TOKEN") or os.getenv("HUGGINGFACE_TOKEN")
    if hf_token:
        print("✅ Hugging Face token detected")
    else:
        print("⚠️ No Hugging Face token found")

    # Test 4: Try importing basic libraries
    try:
        import ping3
        import psutil
        import requests

        print("✅ Basic libraries available")
    except ImportError as e:
        print(f"⚠️ Basic libraries missing: {e}")

    # Test 5: Try importing AI libraries
    try:
        import torch
        import transformers

        print("✅ AI libraries available")
        device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"🔧 Compute device: {device}")
    except ImportError as e:
        print(f"⚠️ AI libraries missing: {e}")
        print("💡 Run: pip install torch transformers")

    print("\n🎯 Test completed!")

    # Show next steps
    print("\n📋 Next Steps:")
    print("1. 🔑 Get HF token: https://huggingface.co/settings/tokens")
    print("2. 🚀 Request access: https://huggingface.co/google/gemma-3-270m")
    print("3. 📦 Install packages: pip install torch transformers")
    print("4. 🧠 Run AI scanner when ready!")


if __name__ == "__main__":
    test_basic_functionality()
