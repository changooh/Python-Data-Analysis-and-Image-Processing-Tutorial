import cv2
import numpy as np

image = np.full((300, 300, 3), 0, np.uint8)
cv2.imshow("Image", image)
cv2.waitKey(1)

# cv2 point (width, height)

# 하나의 직선을 그리는 함수
image = cv2.line(image, (0, 0), (10, 300), (0, 255, 0), 3)
# cv2.line(image, start, end, color(b g r), thickness)
# - start: 시작 좌표 (2차원)
# - end: 종료 좌표 (2차원)
# - thickness: 선의 두께
# - coordinates (width, height)

cv2.imshow("Image", image)
cv2.waitKey(3000)


image = np.full((512, 512, 3), 255, np.uint8)
# 하나의 사각형을 그리는 함수
image = cv2.rectangle(image, (20, 20), (255, 255), (255, 0, 0), 3)
# cv2.rectangle(image, start, end, color(b g r), thickness)
# - start: 시작 좌표 (2차원)
# - end: 종료 좌표 (2차원)
# - thickness: 선의 두께 (채우기: -1)
# - coordinates (width, height)

cv2.imshow("Image", image)
cv2.waitKey(1)

# 하나의 원을 그리는 함수
image = np.full((512, 512, 3), 255, np.uint8)
image = cv2.circle(image, (255, 255), 100, (0, 0, 255), 3)
# cv2.circle(image, center, radian, color, thickness)
# - center: 원의 중심 (2차원)
# - radian: 반지름
# - thickness: 선의 두께 (채우기: -1)
# - coordinates (width, height)

cv2.imshow("Image", image)
cv2.waitKey(1)

# 하나의 다각형을 그리는 함수
image = np.full((512, 512, 3), 255, np.uint8)
points = np.array([[5, 5], [128, 258], [483, 444], [400, 150]])
image = cv2.polylines(image, [points], True, (0, 0, 0), 3)
# cv2.polylines(image, points, is_closed, color, thickness)
# - points: 꼭지점들
# - is_closed: 닫힌 도형 여부
# - thickness: 선의 두께 (채우기: -1)
# - coordinates (width, height)
cv2.imshow("Image", image)
cv2.waitKey(1)

# 하나의 텍스트를 그리는 함수
image = np.full((512, 512, 3), 255, np.uint8)
image = cv2.putText(image, 'Hello World', (0, 200), cv2.FONT_ITALIC, 1, (255, 0, 0))
# cv2.putText(image, text, position, font_type, font_scale, color)
# - position: 텍스트가 출력될 위치
# - font_type: 글씨체
# - font_scale: 글씨 크기 가중치
# - coordinates (width, height)
cv2.imshow("Image", image)
cv2.waitKey(3000)