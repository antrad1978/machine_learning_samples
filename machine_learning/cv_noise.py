import numpy as np
import matplotlib.pyplot as plt

from skimage import data, img_as_float
from skimage.restoration import denoise_nl_means


astro = img_as_float(data.astronaut())
astro = astro[30:180, 150:300]

noisy = astro + 0.3 * np.random.random(astro.shape)
noisy = np.clip(noisy, 0, 1)

denoise = denoise_nl_means(noisy, 7, 9, 0.08, multichannel=True)

fig, ax = plt.subplots(ncols=2, figsize=(8, 4), sharex=True, sharey=True,
                       subplot_kw={'adjustable': 'box-forced'})

ax[0].imshow(noisy)
ax[0].axis('off')
ax[0].set_title('noisy')
ax[1].imshow(denoise)
ax[1].axis('off')
ax[1].set_title('non-local means')

fig.tight_layout()

plt.show()