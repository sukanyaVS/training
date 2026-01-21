f = open('demofile.txt')
print(f.readline())

f1 = open('newfile.txt','w')
f1.writelines(["Hello\n", "Welcome\n", "Sukanya\n"])

print(f.tell())
print(f.seek(8))
# print(f.read())
print(f.tell())


