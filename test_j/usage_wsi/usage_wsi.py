import sys
sys.path.append('../')

import numpy as np
import os
import glob
import matplotlib.pyplot as plt
import scipy.io as sio
import cv2
import json
import openslide

from misc.wsi_handler import get_file_handler
from misc.viz_utils import visualize_instances_dict

wsi_path = '/media/jenny/PRIVATE_USB/Converted_images/Pyramidal_HE_MM009_2_270125_20x_BF_01.tif'
wsi_json_path = '/media/jenny/PRIVATE_USB/Google_colab/json/Pyramidal_HE_MM009_2_270125_20x_BF_01.json'

# get the list of all wsis
wsi_list = glob.glob(wsi_path + '*')

# get a random wsi from the list
rand_wsi = np.random.randint(0,len(wsi_list))
wsi_file = wsi_list[rand_wsi]
wsi_ext = '.svs'

wsi_basename = os.path.basename(wsi_file)
wsi_basename = wsi_basename[:-(len(wsi_ext))]

# read the thumbnail and mask from file

mask_path_wsi = wsi_json_path + 'mask/' + wsi_basename + '.png'
thumb_path_wsi = wsi_json_path + 'thumb/' + wsi_basename + '.png'

thumb = cv2.cvtColor(cv2.imread(thumb_path_wsi), cv2.COLOR_BGR2RGB)
mask = cv2.cvtColor(cv2.imread(mask_path_wsi), cv2.COLOR_BGR2RGB)

# plot the low resolution thumbnail along with the tissue mask

plt.figure(figsize=(15,8))

plt.subplot(1,2,1)
plt.imshow(thumb)
plt.axis('off')
plt.title('Thumbnail', fontsize=25)

plt.subplot(1,2,2)
plt.imshow(mask)
plt.axis('off')
plt.title('Mask', fontsize=25)

plt.show()
