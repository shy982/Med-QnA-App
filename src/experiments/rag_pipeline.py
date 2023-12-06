from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.vectorstores import FAISS

import os
import pickle

def run_rag_pipeline(query, model="gpt-3.5-turbo-instruct", dataset="nfcorpus"):
    # Load index from file
    load_dotenv()
    
    loaded_faiss_vs = FAISS.load_local(
        folder_path=f"./vectordb/faiss/{dataset}/",
        embeddings=OpenAIEmbeddings())
    retriever = loaded_faiss_vs.as_retriever(search_kwargs={'k': 10})
    
    # Define the RAG pipeline
    llm = OpenAI(model_name=model, openai_api_key=os.getenv("OPENAI_API_KEY"))
    
    template = """Answer the question or Explain the topic given this additional context: {context}
    Question: {question}"""
    prompt = ChatPromptTemplate.from_template(template)
    
    docs_file_path = f'./openai_embeddings/{dataset}/doc_embeddings.pkl'
    with open(docs_file_path, 'rb') as file:
        docs = pickle.load(file)
    
    def format_docs(_docs):
        ls = []
        for doc in _docs:
            if doc.page_content in docs:
                ls.append(docs[doc.page_content]["text"][:400])
        return ls
    
    chain = ({"context": retriever | format_docs, "question": RunnablePassthrough()} 
             | prompt 
             | llm 
             | StrOutputParser())
    
    # Run the RAG pipeline
    response = chain.invoke(query)
    return response


if __name__ == "__main__":
    print(run_rag_pipeline(query="Do Cholesterol Statin Drugs Cause Breast Cancer?"))
    