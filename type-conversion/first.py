an_integer = 236
a_float = 25.99
a_string = "456"

an_integer_converted_to_float = float(an_integer)
a_float_converted_to_integer = int(a_float)
an_integer_converted_to_string = str(an_integer)
a_float_converted_to_string = str(a_float)

a_string_converted_to_integer = int(a_string)
a_string_converted_to_float = float(a_string)

# let's check the type

print(type(an_integer))
print(type(a_float))
print(type(a_string))

print(type(an_integer_converted_to_float))
print(type(a_float_converted_to_integer))
print(type(an_integer_converted_to_string))
print(type(a_float_converted_to_string))
print(type(a_string_converted_to_integer))
print(type(a_string_converted_to_float))

'''
<class 'int'>
<class 'float'>
<class 'str'>
<class 'float'>
<class 'int'>
<class 'str'>
<class 'str'>
<class 'int'>
<class 'float'>
'''