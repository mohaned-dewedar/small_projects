import shutil

def compress_directory(input_dir, output_zip_file):
    shutil.make_archive(output_zip_file, 'zip', input_dir)

# Usage
compress_directory('Arab_Celebs_Data_Resized', 'resized_data_zip')
