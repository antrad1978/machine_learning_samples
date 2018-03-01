from skimage.io import imread
from skimage.transform import resize
from matplotlib import pyplot as plt
import matplotlib.cm as cm

#%matplotlib inline
example_file = ("http://www.emoji.co.uk/files/phantom-open-emojis/animals-nature-phantom/12394-dog-face.png")
image = imread(example_file, as_grey=True)
plt.imshow(image, cmap=cm.gray)
plt.show()

import warnings
warnings.filterwarnings("ignore")
from skimage import filters, restoration
from skimage.morphology import disk
median_filter = filters.rank.median(image, disk(1))
#Remove noise from image
#Explained https://en.wikipedia.org/wiki/Noise_reduction#In_images
tv_filter = restoration.denoise_tv_chambolle(image,
                                             weight=0.1)
gaussian_filter = filters.gaussian_filter(image,
sigma=0.7)