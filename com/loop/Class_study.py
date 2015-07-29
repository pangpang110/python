# coding=utf-8
# __author__ = '胖'


class Person(object):
    def __init__(self, name, grade, gender, birthday, job):
        # except 'self" ,other parameter must be initial
        self.name = name
        self.grade = grade
        self.gender = gender
        self.birthday = birthday
        self.job = job


class Person2(object):
    def __init__(self, name, grade, gender, birthday, **args):
        self.name = name
        self.grade = grade
        self.gender = gender
        self.birthday = birthday
        for k, v in args.iteritems():
            setattr(self, k, v)
xiaoming = Person('xiaoming', 'five', 'male', '19810606', job='student')
xiaohong = Person2('xiaoming', 'five', 'male', '19810606', job='farmer')
print xiaoming.name
print xiaoming.job
print xiaohong.job


class Person3(object):
    # class attribute
    address = 'earth'

    def __init__(self, name, gender, score):
        self.name = name
        # this attribute can be,but not advice
        self._gender = gender
        # this attribute cant be access outside
        self.__score = score

    def returen_score(self):
        return  self.__score

people = Person3('animal', 'middle', 505)
print people.name, people._gender # ,people.__score
print people.returen_score()
animal = Person3('fish', 3, 3)
animal2 = Person3('bird', 5, 5)

# show access class attribute
print Person3.address
print animal.address
print animal2.address
print animal.name
print animal2.name

# show activity modify class attribute
Person3.address = 'china'
print Person3.address
print animal.address
print animal2.address

# show change instance attribute not effect class & other instance
animal.address = 'japan'
print animal.address
print animal2.address
print Person3.address

# show activity add instance attribute
animal2.firend = 5
print animal2.firend
animal2.firend = animal2.firend + 14
print animal2.firend

# show activity add class attribute
Person3.solar = 'sun'
print Person3.solar
print animal2.solar
animal2.solar = "mar"
print animal2.solar
print animal.solar


class Person4(object):
    count = 0

    def __init__(self,name):
        self.name = name
        Person4.count = Person4.count + 1

p1 = Person4('Bob')
print Person4.count
p2 = Person4('Alice')
print Person4.count
p3 = Person4('Tim')
print Person4.count


class Person(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_grade(self):
        if self.__score >= 90:
            return 'excellent'
        elif self.__score >= 60:
            return 'pass'
        elif self.__score < 60:
            return 'fail'


p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)

print p1.get_grade()
print p2.get_grade()
print p3.get_grade()
print p3.get_grade  # bound method Person.get_grade of <__main__.Person object at ADDRESS


class Person(object):
    count = 0

    @classmethod
    def how_many(cls):
        return cls.count

    def __init__(self, name):
        self.name = name
        Person.count = Person.count + 1

print Person.how_many()
p1 = Person('Bob')
print Person.how_many()


class Person(object):
    __count = 0
    count = 0

    def __init__(self, name):
        self.name = name
        Person.__count = Person.__count + 1
        Person.count = Person.count + 1

    @classmethod
    def how_many(cls):
        return cls.__count


print Person.how_many()
print Person.count
p1 = Person('Bob')
print Person.how_many()
print Person.count