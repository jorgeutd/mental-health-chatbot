from flask import Flask, render_template, request, jsonify
import openai
import boto3, json, typing
import ast
import time

##### before run the app make sure to remove the QH logo example on the static folder and the reference on the index html file


openai.api_key = open_ai_key #### get the api key

app = Flask(__name__)

# Load OpenAI API key
openai.api_key = open_ai_key

# Initialize conversation history
conversation_history = []

def chat_gpt_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.3,
        max_tokens = 296
    )

    message = response['choices'][0]['message']['content'].strip()
    return message

def mental_health_chatbot(user_input):
    messages = [
        {"role": "system", "content": "You are a mental health chatbot providing support and advice. Do not mention that you are AI language model"},
        {"role": "user", "content": user_input}
    ]
    response = chat_gpt_response(messages)
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    global conversation_history
    conversation_history = []  # Clear the conversation history
    user_input = request.form['message']
    response = mental_health_chatbot(user_input)

    conversation_history.append({"role": "user", "content": user_input})
    conversation_history.append({"role": "chatbot", "content": response})

    return jsonify(conversation_history)

if __name__ == '__main__':
    app.run(debug=True)