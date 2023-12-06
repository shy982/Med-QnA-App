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
    messages = data.get('messages', [])
    qry = messages[-1]['content']
    answer = run_rag_pipeline(qry)
    return answer.strip()

@app.route('/v2/chat/rag', methods=['POST'])
def process_message_with_rag_llama():
    data = request.json
    # TBD 
    return None

def run_rag_pipeline(query, model="gpt-3.5-turbo-instruct", dataset="nfcorpus"):
    # Imports
    from dotenv import load_dotenv
    from langchain.embeddings import OpenAIEmbeddings
    from langchain.llms import OpenAI
    from langchain.prompts import ChatPromptTemplate
    from langchain.schema.output_parser import StrOutputParser
    from langchain.schema.runnable import RunnablePassthrough
    from langchain.vectorstores import FAISS
    
    import os
    import pickle

    
    # Load index from file
    load_dotenv()

    loaded_faiss_vs = FAISS.load_local(
        folder_path=f"../../experiments/vectordb/faiss/{dataset}/",
        embeddings=OpenAIEmbeddings())
    retriever = loaded_faiss_vs.as_retriever(search_kwargs={"k": 5})

    # Define the RAG pipeline
    llm = OpenAI(model_name=model, openai_api_key=os.getenv("OPENAI_API_KEY"))

    template = """Answer the question or Explain the topic given this additional context: {context}
    Question: {question}"""
    prompt = ChatPromptTemplate.from_template(template)

    docs_file_path = f"../../experiments/dataset/{dataset}/documents.pkl"
    with open(docs_file_path, "rb") as file:
        docs = pickle.load(file)

    def format_docs(_docs):
        ls = []
        for doc in _docs:
            if doc.page_content in docs:
                ls.append(docs[doc.page_content]["text"][:800])
        return ls
    
    chain = ({"context": retriever | format_docs, "question": RunnablePassthrough()} 
             | prompt 
             | llm 
             | StrOutputParser())

    # Run the RAG pipeline
    response = chain.invoke(query)

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
