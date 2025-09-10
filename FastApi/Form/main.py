#pip install python-multipart

from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
 
app = FastAPI()
 
@app.get("/")
def root():
    return FileResponse("public/index.html")
 
 
@app.post("/postdata")
def postdata(username = Form(), userage=Form()):
    return {"name": username, "age": userage}
