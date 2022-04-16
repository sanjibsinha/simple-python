firstTuple = (1, 2, 3)
print(id(firstTuple))
print(type(firstTuple))

secondTuple = (1, 2, 3)
print(id(secondTuple))
print(type(secondTuple))

mixedTuple = firstTuple + secondTuple

print(mixedTuple)
print(id(mixedTuple))
print(type(mixedTuple))



'''
139762668549608
<class 'tuple'>
139762668550040
<class 'tuple'>
(1, 2, 3, 1, 2, 3)
140682466415912
<class 'tuple'>
'''