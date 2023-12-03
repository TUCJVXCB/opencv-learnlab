import numpy as np
import cv2

# print(np.array([1, 2, 3]))
#
# print(np.array([[1, 2, 3], [3, 4, 5]]))
#
# print(np.zeros((8, 8, 3), np.uint8))
#
# print(np.full((10, 10, 3), 8))
#
# print(np.identity(9))
#
# print(np.eye(3, 4, 1))


img = np.zeros((512, 512, 3), np.uint8)


roi = img[100:400, 100:400]
roi[:,:] = [0, 0, 255]
count: int = 256

while count > 0:
    img[count, 256] = [0, 0, 255]
    count = count - 1

cv2.imshow('img', img)
cv2.imshow('img1', roi)
key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    exit()
