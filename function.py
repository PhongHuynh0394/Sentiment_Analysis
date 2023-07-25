import warnings

# Suppress all FutureWarnings
warnings.filterwarnings("ignore", category=FutureWarning)

import pickle
import string
import nltk
import numpy as np
from tensorflow.keras.models import load_model
from cleaning_data import cleaning_data

def predict(model_name, text):
  cleaner = cleaning_data()
  clean = cleaner.fit_transform(text)
  if model_name == 'Simple Neutral Net':
    model_name = 'SNN_model.h5'
  if model_name == 'Long Short Term Memory (LSTM)':
    model_name = 'LSTM_model.h5'
  if model_name == 'Convolutional Neutral Net (CNN)':
    model_name = 'CNN_model.h5'

  model_demo = load_model(f"./models/{model_name}")
  return model_demo.predict(clean)


if __name__ == "__main__":
  a = ['i hate you', 'i love you so much']
  model= ['Simple Neutral Net', 'Long Short Term Memory (LSTM)', 'Convolutional Neutral Net (CNN)']
  clean = cleaning_data()
  c = clean.fit_transform(a)
  # print(predict(model[1], a))
  model = load_model("models/SNN_model.h5")
  print(model.predict(c))
  