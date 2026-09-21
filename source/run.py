import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from operations import to_grayscale
from operations import adjust_brightness
from operations import adjust_contrast

img = mpimg.imread("samples/BMW2.png")
gray = to_grayscale(img)
plt.imsave("outputs/BMW2Gray.png", gray, cmap = "gray")


bright = adjust_brightness(img, 0.33)
dark = adjust_brightness(img, -0.33)
high_contrast = adjust_contrast(img,1.3)
low_contrast = adjust_contrast(img, 0.7)

plt.imsave("outputs/bright.jpg", bright)
plt.imsave("outputs/dark.jpg", dark)
plt.imsave("outputs/high_contrast.jpg", high_contrast)
plt.imsave("outputs/low_contrast.jpg", low_contrast)
