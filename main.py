from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    return {"data":"Hello World"}

@app.get("/about")
def about():
    return {"data": "This is FastAPI based server"}

@app.get("/blog/{id}")
def blog(id):
    return {"data":id}