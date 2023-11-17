import sys
import os
from PIL import Image

#grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

print(image_folder, output_folder)


#check if new/ exists, if not create it
if not os.path.exists(output_folder):
    os.mkdir(output_folder)



#loop through pokedex and convert images to png
for i in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{i}')
    clean_name = os.path.splitext(i)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png'  )
print(clean_name)



#save to new folder