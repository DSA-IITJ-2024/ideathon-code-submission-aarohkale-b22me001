# -*- coding: utf-8 -*-
"""DSA_Project_Data_Visualisation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14o_8JwPBrJo6wICiioYpz0VTU1epF7xZ

# **Uppload the image file, and the output file, also update the output file name if required**
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'topological map.jpg'
img = cv2.imread(image_path)
# plt.imshow(img)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h_channel = 2*hsv_img[:,:,0]
print(h_channel.shape)
image_array = h_channel[:512, :512]

def resize(img, new_width):
    height, width = img.shape[0:2]
    ratio = height/width
    new_height = int(ratio*new_width)
    resized_image = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
    return resized_image

image_array = resize(image_array, 128)
print(image_array.shape)
plt.imshow(image_array)
# np.savetxt('array.txt', image_array, fmt='%d')

height, width = image_array.shape[0:2]
print(image_array)

"""*   **Test Case 1**: From (80, 10) To (69, 96) ---> 10250 -> 8928
*   **Test Case 2**: From (70, 15) To (40, 65) ---> 8975 -> 5185
*   **Test Case 2**: From (70, 15) To (65, 40) ---> 8975 -> 8360


"""

def Image_Reconstruction(height, width, data):
  Saturation = np.full((height, width), 254).astype(np.uint8)
  HSV_value = np.full((height, width), 254).astype(np.uint8)
  data = np.divide(data,2)
  Image_New = np.stack((data,Saturation,HSV_value),axis=2)
  Image_New = Image_New.astype(np.uint8)
  Image_New = cv2.cvtColor(Image_New, cv2.COLOR_HSV2RGB)
  return Image_New

height = width = 128
image_new = Image_Reconstruction(height, width, image_array)

plt.imshow(image_new)

Path_Array = np.loadtxt("/content/output_file_8975_to_8360.txt", dtype=int)

image_path = image_new
for i in range(Path_Array.shape[0]):
  p = int(Path_Array[i]/128)
  q = int(Path_Array[i]%128)
  image_path[p, q, 0] = 0
  image_path[p, q, 1] = 0
  image_path[p, q, 2] = 0
plt.imshow(image_path)
