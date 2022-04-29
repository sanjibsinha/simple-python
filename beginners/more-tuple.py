a_list = [1, 3, 'A', 90]

print(a_list)
a_list[2] = 'B'
print(a_list)

a_tuple = (1, 3, 'A', 90)
print(a_tuple)
a_tuple[2] = 'B' # this is the error causing line
print(a_tuple)

'''
[1, 3, 'A', 90]
[1, 3, 'B', 90]
(1, 3, 'A', 90)

TypeError                                 
Traceback (most recent call last)
~/Documents/development/simple-python/more-tuple.py in <module>
      7 a_tuple = (1, 3, 'A', 90)
      8 print(a_tuple)
----> 9 a_tuple[2] = 'B'
     10 print(a_tuple)
     11 

TypeError: 'tuple' object does not support item assignment
'''

