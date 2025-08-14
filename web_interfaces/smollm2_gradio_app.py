import gradio as gr

def chat_with_smollm2(message, history):
    """Chat with SmolLM2"""
    if message:
        response = f"🤖 SmolLM2: Thanks for your message: '{message}'. I'm ready to help!"
        history.append([message, response])
    return "", history

# Create Gradio interface
with gr.Blocks(title="🌟 SmolLM2 LEGENDARY Assistant") as interface:
    gr.Markdown("# 🤖💎 SmolLM2 LEGENDARY Web Interface 💎🤖")

    chatbot = gr.Chatbot(label="💬 Chat with SmolLM2", height=400)

    with gr.Row():
        msg = gr.Textbox(label="Your Message", placeholder="Ask SmolLM2 anything!")
        send_btn = gr.Button("🚀 Send", variant="primary")

    msg.submit(chat_with_smollm2, [msg, chatbot], [msg, chatbot])
    send_btn.click(chat_with_smollm2, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    interface.launch(server_name="0.0.0.0", server_port=7860, share=False)
