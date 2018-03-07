from keras.models import load_model
import pickle
import numpy as np
from keras.preprocessing.sequence import pad_sequences
from keras.utils.np_utils import to_categorical

with open('data.pkl', 'rb') as f:
	X_train, Y_train, word2int, int2word, tag2int, int2tag = pickle.load(f)

	del X_train
	del Y_train

#statement = 'سیب قرمز'.split()
statement='نظامی می\u200cگوید که در سال ۵۱۰ تربت او را زیارت کرده .'.split()

model = load_model('initial_model.h5')
def pred (statement):
	print (statement)
	tokenised_statement = []
	for word in statement:
		try:
			tokenised_statement.append(word2int[word])
		except:
			tokenised_statement.append(4751)
	tokenised_statement = np.asarray([tokenised_statement])
	tokenised_statement = pad_sequences(tokenised_statement, maxlen=300)
	prediction = model.predict(tokenised_statement)
	tagSent = []
	for pred in prediction[0]:

		try:
			tagSent.append(int2tag[np.argmax(pred)])
		except:
			pass
	return (tagSent)

def findAcc ():
	mf = open('test.conll')
	mr = mf.read()
	mrLines = mr.split('\n')
	mrTrain = []
	txTrain = []
	tgTrain = []
	wordsList = []
	tagList = []
	for line in mrLines:
		if line == '':
			continue
		words = line.split()
	
		if words[1] != '.':
			wordsList.append(words[1])
			tagList.append(words[3])
		else:
			wordsList.append(words[1])
			tagList.append(words[3])
			mrTrain.append([wordsList,tagList])
			txTrain.append(wordsList)
			tgTrain.append(tagList)
			wordsList = []
			tagList = []

	total = 0
	false = 0
	true = 0
	for i in range (len(txTrain)):
		res = pred(txTrain[i])
		myTag = tgTrain[i]
		print (res)
		for j in range (len(myTag)):
			total+=1
			if myTag[j]==res[j]:
				true+=1
			else:
				false+=1
	print (float(true)/total)



#print (pred(statement))
findAcc()
