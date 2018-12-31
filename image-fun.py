
"""
This code loads an image, finds edges
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
plt.ion()
img = cv2.imread('derry-girls.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
k = np.ones((7, 7)) / (7**2)
img_gray_smoothed = cv2.blur(img_gray,(7, 7) )
edges = cv2.Canny(img_gray_smoothed, 50, 100, 21)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
faces = face_cascade.detectMultiScale(img_gray, 1.3, 2)

fig = plt.figure("image fun")

plt.subplot(2, 2, 1)
plt.imshow(np.stack((img[:, :, 2], img[:, :, 1], img[:, :, 0]), axis=2))
plt.title('Derry Girls')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 3)
plt.imshow(img_gray, cmap='gray')
plt.title('Grey Derry Girls')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 2)
plt.imshow(edges, cmap='gray')
plt.title('Edgy Derry Girls')
plt.xticks([])
plt.yticks([])

for (x, y, w, h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = img_gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

plt.subplot(2, 2, 4)
plt.imshow(np.stack((img[:, :, 2], img[:, :, 1], img[:, :, 0]), axis=2))
plt.title('Derry Girl Faces')
plt.xticks([])
plt.yticks([])
plt.show()
