import datetime as d
import calendar

class MyClass:
    name = "Sukanya"

obj1 = MyClass()
print(obj1.name)
del obj1 

class Students:
    def __init__(self,n,a):
        self.n = n
        self.a = a

s1 = Students('x',15)

print(s1.n)
print(s1.a)

print(d.date.today())
print(d.datetime.now().time())
print(calendar.month(2026,8))