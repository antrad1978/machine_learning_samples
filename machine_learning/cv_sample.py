import numpy as np
from skimage import data,io

coins = data.coins()
#histo = np.histogram(coins, bins=np.arange(0, 256))

from skimage.feature import canny
edges = canny(coins/255.)

#from scipy import ndimage as ndi
#fill_coins = ndi.binary_fill_holes(edges)

#io.imshow(edges)
#io.show()

from scipy import ndimage as ndi
fill_coins = ndi.binary_fill_holes(edges)

io.imshow(fill_coins)
io.show()