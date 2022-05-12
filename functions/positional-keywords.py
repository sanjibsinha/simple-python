def greet_with(name, location):
    print(f"Hi {name}")
    print(f"Are you in {location}?")
    
greet_with("John", "Texas")

'''
Hi John
Are you in Texas?
'''
greet_with("Texas", "John")

'''
Hi Texas
Are you in John?
'''
def greet_with_name_and_location(name = "John", location = "Texas"):
    print(f"Hi {name}")
    print(f"Are you in {location}?")

greet_with_name_and_location()
'''
Hi John
Are you in Texas?
'''
greet_with_name_and_location("Json", "London")
'''
Hi Jason
Are you in London?
'''
def greet_with_noun_and_pronoun(noun = "Pam", pronoun = "you"):    
    print(f"Hi {noun}.")
    print(f"How are {pronoun}?")
    
greet_with_noun_and_pronoun("John", "you")

'''
Hi John.
How are you?
'''