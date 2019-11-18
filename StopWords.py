from nltk.tokenize import TweetTokenizer as nltktk
from nltk.corpus import stopwords


stp = set(stopwords.words('portuguese'))
a=nltktk()
x =input("")
l=a.tokenize(x)

l=([palavra for palavra in l if palavra not in stp])


print(l)