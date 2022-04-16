
a_dict = {'Name' : 'Json'}
print(a_dict['Name'])

a_dict['Name'] = 'John'
print(a_dict['Name'])


another_dict = {('Name', 'Location') : ('John', 'Back East')}
print(another_dict[('Name', 'Location')])

another_dict[('Name', 'Location')] = ('Json', 'Unknown')
print(another_dict[('Name', 'Location')])

'''
Json
John
('John', 'Back East')
('Json', 'Unknown')
'''

