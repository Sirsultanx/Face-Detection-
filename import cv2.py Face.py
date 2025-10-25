import cv2
from cvzone.FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture(0)
detector = FaceDetector()

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    # Detecting Face
    img, bboxes = detector.findFaces(img)
    cv2.imshow("Camera Feed",img)
    cv2.waitKey(1)