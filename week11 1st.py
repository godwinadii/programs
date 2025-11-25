import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
f=open("test.txt")
text=f.read()
print(text)
sent=sent_tokenize(text)
print("Number of sentences:",len(sent))
for i in range(len(sent)):
    print("\nSentence:",i+1,"\n",sent[i])
w=word_tokenize(text)
print("\nTotal Words:",len(w))
print(w)
