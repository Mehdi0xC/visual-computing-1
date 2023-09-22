import cv2
print(cv2.__version__)
import numpy as np

# Read the image
img = cv2.imread('tree.png')

# Display the image
cv2.imshow('image', img)

# Wait for the user to press any key
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

# Convert the image to grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# OR do it with numpy
# img = img[:, :, 0]
# img = np.mean(img, axis=2)

# Display the image in grayscale
cv2.imshow('image', img)
cv2.waitKey(0)

