x = 1
print(type(x))
print(id(x))


x = 1
y = 1
print(type(x))
print(id(x))
print(type(y))

print(id(y))

if x == y:
    print("True")
else:
    print("False")
if x is y:
    print("True")
else:
    print("False")



a = dict(x=1, y=1)
print(type(a))
print(id(a))
b = dict(x=1, y=1)
print(id(b))
if a == b:
    print("True")
else:
    print("False")
if a is b:
    print("True")
else:
   print("False")

   
for i in range(0, 3):
    print(i, "=", id(i))

'''
<class 'int'>
9788960
<class 'int'>
9788960
<class 'int'>
9788960
True
True
<class 'dict'>
139924802534016
139924802540416
True
False
0 = 9788928
1 = 9788960
2 = 9788992
'''