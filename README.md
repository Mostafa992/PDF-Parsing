# PDF Processing and Vector Search Project

This project demonstrates a system for processing PDF documents, extracting text and images, and implementing semantic search using vector embeddings. It uses various libraries including PyPDF2, pdf2image, ChromaDB, and OpenAI's embedding models.

## Features

- PDF text extraction
- PDF image extraction
- Text processing and chunking
- Vector database creation using ChromaDB
- Semantic search using OpenAI embeddings
- Metadata preservation and retrieval


## Installation

1. Clone the repository:
```bash
git clone https://github.com/Mostafa992/PDF-Parsing.git
cd PDF-Parsing
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Set up environment variables:
Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Project Structure

```
project/
├── pdf_extractor.py      # PDF text and image extraction
├── process_content.py    # Content processing and document creation
├── vectorstore.py        # Vector database creation and search
├── main.py              # Main execution script
├── requirements.txt     # Project dependencies
└── .env                # Environment variables
```

## Usage

1. Run the main script:
```bash
python main.py
```

2. The script will:
   - Extract text and images from the PDF
   - Process the content
   - Create a vector store
   - Perform semantic search

## Dependencies

- PyPDF2==3.0.1
- pdf2image==1.16.3
- Pillow==10.0.0
- chromadb==0.4.22
- langchain-openai==0.0.5

