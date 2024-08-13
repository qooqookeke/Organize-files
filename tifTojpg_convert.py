import os
from PIL import Image

def convert_tif_to_jpg(src_folder, jpg_folder):
    # 출력 폴더가 존재하지 않으면 생성
    if not os.path.exists(jpg_folder):
        os.makedirs(jpg_folder)

    for filename in os.listdir(src_folder):
        if filename.lower().endswith('.tif') or filename.lower().endswith('.tiff'):
            tif_path = os.path.join(src_folder, filename)
            
            jpg_filename = os.path.splitext(filename)[0] + '.jpg'
            jpg_path = os.path.join(jpg_folder, jpg_filename)
            
            with Image.open(tif_path) as img:
                rgb_img = img.convert('RGB')
                rgb_img.save(jpg_path, 'JPEG')
                
            print(f"Converted {filename} to {jpg_filename}")
            print(jpg_path)

# 경로 설정
src_folder = './images/front'  # .tif 파일이 있는 폴더
jpg_folder = './images/front/jpg/'  # .jpg 파일을 저장할 폴더

# 변환 함수 호출
convert_tif_to_jpg(src_folder, jpg_folder)