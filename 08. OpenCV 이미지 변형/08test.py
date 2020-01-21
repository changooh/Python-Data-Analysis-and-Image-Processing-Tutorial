import cv2
import time
import numpy as np

# load image
image = cv2.imread('../images/cat.jpg')

# time stamping
start_time = time.time()

# image BGR handing
image[0:100, 0:100] = [0, 0, 0]

# time stamping
print("--- %s seconds ---" % (time.time() - start_time))

# display image
cv2.imshow('Image', image)
cv2.waitKey(3000)



#  expand size x2
expand = cv2.resize(image, None, fx=3.0, fy=3.0, interpolation=cv2.INTER_CUBIC)
# - dsize: Manual Size
# - fx: 가로 비율
# - fy: 세로 비율
# - interpolation: 보간법
# INTER_CUBIC: 사이즈를 크게 할 때 주로 사용합니다.
# INTER_AREA: 사이즈를 작게 할 때 주로 사용합니다.
# interpolation 보간법은 사이즈가 변할 때 픽셀 사이의 값을 조절하는 방법을 의미합니다.

# image show
cv2.imshow('Image', expand)
cv2.waitKey(3000)

# shrink size x 0.8
shrink = cv2.resize(image, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_AREA)
cv2.imshow('Image', shrink)
cv2.waitKey(3000)

# image position handling
# - 이미지의 모든 좌표 (a, b)는 다음의 좌표로 이동됩니다.

# 행과 열 정보만 저장합니다.
height, width = image.shape[:2]  #(380, 441, 3)
M = np.float32([[1, 0, 50], [0, 1, 10]]) # (a + tx , b + ty)
dst = cv2.warpAffine(image, M, (width, height))
cv2.imshow('Image', dst)
cv2.waitKey(3000)

# image rotation
# 행과 열 정보만 저장합니다.
height, width = image.shape[:2] #height = 380, width = 441
M = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 0.5)
# cv2.getRotationMatrix2D(center, angle, scale) 이미지 회전을 위한 변환 행렬을 생성합니다.
# - center: 회전 중심
# - angle: 회전 각도
# - scale: Scale Factor
dst = cv2.warpAffine(image, M, (width, height))
cv2.imshow('Image', dst)
cv2.waitKey(3000)

M2 = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 1)
# cv2.getRotationMatrix2D(center, angle, scale) 이미지 회전을 위한 변환 행렬을 생성합니다.
# - center: 회전 중심
# - angle: 회전 각도
# - scale: Scale Factor
dst = cv2.warpAffine(image, M2, (width, height))
cv2.imshow('Image', dst)
cv2.waitKey(3000)



