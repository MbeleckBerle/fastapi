from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data': 'blog list'}

@app.get('/mojo/unpublished')
def show(id: int):
    # fetch blog with id = id
    return {'data': 'show all unpublished'}

@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments():
    # fetch comments
    return {'data':{'1', '2'}}

