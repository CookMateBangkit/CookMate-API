import numpy as np
import tensorflow as tf
from PIL import Image
from io import BytesIO
from tensorflow.keras.utils import img_to_array

model = None

def load_model():
  model = tf.keras.models.load_model('./model_capstone.h5')
  print("Model loaded")
  return model

def predict(image: Image.Image):
  global model
  if model is None:
    model = load_model()
    
    image = np.asarray(image.resize((300, 300)))[..., :3]
    print(image.shape)
    image = np.expand_dims(image, 0)
    print(image.shape)
    image = image / 127.5 - 1.0
    
    class_probabilities = model.predict(image) 
    
    response = []
    class_names = ['ayam', 'brokoli', 'jagung', 'kacang_tanah', 'kangkung', 'kentang', 'labu', 'labu_siam', 'lobak_merah', 'mentimun', 'nanas', 'nangka', 'nasi_putih', 'paprika', 'pare', 'pepaya', 'pisang', 'singkong', 'tahu', 'telur', 'tempe', 'terong', 'tomat', 'ubi', 'wortel']
    for (label, p) in zip(class_names, class_probabilities[0]):
        resp = {}
        resp["class"] = str(label)
        resp["confidence"] = f"{p:.4f}%"
        response.append(resp)
        
    return response
    
def read_imagefile(file) -> Image.Image:
  image = Image.open(BytesIO(file))
  return image