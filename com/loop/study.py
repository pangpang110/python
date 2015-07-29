# learn how to using Python to programing

def f(x):
    def g():
        print 'this is :', x
        return x + x
    return g

print f(5) 
a = f(5)
print a() 
print f(5)()
print 'ddddddddd'

def f1(m,n):
    def g(n):
        return m + n
    return g

print f1(5,0)(15)

class Pagebook(object):
    auth = 'wangbo'
    def __init__(self,page):
        self.page = page + 1
        print page
        
    @classmethod
    def class_method(cls,msg):
        print msg
        return '['+msg+']'
        
    @staticmethod
    def class_static(msg):
        print  msg
        return '['+msg+']'
    def class_self(self,msg):
        print msg


class Book(Pagebook):
    def __init__(self,page):
        #super(Book,self).__init__(page)
        self.page = page + 10
        print page
    

'''book_a = Pagebook(10)
book_b = Pagebook(100)

print book_a.auth
print book_b.auth

book_a.auth = 'fire'
print book_a.auth
print book_b.auth'''

print Pagebook.class_method('pass')
print Pagebook.class_static('pass')
one = Pagebook(10)
one.class_method('test')
one.class_static('test2')

bookss = Book(11)