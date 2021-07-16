import cv2
import numpy as np

image = np.zeros((200, 400), np.uint8)
image[:] = 200
image2 = np.zeros((300, 400), np.uint8)
image2.fill(255)
title1 = "aaaaa"
title2 = "bbbbb"

cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(title2)
cv2.moveWindow(title1, 150, 150)
cv2.moveWindow(title2, 400, 50)

cv2.imshow(title1, image)
cv2.imshow(title2, image2)

cv2.resizeWindow(title1, 400, 300)
cv2.resizeWindow(title2, 400, 300)

cv2.waitKey(0)
cv2.destroyAllWindows()


