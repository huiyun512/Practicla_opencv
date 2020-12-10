import cv2

image = cv2.imread("D:\\PyCharm-project\\Practicla_opencv\\images\\trex.png")
core = image[219, 90]
print(core)