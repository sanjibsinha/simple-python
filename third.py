import pandas as panda
import matplotlib.pyplot as plt

data_frame_of_numbers = panda.DataFrame({'name': ['John', 'Emily', 'Json'], 
                      'mark': [56, 89, 65]})

names = data_frame_of_numbers['name']

marks = data_frame_of_numbers['mark']

plt.plot(names, marks)
plt.show()
