import bson

# BSON 파일 읽기
with open('C:/Users/MYCOM/Desktop/dbdump/240108/walk101/users.bson', 'rb') as file:
    data = bson.decode_all(file.read())

# 출력
for document in data:
    print(document)