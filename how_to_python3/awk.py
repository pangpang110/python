# coding=utf-8
__author__ = '胖'


import re
m = re.match(r'^\d{3}\-\d{3,8}$','010-12345')
print(m)

m = re.match(r'(^\d{3})-(\d{3,8}$)', '010-12345678')

print(m.group())
print(m.group(1))
print(m.group(2))

s = re.match(r'^([\w|\d]+)\@(\w+)\.([a-z]+)$', 'someone@gmail.com')
print(s.group())
print(s.group(1))
print(s.group(2))
print(s.group(3))


