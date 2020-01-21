import cv2
import time
import os

# orgin_path = "/home/doosan04/PycharmProjects/dataAnalytics/Python-Data-Analysis-and-Image-Processing-Tutorial/images/"
orgin_path = "../images/"
img_input = "cat.jpg"
img_path = orgin_path + img_input
image = cv2.imread(img_path, cv2.IMREAD_COLOR)

# 픽셀 수 및 이미지 크기 확인
print(image.shape)
print(image.size)

# 이미지 Numpy 객체의 특정 픽셀을 가리킵니다.
px = image[100, 100]
print("GBR %s" %str(px))

# B, G, R 순서로 출력됩니다.
# (단, Gray Scale인 경우에는 B, G, R로 구분되지 않습니다.)

# R 값만 출력하기
print("R value %s" %str(px[2]))

image2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
px = image2[100, 100]
print("Greyscale %s" %str(px))

# if cat.png file
filename = "cat.png"
bool = os.path.isfile(filename)
print(bool)
# already existed?
if bool == True:
    print("already existed")
else:
    img_basic = cv2.imread(img_path, cv2.IMREAD_COLOR)
    cv2.imwrite('cat.png', img_basic)


start_time = time.time()
#1 slow range statment
for i in range(0, 100):
    for j in range(0, 100):
        image[i, j] = [255, 255, 255]
print("--- %s seconds ---" % (time.time() - start_time))
cv2.imshow('Image', image)
cv2.waitKey(3000)

#2 faster range statment
image[0:100, 0:100] = [0, 0, 0]
print("--- %s seconds ---" % (time.time() - start_time))
cv2.imshow('Image', image)
cv2.waitKey(3000)














