
"""
A not completely contrived demo.
Demos
- docstrings
- opencv
  - basic loading of images
  - face finding
  - drawing rectangles
- numpy
  - 2D arrays for images
  - pass by reference
- matplotlib
  - showing images
  - interactive and non-interactive mod
- basic module structure
  - calling from __main__
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

def find_faces(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    face_rois = face_cascade.detectMultiScale(img_gray, 1.3, 3)
    return face_rois

def add_rois_to_image(image, rois):
    for (roi_x, roi_y, roi_w, roi_h) in rois:
        cv2.rectangle(image, (roi_x, roi_y), (roi_x+roi_w, roi_y+roi_h), (255, 0, 0), 2)

def find_faces_and_display(image_file, interactive=True):
    img = cv2.imread(image_file, cv2.IMREAD_COLOR)
    if interactive:
        plt.ion()
    else:
        plt.ioff()
    fig = plt.figure("Face finding demo")
    plt.subplot(1, 2, 1)
    plt.imshow(img[:,:,::-1])
    plt.title('Image')
    plt.xticks([])
    plt.yticks([])

    rois = find_faces(img)
    add_rois_to_image(img, rois)

    plt.subplot(1, 2, 2)
    plt.imshow(img[:,:,::-1])
    plt.title('Image with ROIs')
    plt.xticks([])
    plt.yticks([])
    plt.show()

if __name__ == "__main__":
    find_faces_and_display('derry-girls.jpg', False) 