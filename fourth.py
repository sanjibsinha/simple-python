import pandas as panda

data_frame_of_numbers = panda.DataFrame({'name': ['John', 'Emily', 'Json', 'John', 'Emily', 'Json',], 
                      'mark': [56, 89, 65, 69, 97, 68]})

aggregate_marks = data_frame_of_numbers.groupby('name').sum()

print(aggregate_marks)

'''
name    mark     
Emily   186
John    125
Json    133
'''
