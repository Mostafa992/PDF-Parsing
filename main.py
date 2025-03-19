from extract_text_images import extract_text_and_images
from process_content import process_content, load_processed_content, process_documents
from vectorstore import create_vector_store
from langchain_openai import OpenAIEmbeddings
import os 
from dotenv import load_dotenv
import warnings
warnings.filterwarnings('ignore')

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
pdf_path="/Users/mostafaelgharib/Desktop/prep_sprint/project_1/the-economics-of-global-climate-change.pdf"
output_folder = "images_out"

# Extract text and images from the PDF
content_dict = extract_text_and_images(pdf_path, output_folder)
#Process the content and save to a JSON file
processed_content = process_content(content_dict, "processed_content.json")
#load the processed content
#processed_content = load_processed_content("processed_content_2.json")

#process the content into langchain documents
documents = process_documents(processed_content)
print("number of documents:",len(documents))

#create a vector store from the documents
vectorstore = create_vector_store(documents)

# test
embedding_function = OpenAIEmbeddings(api_key=openai_api_key,model="text-embedding-3-small")
query = "What is the Climate Change and Inequality?"
query_embedding = embedding_function.embed_query(query)

# Query the collection and get metadata
results = vectorstore.query(
    query_embeddings=[query_embedding],
    n_results=2,
    include=['metadatas','documents']
)
print(results)