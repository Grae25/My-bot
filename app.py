from flask import Flask, request

app = Flask(__name__)

@app.route('/')  # This is the root route
def home():
    return "Welcome to the Telegram Bot!"

@app.route('/webhook', methods=['POST'])  # This is your webhook path
def webhook():
    update = request.get_json()
    print("Received update:", update)  # Print the entire update for debugging
    if 'message' in update:
        message = update['message']
        chat_id = message['chat']['id']
        text = message['text']
        print(f"Message from {chat_id}: {text}")  # Print message details
    return 'ok'

if __name__ == '__main__':
    app.run(port=5000)


