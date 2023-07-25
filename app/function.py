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
  """Predict text and return polarity"""

  cleaner = cleaning_data()
  clean = cleaner.fit_transform(text)
  if model_name == 'Simple Neutral Net':
    model_name = 'SNN_model.h5'
  if model_name == 'Long Short Term Memory (LSTM)':
    model_name = 'LSTM_model.h5'
  if model_name == 'Convolutional Neutral Net (CNN)':
    model_name = 'CNN_model.h5'

  model_demo = load_model(f"../models/{model_name}")
  return model_demo.predict(clean)

  