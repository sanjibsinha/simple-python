import pandas as panda
import matplotlib.pyplot as plt

data_frame_one = panda.DataFrame({'axis': ['X', 'Y', 'X', 'Y', 'X', 'Y', 'X', 'Y'], 
                      'value': [2, 4, 4, 6, 6, 8, 8, 10]})

axis = data_frame_one['axis']

value = data_frame_one['value']

plt.plot(axis, value)
plt.show()


