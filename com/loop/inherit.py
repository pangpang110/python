# coding= utf-8
__author__ = '胖'


class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score


class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course


p = Person('Tim', 'Male')
s = Student('Bob', 'Male', 88)
t = Teacher('Alice', 'Female', 'English')

print getattr(t, 'name')
t.name = 'kugua'
print t.name
print setattr(t, 'name', 'tuguan')
print t.name

print t.name
print t.course

print isinstance(p, Person)
print isinstance(t, Teacher)

print type(123)
print type(t)
print dir(123)
print dir(t)

import json


class file_like(object):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        return r'["Tim", "Bob", "Alice"]'


s = file_like('someone')
print json.load(s)

'''
class Person(object):
    pass
class Student(Person):
    pass
class Teacher(Person):
    pass

class SkillMixin(object):
    pass
class BasketballMixin(SkillMixin):
    def skill(self):
        return 'basketball'
class FootballMixin(SkillMixin):
    def skill(self):
        return 'football'

class BStudent(Student, BasketballMixin):
    pass

class FTeacher(Teacher, FootballMixin):
    pass

s = BStudent()
print s.skill()

t = FTeacher()
print t.skill()
'''


class Person(object):
    def __init__(self, name, gender, **kw):
        self.name = name
        self.gender = gender
        for k, v in kw.iteritems():
            setattr(self, k, v)


p = Person('Bob', 'Male', age=18, course='Python')
print p.age
print p.course


def itername(**args):
    for k, v in args.iteritems():
        print k, v


itername(age='18',  mail='163.com')


class Person5(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __str__(self):
        return '(Person5: %s, %s)' %(self.name, self.gender)

p = Person5('Bob', 'male')
print p


class Student5(Person5):
    def __init__(self, name, gender, score):
        super(Student5, self).__init__(name, gender)
        self.score = score

    def __str__(self):
        return 'Student: %s, %s, %s ' %(self.name, self.gender, self.score)
    __repr__ = __str__

s = Student5('bob', 'male', 90)
print s

