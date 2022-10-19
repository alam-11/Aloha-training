# regex means regular expression is special sequence of characters
# that uses a search pattern to find a string or set of strings

import re

sample_text = "this is sample . text foŕ tutorial"
match = re.search(r'text', sample_text)
print(match)  # it returns regex object
print("start index:", match.start())
print("End index:", match.end())

# \ – Backslash
# The backslash (\) makes sure that the character is not treated in a special way
# suppose we want to find the . character in the string be default it will be treated as
# metacharacters so we have excape it

dot_match = re.search(r'\.', sample_text)
print(dot_match)

# [] – Square Brackets
# Square Brackets ([]) represent a character class consisting of a set of characters

# [0, 3] is sample as [0123]
# [a-c] is same as [abc]

# [^0-3] means any number except 0, 1, 2, or 3
# [^a-c] means any character except a, b, or c

# ^ – Caret
# Caret (^) symbol matches the beginning of the string
# ^te will check if the strings with te such as tell,test,ten

# $ – Dollar
# Dollar($) symbol matches the end of the string
# a$ will check for the string that ends with a such as mala,niaz,rina

# . – Dot
# Dot(.) symbol matches only a single character
# a.b will check for the string that contains any character at the place of the dot such as acb, acbd, abbb, etc
# .. will check if the string contains at least 2 characters

# ? – Question Mark
# Question mark(?) checks if the string before the question mark in the regex occurs at least once or not at all
