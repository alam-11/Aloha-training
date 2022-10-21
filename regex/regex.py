# regex means regular expression is special sequence of characters
# that uses a search pattern to find a string or set of strings


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

# | – Or
# Or symbol works as the or operator meaning it checks whether the pattern before or after the or symbol is present in the string or not. For example –
# a|b will match any string that contains a or b such as acd, bcd, abcd, etc.

# ? – Question Mark
# Question mark(?) checks if the string before the question mark in the regex occurs at least once or not at all
# ab?c will bématched for the string ac,acb,dabc but will not be matched for abbc because there are two b similarly,
# it will not be mactched for abdc because b is not followed by c

# * – Star
# Star (*) symbol matches zero or more occurrences of the regex preceding the * symbol. For example –
# ab*c will be matched for the string ac, abc, abbbc, dabc, etc. but will not be matched for abdc because b is not followed by c.

# + – Plus
# Plus (+) symbol matches one or more occurrences of the regex preceding the + symbol. For example –
# ab+c will be matched for the string abc, abbc, dabc, but will not be matched for ac, abdc because there is no b in ac and b is not followed by c in abdc.


# {m, n} – Braces
# Braces match any repetitions preceding regex from m to n both inclusive. For example –
# a{2, 4} will be matched for the string aaab, baaaac, gaad, but will not be matched for strings like abc, bc because there is only one a or no a in both the cases.

# (<regex>) – Group
# Group symbol is used to group sub-patterns. For example –
# (a|b)cd will match for strings like acd, abcd, gacd, etc.

# \A	Matches if the string begins with the given character
# \Afor
#     for you
#     for the world

# \d	Matches any decimal digit, this is equivalent to the set class [0-9]
# \d	123
# gee1

# \D	Matches any non-digit character, this is equivalent to the set class [^0-9]
# \D	geeks
# geek1

# \w	Matches any alphanumeric character, this is equivalent to the class [a-zA-Z0-9_].
# \w	123
# geeKs4
#
# \W	Matches any non-alphanumeric character.
# \W	>$
# gee<>


# \Z	Matches if the string ends with the given regex
# ab\Z	abcdab
# abababab


import re

sample_text = "this is sample 1 . text foŕ tutorial and it is just a text this is some numbers 1234"
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

all_match = re.findall(r'\d+', sample_text)
print(all_match)

# regular expressions are compiled into pattern objects which have methods for various operations such as searching for pattern
# matches or performing string substitutions.

# re.compile() will create regular expression

pattern_for_alphabet = re.compile('[a-d]')
print(pattern_for_alphabet.findall(sample_text))

pattern_for_whitespaces = re.compile('[\s]')
print(len(pattern_for_whitespaces.findall(sample_text)))

# re.sub(pattern, repl, string, count=0, flags=0)

print(re.sub('ub', '000', 'Subject has Uber booked already', flags=re.IGNORECASE))

# if count has been given value 1, the maximum
# times replacement occurs is 1

# \s is for space
print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam',flags = re.IGNORECASE))

# subn() is similar to sub() in all ways, except in its way of providing output
# It returns a tuple with a count of the total of replacement and
# the new string rather than just the string

tuple_for_substring = re.subn('ub', '000', 'Subject has Uber booked already', flags=re.IGNORECASE)
print(tuple_for_substring)