import os
import functools
import mock
from functools import reduce

def deco1(x, y):
    def deco(fun):
        print(x + y)

        def temp(*args, **kwargs):
            print('befor calling')
            c = fun(*args, **kwargs)
            print('after calling')
            return c
        return temp
    return deco


@deco1(1, 4)
def test_deco(a, b):
    return a + b


print(test_deco(1, 32))


import time


def performance(f):
    @functools.wraps(f)
    def exc_time(x):
        t1 = time.time()
        m = f(x)
        t2 = time.time()
        t = t2 - t1
        print(t)
        return m
    return exc_time


@performance
def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1))

print(factorial(100))
print(factorial.__name__)


def performance(unit):
    def perf(f):
        @functools.wraps(f)
        def tmp(*args, **kwargs):
            t1 = time.time()
            m = f(*args, **kwargs)
            t2 = time.time()
            t = (t2 -t1)* 1000 if unit == 'ms' else (t2 - t1)
            print(t)
            return m
        return tmp
    return perf


@performance('ms')
def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1))

print(factorial(100))
print(factorial.__name__)



