from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

messages = []

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

@app.route('/messages', methods=['POST'])
def post_message():
    data = request.get_json()
    message = {
        "id": len(messages) + 1,
        "username": data.get("username"),
        "content": data.get("content")
    }
    messages.append(message)
    return jsonify(message), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
