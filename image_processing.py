import cv2
import sys
import numpy as np
import os
from skimage import io
from scipy import misc
import matplotlib.pyplot as plt
from skimage.transform import resize

def extract_faces(img):
    '''
    INPUT: Image file
    OUTPUT: Re-sized Image file
    '''

    img_size = 100
    faces_in_image_limit = 1
    
    face_cascade = cv2.CascadeClassifier('utils/haarcascade_frontalface_alt.xml')
    eye_cascade = cv2.CascadeClassifier('utils/haarcascade_frontalface_alt.xml')
    imageDataFin = []

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray) #it's not extracting the faces

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)

        if len(eyes) >= 1:
            im = resize(roi_color, (img_size, img_size))
            imageDataFin.append(im)

    if len(imageDataFin) > faces_in_image_limit:
        return []
    else:
        return imageDataFin
