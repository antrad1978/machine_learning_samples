import numpy as np
import matplotlib.pyplot as plot

lines = plot.plot([1,2,3],'b-',[0,1,2],'r--')
plot.legend(lines, ('First','Second'))
plot.savefig('legend')