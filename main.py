from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]





@app.get('/blog')
def index(limit=10, published: bool=True, sort: Optional[str]=None):
    # only get 10 published blogs
    # published=False
    if published:
        return {'data': f'{limit} published blogs from the data db '}
    else:
        return {'data': f'{limit} from the database'}

@app.get('/blog/unpublished')
def show():
    # fetch blog with id = id
    return {'data': 'show all unpublished'}

@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    # fetch comments
    return {'data':{'1', '2'}}


@app.post('/blog')
def create_blog(request: Blog):
    # return request
    return {'data':f'Blog is created with {request.title}'}