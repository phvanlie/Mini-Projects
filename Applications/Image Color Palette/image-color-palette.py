import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans
from PIL import Image

img = mpimg.imread('./asset/ww84.png')
w, h, d = img.shape
pix = img.reshape(w * h, d)

n_colors = 10
kmeans = KMeans(n_clusters=n_colors, random_state=42).fit(pix)
palette = np.uint8(kmeans.cluster_centers_)

plt.imshow([palette])
plt.show()