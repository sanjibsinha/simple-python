import pandas as panda
import matplotlib.pyplot as plt

data_frame_of_numbers = panda.DataFrame({'axis': ['X', 'Y'], 
                      'value': [4, 23]})

axis = data_frame_of_numbers['axis']

value = data_frame_of_numbers['value']

plt.plot(axis, value)
plt.show()