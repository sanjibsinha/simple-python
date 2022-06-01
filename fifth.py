# truth table

is_true = True
is_false = False

if is_true:
    print('It\'s true.')
    # true or false is true
    if is_true or is_false: 
        print('True or false is true, This block will work.')
    # false or false is false
    elif is_true or is_true:
        print('N/A')
    else:
        print('N/A')
        
else:
    print('N/A')
    
'''
It's true.
True or false is true, This block will work.
'''