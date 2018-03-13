# Persian-POSTagger-with-LSTM
a Persian POS Tagger with LSTM

In this Part of Speech Tagger I used an Implementation from [here](https://github.com/aneesh-joshi/LSTM_POS_Tagger) which has used LSTM neural network. you can look at the pdf file in this repository and you can watch [this video](https://drive.google.com/open?id=0B5-t3yDeHRzKVEZ4VUMwSWtwbDA) for more information.
I have trained the model on [Hamshahri corpus](http://dbrg.ut.ac.ir/Hamshahri/) and have tested on it, and get the glove file from [here](https://github.com/HaniehP/PersianNER) to train.


In second commit I added makeCompatible.py which normalize persian text. I used [this code](https://github.com/JKhakpour/virastar.py/blob/master/virastar.py) and slightly have changed it for tokenizing and normalizing input text.
you can put your arbitrary input text in user.text and call model_evaluation.py and get word/POS-tag format of your input.


