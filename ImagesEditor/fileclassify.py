import os
import shutil

def move_images(src_folder, Rap_folder, Rlat_folder, Lap_folder, Llat_folder):
    if not os.path.exists(Rap_folder):
        os.makedirs(Rap_folder)
    if not os.path.exists(Rlat_folder):
        os.makedirs(Rlat_folder)
    if not os.path.exists(Lap_folder):
        os.makedirs(Lap_folder)
    if not os.path.exists(Llat_folder):
        os.makedirs(Llat_folder)


    
    for filename in os.listdir(src_folder):
        file_path = os.path.join(src_folder, filename)
        
        if os.path.isfile(file_path):
            if filename[-5] == '0':  
                shutil.move(file_path, os.path.join(Rap_folder, filename))
            elif filename[-5] == '1':  
                shutil.move(file_path, os.path.join(Rlat_folder, filename))
            elif filename[-5] == '2':  
                shutil.move(file_path, os.path.join(Lap_folder, filename))
            elif filename[-5] == '3':  
                shutil.move(file_path, os.path.join(Llat_folder, filename))



src_folder = 'E:/femur_ap_lat_240804/'  # 원본
Rap_folder = 'E:/femur_ap_lat_240804/Rap/'  # 정면
Rlat_folder = 'E:/femur_ap_lat_240804/Rlat/'  # 측면
Lap_folder = 'E:/femur_ap_lat_240804/Lap/'  # 정면
Llat_folder = 'E:/femur_ap_lat_240804/Llat/'  # 측면



move_images(src_folder, Rap_folder, Rlat_folder, Lap_folder, Llat_folder)
