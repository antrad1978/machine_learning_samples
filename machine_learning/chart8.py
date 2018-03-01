import numpy as np
import matplotlib.pyplot as plot

x = np.random.normal(2, 0.5, 1000)
plot.hist(x, bins=50)
plot.savefig('my_hist')