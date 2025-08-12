#!/usr/bin/env python3
"""
🚀💎⚡ SMOLLM2 GRADIO WEB INTERFACE ⚡💎🚀
Personal AI Assistant with User Preference Learning
"""

import gradio as gr
import subprocess
import json
import time
from datetime import datetime
from pathlib import Path
from typing import List, Tuple, Iterator

class SmolLM2Assistant:
    """Personal AI Assistant using SmolLM2"""

    def __init__(self):
        self.user_prefs = self.load_user_preferences()
        self.conversation_history = []

    def load_user_preferences(self) -> dict:
        """Load user preferences from file"""
        prefs_file = Path("h:/config/user_preferences.json")
        default_prefs = {
            "preferred_name": "Chief",
            "interaction_style": "legendary",
            "first_time": True,
            "conversation_count": 0
        }

        if prefs_file.exists():
            try:
                with open(prefs_file, 'r') as f:
                    return json.load(f)
            except:
                return default_prefs
        return default_prefs

    def save_user_preferences(self):
        """Save user preferences to file"""
        prefs_file = Path("h:/config/user_preferences.json")
        prefs_file.parent.mkdir(exist_ok=True)

        with open(prefs_file, 'w') as f:
            json.dump(self.user_prefs, f, indent=2)

    def ask_for_preferred_name(self, message: str) -> str:
        """Ask user for their preferred name if first time"""
        if self.user_prefs.get("first_time", True):
            name_prompt = """Hello! I'm SmolLM2, your personal AI assistant! 🚀💎

Before we start our legendary journey together, I'd love to know what you'd like me to call you!

You can tell me:
- Your name (like "Call me Sarah")
- A title (like "Call me Chief" or "Call me Boss")
- Whatever makes you comfortable!

What would you prefer I call you?"""

            # Use SmolLM2 to generate a friendly introduction
            response = self.generate_response(name_prompt)
            return response

        return self.generate_response(message)

    def update_user_name(self, response_text: str):
        """Extract and update user's preferred name from their response"""
        # Simple name extraction logic
        response_lower = response_text.lower()

        if "call me" in response_lower:
            # Extract name after "call me"
            parts = response_lower.split("call me")
            if len(parts) > 1:
                name = parts[1].strip().split()[0].title()
                self.user_prefs["preferred_name"] = name
        elif "my name is" in response_lower:
            parts = response_lower.split("my name is")
            if len(parts) > 1:
                name = parts[1].strip().split()[0].title()
                self.user_prefs["preferred_name"] = name
        elif "i'm" in response_lower:
            parts = response_lower.split("i'm")
            if len(parts) > 1:
                name = parts[1].strip().split()[0].title()
                if name not in ["fine", "good", "okay", "great"]:
                    self.user_prefs["preferred_name"] = name

        # Mark as no longer first time
        self.user_prefs["first_time"] = False
        self.save_user_preferences()

    def generate_response(self, prompt: str, temperature: float = 0.7) -> str:
        """Generate response using SmolLM2 via Docker model"""
        try:
            # Add personality and user preferences to prompt
            enhanced_prompt = self.enhance_prompt(prompt)

            # Call Docker model run command
            result = subprocess.run([
                'docker', 'model', 'run', 'ai/smollm2', enhanced_prompt
            ], capture_output=True, text=True, timeout=30)

            if result.returncode == 0:
                response = result.stdout.strip()
                self.log_conversation(prompt, response)
                return response
            else:
                return f"⚠️ Model response error: {result.stderr}"

        except subprocess.TimeoutExpired:
            return "⏰ Response took too long. Please try a shorter prompt."
        except Exception as e:
            return f"❌ Error generating response: {str(e)}"

    def enhance_prompt(self, prompt: str) -> str:
        """Enhance prompt with user preferences and context"""
        user_name = self.user_prefs.get("preferred_name", "Chief")

        if self.user_prefs.get("first_time", True):
            return prompt

        enhanced = f"""You are SmolLM2, a helpful AI assistant. The user prefers to be called {user_name}.

Be friendly, helpful, and enthusiastic. Use emojis when appropriate.
Keep responses concise but informative (ADHD-friendly).

User's message: {prompt}

Response:"""
        return enhanced

    def log_conversation(self, prompt: str, response: str):
        """Log conversation for learning"""
        self.conversation_history.append({
            "timestamp": datetime.now().isoformat(),
            "prompt": prompt,
            "response": response,
            "user_name": self.user_prefs.get("preferred_name", "Chief")
        })

        # Keep only last 50 conversations in memory
        if len(self.conversation_history) > 50:
            self.conversation_history = self.conversation_history[-50:]

    def process_message(self, message: str, history: List[Tuple[str, str]]) -> Iterator[List[Tuple[str, str]]]:
        """Process user message and generate streaming response"""
        if not message.strip():
            return

        # Handle first-time name asking
        if self.user_prefs.get("first_time", True) and message.strip():
            self.update_user_name(message)

        # Generate response
        response = self.generate_response(message)

        # Add to conversation history
        history.append((message, response))

        # Update conversation count
        self.user_prefs["conversation_count"] = self.user_prefs.get("conversation_count", 0) + 1
        self.save_user_preferences()

        yield history

# Initialize the assistant
assistant = SmolLM2Assistant()

# Create the Gradio interface
def create_interface():
    """Create the Gradio web interface"""

    with gr.Blocks(
        theme=gr.themes.Hugging_Face(),
        title="🚀💎⚡ LEGENDARY SMOLLM2 AI ASSISTANT ⚡💎🚀",
        css="""
        .gradio-container {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        .chat-message {
            border-radius: 15px;
            padding: 10px;
            margin: 5px;
        }
        """
    ) as interface:

        gr.Markdown(f"""
        # 🚀💎⚡ LEGENDARY SMOLLM2 AI ASSISTANT ⚡💎🚀

        ## 🤖 Your Personal AI Assistant

        Welcome to SmolLM2! I'm here to help with:
        - **💻 Code generation** and debugging
        - **🧠 Problem solving** and explanations
        - **🎨 Creative writing** and brainstorming
        - **📚 Learning assistance** and tutorials

        **✨ ADHD-Optimized**: Clear, concise, engaging responses!
        """)

        # Chat interface
        chatbot = gr.Chatbot(
            label="💬 Chat with SmolLM2",
            height=500,
            elem_classes=["chat-message"]
        )

        with gr.Row():
            with gr.Column(scale=8):
                msg = gr.Textbox(
                    label="Your message",
                    placeholder="Type your message here... (Ask me anything!)",
                    lines=2,
                    autofocus=True
                )
            with gr.Column(scale=1):
                submit_btn = gr.Button("Send 🚀", variant="primary")
                clear_btn = gr.Button("Clear 🧹", variant="secondary")

        # Advanced options (collapsible)
        with gr.Accordion("⚙️ Advanced Options", open=False):
            with gr.Row():
                temperature = gr.Slider(
                    minimum=0.1, maximum=1.5, value=0.7,
                    step=0.1, label="🌡️ Temperature (Creativity)"
                )
                max_tokens = gr.Slider(
                    minimum=50, maximum=2048, value=2048,
                    step=50, label="📏 Max Response Length"
                )

        # Status and user info
        with gr.Row():
            status = gr.Textbox(
                label="📊 Status",
                value="🟢 SmolLM2 Ready!",
                interactive=False
            )
            user_info = gr.Textbox(
                label="👤 User Info",
                value=f"Welcome {assistant.user_prefs.get('preferred_name', 'Chief')}! 🎊",
                interactive=False
            )

        # Event handlers
        def respond(message, history):
            if not message:
                return "", history

            try:
                # Process with assistant
                for updated_history in assistant.process_message(message, history):
                    yield "", updated_history

                # Update user info display
                user_info.value = f"{assistant.user_prefs.get('preferred_name', 'Chief')} | Chats: {assistant.user_prefs.get('conversation_count', 0)}"

            except Exception as e:
                error_msg = f"❌ Error: {str(e)}"
                history.append((message, error_msg))
                yield "", history

        # Connect events
        msg.submit(respond, [msg, chatbot], [msg, chatbot])
        submit_btn.click(respond, [msg, chatbot], [msg, chatbot])
        clear_btn.click(lambda: ([], "🧹 Chat cleared!"), outputs=[chatbot, status])

        # Welcome message for first-time users
        if assistant.user_prefs.get("first_time", True):
            interface.load(
                lambda: [(None, assistant.ask_for_preferred_name(""))],
                outputs=[chatbot]
            )

    return interface

# Launch the interface
if __name__ == "__main__":
    interface = create_interface()
    interface.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_api=True,
        show_error=True
    )
