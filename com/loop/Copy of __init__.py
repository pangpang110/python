# -*- coding: utf-8 -*-
import os
from _ast import List
import new
from distutils.dep_util import newer
from Tkconstants import FIRST

A = 30
B = 10

print (A + B)
print '100 + 200 =' ,100+200

x1 = 1
d = 3
n = 100 
s = x1 +n*(n-1)*d/2

print "x1 + n * (n-1) * d / 2 = ", s

print ('Python was started in 1989 by "Guido".')
print ('Python \n', 'is free and easy to learn.')

print r'\(~_~)/ \(~_~)/'
print '''line 1
line 2
line 3''' 

print u'支持中文么'
print u'''什么\n和
什么嘛'''


a = 'python'
print 'hello,', a or 'world'

b = ''
print 'hello,', b or 'world'

L= ['tian','ren','he','jia','xing']
print L 
print L[1]
print L[-1]
L.append('added')
print L
L.insert(0, 'front add')
print L 
L.insert(-1, 'newer')
print L
L.pop()
print L 
L.pop(2)
print L
L[0] = "frist"
print L 
M=('t','d','t','h')
print M
T=('a','b','c',['1','2'])
print T 
C = T[3]
print C