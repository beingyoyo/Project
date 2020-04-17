import base64
import numpy as np
import io
from PIL import Image
from tensorflow import keras
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model, Sequential

from flask import Flask, jsonify, request
app = Flask(__name__)

def get_model():
    global model
    model = load_model('C:\\Users\\sniha\\Desktop\\Flask_Apps\\Test.h5')
    print(" * Model loaded!")

def preprocess_image(image, target_size):
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return image

print(" * Loading Keras model...")
get_model()

@app.route("/predict", methods=["POST"])
def predict():
    message = request.get_json(force=True)
    encoded = message['image']
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_image = preprocess_image(image, target_size=(224, 224))
    
    prediction = model.predict(processed_image).tolist()

    response = {
        'prediction': {
            'l0': prediction[0][0],
            'l1': prediction[0][1],
            'l2': prediction[0][2],
            'l3': prediction[0][3],
            'l4': prediction[0][4],
        }
    }
    return jsonify(response)
