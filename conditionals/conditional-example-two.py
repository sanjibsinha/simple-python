def main():
    print("This is main function.")
    conditionals_exec()
    conditional_values()
    
def conditionals_exec():
    a, b = 4, 3
    if a < b:
        print("a is less than b")
    elif a > b:
        print("a is greater than b")
    else:
        print("a is equal to b")
    
def conditional_values():
    a, b = 1, 2
    statements = "a is less than b " if a < b else " a is not less than b."
    print(statements)
    
if __name__== "__main__":main()



'''
output:
------->

This is main function.
a is greater than b
a is less than b 
'''