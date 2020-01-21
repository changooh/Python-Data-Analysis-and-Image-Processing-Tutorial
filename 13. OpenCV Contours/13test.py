import cv2
import numpy as np

image = cv2.imread('fixed_mask_0.png')

# cv2.imshow('Original Image', image)#
# cv2.waitKey(3000)

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

contours, hierarchy = cv2.findContours(image_gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_KCOS)

print(len(contours))

print(contours[0].shape)

print(np.squeeze(contours[0])[:5])

c_image = cv2.drawContours(image, contours, -1, (0, 255, 0), 10)

cv2.imshow('contoured Image', c_image)

c_image2 = cv2.drawContours(image_gray, contours, -1, (0, 0, 225), 2)

cv2.imshow('contoured Image2', c_image2)

# cv2.waitKey(0)
#
# cv2.destroyAllWindows()


