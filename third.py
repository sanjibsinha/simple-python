# truth table

is_true = True
is_false = False

if is_true:
    print('It\'s true.')
    is_true = is_false
    # false and false is false
    if is_true and is_true: 
        print('It\'s false. So it won\'t work.')
    # false or false is false
    elif is_true or is_true:
        print('It\'s also false. So it won\'t work.')
    else:
        print('True is false, so it\'s false now. And it works')
        
else:
    print('It\'s false. It will not come out as output. ')
    
