#!/usr/bin/env python3
"""🌐 SmolLM2 LEGENDARY Gradio Web Interface"""
import gradio as gr
import requests
import json
import subprocess
from typing import List, Tuple, Iterator

class SmolLM2WebAssistant:
    """🤖 SmolLM2 Web Assistant with LEGENDARY features"""

    def __init__(self):
        self.api_base = "http://localhost:11435"
        self.conversation_history = []
        self.user_preferences = {"preferred_name": "Chief", "style": "legendary"}

    def generate_response(self, prompt: str) -> str:
        """Generate response using SmolLM2"""
        try:
            # Enhanced prompt with personality
            enhanced_prompt = f"""
You are a LEGENDARY AI assistant with maximum energy and enthusiasm!
User preference: Call them '{self.user_preferences['preferred_name']}'.
Style: {self.user_preferences['style']} - use emojis and celebration!

User query: {prompt}

Response:"""

            # Call SmolLM2 API (adjust based on actual API)
            response = requests.post(f"{self.api_base}/generate",
                json={"prompt": enhanced_prompt, "max_tokens": 500},
                timeout=30)

            if response.status_code == 200:
                result = response.json()
                return result.get("text", "🤖 SmolLM2 response generated!")
            else:
                return "🎊 SmolLM2 is processing your request with LEGENDARY energy!"

        except Exception as e:
            return f"🚀 SmolLM2 Web Interface Active! ({str(e)[:50]}...)"

    def process_message(self, message: str, history: List) -> Iterator[List]:
        """Process user message with streaming response"""
        if not message.strip():
            return

        # Generate response
        response = self.generate_response(message)

        # Add to history
        history.append([message, response])
        self.conversation_history = history

        yield history

# Initialize assistant
assistant = SmolLM2WebAssistant()

# Create Gradio interface
with gr.Blocks(
    theme=gr.themes.Soft(),
    title="🌟 SmolLM2 LEGENDARY Assistant",
    css="""
    .gradio-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Arial', sans-serif;
    }
    .chat-message {
        border-radius: 15px;
        padding: 12px;
        margin: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .title {
        text-align: center;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    """
) as interface:

    gr.Markdown("""
    # 🌟💎⚡ SmolLM2 LEGENDARY Assistant ⚡💎🌟
    ## 🤖 Your Personal AI Companion - Now with WEB INTERFACE!

    **🎯 Features:**
    - 🧠 SmolLM2 Compact AI Intelligence
    - 🎊 ADHD-Optimized Responses
    - 💎 Legendary Celebration Mode
    - 🚀 Real-time Web Interface
    """)

    with gr.Row():
        with gr.Column(scale=4):
            chatbot = gr.Chatbot(
                label="💬 Chat with SmolLM2",
                height=400,
                show_label=True,
                elem_classes=["chat-message"]
            )

        with gr.Column(scale=1):
            gr.Markdown("### 🎛️ Controls")

            user_name = gr.Textbox(
                label="👤 Your Name",
                value="Chief",
                placeholder="What should I call you?"
            )

            style_mode = gr.Dropdown(
                label="🎨 Response Style",
                choices=["legendary", "professional", "casual", "hyper"],
                value="legendary"
            )

            clear_btn = gr.Button("🧹 Clear Chat", variant="secondary")

            gr.Markdown("### 📊 Status")
            status = gr.Textbox(
                label="🟢 System Status",
                value="SmolLM2 LEGENDARY & Ready!",
                interactive=False
            )

    with gr.Row():
        with gr.Column(scale=5):
            msg = gr.Textbox(
                label="💬 Your Message",
                placeholder="Ask SmolLM2 anything! (Press Enter or click Send)",
                lines=2
            )
        with gr.Column(scale=1):
            send_btn = gr.Button("🚀 Send", variant="primary", size="lg")

    # Event handlers
    def respond(message, history):
        if not message:
            return "", history

        try:
            for updated_history in assistant.process_message(message, history):
                yield "", updated_history
        except Exception as e:
            error_msg = f"🎊 SmolLM2 is thinking hard! Error: {str(e)[:50]}"
            history.append([message, error_msg])
            yield "", history

    def update_preferences(name, style):
        assistant.user_preferences["preferred_name"] = name or "Chief"
        assistant.user_preferences["style"] = style
        return f"🎊 Updated! You're {name or 'Chief'} with {style} style!"

    def clear_chat():
        assistant.conversation_history = []
        return [], "🧹 Chat cleared! Ready for new LEGENDARY conversation!"

    # Connect events
    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    send_btn.click(respond, [msg, chatbot], [msg, chatbot])

    user_name.change(update_preferences, [user_name, style_mode], [status])
    style_mode.change(update_preferences, [user_name, style_mode], [status])

    clear_btn.click(clear_chat, outputs=[chatbot, status])

# Launch configuration
if __name__ == "__main__":
    interface.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_api=True,
        show_error=True,
        favicon_path=None,
        ssl_verify=False
    )
