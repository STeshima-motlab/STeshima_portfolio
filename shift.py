"""Add offset to img"""
import os
import cv2
import numpy as np

os.chdir(os.path.dirname(os.path.abspath(__file__)))

offset = 100
cam = 1

os.makedirs('../process/shift/removeBG', exist_ok=True)
os.makedirs('../process/shift/wall', exist_ok=True)

for case in range(1, 35):
    os.makedirs('../process/shift/removeBG/case%02d' %(case), exist_ok=True)
    for num in range(0, 100):
        img = cv2.imread('../process/removeBG/case%02d/img%d-%02d.bmp' %(case, cam, num), 0)
        new_img = np.zeros(img.shape)
        #new_img[:,offset:img.shape[1]] = img[:, :img.shape[1]-offset]
        new_img[:,:img.shape[1]-offset] = img[:, offset:img.shape[1]]
        cv2.imwrite('../process/shift/removeBG/case%02d/img%d-%02d.bmp' %(case, cam, num), new_img)
print('hi')
for case in range(1, 35):
    for num in range(0, 100):
        img = cv2.imread('../process/removeBG/case%02d/img%d-%02d.bmp' %(case, 0, num), 0)
        cv2.imwrite('../process/shift/removeBG/case%02d/img%d-%02d.bmp' %(case, 0, num), img)
print('hi')
for case in range(1, 35):
    img = cv2.imread('../process/wall/wall_%02d_%d.bmp' %(case, cam), 0)
    new_img = np.zeros(img.shape)
    #new_img[:,offset:img.shape[1]] = img[:, :img.shape[1]-offset]
    new_img[:,:img.shape[1]-offset] = img[:, offset:img.shape[1]]
    cv2.imwrite('../process/shift/wall/wall_%02d_%d.bmp' %(case, cam), new_img)
print('hi')
for case in range(1, 35):
    img = cv2.imread('../process/wall/wall_%02d_%d.bmp' %(case, 0), 0)
    cv2.imwrite('../process/shift/wall/wall_%02d_%d.bmp' %(case, 0), img)
