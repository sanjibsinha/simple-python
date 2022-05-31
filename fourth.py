import numpy as np

list_of_numbers = [2, 4, 4, 4, 5, 5, 7, 9]

variance = np.var(list_of_numbers)
print(f'The Variance is {variance}') # 4.0
standard_deviation = np.std(list_of_numbers)
print(f'The Standard deviation is: {standard_deviation}') # 2.0