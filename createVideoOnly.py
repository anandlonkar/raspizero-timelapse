import os
from moviepy.editor import ImageSequenceClip, ImageClip
import datetime
from PIL import Image

# Define the local path where the images are stored
local_path = r'C:\Users\anand\OneDrive\Documents\Lexington Landon Home\Timelapse'

# Get today's date in the required format
today_date = datetime.datetime.now().strftime('%Y%m%d')

# List all files in the directory
all_files = os.listdir(local_path)

# Filter files based on the desired pattern (e.g., img_*.jpg)
image_files = [file for file in all_files if file.startswith('img_') and file.endswith('.jpg')]

# Sort the files to ensure they are in the correct order
image_files.sort()

# Create the full paths for the image files
image_files = [os.path.join(local_path, file) for file in image_files]

# Rotate each image by 90 degrees to the left and save to a temporary list
rotated_images = []
for image_file in image_files:
    with Image.open(image_file) as img:
        rotated_img = img.rotate(90, expand=True)
        rotated_img_path = os.path.join(local_path, f"rotated_{os.path.basename(image_file)}")
        rotated_img.save(rotated_img_path)
        rotated_images.append(rotated_img_path)

# Create a timelapse video using moviepy
try:
    clip = ImageSequenceClip(rotated_images, fps=3)
    output_file = os.path.join(local_path, f"{today_date}.mp4")
    clip.write_videofile(output_file, codec="libx264")
    print(f"Timelapse video created successfully: {output_file}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Clean up temporary rotated images
    for rotated_image in rotated_images:
        os.remove(rotated_image)