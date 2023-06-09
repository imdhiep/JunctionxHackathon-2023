# -*- coding: utf-8 -*-
"""data_label.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i8FQ9HxD3Ra21PyGSlJ5EDuz6Xo-KffN
"""

!command -v ffmpeg >/dev/null || (apt update && apt install -y ffmpeg)
!pip install -q mediapy

import itertools
import math
import warnings

import cv2
import mediapy as media
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from google.colab.patches import cv2_imshow

!apt-get update
!apt-get install ffmpeg libav-tools x264 x265 bc
!apt-get install mediainfo
!pip install ffmpeg
!apt-get install mp4v2-utils
!apt-get install jq
!apt-get install bc

!add-apt-repository ppa:savoury1/ffmpeg4
!apt-get update
!apt-get install ffmpeg
!ffmpeg -version
!apt-get install mp4v2-utils

import cv2
import os

from google.colab import drive
drive.mount('/content/drive')

true_folder = 'junction/Public_Test/groundtruth/scene3cam_02/'
video_link = "junction/Public_Test/videos/scene3cam_02/"

# Commented out IPython magic to ensure Python compatibility.
import os
import sys
if 'google.colab' in str(get_ipython()):
  print('Running on CoLab')
  root_dir='/content/drive/My Drive/' + video_link
  if os.path.isdir(root_dir):
#     %cd $root_dir
  else:
    print('Check your working_folder or if Google drive is mounted')
    sys.exit()
  sys.path.append(root_dir)  
  print('Colab code has been executed')
else:
  print('Not running on Colab')

exit()

import os
import cv2

# Read the videos from specified path
for filename in os.listdir('/content/drive/MyDrive/junction/Public_Test/videos/scene3cam_02/'):
    if filename.endswith('.mp4'):
        print(filename)
        folder = filename[:-4]
        print(folder)
        cam = cv2.VideoCapture(f"/content/drive/MyDrive/junction/Public_Test/videos/scene3cam_02/{filename}")

        try:
            # creating a folder named data
            if not os.path.exists(folder):
                os.makedirs(folder)

        # if not created then raise error
        except OSError:
            print(f'Error: Creating directory of {folder}')

        # frame
        currentframe = 0
        
        while True:
            ret, frame = cam.read()
            if not ret:
                break

            if ret:
                # if video is still left continue creating images
                name = f'{folder}/{folder}_' + str(currentframe) + '.jpg'
                print(f'Creating... {name}')
                
                # writing the extracted images
                cv2.imwrite(name, frame)

                # show how many frames are created
                currentframe += 1

            else:
                break

        # Release all space and windows once done
        cam.release()
        cv2.destroyAllWindows()

#đã có frames từ các ảnh, giờ phải gán nhãn

"""# Scence3cam_02_image1
data cho viec train
"""

from google.colab.patches import cv2_imshow

camera1 = open("/content/drive/MyDrive/junction/Public_Test/groundtruth/scene3cam_02/CAM_1.txt", 'r')

pointsList = []
for line in camera1:
  str = line.split()
  lst = str[1]
  lst = lst.replace(")", "")
  lst = lst.replace("(", "")
  lst=lst.split(",") 
  lst = lst[:len(lst)-1] 
  lst = [int(item) for item in lst]
  new_lst = [tuple([lst[i], lst[i+1]] )for i in range(0,len(lst)-2,2) ]
  pointsList.append(new_lst)

path = '/content/drive/MyDrive/junction/Public_Test/videos/scene3cam_02/CAM_1/CAM_1_'
list_of_image = []
for i in range(15):
  path1 = "/content/drive/MyDrive/junction/Public_Test/videos/scene3cam_02/CAM_1/CAM_1_{0}.jpg".format(i)
  image = cv2.imread(path1)
  isClosed = True 
  color = (255, 0, 0)
  thickness = 2
  pts = np.array(pointsList[i], np.int32)
  image = cv2.polylines(image, [pts], isClosed, color, thickness)
  list_of_image.append(image)
  cv2_imshow(image)

list_of_image

import os
import cv2
import numpy as np

if not os.path.exists('/content/drive/MyDrive/junction/training_data/my_images_folder_1'):
    os.makedirs('/content/drive/MyDrive/junction/training_data/my_images_folder_1')

for i, img in enumerate(list_of_image):
  
  filename = f'image_{i}.jpg'
  path = os.path.join('/content/drive/MyDrive/junction/training_data/my_images_folder_1', filename)
  cv2.imwrite(path, img)

"""# Scence3cam_02_image2
data cho training
"""

from google.colab.patches import cv2_imshow

camera1 = open("/content/drive/MyDrive/junction/Public_Test/groundtruth/scene3cam_02/CAM_3.txt", 'r')

pointsList = []
for line in camera1:
  str = line.split()
  lst = str[1]
  lst = lst.replace(")", "")
  lst = lst.replace("(", "")
  lst=lst.split(",") 
  lst = lst[:len(lst)-1] 
  lst = [int(item) for item in lst]
  new_lst = [tuple([lst[i], lst[i+1]] )for i in range(0,len(lst)-2,2) ]
  pointsList.append(new_lst)

path = '/content/drive/MyDrive/junction/Public_Test/videos/scene3cam_02/CAM_3/CAM_3_'
list_of_image = []
for i in range(15):
  path1 = "/content/drive/MyDrive/junction/Public_Test/videos/scene3cam_02/CAM_3/CAM_3_{0}.jpg".format(i)
  image = cv2.imread(path1)
  isClosed = True 
  color = (255, 0, 0)
  thickness = 2
  pts = np.array(pointsList[i], np.int32)
  image = cv2.polylines(image, [pts], isClosed, color, thickness)
  list_of_image.append(image)

import os
import cv2
import numpy as np

if not os.path.exists('/content/drive/MyDrive/junction/training_data/my_images_folder_3'):
    os.makedirs('/content/drive/MyDrive/junction/training_data/my_images_folder_3')

for i, img in enumerate(list_of_image):
  
  filename = f'image_{i}.jpg'
  path = os.path.join('/content/drive/MyDrive/junction/training_data/my_images_folder_3', filename)
  cv2.imwrite(path, img)

true_folder = 'junction/Public_Test/groundtruth/scene3cam_01/'
video_link = "junction/Public_Test/videos/scene3cam_01/"

# Commented out IPython magic to ensure Python compatibility.
import os
import sys
if 'google.colab' in str(get_ipython()):
  print('Running on CoLab')
  root_dir='/content/drive/My Drive/' + video_link
  if os.path.isdir(root_dir):
#     %cd $root_dir
  else:
    print('Check your working_folder or if Google drive is mounted')
    sys.exit()
  sys.path.append(root_dir)  
  print('Colab code has been executed')
else:
  print('Not running on Colab')

import os
import cv2

# Read the videos from specified path
for filename in os.listdir('/content/drive/MyDrive/junction/Public_Test/videos/scene3cam_01/'):
  if filename.endswith('.mp4'):
    print(filename)
    folder = filename[:-4]
    print(folder)
    cam = cv2.VideoCapture(f"/content/drive/MyDrive/junction/Public_Test/videos/scene3cam_01/{filename}")

    try:
        # creating a folder named data
      if not os.path.exists(folder):
        os.makedirs(folder)

    # if not created then raise error
    except OSError:
      print(f'Error: Creating directory of {folder}')

    # frame
    currentframe = 0
    
    while True:
      ret, frame = cam.read()
      if not ret:
        break

      if ret:
        # if video is still left continue creating images
        name = f'{folder}/{folder}_' + str(currentframe) + '.jpg'
        print(f'Creating... {name}')
        
        # writing the extracted images
        cv2.imwrite(name, frame)

        # show how many frames are created
        currentframe += 1

      else:
          break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()