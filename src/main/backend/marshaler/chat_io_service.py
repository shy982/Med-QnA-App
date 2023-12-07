import time

from flask import Flask, request
from flask_cors import CORS
from qna_service.openai_client import request_gpt_turbo
from qna_service.openai_client import run_rag_pipeline

app = Flask(__name__)
CORS(app)


# TODO: Maintain conversation i.e. previous chats to be taken into account
# TODO: API to process uploaded document text and consider as context.

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
    messages = data.get('messages', [])
    response = request_gpt_turbo(messages)
    return response


@app.route('/v1/chat/rag', methods=['POST'])
def process_message_with_rag_chatgpt():
    data = request.json
    messages = data.get('messages', [])
    answer = run_rag_pipeline(messages)
    return answer.strip()


@app.route('/v2/chat/rag', methods=['POST'])
def process_message_with_rag_llama():
    data = request.json
    # TBD 
    return None


if __name__ == '__main__':
    app.run(host='0.0.0.0')
