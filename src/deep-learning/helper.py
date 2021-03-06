import numpy as np
from random import randint
import os

maxSeqLength = 250
batchSize = 24
lstmUnits = 64
numClasses = 2
iterations = 100000

wordsList = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/training_data/wordsList.npy'))
print('Loaded the word list.')

wordsList = wordsList.tolist()
wordsList = [word.decode('UTF-8') for word in wordsList]

wordVectors = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/training_data/wordVectors.npy'))
print('Loaded word vectors.')

ids = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/training_data/idsMatrix.npy'))
print('Loaded IDs.')

def getTrainBatch():
  labels = []
  arr = np.zeros[batchSize, maxSeqLength]

  for i in range(batchSize):
    if (i % 2 == 0):
      num = randint(1, 11499)
      labels.append([1, 0])
    else:
      num = randint(13499, 24999)
      labels.append([0, 1])
    
    arr[i] = ids[num-1:num]

  return arr, labels

def getTestBatch():
  labels = []
  arr = np.zeros([batchSize, maxSeqLength])

  for i in range(batchSize):
    num = randint(11499, 13499)

    if (num <= 12499):
      labels.append([1, 0])
    else:
      labels.append([0, 1])
    
    arr[i] = ids[num-1:num]
  
  return arr, labels