import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

dataset = None

def load_dataset():
  dataset = pd.read_excel('./dataset.xlsx')
  
  return dataset

def get_recommendation(keyword):
  
  global dataset
  if dataset is None:
    dataset = load_dataset()
    
  vectorizer = TfidfVectorizer()
  recipe_matrix = vectorizer.fit_transform(dataset['main_ingredient'])
  
  query_vector = vectorizer.transform([keyword])
  similarity_scores = cosine_similarity(query_vector, recipe_matrix)
  
  top_recipe_indices = similarity_scores.argsort()[0][::-1]
  top_10_recipes = dataset.iloc[top_recipe_indices][:3]
  recipes = top_10_recipes.reset_index().to_dict(orient='index')
  
  recipes_cleaned = list(recipes.values())
  
  for dictionary in recipes_cleaned:
    del dictionary['index']
    del dictionary['main_ingredient']
  
  return recipes_cleaned

def get_all_recipes():
  
  global dataset
  if dataset is None:
    dataset = load_dataset()
    
  recipes = dataset.reset_index().to_dict(orient='index')
  recipes = list(recipes.values())
  
  for dictionary in recipes:
    del dictionary['index']
    del dictionary['main_ingredient']
    
  return recipes
    
def get_detail_recipe(id):

  global dataset
  if dataset is None:
    dataset = load_dataset()
  
  recipe = dataset.loc[dataset['id'] == id]
  recipe = recipe.to_dict('records')[0]
    
  return recipe
    