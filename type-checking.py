a_whole_number = 123

a_floating_point_number = 45.78

a_string_value = "I am anaconda"

print(type(a_whole_number))
print(type(a_floating_point_number))
print(type(a_string_value))

# we can convert to other type

converted_whole_number_to_float = float(a_whole_number)
print(type(converted_whole_number_to_float))

converted_string_to_float = float("23.67")
print(type(converted_string_to_float))

converted_float_to_int = int(23.67)
print(type(converted_float_to_int))

''''
<class 'int'>
<class 'float'>
<class 'str'>
<class 'float'>
<class 'float'>
<class 'int'>
'''