english_dictionaries = {
    "Good" : "A rare species which still exist.",
    "Bad" : "Most common that we see around us.",
    "Ugly" : "Not uncommon, present in every specimen.",
}

# print(english_dictionaries)
'''
{'Good': 'A rare species which still exist.', 
'Bad': 'Most common that we see around us.', 
'Ugly': 'Not uncommon, present in every specimen.'}
'''

# adding new value
english_dictionaries["Cinema"] = "An epic Western Movie."
# print(english_dictionaries)

'''
{'Good': 'A rare species which still exist.', 
'Bad': 'Most common that we see around us.', 
'Ugly': 'Not uncommon, present in every specimen.', 
'Cinema': 'An epic Western Movie.'}
'''

# ediitng dictionary
english_dictionaries["Good"] = "Let's want to be good."
english_dictionaries["Bad"] = "Let's not do anything bad."
english_dictionaries["Ugly"] = "Let's know our ugly side and rectify."
english_dictionaries["Cinema"] = "I've seen this movie."
# print(english_dictionaries)

for key in english_dictionaries:
    print(key)
    print(english_dictionaries[key])
    
'''
Good
Let's want to be good.
Bad
Let's not do anything bad.
Ugly
Let's know our ugly side and rectify.
Cinema
I've seen this movie.
'''

'''
{'Good': "Let's want to be good.", 
'Bad': "Let's not do anything bad.", 
'Ugly': "Let's know our ugly side and rectify.", 
'Cinema': "I've seen this movie."}
'''

# wee can delete any dictionary by declaring it empty
#english_dictionaries = {}
#print(english_dictionaries)
# {}
