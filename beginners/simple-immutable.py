aString = "string"
print(aString[0]) # output: s
# now we want to change the value from s to a
aString[0] = "a"
print(aString)

'''
TypeError                                 
Traceback (most recent call last)
/home/sanjib/Documents/development/simple-python/simple-immutable.py in <cell line: 2>()
      1 aString = "string"
----> 2 aString[0] = "a"
      3 print(aString)

TypeError: 'str' object does not support item assignment
'''