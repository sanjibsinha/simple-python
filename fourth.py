import pandas as panda
import matplotlib.pyplot as plt

data_frame_of_numbers = panda.DataFrame({'name': ['John', 'Emily', 'Json', 'John', 'Emily', 'Json',], 
                      'mark': [56, 89, 65, 69, 97, 68]},)

names = data_frame_of_numbers['name']

aggregate_marks = data_frame_of_numbers.groupby('name').sum()

plt.plot(aggregate_marks, 'g--')
plt.show()


