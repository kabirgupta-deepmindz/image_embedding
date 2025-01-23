import os
import json
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

embedding_file = './embedding.json'

text_embeddings=[]
with open(embedding_file,'r') as f:
    text_embeddings = json.load(f)

def search_images(query, top_k):
    # print(text_embeddings)
    text_embedding = model.encode(query).reshape(1, -1)
    print("Embedding Generated!")
    simlarities = []
    for item in text_embeddings:
        embedding = np.array(item['embedding']).reshape(1, -1)
        similarity = cosine_similarity(embedding, text_embedding)[0][0]
        simlarities.append((item['filename'], item['description'], similarity))
    
    simlarities = sorted(simlarities,key=lambda x: x[2], reverse=True)

    return simlarities[:top_k]



print("File Loaded sucessfully!")
# print(search_images('Head of school.',5))