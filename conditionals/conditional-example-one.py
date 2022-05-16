def conditionals_exec():
    a, b = 1, 3
    if a < b:
        print("a is less than b")
    elif a > b:
        print("a is greater than b")
    else:
        print("a is equal to b")
        
conditionals_exec() # a is less than b

def conditional_values():
    a, b = 1, 2
    statements = "a is less than b " if a < b else " a is not less than b."
    print(statements)
conditional_values() # a is less than b

