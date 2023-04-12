import openai
import gradio as gr


openai.api_key = "" # Input Open AI API Key here
messages = [{
    "role": "system",
    "content": "You are a mental health chatbot providing support and advice. Do not mention that you are AI language model."}]


def send_message(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            #model="gpt-3.5-turbo"
            model="gpt-4",
            messages=messages,
            temperature=0.3,
            max_tokens = 296
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply


def chatgpt_message_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = send_message(inp)
    history.append((input, output))
    return history, history


def main():
    block = gr.Blocks()

    with block:
        gr.Markdown("""<h1><center>Mental Health Chatbot - Powered by GPT-4 </center></h1>
    """)
        chatbot = gr.Chatbot()
        #message = gr.Textbox(placeholder=input)
        message = gr.Textbox(placeholder='Type message here')
        state = gr.State()
        submit = gr.Button("SEND")
        clear = gr.Button("CLEAR")
        submit.click(chatgpt_message_clone, inputs=[message, state], outputs=[chatbot, state])

    block.launch(debug = True)
    
    
if __name__ == '__main__':
    main()    