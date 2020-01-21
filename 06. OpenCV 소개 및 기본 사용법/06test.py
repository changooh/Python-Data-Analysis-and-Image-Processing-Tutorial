import cv2

# import matplotlib.pyplot as plt

orgin_path = "../images/"
img_input = "cat.jpg"
img_path = orgin_path + img_input
img_basic = cv2.imread(img_path, cv2.IMREAD_COLOR)
cv2.imshow(img_input, img_basic)
cv2.waitKey(3000)

img_basic = cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY)
cv2.imshow('cat_grey', img_basic)
cv2.waitKey(3000)
cv2.imwrite('cat_grey.png', img_basic)

cv2.destroyAllWindows()

img_input = "cat_grey.png"
img_path = img_input
img_basic = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
cv2.imshow(img_input, img_basic)
cv2.waitKey(1000)




