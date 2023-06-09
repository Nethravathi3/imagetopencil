# -*- coding: utf-8 -*-
"""imagetopencil.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lT--asFEEZEkx2YJQJBsfG_A9UvIO7wv
"""

import cv2
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow

img=cv2.imread("/content/image1.jpg")

cv2_imshow(img)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(img)
plt.axis(False)
plt.show()

plt.imshow(img[:,:,::-1])
plt.axis(False)
plt.show()

RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(RGB_img)
plt.axis(False)
plt.show()

grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

invert_img=cv2.bitwise_not(grey_img)
#invert_img=255-grey_img

invert_img=cv2.bitwise_not(grey_img)
#invert_img=255-grey_img

blur_img=cv2.GaussianBlur(invert_img, (111,111),0)

invblur_img=cv2.bitwise_not(blur_img)
#invblur_img=255-blur_img

sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)

cv2.imwrite("/content/SANT5203.JPG",sketch_img)

cv2_imshow(sketch_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.figure(figsize=(14,8))
plt.subplot(1,2,1)
plt.title('Original image', size=18)
plt.imshow(RGB_img)
plt.axis('off')
plt.subplot(1,2,2)
plt.title('Sketch', size=18)
rgb_sketch=cv2.cvtColor(sketch_img, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_sketch)
plt.axis('off')
plt.show()

