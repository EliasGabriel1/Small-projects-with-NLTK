from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("portuguese")
def a():
    a = stemmer.stem(x)
    print(a)

x=input("")

from nltk.tokenize import TweetTokenizer as nltktk
from nltk.corpus import stopwords


stp = set(stopwords.words('portuguese'))
b=nltktk()
z =input("")
l=b.tokenize(z)

l=([palavra for palavra in l if palavra not in stp])

print(l)
stemmer2 = SnowballStemmer ("portuguese", ignore_stopwords = True)
for i in range(3):
    l[i]=stemmer.stem(l[i])

print(l)
print (stemmer2.stem ("inteiramente"))
print(SnowballStemmer("portuguese").stem("generosamente"))
print (SnowballStemmer ("portuguese"). stem ("generosamente"))
print(a())