#Tokenization [Sentence & Word]
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
f = open("Test.txt")
text = f.read()
print(text)
sent = sent_tokenize(text)
print("Number of sentences:", len(sent))
for i in range(len(sent)):
    print("\nSentence:", i + 1, "\n", sent[i])
w = word_tokenize(text)
print("\nTotal Words:", len(w))
print(w)

#N-Grams
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
w = word_tokenize(text)
print("Bi-Grams:\n\n", list(ngrams(w, 2)))
print("\n\nTri-Grams:\n\n", list(ngrams(w, 3)))

#Frequency Distribution of Words
import pandas as p
import matplotlib.pyplot as m
from nltk.probability import FreqDist
freq = FreqDist(w)
print("Count of and word:", freq['and'])
freq = p.Series(dict(freq))
m.figure(figsize=(18, 10))
freq.plot(kind='bar')
m.show()

#Removing Stop-words
import nltk
from nltk.probability import FreqDist
w = word_tokenize(text)
print("Before Removal of Stopwords words count:", len(w))
stop_w = nltk.corpus.stopwords.words('english')
removed_stopw = []
for i in w:
    if i not in stop_w:
        removed_stopw.append(i)
print("\nAfter Removal of StopWords:", len(removed_stopw))
freq = FreqDist(removed_stopw)
freq_series = p.Series(dict(freq))
m.figure(figsize=(18, 10))
freq_series.plot(kind='bar')
m.show()


#Word-cloud
from wordcloud import WordCloud, STOPWORDS

stop_w = set(STOPWORDS)

wc = WordCloud(width=800, height=800,
               background_color='black', colormap='plasma',
               stopwords=stop_w,
               min_font_size=10).generate(text)

m.figure(figsize=(8, 8), facecolor=None)
m.imshow(wc)
m.axis('off')
m.tight_layout(pad=0)
m.show()


# Stemming & Lemmatization

import re
from nltk.tokenize import word_tokenize
text = text.lower()
text = re.sub('[^A-Za-z0-9]+', ' ', text)
text = re.sub("\S*\d\S*", "", text).strip()
print(text)
w = word_tokenize(text, preserve_line=True)
from nltk.stem import PorterStemmer
ps = PorterStemmer()
ps_st = [ps.stem(i) for i in w]
print("\nStemming:\n\n", ps_st)
from nltk import WordNetLemmatizer
wnl = WordNetLemmatizer()
lema = [wnl.lemmatize(u) for u in w]
print("\n Lemmatization:\n\n", lema)