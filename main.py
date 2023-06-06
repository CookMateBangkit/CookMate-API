from fastapi import FastAPI, UploadFile, File
import uvicorn

from helpers import predict, read_imagefile

app = FastAPI(title='CookMate!')

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/api/predict")
async def predict_api(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg","jpeg","png")
    if not extension:
        return "Image must be jpg or png format!"
    image = read_imagefile(await file.read())
    prediction = predict(image)
    
    return prediction

if __name__ == "__main__":
    uvicorn.run(app, debug=True)