import cv2
import numpy as np


img = np.zeros((512, 512, 3), np.uint8)

b, g, r = cv2.split(img)

r1 = np.zeros((512, 512), np.uint8)

b[10:100, 10:100] = 124
g[10:100, 10:100] = 124



newImg = cv2.merge((b,g,r1))
cv2.imshow('img1', newImg)
cv2.waitKey(0)