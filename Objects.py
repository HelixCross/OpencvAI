import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

img = cv2.imread("/Users/Hetze/OneDrive/Desktop/test.jpg")

bbox, label, conf = cv.detect_common_objects(img)

output_img = draw_bbox(img, bbox, label, conf)

plt.imshow(output_img)

plt.show()
