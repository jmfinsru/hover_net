import pyvips

# Load the original TIFF file
image = pyvips.Image.tiffload('/media/jenny/PRIVATE_USB/MM_Andregangsstudiet_HE_20x_TIFF/HE_MM009_2_270125_vsi_Collection/HE_MM009_2_270125_20x_BF_01/HE_MM009_2_270125_20x_BF_01.tif')

# Save as a pyramidal tiled TIFF
image.tiffsave('/media/jenny/PRIVATE_USB/Converted_images/Pyramidal_HE_MM009_2_270125_20x_BF_01.tif',
               tile=True,
               pyramid=True,
               compression='jpeg',  # or 'lzw', 'deflate', etc.
               tile_width=256,
               tile_height=256)  
