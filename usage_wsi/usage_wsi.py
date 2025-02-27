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
wsi_path_to_json_mask_thumb = '/media/jenny/PRIVATE_USB/Google_colab/'

# get the list of all wsis
wsi_list = glob.glob(wsi_path + '*')
print(f"wsi_list: {wsi_list}")

# get a random wsi from the list
rand_wsi = np.random.randint(0,len(wsi_list))
wsi_file = wsi_list[rand_wsi]
wsi_ext = '.svs'
print(f"wsi_file: {wsi_file}")
wsi_basename = os.path.basename(wsi_file)
wsi_basename = wsi_basename[:-(len(wsi_ext))]
print(f"wsi_basename: {wsi_basename}")

# read the thumbnail and mask from file
mask_path_wsi = wsi_path_to_json_mask_thumb + 'mask/' + wsi_basename + '.png'
thumb_path_wsi = wsi_path_to_json_mask_thumb + 'thumb/' + wsi_basename + '.png'

print(f"mask_path_wsi: {mask_path_wsi}")
print(f"thumb_path_wsi: {thumb_path_wsi}")
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

# load the json file (may take ~20 secs)

json_path_wsi = wsi_path_to_json_mask_thumb + 'json/' + wsi_basename + '.json'

bbox_list_wsi = []
centroid_list_wsi = []
contour_list_wsi = [] 
type_list_wsi = []

# add results to individual lists
with open(json_path_wsi) as json_file:
    data = json.load(json_file)
    mag_info = data['mag']
    nuc_info = data['nuc']
    for inst in nuc_info:
        inst_info = nuc_info[inst]
        inst_centroid = inst_info['centroid']
        centroid_list_wsi.append(inst_centroid)
        inst_contour = inst_info['contour']
        contour_list_wsi.append(inst_contour)
        inst_bbox = inst_info['bbox']
        bbox_list_wsi.append(inst_bbox)
        inst_type = inst_info['type']
        type_list_wsi.append(inst_type)

# generate a tile from the WSI

# define the region to select
# Coordinate (0,0) is the upper left corner
x_tile = 0
y_tile = 10000
w_tile = 10000
h_tile = 10000

# load the wsi object and read region
cache_path = '/media/jenny/PRIVATE_USB/Google_colab/cache_test'
wsi_obj = get_file_handler(wsi_file, wsi_ext)
print(f"wsi_obj: {wsi_obj}")
print(f"mag_info: {mag_info}")
wsi_obj.prepare_reading(read_mag=mag_info, cache_path=cache_path)
wsi_tile = wsi_obj.read_region((x_tile,y_tile), (w_tile,h_tile))

# only consider results that are within the tile

coords_xmin = x_tile
coords_xmax = x_tile + w_tile
coords_ymin = y_tile
coords_ymax = y_tile + h_tile

tile_info_dict = {}
count = 0
for idx, cnt in enumerate(contour_list_wsi):
    cnt_tmp = np.array(cnt)
    cnt_tmp = cnt_tmp[(cnt_tmp[:,0] >= coords_xmin) & (cnt_tmp[:,0] <= coords_xmax) & (cnt_tmp[:,1] >= coords_ymin) & (cnt_tmp[:,1] <= coords_ymax)] 
    label = str(type_list_wsi[idx])
    if cnt_tmp.shape[0] > 0:
        cnt_adj = np.round(cnt_tmp - np.array([x_tile,y_tile])).astype('int')
        tile_info_dict[idx] = {'contour': cnt_adj, 'type':label}
        count += 1


# plot the overlay

# the below dictionary is specific to PanNuke checkpoint - will need to modify depeending on categories used
type_info = {
    "0" : ["nolabe", [0  ,   0,   0]], 
    "1" : ["neopla", [255,   0,   0]], 
    "2" : ["inflam", [0  , 255,   0]], 
    "3" : ["connec", [0  ,   0, 255]], 
    "4" : ["necros", [255, 255,   0]], 
    "5" : ["no-neo", [255, 165,   0]] 
}

plt.figure(figsize=(18,15))
overlaid_output = visualize_instances_dict(wsi_tile, tile_info_dict, type_colour=type_info)
plt.imshow(overlaid_output)
plt.axis('off')
plt.title('Segmentation Overlay')
plt.show()