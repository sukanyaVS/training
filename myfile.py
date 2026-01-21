import keyword
print("The list of keywords are : ")
print(keyword.kwlist)

x = 5j
y = "s"
z = 5.1
a = ["z","c"]
b = ("x","c")
c = {"x" : 'c', 'v' : 6}

print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print(type(c))

name = "Sukanya"
print(name[0:4])
print(name[2:])

print(id(name))

def dispName():
    global name
    name = 'Ridhi'
    lastName = 'V'
    print(name, end=' ')
    print(lastName)

dispName()
print(name)

s = 1+2+\
1+2+1+\
3

print(s)

"""name = input("Enter your name : ")
print("Welcome",name)"""

# age = int(input("age:"))
# print("age is",age)

age = [1,2,3,4]
print(age)
age.insert(2,10)
print(age)

print(type(type(int)))

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)



numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

s = "PyThOnProGRam"
result = ([ch for ch in s if ch.islower()] +
                 [ch for ch in s if ch.isupper()])
print(result)

word = "MaLbAcYdZ"
sorted_word = sorted(word, key=lambda lt: lt.isupper(), reverse=False)
print(''.join(sorted_word))



she = ['gree','nee','suk','div','le']
new = []
new = [i for i in she if 'e' in i]
print("=====", new)

try:
    print(x)
except NameError:
    print("not defined")
except:
    print("error")        