import pyexcel.cookbook as pc
import sys
import time

## euc-kr to utf-8 convert

# 파일 이름 입력 받기
filename = sys.argv[1]

# euc-kr로 인코딩된 파일을 실행
in_file = open(filename, encoding='euc-kr')

# utf-8로 저장할 파일을 실행
out_file = open('utf8_'+filename, 'w', encoding='utf-8')

content = in_file.read()
out_file.write(content)

in_file.close()
out_file.close()


# csv to xlsx
input_file = sys.argv[1]

result_file = sys.argv[2]

pc.merge_all_to_a_book([input_file], result_file)
print('Done')