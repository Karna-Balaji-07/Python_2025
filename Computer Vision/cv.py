import cv2
import numpy as np
def contrast_stretching(image):
    min_val = np.min(image)
    max_val = np.max(image)

    new_min_val = 0
    new_max_val= 255

    stretched_image = ((image-min_val) * (new_max_val - new_min_val) / (max_val - min_val)).astype(np.uint8)

    return stretched_image

image_path = r"E:\Python_2025\Computer Vision\wall-e-wallpaper-preview.jpg"
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
stretched = contrast_stretching(original_image)

cv2.imshow("Original Image", original_image)
cv2.imshow("Contrast Stretched Image", stretched)

# Keep the windows open until a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()