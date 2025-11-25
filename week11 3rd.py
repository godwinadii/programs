import pandas as p
import matplotlib.pyplot as m
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
f=open("test.txt")
text=f.read()
w=word_tokenize(text)
freq=FreqDist(w)
print("Count of and word:",freq['and'])
freq=p.Series(dict(freq))
m.figure(figsize=(18,10))
freq.plot(kind='bar')
m.show()
