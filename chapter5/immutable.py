''' int, string and tuples are immutable

1
10914496
<class 'int'>
2
10914528
<class 'int'>
false

'''

x = 1
print(x)
print(id(x))
print(type(x))
y = 2
print(y)
print(id(y))
print(type(y))

if(x == y):
    print('true')
else:
    print('false')

# false

