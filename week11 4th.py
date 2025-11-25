import nltk
import matplotlib.pyplot as m
import pandas as p
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
f=open("test.txt")
text=f.read()
w = word_tokenize(text)
print("Before Removal of Stopwords words count:",len(w))
stop_w = nltk.corpus.stopwords.words('english')
removed_stopw = []
for i in w:
    if i not in stop_w:
        removed_stopw.append(i)
print("\nAfter Removal of StopWords:",len(removed_stopw))
freq = FreqDist(removed_stopw)
freq_series = p.Series(dict(freq))
m.figure(figsize=(18, 10))
freq_series.plot(kind='bar')
m.show()
