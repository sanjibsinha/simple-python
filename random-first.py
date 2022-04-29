import random
from quote import quote

random_float = random.random()
print(random_float)
# 0.9679994499898359

random_number = random.randint(1, 10)
print(random_number)
# 8

random_quote = quote('friend',limit = 1)
print(random_quote)

'''
[{'author': 'Albert Camus', 'book': '', 'quote': 'Don’t walk in front of me… 
I may not followDon’t 
walk behind me… I may not leadWalk beside me… just be my friend'}]
'''

for i in range(len(random_quote)):
    print(random_quote[i]['author'])
    
# Albert Camus

for i in range(len(random_quote)):
    print(random_quote[i]['quote'])
    
'''
Don’t walk in front of me… I may not follow
Don’t walk behind me… I may not lead
Walk beside me… just be my friend
'''
    
