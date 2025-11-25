import re
from nltk.tokenize import word_tokenize
f=open("test.txt")
text=f.read()
text=text.lower()
text=re.sub('[^A-Za-z0-9]+',' ',text)
text=re.sub("\S*\d\S*","",text).strip()
print(text)
w=word_tokenize(text,preserve_line=True)
from nltk.stem import PorterStemmer
ps=PorterStemmer()
ps_st=[ps.stem(i) for i in w]
print("\nStemming:\n\n",ps_st)
from nltk import WordNetLemmatizer
wnl=WordNetLemmatizer()
lema=[wnl.lemmatize(u) for u in w]
print("\n Lemmatization:\n\n",lema)
