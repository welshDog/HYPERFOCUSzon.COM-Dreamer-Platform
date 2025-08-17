import gradio as gr
import subprocess
import sys

def query_smollm2(message):
    """Query SmolLM2 via Docker Model Runner"""
    if not message.strip():
        return "Please enter a message!"

    try:
        print(f"Querying SmolLM2: {message[:50]}...")
        result = subprocess.run([
            'docker', 'model', 'run', 'ai/smollm2', message
        ], capture_output=True, text=True, timeout=30)

        if result.returncode == 0:
            response = result.stdout.strip()
            logger.info("🌌 Response received successfully!")
            return response
        else:
            error_msg = f"Error: {result.stderr}"
            print(error_msg)
            return error_msg

    except subprocess.TimeoutExpired:
        return "Request timed out. Please try a shorter message."
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        print(error_msg)
        return error_msg

def chat_interface(message, history):
    """Chat interface function"""
    if not message:
        return "", history

    # Get response from SmolLM2
    response = query_smollm2(message)

    # Add to history
    history.append((message, response))

    return "", history

# Create Gradio interface
logger.info("🌌 Creating SmolLM2 Web Interface...")

with gr.Blocks(title="SmolLM2 AI Assistant", theme=gr.themes.Default()) as demo:
    gr.Markdown("# 🚀 SmolLM2 AI Assistant")
    gr.Markdown("Your compact AI assistant powered by SmolLM2! Ask me anything!")

    chatbot = gr.Chatbot(height=400, label="Chat with SmolLM2")

    with gr.Row():
        msg = gr.Textbox(label="Your message", placeholder="Type your message here...", scale=4)
        submit_btn = gr.Button("Send", variant="primary", scale=1)

    clear_btn = gr.Button("Clear Chat")

    # Connect events
    msg.submit(chat_interface, [msg, chatbot], [msg, chatbot])
    submit_btn.click(chat_interface, [msg, chatbot], [msg, chatbot])
    clear_btn.click(lambda: [], outputs=chatbot)

if __name__ == "__main__":
    logger.info("🌌 🚀 Launching SmolLM2 Web Interface...")
    logger.info("🌌 🌐 Access your AI Assistant at: http://localhost:7860")
    logger.info("🌌 =" * 50)

    # Launch interface
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True
    )
