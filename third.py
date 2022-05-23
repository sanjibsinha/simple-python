import pandas as panda

data_frame_of_numbers = panda.DataFrame({'name': ['John', 'Emily', 'Json'], 
                      'mark': [56, 89, 65]})

names = data_frame_of_numbers['name']
print(names.str.upper())
marks = data_frame_of_numbers['mark']
print(marks.sum())

'''
0     JOHN
1    EMILY
2     JSON
Name: name, dtype: object
210
'''