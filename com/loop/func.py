'''
Created on 201577

@author: 
'''
from audioop import avg
from __builtin__ import range

if __name__ == '__main__':
    pass

i = 0
L = []
while i < 100:
    i = i + 1
    L.append(i*i)
print L
print sum(L)

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

def square_of_sum(X):
    sum = 0
    for i in X:
        sum = sum + i*i
    return sum
    
print square_of_sum([2,3,4])

import math
def move(x,y,step,angle):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx,ny
    
d = move(100, 100, 60, math.pi/6)
print d


def sqrt12(a,b,c):
    a1 = 0
    a2 = 0
    return a1 ,a2
print sqrt12(2, 3, 6)

def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n - 1)
print fact(10)

def power(x,n=2):
    s= 1
    while n > 0:
        n = n -1
        s = s * x
    return s
print power(5,4)


def greet(name=''):
    if name == '':
        print 'Hello,world'
    else:
        print 'Hello,word,' + name
        
greet()

def fn(*text):
    print text
fn()
fn('a')

def average(*avg):
    if avg == ():
        return avg
    else:
        sum = 0
        for i in avg:
           sum = sum + i
        averagesum = sum/len(avg)
        return averagesum
print average()
print average(1,2,3)
print average(1,2,3,4,5,6,7)

L = range(1,101)
print L
print L[0:10]
print L[2::3]
print L[4:50:5]
print L[-10:]
print L[-46::5]

def upperfirst(s):
    s1 = s[:1].upper()
    s2 = s[2:]
    return s1 + s2
print upperfirst('fsdfsdfsdfs')

L = ['tian','ren','he','jia','xing','he']
for index , name in zip(range(1,len(L)+1),L):
    print index , '-', name
    
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum = 0
for i in d.values():
    sum = sum + i
    aver= sum / len(d.values())
print aver
print d.keys()
print d.items()
print d.iteritems()
for x in d.iteritems():
    print x

m = { 'Adam1': 95, 'Lisa2': 85, 'Bart3': 59, 'Paul4': 74 }
sum = 0
for key, value in m.items():
    print key ,':',value
    sum = sum + value
print 'average',':',sum/len(m.items())

tt =  [x * x for x in range(1,100,2) if x % 3 == 0]
print tt


def theupper(L):
    L = [x.upper() for x in L if isinstance(x, str)]
    return L
print theupper(['Hello', 'world', 101])
 
L = [x*100 + y*10 + n for x in range(1,9) for y in range(1,9) for n in range(1,9) if x == n ]
print L
