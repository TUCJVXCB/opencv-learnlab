import cv2

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
eyesCascade = cv2.CascadeClassifier("Resources/haarcascade_eye.xml")

def detect_face(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

def detect_face_and_eyes(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.1, 2)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        #注意y在前面
        roi_img = img[y:y+h, x:x+w]
        eyes = eyesCascade.detectMultiScale(roi_img, 1.1, 2)
        for (x1, y1, w1, h1) in eyes:
            cv2.rectangle(roi_img, (x1, y1), (x1 + w1, y1 + h1), (255, 0, 0), 2)

while True:
    success, img = cap.read()
    detect_face_and_eyes(img)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
