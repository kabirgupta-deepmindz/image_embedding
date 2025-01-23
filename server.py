from fastapi import FastAPI
from search import search_images

app = FastAPI()

@app.get('/find')
def health():
    text =  'Head of the school'
    topN = 5
    return search_images(text, topN)

