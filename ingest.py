import os
import numpy as np
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.document_loaders import PyPDFLoader

# Load API key
os.environ["GOOGLE_API_KEY"] = os.getenv("AIzaSyBn2lRNujbjl3xajStiqTONl8iUWSrN11w")

PDF_FOLDER = "docs"
VECTOR_FOLDER = "vectorstore"

def build_vectorstore():
    pdf_files = [f for f in os.listdir(PDF_FOLDER) if f.endswith(".pdf")]

    if not pdf_files:
        raise Exception(" No PDFs found in docs/ folder.")

    all_docs = []

    for pdf in pdf_files:
        loader = PyPDFLoader(os.path.join(PDF_FOLDER, pdf))
        docs = loader.load()
        all_docs.extend(docs)

    print(f"Loaded {len(all_docs)} pages from PDFs.")

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(all_docs)

    print(f"Created {len(chunks)} text chunks.")

    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(VECTOR_FOLDER)

    print(" Vectorstore created and saved successfully!")

if __name__ == "__main__":
    build_vectorstore()

