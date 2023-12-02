import cv2


cap = cv2.VideoCapture(0)

while True:
    res, img = cap.read()
    if not res:
        continue
    cv2.imshow('cap', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()