import numpy as np

list_of_numbers = [202, 4, 4, 4, 5, 5, 72, 9, 1002]

mean = np.mean(list_of_numbers)
print(f'The Mean is {mean}')
# The Mean is 145.22222222222223

variance = np.var(list_of_numbers)
print(f'The Variance is {variance}')
# The Variance is 95596.17283950618

standard_deviation = np.std(list_of_numbers)
print(f'The Standard deviation is: {standard_deviation}') 
# The Standard deviation is: 309.1863076520469
