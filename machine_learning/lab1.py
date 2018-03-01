import numpy
file="./test.txt"

def count_words(file):
    wordDict = {}
    lines = open(file, "r").readlines()
    for line in lines:
        line = line.lower().replace('.', '').replace(',', '')
        for word in line.split():
            if word not in wordDict:
                wordDict[word] = wordDict.get(word, 0) + 1
            else:
                wordDict[word] = wordDict[word]+1
    return wordDict

res=count_words(file)

print(res)

from operator import itemgetter

ordered = sorted(res.items(), key=itemgetter(1))

lasts = ordered[-4:]

labels = []
y = numpy.empty(0)

for item in lasts:
    y = numpy.append(y, item[1])
    labels.append(item[0])

file = open(file, "r", encoding="utf-8-sig")

from collections import Counter
wordcount = Counter(file.read().split())

import matplotlib.pyplot as plt

# Data to plot
labels.append("Other")
y=numpy.append(y,sum(wordcount.values())-(numpy.sum(y)))
sizes = y.tolist()
colors = ['gold',  'blue', 'green', 'red']
explode = numpy.zeros(len(sizes)) # explode 1st slice

# Plot
#plt.pie(sizes, explode=explode, labels=labels, colors=colors,
#        autopct='%1.1f%%', shadow=True, startangle=140)

plt.pie(sizes, explode=explode, labels=labels, colors=colors)

plt.axis('equal')
plt.show()