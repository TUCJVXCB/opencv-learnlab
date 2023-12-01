import cv2
import matplotlib.pylab as plt
import numpy as np


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def show_img(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def show_video():
    vc = cv2.VideoCapture('/Users/tanyu/Downloads/dog.mp4')
    if vc.isOpened():
        open, frame = vc.read()
    else:
        open = False

    while open:
        res, frame = vc.read()
        if frame is None:
            break
        if res == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('result', gray)
            if cv2.waitKey(10) & 0xFF == 27:
                break
    vc.release()
    cv2.destroyAllWindows()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    img = cv2.imread('Resources/lena.png')
    kernel = np.ones((5, 5), np.uint8)
    print(type)

    grayImg = img
    blurImg = cv2.GaussianBlur(grayImg, (7, 7), 0)

    imgCanny1 = cv2.Canny(img, 150, 200)
    imgCanny2 = cv2.Canny(img, 100, 150)

    imgDilate = cv2.dilate(imgCanny1, kernel, iterations=1)

    imgErode = cv2.erode(imgDilate, kernel, iterations=1)

    # cv2.imshow('canny', imgCanny1)
    # cv2.imshow('dilate', imgDilate)
    # cv2.imshow('erode', imgErode)

    cv2.waitKey(0)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
