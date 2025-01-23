from fastapi import FastAPI, Response, Request, status
from fastapi.middleware.cors import CORSMiddleware
from search import search_images

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with specific domains for better security
    allow_credentials=True,
    allow_methods=["*"],  # Specify allowed HTTP methods
    allow_headers=["*"],  # Specify allowed headers
)


@app.get("/")
def ping():
    return "API in Running!"


@app.get("/find")
def search_image(request: Request, response: Response):

    query_params = request.query_params
    query = query_params.get("query","")
    topN = query_params.get("topN",5)

    if not query:
        response.status_code = status.HTTP_200_OK
        return 
    return search_images(query, topN)
