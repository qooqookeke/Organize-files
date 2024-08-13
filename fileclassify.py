import os
import shutil

def move_images(src_folder, front_folder, Rside_folder, Lside_folder):
    if not os.path.exists(front_folder):
        os.makedirs(front_folder)
    if not os.path.exists(Rside_folder):
        os.makedirs(Rside_folder)
    if not os.path.exists(Lside_folder):
        os.makedirs(Lside_folder)
    
    for filename in os.listdir(src_folder):
        file_path = os.path.join(src_folder, filename)
        
        if os.path.isfile(file_path):
            if filename[-1] == '0':  
                shutil.move(file_path, os.path.join(front_folder, filename))
                print(f"Moved to front_folder: {filename}")
            elif filename[-1] == '1':  
                shutil.move(file_path, os.path.join(Rside_folder, filename))
            elif filename[-1] == '2':
                shutil.move(file_path, os.path.join(Lside_folder, filename))

src_folder = 'images'  # 원본
front_folder = './images/front/'  # 정면
Rside_folder = './images/Rside/'  # 오른쪽 측면
Lside_folder = './images/Lside/'  # 왼쪽 측면

move_images(src_folder, front_folder, Rside_folder, Lside_folder)
