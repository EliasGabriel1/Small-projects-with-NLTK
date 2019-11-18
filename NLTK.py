from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import TweetTokenizer as tlkk
from nltk.corpus import stopwords as stp
from nltk.stem import LancasterStemmer


stp=set(stp.words('portuguese')) #Chamando todas stopwords em português
stemmer=SnowballStemmer('portuguese') #chamando todos tipos de prefixo
c="cachorro"
a=tlkk() #chama a função da nltk de toquenizar
y=input("")
l=a.tokenize(y) #   Quebra toda frase em toquens
#l.upper(c)
l=([palavra for palavra in l if palavra not in stp]) #tira todas stop words

for i in range(len(l)):
    l[i]=stemmer.stem(l[i])#todo prefixo como: ExtramENTE, ousadamENTE,socialMENTE é tirado

print(l)
