type_your_name = input("What is your name?\n")

print(type_your_name)

length_of_a_name = len(type_your_name)

length_of_a_name_in_a_string = str(length_of_a_name)

print("Your name is " + length_of_a_name_in_a_string + " characters.")

'''
sanjib
Your name is 6 characters.
'''

'''
TypeError                                 
Traceback (most recent call last)
~/Documents/development/simple-python/variables.py in <module>
      5 length_of_a_name = len(type_your_name)
      6 
----> 7 print("Your name is " + length_of_a_name + " characters.")

TypeError: must be str, not int
'''
