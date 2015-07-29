# coding=utf-8
import functools
import operator

def cmp_ignore_case(s1, s2):
    if s1.upper() > s2.upper():
        return 1
    elif s1.upper() < s2.upper():
        return -1

# print(sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case))

# 其中cmp是sort参数
sorted_ignore_case1 = functools.partial(sorted, cmp=lambda s1, s2: cmp(s1.upper(), s2.upper()))
sorted_ignore_case2 = functools.partial(sorted, cmp=lambda x1, x2: 1 if x1.upper() > x2.upper() else -1)
sorted_ignore_case3 = functools.partial(sorted, cmp=cmp_ignore_case)
print(sorted_ignore_case1(['bob', 'about', 'Zoo', 'Credit']))
print(sorted_ignore_case2(['bob', 'about', 'Zoo', 'Credit']))
print(sorted_ignore_case3(['bob', 'about', 'Zoo', 'Credit']))
