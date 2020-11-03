import cv2
import numpy as np

# Loading the haarcascade from the main path.
faceCascade = cv2.CascadeClassifier("/Users/Hetze/PycharmProjects/OpenCV/haarcascade_frontalface_default.xml")

# Calling the image from its original path.
img = cv2.imread("/Users/Hetze/OneDrive/Desktop/1.jpg")

# Image conversion into a grayscale filter.
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Setting up the variable to call the face detection location on the image.
faces = faceCascade.detectMultiScale(imgray, 1.1, 4)

# Looping the dimensions of the face soa that we can mark the location of the face.
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)


# Showing the image and the wait time is then set to 0.
cv2.imshow("Face", img)
cv2.waitKey(0)
