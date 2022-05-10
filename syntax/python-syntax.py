# python syntax refers to rules and guidelines 
# it starts with indentation and ends with indentation

first_number = 5

if first_number > 4:
    second_number = first_number ** 2
    
print(f"We have no curly brace to mark the code block : {second_number}")
    
# We have no curly brace to mark the code block : 25

for i in range(5):
    total_of_i = i
    total_of_i += total_of_i
    
print(f"The chance of letter F ending with k is: {total_of_i}."
      + " Just maintaining the line.")
# The chance of letter F ending with k is: 8 Just maintaining the line.
