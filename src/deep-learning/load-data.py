import numpy as np

wordsList = np.load('/Users/nicbonetto/npm-packages/smart-sentiment/src/deep-learning/data/training_data/wordsList.npy')
print('Loaded the word list.')

wordsList = wordsList.tolist()
wordsList = [word.decode('UTF-8') for word in wordsList]

wordVectors = np.load('/Users/nicbonetto/npm-packages/smart-sentiment/src/deep-learning/data/training_data/wordVectors.npy')
print('Loaded word vectors.')