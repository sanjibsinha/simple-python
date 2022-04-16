
a_dict = {'Name' : 'Json'}
print(a_dict['Name'])

a_dict['Name'] = 'John'
print(a_dict['Name'])

another_dict = {('Name', 'Location') : ('John', 'Back East')}
print(another_dict[('Name', 'Location')])

another_dict[('Name', 'Location')] = ('Json', 'Unknown')
print(another_dict[('Name', 'Location')])

a_dict['Job'] = a_dict.pop('Name')

print(a_dict)

another_dict[('Name', 'Location')] = another_dict.pop(('xyz', 'abcd'))

print(another_dict)


'''
Json
John
('John', 'Back East')
('Json', 'Unknown')
{'Job': 'John'}

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