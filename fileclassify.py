import os
import shutil

def move_images(src_folder, front_folder, side_folder):
    if not os.path.exists(front_folder):
        os.makedirs(front_folder)
    if not os.path.exists(side_folder):
        os.makedirs(side_folder)
    
    for filename in os.listdir(src_folder):
        file_path = os.path.join(src_folder, filename)
        
        if os.path.isfile(file_path):
            if filename[-5] == '0':  
                shutil.move(file_path, os.path.join(front_folder, filename))
            elif filename[-5] == '1':  
                shutil.move(file_path, os.path.join(side_folder, filename))

src_folder = 'images'  # 원본
front_folder = 'front/'  # 정면
side_folder = 'side/'  # 측면

move_images(src_folder, front_folder, side_folder)
