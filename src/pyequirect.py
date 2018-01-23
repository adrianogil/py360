import cv2
import numpy as np
from matplotlib import pyplot as plt
 
# img = cv2.imread("../dataset/set1/equi/Orion360_test_image_1280x640.jpg")
# img = cv2.imread("../dataset/set1/equi/Orion360_test_image_2048x1024.jpg")
img = cv2.imread("../dataset/360/27548691920_dc2c279307_h.jpg")
# Convert RGB to Grayscale
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

print("img size: " + str(img.shape))

sizex,sizey = img.shape

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

# last_c = 0

# gzeroes_by_height = []

# for y in xrange(0, sizey):
#     # img_gradients = []
#     gzeroes = 0
#     for x in xrange(0, sizex):
#         c = (img[x][y][0] + img[x][y][1] + img[x][y][2])/3.0
#         if x > 0:
#             g = c - last_c
#             # img_gradients.append(g)
#             if g == 0:
#                 gzeroes = gzeroes + 1
#         last_c = c
#     gzeroes_by_height.append(gzeroes)
    
# plt.plot(range(0,len(gzeroes_by_height)), gzeroes_by_height)
# plt.show()

