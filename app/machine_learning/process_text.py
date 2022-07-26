import numpy as np 
import tensorflow as tf
import nltk 
from nltk.corpus import stopwords 
import urllib.request 
import zipfile 
import os.path
from nltk.stem import WordNetLemmatizer
import re
from tensorflow.keras.preprocessing.text import Tokenizer


def remove_sw(text): 
    # try:
    #     nltk.data.find('corpora/stopwords')
    # except LookupError:
    #     nltk.download('stopwords')

    stop_words = stopwords.words('english')
    filtered_words = []
    for x in text: 
        if x not in stop_words:
            filtered_words.append(x)
    
    return filtered_words 

def lemmatize_token(text):
    # try:
    #     nltk.data.find('corpora/omw-1.4')
    #     nltk.data.find('corpora/wordnet')
    # except LookupError:
    #     nltk.download('wordnet')
    #     nltk.download('omw-1.4')

    lemmatizer = WordNetLemmatizer()
        
    lemmatized_token = [lemmatizer.lemmatize(x) for x in text] 

    return lemmatized_token 

def text_preprocessing(text): 
    text = text.lower() 
    text = re.sub('[^A-Za-z0-9 ]+', '', text)
    text =  np.array(text.split(" "))  
 
    # filtered_text = remove_sw(text) 

    lemmatized_token = lemmatize_token(text) 

    tokenizer = Tokenizer(num_words=5000)
    tokenizer.fit_on_texts(text)
    # print(lemmatized_token)

    token_array = np.array(lemmatized_token)

    input_array = token_array[np.newaxis, :]
    # print(input_array)

    input_text = tokenizer.texts_to_sequences(input_array.tolist())
    # print(input_text)

    padded_text = tf.keras.utils.pad_sequences(input_text, maxlen=100, dtype='float32', padding='post') 

    # print(padded_text)

    return padded_text



