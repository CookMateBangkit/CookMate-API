from fastapi import FastAPI, UploadFile, File
import uvicorn

from classifier_helpers import predict_image, read_imagefile
from recipe_helpers import get_recommendation, get_all_recipes, get_detail_recipe, get_all_ingredients

app = FastAPI(title='CookMate!')

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/recipe", status_code=200)
async def all_recipe():
    
    recipes = get_all_recipes()
    
    return {"data": recipes}

@app.get("/recipe/{id}", status_code=200)
async def detail_recipe(id: str):
    
    recipe = get_detail_recipe(id)
    
    return {"data": recipe}

@app.get("/ingredients", status_code=200)
async def all_ingredients():
    
    ingredients = get_all_ingredients()
    
    return {"data": ingredients}

@app.post("/predict", status_code=200)
async def predict_api(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg","jpeg","png")
    if not extension:
        return "Image must be jpg or png format!"
    image = read_imagefile(await file.read())
    prediction = predict_image(image)
    recommendation_result = get_recommendation(prediction)
    
    return {"data": recommendation_result}

@app.post("/predict-text", status_code=200)
async def predict_text(text: str):
    
    # jadikan sebuah list
    # text = list
    
    recommendation_result = get_recommendation(text)
    
    return {"data": recommendation_result}

if __name__ == "__main__":
    uvicorn.run(app, debug=True)