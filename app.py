import gradio as gr

def chatbot(message, history):
    history = history or []
    response = f"مرحبا شيماء! نتي قلتي: {message}"
    history.append((message, response))
    return history, history

with gr.Blocks(title="Shima Bot SNU 2027") as demo:
    gr.Markdown("# 🤖 Shima Bot - SNU 2027")
    gr.Markdown("بوت ذكي صاوباتو شيماء كرومي")
    
    chatbot_ui = gr.Chatbot()
    msg = gr.Textbox(placeholder="كتبي سؤالك هنا...")
    clear = gr.Button("مسح المحادثة")
    
    msg.submit(chatbot, [msg, chatbot_ui], [chatbot_ui, msg])
    clear.click(lambda: None, None, chatbot_ui, queue=False)

demo.launch(server_name="0.0.0.0", server_port=7860)
