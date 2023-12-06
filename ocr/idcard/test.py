# import idcard_recognize
import cv2
import numpy as np

# print(idcard_recognize.process('../../Resources/person1.jpeg'))

img = np.zeros((512, 512), np.uint8)
print(img)
print(cv2.UMat(img))
cv2.imshow('aa', img)
cv2.imshow('bb', cv2.UMat(img))
cv2.waitKey(0)
