import cv2
import numpy as np
import matplotlib.pyplot as plt

# load the image
image = cv2.imread(r"E:\Python_2025\Computer Vision\wall-e-wallpaper-preview.jpg")

# convert to RBG ( openCV reads images in BGR format)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# set contrast alpha and brightness beta values
alpha = 1.0 # contrast control 1.0 - 3.0
beta = 25 # brightness control -100 - 100

# apply the contrast and brightness
adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# display the original and adjusted images
plt.figure(figsize=(10,5))
plt.subplot(121)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

plt.subplot(122)
plt.imshow(adjusted)
plt.title(f'Brightness: {beta}, Contrast: {alpha}')
plt.axis('off')

plt.show()
# Keep the windows open until a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
