# truth table

is_true = True
is_false = False

if is_true:
    print('It\'s true.')
    # true and false is false
    if is_true and is_false: 
        print('True and false is false, This block will not work. N/A')
    # true or false is true
    elif is_true or is_false:
        print('True or false is true, This block will work.')
    else:
        print('N/A')
        
else:
    print('N/A')
    
'''
It's true.
True or false is true, This block will work.
'''