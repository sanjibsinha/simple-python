import numpy as np

list_of_numbers = [2, 4, 4, 4, 5, 5, 7, 9, 10]

mean = np.mean(list_of_numbers)
# The Mean is 5.555555555555555
print(f'The Mean is {mean}')
variance = np.var(list_of_numbers)
print(f'The Variance is {variance}')
# The Variance is 6.024691358024692
standard_deviation = np.std(list_of_numbers)
print(f'The Standard deviation is: {standard_deviation}') 
# The Standard deviation is: 2.454524670486058