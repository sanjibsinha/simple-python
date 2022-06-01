import numpy as np

print('Enter heights of your family in integer. Remember 5 Feet is 152 cm, and '
      '6 feet is 182 cm. More or less or in-between. '
      'The program will find whether the family members\' height close or diverse.')

a1 = input('First height: ')
first_height = int(a1)
a2 = input('Second height: ')
second_height = int(a2)
a3 = input('Third height: ')
third_height = int(a3)
a4 = input('Fourth height: ')
fourth_height = int(a4)
a5 = input('Fifth height: ')
fifth_height = int(a5)

list_of_heights = [first_height, second_height, third_height, fourth_height, fifth_height]

standard_deviation = np.std(list_of_heights)

if standard_deviation <= 5:
    print('Your family members are of equal heights. No one is very tall'
          ' or very short.')
else:
    print('Your family members\' height are diversed. Someone is very tall,'
          ' or very short.')
    
'''
First height: 151
Second height: 149
Third height: 157
Fourth height: 153
Fifth height: 150
Your family members are of equal heights. No one is very tall or very short.
'''

'''
First height: 168
Second height: 147
Third height: 185
Fourth height: 176
Fifth height: 150
Your family members' height are diversed. Someone is very tall, or very short.
'''