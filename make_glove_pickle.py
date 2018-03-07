import pickle
import numpy as np

embeddings_index = {}

f = open('glove.6B.100d.txt')

for line in f:
    values = line.split()
    word = values[0]
    print (word)
    try:
    	coefs = np.asarray(values[1:], dtype='float32')
    except:
    	pass
    embeddings_index[word] = coefs
f.close()

with open('PickledData/Glove.pkl', 'wb') as f:
	pickle.dump(embeddings_index, f)