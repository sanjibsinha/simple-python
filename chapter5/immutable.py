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
    
'''
1
10914496
<class 'int'>
2
10914496
<class 'int'>
true
true
'''

'''
An object’s identity never changes 
once it has been created; you may think of 
it as the object’s address in memory.
'''

y = 2
print(y)
print(id(y)) # 10914528
print(type(y)) # <class 'int'>

if(x == y):
    print('true')
else:
    print('false')
    
if x is y:
    print('true')
else:
    print('false')
    
'''
false
false
'''


''' 
int, string and tuples are immutable
'''

'''
The is operator compares the identity of two objects; 
the id() function returns an integer representing its identity.
'''