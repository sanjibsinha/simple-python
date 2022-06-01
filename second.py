import numpy as np

print('Enter heights of your family members in integer. Remember 5 Feet is 152 cm, and '
      '6 feet is 182 cm. You can enter more, less or in-between this range. '
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
Enter heights of your family members in integer. 
Remember 5 Feet is 152 cm, and 6 feet is 182 cm. 
You can enter more, less or in-between this range. 
The program will find whether the family members' height close or diverse.
First height: 149
Second height: 152
Third height: 156
Fourth height: 157
Fifth height: 160
Your family members are of equal heights. No one is very tall or very short.
'''

'''
Enter heights of your family members in integer. Remember 5 Feet is 152 cm, 
and 6 feet is 182 cm. You can enter more, less or in-between this range. 
The program will find whether the family members' height close or diverse.
First height: 180
Second height: 146
Third height: 152
Fourth height: 189
Fifth height: 147
Your family members' height are diversed. Someone is very tall, or very short.
'''