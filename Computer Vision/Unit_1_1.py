# Histogram equilization

import cv2
import numpy as np
import matplotlib.pyplot as plt

# load the image in grayscale mode
image = cv2.imread(r"E:\Python_2025\Computer Vision\wall-e-wallpaper-preview.jpg",cv2.IMREAD_GRAYSCALE)

# Apply histogram equalization
equ = cv2.equalizeHist(image)

# compute histograms
hist_original = cv2.calcHist([image],[0],None,[256],[0,256])
hist_equ = cv2.calcHist([equ],[0],None,[256],[0,256])

# display the images
plt.figure(figsize=(10,5))
plt.subplot(221)
plt.imshow(image,cmap='gray')
plt.title('Original Image')
plt.axis('off')
#plt.show()

plt.subplot(222)
plt.imshow(equ,cmap='gray')
plt.title('Equalized Image')
plt.axis('off')
#plt.show()

plt.subplot(223)
plt.plot(hist_original)
plt.title('Original Histogram')
#plt.show()

plt.subplot(224)
plt.plot(hist_equ)
plt.title('Equalized Histogram')
#plt.show()

# Keep the windows open until a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()

# show all the images and graphs in one window
plt.show()


