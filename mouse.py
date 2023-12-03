import cv2
import numpy_demo as np


def mouse_callback(event, x, y, flags, userdata):
    print(event, x, y, flags, userdata)


img = np.zeros((512, 512), np.uint8)

cv2.imshow('img', img)
cv2.setMouseCallback('img', mouse_callback, "123")

cv2.waitKey(0)
