import tensorflow as tf
 from tensorflow import keras
  from tensorflow.keras.layers import Dense, Embedding, Bidirectional, LSTM 
  from tensorflow.keras.datasets import imdb 
  
  num_words = 16000 # nombre de mots à utiliser 
  maxlen = 100 # longueur maximale de chaque avis 
  (x_train, y_train), (x_test, y_test) imdb.load_data(num_words=num_words)