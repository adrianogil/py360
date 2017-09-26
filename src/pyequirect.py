import cv2
import numpy as np
from matplotlib import pyplot as plt
 
# img = cv2.imread("../dataset/set1/equi/Orion360_test_image_1280x640.jpg")
img = cv2.imread("../dataset/set1/equi/Orion360_test_image_2048x1024.jpg")

print("img size: " + str(img.shape))

sizex,sizey,_ = img.shape

last_c = 0

gzeroes_by_height = []

for y in xrange(0, sizey):
    # img_gradients = []
    gzeroes = 0
    for x in xrange(0, sizex):
        c = (img[x][y][0] + img[x][y][1] + img[x][y][2])/3.0
        if x > 0:
            g = c - last_c
            # img_gradients.append(g)
            if g == 0:
                gzeroes = gzeroes + 1
        last_c = c
    gzeroes_by_height.append(gzeroes)
    
plt.plot(range(0,len(gzeroes_by_height)), gzeroes_by_height)
plt.show()

