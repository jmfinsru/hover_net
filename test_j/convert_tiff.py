import pyvips

# Load the original TIFF file
image = pyvips.Image.tiffload('/media/jenny/PRIVATE_USB/HE_MM009_2_40x/HE_MM009_2_40x_TIFF/HE_009_2_190325.vsi.Collection/HE_009_2_190325_40x_BF_01/HE_009_2_190325_40x_BF_01.tif')

# Save as a pyramidal tiled TIFF
image.tiffsave('/media/jenny/PRIVATE_USB/Converted_images/Pyramidal_HE_009_2_190325_40x_BF_01.tif',
               tile=True,
               pyramid=True,
               compression='jpeg',  # or 'lzw', 'deflate', etc.
               tile_width=256,
               tile_height=256)  
