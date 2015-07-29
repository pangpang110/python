# coding=utf-8
__author__ = '胖'


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)

    __repr__ = __str__

    def __cmp__(self, s):
        if self.score == s.score:
            return cmp(self.name, s.name)
        return -cmp(self.score, s.score)


L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
print sorted(L)



class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score

    @property
    def grade(self):
        if self.score >= 80:
            return ('A')
        elif self.score >= 60:
            return ('B')
        else:
            return ('C')


s = Student('Bob', 59)
print s.grade

s.score = 60
print s.grade

s.score = 99
print s.grade