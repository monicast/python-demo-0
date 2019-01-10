#!/usr/bin/env python
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

Suggested next steps
- update add_rois_to_image to return a modified image, not modify the image passed
to it
- check that the ROIs actually fit into the image size
"""

import cv2
from matplotlib import pyplot as plt

def find_faces(img):
    """
    Uses opencv to find faces in the image
    """
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    face_rois = face_cascade.detectMultiScale(img_gray, 1.3, 3)
    return face_rois

def add_rois_to_image(image, rois, color = (255, 0, 0)):
    """
    Adds rectangles to image corresponding the to the numpy arrays x,y,width,height arrays.
    Note that this is altering the numpy image passed into it
    """
    for (roi_x, roi_y, roi_w, roi_h) in rois:
        cv2.rectangle(image, (roi_x, roi_y), (roi_x+roi_w, roi_y+roi_h), color, 2)

def find_faces_and_display(image_file, interactive=True):
    """
    Loads image file. Finds faces. Displays figure with two subplots. The left subplot is simply
    the image itself. The right image shows the image with ROIs indicating where faces were detected
    """
    img = cv2.imread(image_file, cv2.IMREAD_COLOR)
    if interactive:
        plt.ion()
    else:
        plt.ioff()
    plt.figure("Face finding demo")
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