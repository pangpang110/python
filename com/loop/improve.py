'''
Created on 2015715

@author: 
'''
# coding utf8

import math
from _ast import Index
from cgi import log


def add(x, y, f):
    return f(x) + f(y)


print add(25, 9, math.sqrt)


def formatname(s):
    # for u in s:
    s1 = s[:1].upper()
    s2 = s[1:].lower()
    return s1 + s2


print map(formatname, ['adam', 'LISA', 'barT'])


def perd(x, y):
    return x * y


print reduce(perd, [2, 4, 5, 7, 12])


def sqrt_ini(s):
    x = int(math.sqrt(s))
    if s == x * x:
        return True


print filter(sqrt_ini, range(1, 101))


def cmp_ignore_case(s1, s2):
    if s1.upper > s2.upper:
        return 1
    elif s1.upper < s2.upper:
        return -1


print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)


def f():
    print 'call f()...'

    def g():
        print 'call g()...'

    return g


x = f()
print x
x()
print ''''''
print f()


def calc_prod(list):
    def mutil():
        m = 1
        for i in list:
            m = i * m
        return m

    return mutil


def calc_prod2(list):
    def mulit():
        def combin(x, y):
            return x * y

        return reduce(combin, list, 1)

    return mulit


f = calc_prod([1, 2, 3, 4, 5])
t = calc_prod2([1, 2, 3, 4, 5])
print f()
print t()


def count():
    fs = []

    def fun(j):
        def s():
            return j * j

        return s

    for i in range(1, 4):
        fs.append(fun(i))
    return fs


f1, f2, f3 = count()
print f1()
print f2()
print f3()


def is_not_empty(s):
    if s == None:
        return False
    elif len(s.strip()) > 0:
        return True


print filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])


def is_not_empty2(s):
    return s and len(s.strip()) > 0


print filter(is_not_empty2, ['test', None, '', 'str', '  ', 'END'])

# print filter(lambda s : False if s == None elif len(s.strip()) > 0 True, ['test', None, '', 'str', '  ', 'END'])
print filter(lambda s: s and len(s.strip()) > 0, ['test', None, '', 'str', '  ', 'END'])


def log(f):
    def fn(*args, **kw):
        print 'call ' + f.__name__ + '()...'
        return f(*args, **kw)

    return fn


'''factorial = log(factorial)
print factorial(10)'''


@log
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print factorial(10)

x = 4 + 3j


def xx():
    pass


xxx = []
print type(x)
print type(xx)
print type(xxx)

a = '1w3s2d45f6g'
print a[0]
b = a.upper()
print b

score = []
stu = 10
x = 0
if x <= stu:
    # score.append(input('pls input score:'))
    x = x + 1
print score

for x, y in [[1, 2], [3, 4]]:
    print x, y

for x in [[1, 2], [3, 4]]:
    for y in x:
        print x

x = 0
for x in range(0, 101):
    if x % 2 == 0 and x % 3 == 0:
        print x

b = zip([1, 2, 3, 4], [5, 6, 7, 8], 'aa', 'bb', 'cc')
print b

