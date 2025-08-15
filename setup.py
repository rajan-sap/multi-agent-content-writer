#!/usr/bin/env python3
"""
Setup script for Multi-Agent Content Writer
"""

import os
import subprocess
import sys
from pathlib import Path


def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required")
        return False
    print(f"✅ Python {sys.version.split()[0]} detected")
    return True


def install_requirements():
    """Install required packages"""
    print("📦 Installing requirements...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                      check=True, capture_output=True)
        print("✅ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        return False


def create_env_file():
    """Create .env file from template if it doesn't exist"""
    env_file = Path(".env")
    env_example = Path(".env.example")
    
    if not env_file.exists() and env_example.exists():
        print("📝 Creating .env file from template...")
        env_file.write_text(env_example.read_text())
        print("✅ .env file created")
        print("⚠️  Please edit .env file and add your API keys")
        return True
    elif env_file.exists():
        print("✅ .env file already exists")
        return True
    else:
        print("❌ .env.example file not found")
        return False


def check_api_keys():
    """Check if API keys are configured"""
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        openai_key = os.getenv("OPENAI_API_KEY")
        if not openai_key or openai_key == "your_openai_api_key_here":
            print("⚠️  OPENAI_API_KEY not configured in .env file")
            return False
        
        print("✅ API keys appear to be configured")
        return True
    except ImportError:
        print("❌ python-dotenv not installed")
        return False


def main():
    """Main setup function"""
    print("🚀 Setting up Multi-Agent Content Writer")
    print("=" * 50)
    
    if not check_python_version():
        return
    
    if not install_requirements():
        return
    
    if not create_env_file():
        return
    
    print("\n🎉 Setup completed!")
    print("\nNext steps:")
    print("1. Edit .env file and add your API keys (OpenAI, Serper)")
    print("2. Run: python main.py")
    print("\nFor help with API keys:")
    print("- OpenAI: https://platform.openai.com/api-keys")
    print("- Serper: https://serper.dev/api-key")


if __name__ == "__main__":
    main()
