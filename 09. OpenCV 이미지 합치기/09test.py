
import cv2

image_1 = cv2.imread('../images/image_1.jpg')
image_2 = cv2.imread('../images/image_2.png')

# cv2.add(): Saturation 연산을 수행합니다. 0보다 작으면 0, 255보다 크면 255로 표현
result = cv2.add(image_1, image_2)
cv2.imshow('image', result)
cv2.waitKey(3000)

# np.add(): Modulo 연산을 수행합니다. 256은 0, 257은 1로 표현
result = image_1 + image_2
cv2.imshow('image', result)
cv2.waitKey(3000)

