from flask import Flask, request, jsonify
from flask_cors import CORS
import time
import openai
from dotenv import load_dotenv
# from ..qna_service.openai_client import request_gpt_turbo
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
    messages = data.get('messages', [])
    # response = request_gpt_turbo(messages)
    load_dotenv()
    client = openai.OpenAI()
    # prompt = "\n".join([message['content'] for message in messages])
    qry = messages[-1]['content']
    answer = client.completions.create(
                              model="gpt-3.5-turbo-instruct",
                              prompt = "Answer the query briefly: " + qry,
                              max_tokens = 200
                          )
    return answer.choices[0].text.strip()
    # return response

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
