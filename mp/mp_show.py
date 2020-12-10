import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image = mpimg.imread("D:\PyCharm-project\Practicla_opencv\cat.jpg")
plt.imshow(image)
plt.show()

plt.axis("off")
plt.imshow(image)
plt.show()