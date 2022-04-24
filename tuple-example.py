firstTuple = (1, 2, 3)
print(id(firstTuple))
print(type(firstTuple))

'''
139762668549608
<class 'tuple'>
'''

secondTuple = (1, 2, 3)
print(id(secondTuple))
print(type(secondTuple))

'''
139762668550040
<class 'tuple'>
'''

mixedTuple = firstTuple + secondTuple

print(mixedTuple)
print(id(mixedTuple))
print(type(mixedTuple))

'''
(1, 2, 3, 1, 2, 3)
140682466415912
<class 'tuple'>
'''

# we can nest tuple
a_tuple = 1234, 5431, 'helicopter, you will fly!'
another_tuple = a_tuple, 145, 'Dhoko', 569
print(another_tuple)

'''
((1234, 5431, 'helicopter, you will fly!'), 145, 'Dhoko', 569)
'''

tuple_one = 1234, 5431, 'helicopter, you will fly!'
print(tuple_one)

'''
(1234, 5431, 'helicopter, you will fly!')
'''

# sequence unpacking
x, y, z = tuple_one
print(x)

'''
1234
'''