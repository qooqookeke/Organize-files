import os

def rename_files(src_folder, prefix='', suffix='', replace_str='', new_str='', start_num=1, padding=0):
    files = os.listdir(src_folder)
    
    # 순차적으로 파일 이름 변경
    for count, filename in enumerate(files, start=start_num):
        old_path = os.path.join(src_folder, filename)
        
        # 파일 확장자 분리
        name, ext = os.path.splitext(filename)

        # 파일명에 패딩 숫자를 추가하여 새 이름 생성(변경될 이름 적용 부분)
        new_name = f"{prefix}{str(count).zfill(padding)}{suffix}{ext}"

        # 기존 문자열을 새로운 문자열로 치환(옵션)
        if replace_str and new_str:
            new_name = new_name.replace(replace_str, new_str)
        
        new_path = os.path.join(src_folder, new_name)
        
        os.rename(old_path, new_path)
        
        print(f"Renamed: {filename} -> {new_name}")

# 경로 설정 중요!
src_folder = './images/front/jpg/'


# 파일명 변경 함수 호출
rename_files(
    src_folder, 
    prefix='front_',  # 파일 이름 앞에 붙일 접두사
    suffix='_foot',  # 파일 이름 뒤에 붙일 접미사
    replace_str='',  # 교체할 문자열
    new_str='',  # 교체 후 문자열
    start_num=1,  # 시작 숫자
    padding=3  # 숫자에 대한 자리수 (예: 001, 002, ...)
)