import matplotlib.pyplot as m
f=open("test.txt")
text=f.read()
from wordcloud import WordCloud, STOPWORDS
stop_w=set(STOPWORDS)
wc=WordCloud(width=800,height=800,
background_color='black',colormap='plasma',
stopwords=stop_w,
min_font_size=10).generate(text)
m.figure(figsize=(8,8),facecolor=None)
m.imshow(wc)
m.axis('off')
m.tight_layout(pad=0)
m.show()
