import numpy as np
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def load_vectorstore(path="vectorstore"):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    return FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)

def search_context(vectorstore, query, k=3):
    docs = vectorstore.similarity_search(query, k=k)
    return "\n\n".join([d.page_content for d in docs])
