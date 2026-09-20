import matplotlib.image as mpimg        #Just for I/O operations

img = mpimg.imread("samples/BMW2.png")

print(type(img))        # ---> <class 'numpy.ndarray'>

print(img.shape)        # ---> (501, 399, 4)

print(img.dtype)        # ---> float32


# Now we write features one by one

def to_grayscale(img):
    G = img[:, :, 1 ]
    R = img[:, :, 0 ]
    B = img[:, :, 2 ]

    gray = 0.299*R + 0.587*G + 0.114*B
    return gray






