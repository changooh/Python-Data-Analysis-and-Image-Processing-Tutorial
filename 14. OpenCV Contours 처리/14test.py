import cv2
image = cv2.imread('../images/fixed_mask_0.png')
# image = cv2.imread('../images/fixed_mask_0_grey.png')
# cv2.imshow('Original Image', image)
# cv2.waitKey(3000)

# - 입력 이미지는 Gray Scale Threshold 전처리 과정이 필요합니다.
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(image_gray, 220, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('thresh_gray', thresh)
cv2.waitKey(3000)

# # Contours 찾기
# # 이미지에서 Contours 찾는 함수 # cv2.findContours(image, mode, method)
# contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]
#
# # - mode: Contours 찾는 방법
# #   RETR_EXTERNAL: 바깥쪽 Line만 찾기
# #   RETR_LIST: 모든 Line을 찾지만, Hierarchy 구성 X
# #   RETR_TREE: 모든 Line을 찾으며, 모든 Hierarchy 구성 O
# # - method: Contours 찾는 근사치 방법
# #   CHAIN_APPROX_NONE: 모든 Contour 포인트 저장
# #   CHAIN_APPROX_SIMPLE: Contour Line 그릴 수 있는 포인트만 저장
#
# # Contours 그리기
# # Contour 그리는 함수 # cv2.drawContours(image, contours, contour_index, color, thickness)
# image = cv2.drawContours(image, contours, -1, (0, 0, 255), 4)
# # - contour_index: 그리고자 하는 Contours Line (전체: -1)
# cv2.imshow('image', image)
# cv2.waitKey(3000)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

image = cv2.drawContours(image, contours, -1, (0, 255, 0), 4)
cv2.imshow('contours Image', image)
cv2.waitKey(1000)
#
#
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#
# image = cv2.drawContours(image, contours, -1, (0, 255, 0), 4)
# cv2.imshow('contours Image2 ', image)
# cv2.waitKey(1000)

