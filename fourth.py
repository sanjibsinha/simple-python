# truth table

is_true = True
is_false = False

if is_true:
    print('It\'s true.')
    # true and true is true
    if is_true and is_true: 
        print('True and true is true, This block will work.')
    # false or false is false
    elif is_true or is_true:
        print('N/A')
    else:
        print('N/A')
        
else:
    print('N/A')
    
'''
It's true.
True and true is true, This block will work.
'''