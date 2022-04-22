x = 3 /2
print(x)
print(id(x))
print(type(x))
print("*********")
'''
1.5
140597976235696
<class 'float'>
*********
'''
x = round(42 / 9)
print(x)
print(id(x))
print(type(x))
print("*********")
'''
5
140597976233680
<class 'int'>
*********
'''

x = 42
y = 9
z = x / y

print(z) # 4.666666666666667

# we want to round it up
x = 42 // 9
print(x)
print(id(x))
print(type(x))
print("*********")
'''
4
9789056
<class 'int'>
*********
'''
# how many digits we want to round to
x = round(42 / 9, 3)
print(x)
print(id(x))
print(type(x))
print("*********")
'''
4.667
140597976235696
<class 'float'>
*********
'''
x = 43 % 7
print(x)
print(id(x))
print(type(x))
print("*********")
'''
1
9788960
<class 'int'>
*********
'''
x = int(34.78)
print(x)
print(id(x))
print(type(x))
print("*********")
'''
34
9790016
<class 'int'>
*********
'''
x = float(23)
print(x)
print(id(x))
print(type(x))
print("*********")

'''
23.0
140597976235696
<class 'float'>
*********
'''