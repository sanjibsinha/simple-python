strings = "I love you."
print(strings)
anotherStrings = "I love you but\nI don't know how much you love me."
print(anotherStrings)

'''
I love you.
I love you but
I don't know how much you love me.
'''

strings = "I love you."
print(strings)
anotherStrings = "I love you but\nI don't know how much you love me."
print(anotherStrings)
rawStrings = r"I love you but\nI don't know how much you love me."
print(rawStrings)

'''
I love you.
I love you but
I don't know how much you love me.
I love you but\nI don't know how much you love me.
'''

days = 8
lyrics = "%s days a week is not enough to love you." %days
print(lyrics)

'''
8 days a week is not enough to love you.
'''

days = 8
lyrics = "{} days a week is not enough to love you."
print(lyrics.format(days))

'''
8 days a week is not enough to love you.
'''

# multi lines output

newLines = """\
first line
second line
third line
more to come...
"""
print(newLines)

'''
first line
second line
third line
more to come...
'''