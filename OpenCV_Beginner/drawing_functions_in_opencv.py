import cv2
import numpy as np

# img = cv2.imread("lena.jpg", 1)
img = np.zeros([512, 512, 3], np.uint8)  # alternatively, use numpy to draw a black image

img = cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 5)
img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 5)  # BGR - Blue

img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 5)  # BGR - Green
img = cv2.rectangle(img, (384, 128), (510, 256), (0, 0, 255), -1)  # red fill

img = cv2.circle(img, (128, 63), 63, (0, 255, 0), -1)  # BGR - Green

img = cv2.putText(img, "OpenCV", (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 10, cv2.LINE_AA)

cv2.imshow('lena', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
