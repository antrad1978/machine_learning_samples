import numpy as np
import matplotlib.pyplot as plot

labels = ["Baseline", "System"]
data =   [3.75, 4.75]
yerror =  [0.3497, 0.3108]
xerror = [0.2, 0.2]
xlocations = np.array(range(len(data)))+0.5
width = 0.5
csize = 10
ec = 'r'
plot.bar(xlocations, data, yerr=yerror, width=width,
  xerr=xerror, capsize=csize, ecolor=ec)
plot.yticks(range(0, 8))
plot.xticks(xlocations+ width/2, labels)
plot.xlim(0, xlocations[-1]+width*2)
plot.title("Average Ratings on the Training Set")
plot.savefig('bar')