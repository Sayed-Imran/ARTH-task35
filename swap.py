import cv2
import numpy as np

img1 = cv2.imread("lotus1.jpg")
img2 = cv2.imread("lotus2.jpg")
im3 = cv2.imread("lotus1.jpg")


imgc = img1[3:330,60:465]
imgd = img2[3:330,60:465]
im3[3:330,60:465] = imgd
img2[3:330,60:465] = imgc



while True:
    # cv2.imshow("Lotus 1", img1)
    # cv2.imshow("Lotus 2", img2)
    # cv2.imshow("Image part1", imgc)
    # cv2.imshow("Image part2", imgd)
    cv2.imshow("Image 1", im3)
    cv2.imshow("Image 2", img2)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break