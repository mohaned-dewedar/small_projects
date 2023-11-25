import os
from PIL import Image

def resize_images(input_dir, output_dir, size=(224, 224)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for celeb_folder in os.listdir(input_dir):
        celeb_path = os.path.join(input_dir, celeb_folder)
        output_celeb_path = os.path.join(output_dir, celeb_folder)

        if not os.path.exists(output_celeb_path):
            os.makedirs(output_celeb_path)

        for image_name in os.listdir(celeb_path):
            if image_name.endswith('.jpg'):
                image_path = os.path.join(celeb_path, image_name)
                with Image.open(image_path) as img:
                    img = img.resize(size)
                    img.save(os.path.join(output_celeb_path, image_name))

# Usage
input_directory = 'Arab_Celebs_Data'
output_directory = 'resized_data'
resize_images(input_directory, output_directory)
