import cv2
import numpy as np

path = "raw_datasets/HAM10000/HAM10000_images_part_1/ISIC_0024307.jpg"

image = cv2.imread(path)

cv2.imshow("Image Window",image)
cv2.waitKey(0)
cv2.destroyAllWindows()