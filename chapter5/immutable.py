x = 1
print(x)
print(id(x))
print(type(x))
y = 1
print(y)
print(id(y))
print(type(y))

if(x == y):
    print('true')
else:
    print('false')
    
if x is y:
    print('true')
else:
    print('false')


''' int, string and tuples are immutable

1
10914496
<class 'int'>
2
10914496
<class 'int'>
true
true
'''