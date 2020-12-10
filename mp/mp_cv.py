import cv2
import matplotlib.pyplot as plt

image = cv2.imread("D:\PyCharm-project\Practicla_opencv\cat.jpg")
plt.axis("off")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()