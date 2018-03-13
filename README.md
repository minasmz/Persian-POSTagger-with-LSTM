# Persian-POSTagger-with-LSTM
A Persian POS Tagger with LSTM

In this Part of Speech Tagger I used an Implementation from [here](https://github.com/aneesh-joshi/LSTM_POS_Tagger) which has used LSTM neural network. you can look at the pdf file in this repository and you can watch [this video](https://drive.google.com/open?id=0B5-t3yDeHRzKVEZ4VUMwSWtwbDA) for more information.
I have trained the model with [Hamshahri corpus](http://dbrg.ut.ac.ir/Hamshahri/) and have tested on it, and get the glove file from [here](https://github.com/HaniehP/PersianNER) to train.


In second commit I added makeCompatible.py which normalizes persian texts. I have used [this code](https://github.com/JKhakpour/virastar.py/blob/master/virastar.py), and slightly have changed it for tokenizing and normalizing input text.


For running this POS Tagger put your arbitrary input text in user.txt file, and call model_evaluation.py and get word/POS-tag format of your input.

### You can see a sample output of this LSTM POS Tagger below:
> نوروز/N نخستین/ADJ روز/N سال/N خورشیدی/N ایرانی/ADJ برابر/N با/P یکم/N فروردین/N ماه/N ،/DELM جشن/N آغاز/N سال/N نوی/N ایرانی/ADJ و/CON یکی/NUM از/P کهن‌ترین/N جشن‌های/N به/P جا/N مانده/V از/P دوران/N ایران/N باستان/ADJ است/V ./DELM 
خاستگاه/N نوروز/N در/P ایران/N باستان/ADJ است/V و/CON هنوز/ADV هم/CON مردم/N مناطق/N گوناگون/ADJ فلات/N ایران/N ،/DELM نوروز/N را/CLITIC جشن/N می‌گیرند/V ./DELM 
زمان/N برگزاری/N نوروز/N ،/DELM در/P آغاز/N فصل/N بهار/N است/V که/CON امروزه/ADV به/P آن/DET برابری/N بهاری/N یا/CON اکیونوس/N می‌گویند/V ./DELM 
نوروز/N در/P ایران/N و/CON افغانستان/N آغاز/N سال/N نو/ADJ محسوب/ADJ می‌شود/V و/CON در/P برخی/DET دیگر/ADJ از/P کشورها/N یعنی/CON تاجیکستان/N ،/DELM روسیه/N ،/DELM قرقیزستان/N ،/DELM قزاقستان/N ،/DELM سوریه/N ،/DELM عراق/N ،/DELM گرجستان/N ،/DELM جمهوری/N آذربایجان/N ،/DELM آلبانی/N ،/DELM چین/N ،/DELM ترکیه/N ،/DELM ترکمنستان/N ،/DELM هند/N ،/DELM پاکستان/N و/CON ازبکستان/N تعطیل/ADJ رسمی/ADJ است/V و/CON مردمان/N آن/DET جشن/N را/CLITIC برپا/ADJ می‌کنند/V ./DELM 



