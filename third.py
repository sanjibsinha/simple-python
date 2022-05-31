import math

list_of_numbers = [2, 4, 4, 4, 5, 5, 7, 9]

how_many_numbers_in_the_list = len(list_of_numbers)

mean = 0
sum_of_all_numbers_in_list = 0

for val in list_of_numbers:
    sum_of_all_numbers_in_list = sum_of_all_numbers_in_list + val
    
print(f'Sum of all numbers in the list {sum_of_all_numbers_in_list}') # 40
mean = sum_of_all_numbers_in_list / how_many_numbers_in_the_list
print(f'The Mean is: {mean}') # 5.0

sum_of_all_numbers_in_list_of_deviation = 0
variance = 0
for val in list_of_numbers:
    sum_of_all_numbers_in_list_of_deviation = ((val - 5) ** 2) + sum_of_all_numbers_in_list_of_deviation

""" print(sum_of_all_numbers_in_list_of_deviation) # 32 """
    
variance = sum_of_all_numbers_in_list_of_deviation / how_many_numbers_in_the_list
print(f'The Variance is {variance}') # 4.0

standard_deviation = math.sqrt(variance)

print(f'The Standard deviation is: {standard_deviation}')
    




