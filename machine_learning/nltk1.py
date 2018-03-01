from nltk.book import *
from nltk.corpus import *
from nltk import *

download()

#find simiar words in text
text1.similar("monstrous")

#plot words distribution
fdist1=FreqDist(text1)

fdist1.plot(20,cumulative=True)

#V = set(text1)

#long_words = [w for w in V if len(w) > 15]

#print(sorted(long_words))

#print(gutenberg.fileids())

#words = gutenberg.words('austen-emma.txt')

#print(len(words))

from nltk.corpus import brown

print(brown.categories())

news_text = brown.words(categories="news")

fdist = FreqDist(w.lower() for w in news_text)

modals = ["can", "could", "may", "might", "must", "will"]

for m in modals:
    print(m + ":", fdist[m])
