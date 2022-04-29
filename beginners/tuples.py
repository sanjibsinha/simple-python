
a_dict = {'Name' : 'Json'}
print(a_dict['Name'])

a_dict['Name'] = 'John'
print(a_dict['Name'])

aDictWithTupleKey = {('Name') : ('Pam')}
print(aDictWithTupleKey)

another_dict = {('Name', 'Location') : ('John', 'Back East')}
print(another_dict[('Name', 'Location')])

another_dict[('Name', 'Location')] = ('Json', 'Unknown')
print(another_dict[('Name', 'Location')])

a_dict['Job'] = a_dict.pop('Name') # a dictionary is mutable

print(a_dict) # this will not give errors

aDictWithTupleKey[('Name')] = aDictWithTupleKey.pop(('FirstName')) 
# key of the dictionary is Tuple which is immutable, it will give error

another_dict[('Name', 'Location')] = another_dict.pop(('xyz', 'abcd'))
# key of the dictionary is Tuple which is immutable, it will also give error



'''
Json
John
('John', 'Back East')
('Json', 'Unknown')
{'Job': 'John'}

KeyError                                  
Traceback (most recent call last)
~/Documents/development/simple-python/tuples.py in <module>
     19 print(a_dict) # this will not give errors
     20 
---> 21 aDictWithTupleKey[('Name')] = aDictWithTupleKey.pop(('FirstName'))
     22 # key of the dictionary is Tuple which is immutable, it will give error
     23 

KeyError: 'FirstName'

KeyError                                  
Traceback (most recent call last)
~/Documents/development/simple-python/tuples.py in <module>
     16 print(a_dict)
     17 
---> 18 another_dict[('Name', 'Location')] = another_dict.pop(('xyz', 'abcd'))
     19 
     20 print(another_dict)

KeyError: ('xyz', 'abcd')
'''