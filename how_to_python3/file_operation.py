# coding=utf-8
__author__ = '胖'

'''
try:
    file_op = open(r'E:\eclipse\practise\how_to_python3\txt_file', 'r')
    print(file_op.read())
except FileNotFoundError as e:
    print('FileNotFound', e)
else:
    print('ok')
finally:
    print('END')
'''

with open(r'E:\eclipse\practise\how_to_python3\dasheng.jpg', 'rb') as dasheng:
    print(dasheng.readline())


with open(r'E:\eclipse\practise\how_to_python3\txt_file', 'r', encoding='GBK',errors='ignore') as e:
    print(e.read())
    # print(e.readline())

with open(r'E:\eclipse\practise\how_to_python3\txt_file', 'w', encoding='GBK') as t:
    t.write('add something')

with open(r'E:\eclipse\practise\how_to_python3\txt_file', 'r', encoding='GBK',errors='ignore') as e:
    print(e.read())

import io


sio = io.StringIO()
sio.write('test string\n from strio\n good')
sio.close()
print(sio.readline())

while True:
    s = sio.readline()
    if s == '':
        break
    print(s.strip())

import json
json.dump()