import re
import os
import pickle
from nltk.corpus import stopwords
from tensorflow.keras.preprocessing.text import Tokenizer 
from tensorflow.keras.preprocessing.sequence import pad_sequences

# nltk.download('stopwords')
class cleaning_data:
  def __init__(self, text=''):
    self.text = text
    with open("../models/word_tokenizer.pkl", "rb") as file:
      self.word_tokenizer = pickle.load(file)
  
  def remove_abb(self,text):
    """ Convert abbreviated into full form"""
    text = re.sub(r"he's", "he is", text)
    text = re.sub(r"there's", "there is", text)
    text = re.sub(r"We're", "We are", text)
    text = re.sub(r"That's", "That is", text)
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"they're", "they are", text)
    text = re.sub(r"Can't", "Cannot", text)
    text = re.sub(r"wasn't", "was not", text)
    text = re.sub(r"don't", "do not", text)
    text= re.sub(r"aren't", "are not", text)
    text = re.sub(r"isn't", "is not", text)
    text = re.sub(r"What's", "What is", text)
    text = re.sub(r"haven't", "have not", text)
    text = re.sub(r"hasn't", "has not", text)
    text = re.sub(r"There's", "There is", text)
    text = re.sub(r"He's", "He is", text)
    text = re.sub(r"It's", "It is", text)
    text = re.sub(r"You're", "You are", text)
    text = re.sub(r"I'M", "I am", text)
    text = re.sub(r"shouldn't", "should not", text)
    text = re.sub(r"wouldn't", "would not", text)
    text = re.sub(r"i'm", "I am", text)
    text = re.sub(r"I'm", "I am", text)
    text = re.sub(r"I'm", "I am", text)
    text = re.sub(r"Isn't", "is not", text)
    text = re.sub(r"Here's", "Here is", text)
    text = re.sub(r"you've", "you have", text)
    text = re.sub(r"you've", "you have", text)
    text = re.sub(r"we're", "we are", text)
    text = re.sub(r"what's", "what is", text)
    text = re.sub(r"couldn't", "could not", text)
    text = re.sub(r"we've", "we have", text)
    text = re.sub(r"it's", "it is", text)
    text = re.sub(r"doesn't", "does not", text)
    text = re.sub(r"It's", "It is", text)
    text = re.sub(r"Here's", "Here is", text)
    text = re.sub(r"who's", "who is", text)
    text = re.sub(r"I've", "I have", text)
    text = re.sub(r"y'all", "you all", text)
    text = re.sub(r"can't", "cannot", text)
    text = re.sub(r"would've", "would have", text)
    text = re.sub(r"it'll", "it will", text)
    text = re.sub(r"we'll", "we will", text)
    text = re.sub(r"wouldn't", "would not", text)
    text = re.sub(r"We've", "We have", text)
    text = re.sub(r"he'll", "he will", text)
    text = re.sub(r"Y'all", "You all", text)
    text = re.sub(r"Weren't", "Were not", text)
    text = re.sub(r"Didn't", "Did not", text)
    text = re.sub(r"they'll", "they will", text)
    text = re.sub(r"they'd", "they would", text)
    text = re.sub(r"DON'T", "DO NOT", text)
    text = re.sub(r"That's", "That is", text)
    text = re.sub(r"they've", "they have", text)
    text = re.sub(r"i'd", "I would", text)
    text = re.sub(r"should've", "should have", text)
    text = re.sub(r"You're", "You are", text)
    text = re.sub(r"where's", "where is", text)
    text = re.sub(r"Don't", "Do not", text)
    text = re.sub(r"we'd", "we would", text)
    text = re.sub(r"i'll", "I will", text)
    text = re.sub(r"weren't", "were not", text)
    text = re.sub(r"They're", "They are", text)
    text = re.sub(r"Can't", "Cannot", text)
    text = re.sub(r"you'll", "you will", text)
    text = re.sub(r"I'd", "I would", text)
    text = re.sub(r"let's", "let us", text)
    text = re.sub(r"it's", "it is", text)
    text = re.sub(r"can't", "cannot", text)
    text = re.sub(r"don't", "do not", text)
    text = re.sub(r"you're", "you are", text)
    text = re.sub(r"i've", "I have", text)
    text = re.sub(r"that's", "that is", text)
    text = re.sub(r"i'll", "I will", text)
    text = re.sub(r"doesn't", "does not",text)
    text = re.sub(r"i'd", "I would", text)
    text = re.sub(r"didn't", "did not", text)
    text = re.sub(r"ain't", "am not", text)
    text = re.sub(r"you'll", "you will", text)
    text = re.sub(r"I've", "I have", text)
    text = re.sub(r"Don't", "do not", text)
    text = re.sub(r"I'll", "I will", text)
    text = re.sub(r"I'd", "I would", text)
    text = re.sub(r"Let's", "Let us", text)
    text = re.sub(r"you'd", "You would", text)
    text = re.sub(r"It's", "It is", text)
    text = re.sub(r"Ain't", "am not", text)
    text = re.sub(r"Haven't", "Have not", text)
    text = re.sub(r"Could've", "Could have", text)
    text = re.sub(r"youve", "you have", text)
    text = re.sub(r"don't", "do not", text)
    return text
  
  def clean_text(self, text):
    '''clean up text'''
    text = text.lower()

    #remove html tags
    Tag_re = re.compile(r'<[^>]+>')
    text  = Tag_re.sub(' ', text)

    #change abbreviated into full words
    text = self.remove_abb(text)

    #remove punctuations and numbers
    text = re.sub(r'[^a-zA-Z]', ' ', text)

    #Single character removal
    text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)

    #remove multiple spaces
    text = re.sub(r'\s+', ' ', text)

    #remove stopwords
    stopwords_list = [word for word in stopwords.words('english') if word != 'not']
    pattern = re.compile(r'\b(' + r'|'.join(stopwords_list) + r')\b\s*')
    text = pattern.sub('', text)
    return text 

  def fit_transform(self, corpus):
    cleaned = [self.clean_text(text) for text in corpus]
    cleaned = self.word_tokenizer.texts_to_sequences(cleaned)
    return pad_sequences(cleaned, padding="post", maxlen=100)

if __name__ == "__main__":
  print(os.getcwd())