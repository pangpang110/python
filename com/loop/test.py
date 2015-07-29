# -*- coding: utf-8 -*-
#
age = 25
if age >= 20:
    print 'your age ', age
    print 'adult'

print 'end'

'''
if score >= 60:
    print "you pass the exea"
else:
    print 'you are fail'
'''

score = 79
if score >= 90:
    print 'excellent'
elif score >= 80:
    print 'good'
elif score >= 60:
    print 'passed'
elif score <= 60:
    print 'fail'

L = ['tian', 'ren', 'he', 'jia', 'xing', 'he']

K = ('tian', 'ren', 'he', 'jia', 'xing')
'''print L'''
for name in L:
    print name
print 'this is a test.'
L = [75, 92, 59, 68]
sum = 0.0
for i in L:
    sum = sum + i
print sum / 4

N = 10
M = 0
while N >= M:
    print M
    M = M + 1

X = 0
Y = 1
while 1 > 0:
    X = X + 1
    Y = Y + 10
    print X
    print Y
    if Y > 500:
        break
print "finally Y =", Y

# for x in [range(100)]:
# L = [56,67,78]
v = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
     31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
     60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88,
     89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
for x in v:
    if x / 10 < x % 10:
        print x

x = 0
while x <= 100:
    x = x + 1

    if x < 10:
        continue
    elif x / 10 < x % 10:
        print x
print "done"

price = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    't': 1243567890
}

print price['a']  # print a value
print price.get('f','default')
print price.get('e')

for T in price:
    print T, ':', price.get(T)
price['e'] = 4
print price
print price.has_key('a')
print price.values()

price['a'] = 10
print price

for key in price:
    print key

print 'below is set'
L = ['tian', 'ren', 'he', 'jia', 'xing', 'he']
s = set(L)
print s
print len(s)

print 'he' in L
print 'hee' in L

Y = set(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
Y1 = '1'
Y2 = '101'
if Y1 in Y:
    print 'Y1 ok'
else:
    print 'Y1 error'
if Y2 in Y:
    print 'Y2 ok'
else:
    print 'Y2 error'
for xy in Y:
    print xy

s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print x[0], ':', x[1]

S = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
# 这段语法有问题
'''
for P in L:
    for T in S:
        if P == T:
            S.remove(T)
        else:
            S.add(T) 
print s
'''
for name in L:
    if name in S:
        S.remove(name)
    else:
        S.add(name)
print S

print 'Bart' in S

import eventlet