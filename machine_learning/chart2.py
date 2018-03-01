import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
line, = ax.plot(np.random.rand(10))
ax.set_ylim(0, 1)

plt.show()