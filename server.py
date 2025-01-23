from fastapi import FastAPI, Response, Request, status
from search import search_images

app = FastAPI()


@app.get("/find")
def health(request: Request, response: Response):

    query_params = request.query_params
    query = query_params.get("query","")
    topN = query_params.get("topN",5)

    if not query:
        response.status_code = status.HTTP_200_OK
        return 
    return search_images(query, topN)
