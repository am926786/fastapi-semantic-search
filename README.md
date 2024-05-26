# fastapi-semantic-search
A FastAPI application for semantic search of PDF documents using Sentence Transformers.

# FastAPI Semantic Search

A FastAPI application for semantic search of PDF documents using Sentence Transformers. This project allows you to upload PDF documents and perform semantic searches to find relevant documents based on a query.

## Features

- Upload PDF documents
- Extract text from PDF files
- Generate embeddings using Sentence Transformers
- Perform semantic search based on the embeddings

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- PyPDF2
- Sentence Transformers
- Scikit-learn

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fastapi-semantic-search.git
   cd fastapi-semantic-search

Create and activate a virtual environment:


python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
Install the dependencies:

pip install -r requirements.txt
# Usage
Run the FastAPI application:

uvicorn main:app --reload
Open your browser and navigate to http://127.0.0.1:8000.

API Endpoints
POST /upload: Upload a new PDF document.
GET /docs?q=<query>: Search for relevant documents based on the query.
