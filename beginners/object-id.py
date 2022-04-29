from re import I


print(id(10))

a = 10 
print(id(a))
b = 10
print(id(b))

print(id(dict(a = 10)))
x = dict(a = 10)
print(id(x))
y = dict(a = 10)
print(id(y))


'''
9789248
9789248
9789248
139975002801280
139975002649088
139975002802240
'''

'''
Caching can work only with immutable objects, 
notice that integer, string, tuples are immutable. So Python 
implementation can use caching to save memory space and improve performance.
'''