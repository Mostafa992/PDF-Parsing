import warnings
warnings.filterwarnings('ignore')

from process_content import process_documents,load_processed_content
from langchain_openai import OpenAIEmbeddings
import chromadb
import uuid
import os

def create_vector_store(documents):
    #create a vector database from the processed content 
    embedding_function = OpenAIEmbeddings(api_key=os.environ['OPENAI_API_KEY'],model="text-embedding-3-small")
    chroma_client = chromadb.Client()
    collection = chroma_client.create_collection(name="my_collection")
    print(collection)
    
    # Extract text content and metadata from documents
    texts = [doc.page_content for doc in documents]
    metadatas = [doc.metadata for doc in documents]
    
    # Generate embeddings for the documents
    embeddings = embedding_function.embed_documents(texts)
    
    # Add documents with their embeddings and metadata
    collection.add(
        documents=texts,
        ids=[str(uuid.uuid4()) for _ in range(len(documents))],
        embeddings=embeddings,
        metadatas=metadatas
    )
    return collection
