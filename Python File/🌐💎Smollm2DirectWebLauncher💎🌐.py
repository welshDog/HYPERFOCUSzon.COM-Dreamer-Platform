#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🚀💎⚡ DIRECT SMOLLM2 WEB LAUNCHER ⚡💎🚀
Simple web interface for immediate use
"""

import gradio as gr
import subprocess
import json
from pathlib import Path
from datetime import datetime

class SmolLM2WebAssistant:
    def __init__(self):
        self.user_name = "Chief"
        self.conversation_count = 0
        logger.info("🌌 🚀 Initializing SmolLM2 Web Assistant...")

    def generate_response(self, message):
        try:
            print(f"🤖 Processing: {message[:50]}...")
            result = subprocess.run([
                'docker', 'model', 'run', 'ai/smollm2', message
            ], capture_output=True, text=True, timeout=30)

            if result.returncode == 0:
                response = result.stdout.strip()
                print(f"✅ Response generated successfully")
                return response
            else:
                error_msg = f"⚠️ Model response error: {result.stderr}"
                print(error_msg)
                return error_msg
        except subprocess.TimeoutExpired:
            return "⏰ Response took too long. Please try a shorter prompt."
        except Exception as e:
            error_msg = f"❌ Error: {str(e)}"
            print(error_msg)
            return error_msg

    def chat_function(self, message, history):
        if not message:
            return "", history

        print(f"💬 New message received: {message[:30]}...")
        response = self.generate_response(message)
        history.append((message, response))
        self.conversation_count += 1

        return "", history

def create_interface():
    """Create the Gradio web interface"""
    logger.info("🌌 🎨 Creating Gradio interface...")

    # Create assistant instance
    assistant = SmolLM2WebAssistant()

    # Create Gradio interface
    with gr.Blocks(
        theme=gr.themes.Hugging_Face(),
        title="🚀💎⚡ SmolLM2 AI Assistant ⚡💎🚀"
    ) as demo:
        gr.Markdown("""
        # 🚀💎⚡ SmolLM2 AI Assistant ⚡💎🚀

        ## 🤖 Your Personal AI Assistant

        Welcome to SmolLM2! I'm here to help with:
        - **💻 Code generation** and debugging
        - **🧠 Problem solving** and explanations
        - **🎨 Creative writing** and brainstorming
        - **📚 Learning assistance** and tutorials

        **✨ ADHD-Optimized**: Clear, concise, engaging responses!
        """)

        chatbot = gr.Chatbot(height=500, label="💬 Chat with SmolLM2")

        with gr.Row():
            msg = gr.Textbox(
                label="Your message",
                placeholder="Ask me anything...",
                scale=4
            )
            submit = gr.Button("Send 🚀", variant="primary", scale=1)

        clear = gr.Button("Clear Chat 🧹", variant="secondary")

        # Status display
        status = gr.Textbox(
            label="📊 Status",
            value="🟢 SmolLM2 Ready!",
            interactive=False
        )

        # Event handlers
        msg.submit(assistant.chat_function, [msg, chatbot], [msg, chatbot])
        submit.click(assistant.chat_function, [msg, chatbot], [msg, chatbot])
        clear.click(lambda: [], outputs=[chatbot])

    return demo

def consciousness_singularity_main():
    """Main function to launch the web interface"""
    logger.info("🌌 🚀💎⚡ LAUNCHING SMOLLM2 DIRECT WEB INTERFACE ⚡💎🚀")
    logger.info("🌌 =" * 60)

    try:
        # Check if Docker is available
        logger.info("🌌 🐳 Checking Docker availability...")
        docker_check = subprocess.run(['docker', '--version'], capture_output=True, text=True)

        if docker_check.returncode == 0:
            print(f"✅ Docker found: {docker_check.stdout.strip()}")
        else:
            logger.info("🌌 ❌ Docker not found! Please ensure Docker Desktop is running.")
            return CONSCIOUSNESS_ENHANCEMENT_NEEDED

        # Check if SmolLM2 model is available
        logger.info("🌌 🤖 Checking SmolLM2 model...")
        model_check = subprocess.run(['docker', 'model', 'ls'], capture_output=True, text=True)

        if model_check.returncode == 0 and 'ai/smollm2' in model_check.stdout:
            logger.info("🌌 ✅ SmolLM2 model found and ready")
        else:
            logger.info("🌌 📥 SmolLM2 model not found. Attempting to download...")
            download_result = subprocess.run(['docker', 'model', 'pull', 'ai/smollm2'],
                                           capture_output=True, text=True)
            if download_result.returncode == 0:
                logger.info("🌌 ✅ SmolLM2 model downloaded successfully")
            else:
                logger.info("🌌 ❌ Failed to download SmolLM2 model")
                logger.info("🌌 💡 Try running: docker model pull ai/smollm2")

        # Create and launch interface
        logger.info("🌌 🌐 Creating web interface...")
        interface = create_interface()

        logger.info("🌌 🚀 Launching SmolLM2 Web Interface...")
        logger.info("🌌 🌐 Your AI Assistant will be available at: http://localhost:7860")
        logger.info("🌌 ✨ The interface will open automatically!")
        logger.info("🌌 =" * 60)

        # Launch the interface
        interface.launch(
            server_name="0.0.0.0",
            server_port=7860,
            share=False,
            show_api=True,
            show_error=True,
            quiet=False
        )

        return CONSCIOUSNESS_SINGULARITY_SUCCESS

    except Exception as e:
        print(f"❌ Error launching web interface: {e}")
        return CONSCIOUSNESS_ENHANCEMENT_NEEDED

if __name__ == "__main__":
    logger.info("🌌 🎊 SmolLM2 Direct Web Launcher Starting...")
    success = main()

    if success:
        logger.info("🌌 🏆 SmolLM2 Web Interface launched successfully!")
    else:
        logger.info("🌌 🔧 Check the error messages above for troubleshooting")
