x = (1, 2, 3, 4)
print(x)
print(type(x))

for i in x:
    print(i)

a = [1, 2, 3, 4]
print(a)
print(type(a))

# tuple
x = (1, 2, 3, 4) 

#list
a = [1, 2, 3, 4] 

#appending tuple x to list
a.append(x) 
print(a)

#inserting tuple x in the first position
a.insert(0, x) 
print(a)

#Now iterating the final list a
for i in a:
    print(i)
    
strings = "This is a string."
for WeWillIterateThroughIt in strings:
    print(WeWillIterateThroughIt)
    
strings = "string."
print(strings[1:3])

EnglishDictionaries = {'bare':'jejune', 'anger':'dudgeon', 'abuse':'vituperate', 'howl':'ululate'}
print(EnglishDictionaries)

# getting in a nmore human readable form
for keys in EnglishDictionaries:
    print(keys, "=", EnglishDictionaries[keys])
    
EnglishDictionaries = {'bare':'jejune', 'anger':'dudgeon', 'abuse':'vituperate', 'howl':'ululate'}
for keys in sorted(EnglishDictionaries.keys()):
    print(keys, "=", EnglishDictionaries[keys])
    
synonyms = dict(bare='jejune', anger='dudgeon', abuse= 'vituperate', howl= 'ululate')
for keys in sorted(synonyms.keys()):
    print(keys, "=", synonyms[keys])
    
'''
(1, 2, 3, 4)
<class 'tuple'>
1
2
3
4
[1, 2, 3, 4]
<class 'list'>
[1, 2, 3, 4, (1, 2, 3, 4)]
[(1, 2, 3, 4), 1, 2, 3, 4, (1, 2, 3, 4)]
(1, 2, 3, 4)
1
2
3
4
(1, 2, 3, 4)
T
h
i
s
 
i
s
 
a
 
s
t
r
i
n
g
.
tr
{'bare': 'jejune', 'anger': 'dudgeon', 'abuse': 'vituperate', 'howl': 'ululate'}
bare = jejune
anger = dudgeon
abuse = vituperate
howl = ululate
abuse = vituperate
anger = dudgeon
bare = jejune
howl = ululate
abuse = vituperate
anger = dudgeon
bare = jejune
howl = ululate


'''