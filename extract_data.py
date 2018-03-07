import pickle
import numpy as np
import os

mf = open('train.conll')
mr = mf.read()
mrLines = mr.split('\n')
mrTrain = []
words = []
tags = []
X_train = []
Y_train = []
wordsList = []
tagList = []
for line in mrLines:
	if line == '':
		continue
	words1 = line.split()
	
	if words1[1] != '.':
		wordsList.append(words1[1])
		words.append(words1[1])
		tagList.append(words1[3])
		tags.append(words1[3])
	else:
		words.append(words1[1])
		tags.append(words1[3])
		wordsList.append(words1[1])
		tagList.append(words1[3])
		mrTrain.append([wordsList,tagList])
		X_train.append(wordsList)
		Y_train.append(tagList)
		wordsList = []
		tagList = []

print('TOTAL NO OF SAMPLES: ', len(X_train), '\n')


print('sample X_train: ', X_train[42], '\n')
print('sample Y_train: ', Y_train[42], '\n')

words = set(words)
tags = set(tags)

print('VOCAB SIZE: ', len(words))
print('TOTAL TAGS: ', len(tags))

assert len(X_train) == len(Y_train)


word2int = {}
int2word = {}

for i, word in enumerate(words):
	word2int[word] = i+1
	int2word[i+1] = word

tag2int = {}
int2tag = {}

for i, tag in enumerate(tags):
	tag2int[tag] = i+1
	int2tag[i+1] = tag

X_train_numberised = []
Y_train_numberised = []

for sentence in X_train:
	tempX = []
	for word in sentence:
		tempX.append(word2int[word])
	X_train_numberised.append(tempX)

for tags in Y_train:
	tempY = []
	for tag in tags:
		tempY.append(tag2int[tag])
	Y_train_numberised.append(tempY)

print('sample X_train_numberised: ', X_train_numberised[42], '\n')
print('sample Y_train_numberised: ', Y_train_numberised[42], '\n')

X_train_numberised = np.asarray(X_train_numberised)
Y_train_numberised = np.asarray(Y_train_numberised)

pickle_files = [X_train_numberised, Y_train_numberised, word2int, int2word, tag2int, int2tag]

with open('data.pkl', 'wb') as f:
	pickle.dump(pickle_files, f)

print('Saved as pickle file')
