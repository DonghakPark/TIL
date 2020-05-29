import numpy as np
# import argparse
import cv2

# # ap = argparse.ArgumentParser()
# # ap.add_argument("-i", "--image", required = True,
# #                 help = "Path to the image")
# # args = vars(ap.parse_args(()))
#
# image = cv2.imread("./image1.jpg")
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Original", image)
#
# # lap = cv2.Laplacian(image,cv2.CV_64F)
# # lap = np.uint8(np.absolute(lap))
# # cv2.imshow("Laplacian", lap)
#
#
# sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
# sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)
#
# sobelX = np.uint8(np.absolute(sobelX))
# sobelY = np.uint8(np.absolute(sobelX))
#
# sobelCombined = cv2.bitwise_or(sobelX, sobelY)
#
# cv2.imshow("Sobel X", sobelX)
# cv2.imshow("Sobel Y", sobelY)
# cv2.imshow("Sobel Combined", sobelCombined)
# cv2.waitKey(0)

image = cv2.imread("./image1.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Blurred", image)

canny = cv2.Canny(image, 30, 150)
cv2.imshow("Canny", canny)
cv2.waitKey(0)