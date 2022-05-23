import pandas as panda

data_frame_of_numbers = panda.DataFrame({'name': ['John', 'Emily', 'Json'], 
                      'mark': [56, 89, 65]})

names = data_frame_of_numbers['name']
print(names)
marks = data_frame_of_numbers['mark']
print(marks)

''''
0     John
1    Emily
2     Json
Name: name, dtype: object
0    56
1    89
2    65
Name: mark, dtype: int64
'''