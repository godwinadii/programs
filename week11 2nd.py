from nltk.util import ngrams
from nltk.tokenize import word_tokenize
f=open("test.txt")
text=f.read()
w=word_tokenize(text)
print("Bi-Grams:\n\n",list(ngrams(w,2)))
print("\n\nTri-Grams:\n\n",list(ngrams(w,3)))