from fastapi import FastAPI, File, UploadFile
from typing import List
from pydantic import BaseModel
import PyPDF2
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = FastAPI()

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

class SearchResult(BaseModel):
    documents: List[str]

document_embeddings = {
    "Sample Document 1": np.random.rand(384),
    "Sample Document 2": np.random.rand(384)
}

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page in range(reader.numPages):
            text += reader.getPage(page).extract_text()
    return text

def get_document_embedding(text):
    return model.encode(text)

def search_documents(query):
    query_embedding = model.encode(query)
    scores = {doc: cosine_similarity([query_embedding], [embedding])[0][0]
              for doc, embedding in document_embeddings.items()}
    sorted_docs = sorted(scores, key=scores.get, reverse=True)
    return sorted_docs

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}

@app.get("/docs", response_model=SearchResult)
async def search_docs(q: str):
    results = search_documents(q)
    return {"documents": results}
