from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import uvicorn
import requests

from helpers import predict_image, read_imagefile

app = FastAPI(title='CookMate!')

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/api/predict", status_code=200)
async def predict_api(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg","jpeg","png")
    if not extension:
        return "Image must be jpg or png format!"
    image = read_imagefile(await file.read())
    predict_image(image)
    
    url = "https://backend-g7swsp3jxa-as.a.run.app/resep"
    recipes = requests.get(url)
    
    return {"data": recipes.json()}

if __name__ == "__main__":
    uvicorn.run(app, debug=True)