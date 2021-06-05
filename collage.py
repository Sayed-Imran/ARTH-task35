import cv2
import numpy as np

img1 = cv2.imread("1lambo.jpg")
img2 = cv2.imread("2lambo.jpg")
img3 = cv2.imread("3lambo.jpg")
img4 = cv2.imread("4lambo.jpg")


imglam1 = np.hstack((img1, img2))
imglam2 = np.hstack((img3, img4))
imgf = np.vstack((imglam1, imglam2))
imgfinal = cv2.resize(imgf, (1000,800))
while True:
    # cv2.imshow("Lambo 1", img1)
    # cv2.imshow("Lambo 2", img2)
    # cv2.imshow("Lambo 3", img3)
    # cv2.imshow("Lambo 4", img4)
    # cv2.imshow("Lambo col1", imglam1)
    # cv2.imshow("Lambo col2", imglam2)
    cv2.imshow("Collage Image", imgfinal)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break