from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from bs4 import BeautifulSoup
from serial.request import Request
from statsmodels.compat import urlopen
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from collections import defaultdict
from heapq import nlargest


stp = set(stopwords.words('portuguese')+ list(punctuation))


link = Request('http://ultimosegundo.ig.com.br/politica/2017-04-25/reforma-da-previdencia.html',headers={'User-Agent': 'Mozilla/5.0'})
pagina = urlopen(link).read().decode('utf-8', 'ignore')

soup = BeautifulSoup(pagina, "lxml")
texto = soup.find(id="noticia").text
sentencas = sent_tokenize(texto)
palavras = word_tokenize(texto.lower())
stopwords = stp
palavras_sem_stopwords = [palavra for palavra in palavras if palavra not in stopwords]

frequencia = FreqDist(palavras_sem_stopwords)
sentencas_importantes = defaultdict(int)
for i, sentenca in enumerate(sentencas):
    for palavra in word_tokenize(sentenca.lower()):
        if palavra in frequencia:
            sentencas_importantes[i] += frequencia[palavra]
idx_sentencas_importantes=nlargest(4,sentencas_importantes,sentencas_importantes.get)

for i in sorted(idx_sentencas_importantes):
    print(sentencas[i])