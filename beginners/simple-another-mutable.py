aList = ['x', 123, '8', 45]

print(aList[1]) # output: 123

# we can change the value of a list
aList[1] = 145623

print(aList[1]) # output: 145623

# the same principle is true for dictionary

aDictionary = dict(x = 1, y = 10)

print(aDictionary['x']) # output: 1
print(aDictionary['y']) # output: 10

# let's swipe the value by changing the disctionary
aDictionary['x'] = 10
aDictionary['y'] = 1

print(aDictionary['x']) # output: 10
print(aDictionary['y']) # output: 1