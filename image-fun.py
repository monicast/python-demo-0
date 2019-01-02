
"""
This code loads an image and do stuff with it
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

def find_faces(image_file='derry-girls.jpg'):
    plt.ion()
    img = cv2.imread(image_file, cv2.IMREAD_COLOR)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(img_gray, 1.3, 2)
    return faces

def show_rois(image, rois, window_title='', figure_titles=['',''], rgb_or_bgr='bgr'):
    fig = plt.figure(window_title)
    plt.subplot(1, 2, 1)
    if rgb_or_bgr.lower() == 'bgr':
        plt.imshow(image[:,:,::-1])
    else:
        plt.imshow(image)
    plt.title('No ROIs')
    plt.xticks([])
    plt.yticks([])

    plt.subplot(2, 2, 4)
    plt.imshow(np.stack((img[:, :, 2], img[:, :, 1], img[:, :, 0]), axis=2))
    plt.title('Derry Girl Faces')
    plt.xticks([])
    plt.yticks([])
    plt.show()

for (face_x, face_y, face_w, face_h) in faces:
    cv2.rectangle(img, (face_x, face_y), (face_x+face_w, face_y+face_h), (255, 0, 0), 2)
    roi_gray = img_gray[face_y:face_y+face_h, face_x:face_x+face_w]
    roi_color = img[face_y:face_y+face_h, face_x:face_x+face_w]

fig = plt.figure("image fun")
plt.setp(axes, xticks=[], yticks=[])
plt.subplot(2, 2, 1)
# plt.imshow(np.stack((img[:, :, 2], img[:, :, 1], img[:, :, 0]), axis=2))
plt.imshow(img[:,:,::-1])
plt.title('RGB Image')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 3)
plt.imshow(img_gray, cmap='gray')
plt.title('Greyscale')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 2)
plt.imshow(edges, cmap='gray')
plt.title('Edges')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 4)
plt.imshow(np.stack((img[:, :, 2], img[:, :, 1], img[:, :, 0]), axis=2))
plt.title('Derry Girl Faces')
plt.xticks([])
plt.yticks([])
plt.show()

if __name__ == "__main__":
    pass
     