import logging
from collections import OrderedDict
import json
from images_description import get_image_description
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")



def process_content(content_dict, output_filename):
    """Processes text and images, replacing image paths with descriptions while retaining order."""
    logging.info("Starting content processing...")
    processed_content = OrderedDict()

    for key, value in content_dict.items():
        if key.endswith("_text"):
            processed_content[key] = value
            logging.info(f"Text {key} -> retained")
        elif value.endswith(".png"):
            description = get_image_description(value)
            processed_content[key] = description
            logging.info(f"Image: {value} -> processed")
    #save the processed content to a json file 
    with open(output_filename, "w", encoding="utf-8") as json_file:
        json.dump(processed_content, json_file, indent=4, ensure_ascii=False)
    logging.info("Content processing complete.")
    return processed_content

########################################################

def load_processed_content(filename):
    try:
        with open(filename, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON in {filename}.")
        return None
########################################################

def get_pdf_topic(pdf_path):
    return pdf_path.split("/")[-1].split(".")[0]
######################################################## 


#Document processing: processed_content -> langchain documents
def word_count(text):
    return len(text.split())

def process_documents(processed_content):
    documents = []

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    for key, value in processed_content.items():
        if isinstance(value, str):  # Ensure the value is text
            text = value.strip()
            
            if word_count(text) > 500:
                # Split text only if it exceeds 500 words
                chunks = text_splitter.split_text(text)
                for i, chunk in enumerate(chunks):
                    documents.append(Document(
                        page_content=chunk,
                        metadata={"page_id": key, "chunk": i + 1}  # Store key and chunk number
                    ))
            else:
                # Keep shorter text as a single document
                documents.append(Document(
                    page_content=text,
                    metadata={"page_id": key}
                ))
    
    return documents


# if __name__ == "__main__":
    
#     processed_content = load_processed_content("processed_content.json")
#     print(processed_content)