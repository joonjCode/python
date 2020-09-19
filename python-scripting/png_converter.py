import sys
import os
from PIL import Image


# First and second argument from the syste,
image_folder = sys.argv[1]
output_folder = sys.argv[2]
# Check if new directory exists if not create 
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name =os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png','png')
    print('all done')



# loop through the folder 
# convert images to png
# Save them to the new folder 