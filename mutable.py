# example of mutability
m = [1, 2, 3]
print(id(m)) # 140036389429640
print(type(m)) # <class 'list'>
n = [1, 2, 3]
print(id(n)) # 140036336894536
print(type(n)) # <class 'list'>

if(m == n):
    print('true')
else:
    print('false')
    
if m is n:
    print('true')
else:
    print('false')
    
'''
true
false
'''

a = dict(x = 1, y = 2)
print(id(a)) # 139948631430704
print(type(a)) # <class 'dict'>
b = dict(x = 1, y = 2)
print(id(b)) # 139948631430488
print(type(b)) # <class 'dict'>

if(a == b):
    print('true')
else:
    print('false')
    
if a is b:
    print('true')
else:
    print('false')

'''
true
false
'''