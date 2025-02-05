from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import os

app = FastAPI()

#load the pre-trained model
model_path = os.path.join(os.path.dirname(__file__),"models","sentiment_model.h5")
model = load_model(model_path)

#Load the tokenizer
tokenizer = 




class TextInput(BaseModel):
    text: str


@app.post("/predict")
async def predict_sentiment(input: TextInput):
    try:

        #preprocess the input text
        sequence= tokenizer.texts_to_sequences([input.text])
        padded_sequence = pad_sequences(sequence, maxlen=32)


        prediction = model.predict(padded_sequence)
        sentiment = "Positive" if prediction >0.5 else "Negative"
        return {"sentiment": sentiment, "confidence":float(prediction[0][0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
