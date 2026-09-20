import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from operations import to_grayscale

img = mpimg.imread("samples/BMW2.png")
gray = to_grayscale(img)
plt.imsave("outputs/BMW2Gray.png", gray, cmap = "gray")