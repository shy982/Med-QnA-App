from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

@app.route('/v1/chat/simple', methods=['POST'])
def process_message_simple_test():
    # Sanity test of the API functioning. Use for debugging purposes
    data = request.json
    messages = data.get('messages', [])
    uppercased_message = messages[-1]['content'].upper()
    time.sleep(2)
    # Returns capitalized user text as response
    return "MediMate says: " + uppercased_message

@app.route('/v1/chat/openai', methods=['POST'])
def process_message_with_chatgpt():
    data = request.json
    # TBD 
    return None

@app.route('/v1/chat/rag', methods=['POST'])
def process_message_with_rag_chatgpt():
    data = request.json
    # TBD 
    return None

@app.route('/v2/chat/rag', methods=['POST'])
def process_message_with_rag_llama():
    data = request.json
    # TBD 
    return None

if __name__ == '__main__':
    app.run(host='0.0.0.0')
