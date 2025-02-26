import numpy as np
import matplotlib.pyplot as plt
import os


def save_image_patches(file_path, output_dir):
    images = np.load(file_path)
    print("Array Shape:", images.shape)
    print("Data Type:", images.dtype)
    print("Max value:", np.max(images))
    print("Min value:", np.min(images))


    # Ensure the pixel values are within the 0-255 range and are integers
    assert images.max() <= 255 and images.min() >= 0, "Pixel values are out of the expected range."

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    
    num_images_to_save = min(2523, images.shape[0])
    for i in range(num_images_to_save):
        # Convert the image data type to uint8 if it is not already
        image_uint8 = images[i].astype(np.uint8)

        plt.imsave(os.path.join(output_dir, f'image_{i+1}.png'), image_uint8)  
        print(f"Image {i+1} saved as image_{i+1}.png")

file_path = '/home/jenny/Downloads/pannuke_dataset/fold_2/Fold_2/images/fold2/images.npy'
output_dir = '/home/jenny/Downloads/pannuke_dataset/All_images_pannuke/fold2_images'
save_image_patches(file_path, output_dir)