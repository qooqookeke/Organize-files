from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

# 루트 디렉토리 설정
ROOT_DIR = 'D:/project'
ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png'}

def get_directory_structure(root_dir):
    """
    주어진 루트 디렉토리에서 디렉토리 트리와 각 폴더 내의 이미지 정보를 가져옵니다.
    """
    dir_structure = []
    for root, dirs, files in os.walk(root_dir):
        # 디렉토리 깊이 계산
        depth = root.replace(root_dir, "").count(os.sep)
        folder_name = os.path.basename(root) or os.path.basename(root_dir)

        # 이미지 파일 필터링
        image_files = [
            f for f in files
            if os.path.splitext(f)[1].lower() in ALLOWED_EXTENSIONS
        ]
        images_to_show = image_files[:4]

        # 이미지 경로를 root에서 상대 경로로 저장
        web_paths = [os.path.relpath(os.path.join(root, img), start=root_dir) for img in images_to_show]

        # 디렉토리 구조에 정보 추가
        dir_structure.append({
            'depth': depth,
            'folder_name': folder_name,
            'image_count': len(image_files),
            'image_paths': web_paths
        })

    return dir_structure

@app.route('/')
def index():
    dir_structure = get_directory_structure(ROOT_DIR)
    return render_template('index.html', dir_structure=dir_structure)

@app.route('/image/<path:filename>')
def serve_image(filename):
    return send_file(os.path.join(ROOT_DIR, filename), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)

    
    
# pip install flask
# http://127.0.0.1:5000/ 접속