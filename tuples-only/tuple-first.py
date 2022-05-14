tuple_example = 1, 'Hello World', 12.12, True, False, (45, 78)

print(tuple_example)

an_empty_tuple = ()
print(len(an_empty_tuple))

another_empty_tuple_after_comma = 'Hi',
print(len(another_empty_tuple_after_comma))

# functions that have multiple return values
lat_of_kolkata = 22.5726
lat_kol_tuple = lat_of_kolkata.as_integer_ratio()
print(lat_kol_tuple)
long_of_kolkata = 88.3639
long_kol_tuple = long_of_kolkata.as_integer_ratio()
print(long_kol_tuple)

print(lat_kol_tuple[0])
print(lat_kol_tuple[1])
print(long_kol_tuple[0])
print(long_kol_tuple[1])

'''
(1, 'Hello World', 12.12, True, False, (45, 78))
0
1
(3176811029649477, 140737488355328)
(1554514168410171, 17592186044416)
3176811029649477
140737488355328
1554514168410171
17592186044416
'''




