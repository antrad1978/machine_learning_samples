from skimage.io import imread
from skimage.transform import resize
from matplotlib import pyplot as plt
import matplotlib.cm as cm

#%matplotlib inline
example_file = ("http://images.all-free-download.com/images/graphiclarge/cute_dog_photo_picture_7_168843.jpg")
image = imread(example_file, as_grey=True)

import warnings
warnings.filterwarnings("ignore")
from skimage import filters, restoration
from skimage.morphology import disk
median_filter = filters.rank.median(image, disk(1))
tv_filter = restoration.denoise_tv_chambolle(image,
                                             weight=0.1)
gaussian_filter = filters.gaussian_filter(image,
sigma=0.7)

fig = plt.figure()
for k,(t,F) in enumerate((('Median filter',median_filter),('TV filter',tv_filter),('Gaussian filter', gaussian_filter))):
    f=fig.add_subplot(1,3,k+1)
    plt.axis('off')
    f.set_title(t)
    plt.imshow(F, cmap=cm.gray)
plt.show()

print("data type: %s, shape: %s" %
      (type(image), image.shape))