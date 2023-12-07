import os
import pickle

import openai
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.vectorstores import FAISS


def request_gpt_turbo(messages):
    load_dotenv()
    client = openai.OpenAI()
    # prompt = "\n".join([message['content'] for message in messages])
    qry = messages[-1]['content']
    answer = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt="Give a friendly answer to the query" + qry,
        max_tokens=200
    )
    return answer.choices[0].text.strip()


def run_rag_pipeline(messages, model="gpt-3.5-turbo-instruct", dataset="nfcorpus"):
    load_dotenv()
    query = messages[-1]['content']
    # Load index from file
    print(os.getcwd())
    loaded_faiss_vs = FAISS.load_local(
        folder_path=f"./qna_service/datastore/vectordb/faiss/{dataset}/",
        embeddings=OpenAIEmbeddings())
    retriever = loaded_faiss_vs.as_retriever(search_kwargs={"k": 5})

    # Define the RAG pipeline
    llm = OpenAI(model_name=model, openai_api_key=os.getenv("OPENAI_API_KEY"))

    template = """Answer the question or Explain the topic given this additional context: {context}
    Question: {question}"""
    prompt = ChatPromptTemplate.from_template(template)

    docs_file_path = f"./qna_service/datastore/dataset/{dataset}/documents.pkl"
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