students = {
    "John" : 80,
    "Json" : 68,
    "Emily" : 85,
    "Erikson" : 97,
    "Katy" : 99,
}

grades = {}

for name in students:
    grades = students[name]
    if grades > 90:
        students[name] = "Outstanding"
    elif grades > 80:
        students[name] = "Excellent"
    elif grades > 60:
        students[name] = "Fair"
    else:
        students[name] = "Work Hard"
        
print(students)

'''
{'John': 'Fair', 
'Json': 'Fair', 
'Emily': 'Excellent', 
'Erikson': 'Outstanding', 
'Katy': 'Outstanding'}
'''