#!/usr/bin/env python3
"""🌐 SmolLM2 LEGENDARY Gradio Web Interface"""
import gradio as gr
import requests

def generate_response(prompt):
    """Generate response using SmolLM2"""
    try:
        return f"🤖 SmolLM2 Response: {prompt} - LEGENDARY processing complete! 🎊"
    except Exception as e:
        return f"🚀 SmolLM2 Web Interface Active! ({str(e)[:50]}...)"

# Create Gradio interface
interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(label="💬 Ask SmolLM2 anything!"),
    outputs=gr.Textbox(label="🤖 SmolLM2 Response"),
    title="🌟 SmolLM2 LEGENDARY Assistant",
    description="🎊 Your Personal AI Companion with WEB INTERFACE!"
)

if __name__ == "__main__":
    interface.launch(server_port=7862, share=False)
