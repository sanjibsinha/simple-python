a = 1
b = a + 2
a_dict = {a : 'One'}
print(a_dict)

if a == 3:
    a_dict[a] = a_dict.pop(a)
    print(a_dict)
else :
    b = 3
    a_dict[b] = a_dict.pop(a)
    print(a_dict)
    
a = (2, 1)
a_dict = {a : 'One'}
print(a_dict)

b = 'Two'
a_dict[b] = a_dict.pop(a)
print(a_dict)

'''
{1: 'One'}
{3: 'One'}
{(2, 1): 'One'}
{'Two': 'One'}
'''

a_dict[b] = a_dict.pop(a[0])
print(a_dict)


'''
KeyError                                  
Traceback (most recent call last)
~/Documents/development/simple-python/simple-dictionary.py in <module>
      9 b = 'Two'
     10 
---> 11 a_dict[b] = a_dict.pop(a[0])
     12 print(a_dict)
     13 

KeyError: 2
'''




