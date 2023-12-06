import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Resources/lena.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
light = cv2.threshold(gray, 0, 255,
                              cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

hist = cv2.calcHist([light], [0], None, [256], [0, 256])

plt.plot(hist)
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()