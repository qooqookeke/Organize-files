import os
import shutil

def classify_images(image_dir):
    """
    105101_20240722_152748.jpg 형태의 파일명을 가진 이미지 파일들을 
    105101 위치의 폴더를 생성하여 각각 분류하여 넣습니다.

    Args:
        image_dir (str): 이미지 파일들이 있는 디렉토리 경로
    """
    for filename in os.listdir(image_dir):
        if filename.endswith(".jpg"):
            # 파일명에서 폴더명 추출
            folder_name = filename.split("_")[0]

            # 폴더 경로 생성
            folder_path = os.path.join(image_dir, folder_name)

            # 폴더가 없으면 생성
            os.makedirs(folder_path, exist_ok=True)

            # 이미지 파일 이동
            source_path = os.path.join(image_dir, filename)
            destination_path = os.path.join(folder_path, filename)
            shutil.move(source_path, destination_path)

# 이미지 디렉토리 경로
image_dir = "D:/이미지 정리//"

# 이미지 분류 실행
classify_images(image_dir)