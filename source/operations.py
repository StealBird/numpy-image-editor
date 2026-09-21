import matplotlib.image as mpimg 
import numpy as np       #Just for I/O operations

img = mpimg.imread("samples/BMW2.png")

#print(type(img))        # ---> <class 'numpy.ndarray'>

#print(img.shape)        # ---> (501, 399, 4)

#print(img.dtype)        # ---> float32


# Now we write features one by one

def to_grayscale(img):
    G = img[:, :, 1 ]
    R = img[:, :, 0 ]
    B = img[:, :, 2 ]

    gray = 0.299*R + 0.587*G + 0.114*B
    return gray


def adjust_brightness(img, value):
   
    result = img + value
    result = np.clip(result,0,1)
    return result.astype(np.float32)

def adjust_contrast(img,factor):
    
    result = img * factor 
    result = np.clip(result, 0, 1)
    return result.astype(np.float32)


def crop(img,top,bottom,left,right):
    return img[top:bottom, left:right]

def horizontal_flip(img):
    return img[ :, ::-1]

def vertical_flip(img):
    return img[:: -1, :]






