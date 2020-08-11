import re

# Simple match example
# The example below checks if the pattern "spam" matches the string and prints "Match" if it does.
# Here pattern "pamspam" will not Match. That means the function is looking at the pattern from the start itself.
print("Simple Match Example.")
pattern = r"spam"
if re.match(pattern, "spamspamspam"):
    print("Match")
else:
    print("No match")
print()
'''
Output: 
Match
'''

# Regular Expressions
# Other functions to match patterns are re.search and re.findall
# re.search finds a match pattern anywhere in the string.
# re.findall returns a list of all substrings that match a pattern.
# Example
# In this example, the match function did not match the pattern, as it looks at the beginning of the string.
# The search function found a match in the string.
# Another function, re.finditer, does the same thing as re.findall, except it returns an iterator, rather than a list.
print("Functions available and their outputs.")
pattern = r"spam"
string = "eggspamsausagespam"
if re.match(pattern, string):
    print("Match")
else:
    print("No match")
if re.search(pattern, string):
    print("Match")
else:
    print("No match")
print(re.findall(pattern, string))
print()
'''
Output:
No match
Match
['spam', 'spam']
'''

# Regex search returns an object which has several methods.
# These methods include 
# group(), which returns the string matched.
# start(), and end(), which returns the start and ending position of the first match.
# span(), which returns the start and end positions of the first match as tuple.
print("Methods of Object returned by re.search() method.")
pattern = r"pam"
string = "eggspamsausage"
match = re.search(pattern, string)
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())
print()
'''
Output:
pam
4
7
(4, 7)
'''


# Search and Replace
# One of the most imp re methods that use regular expressions is sub
# re.sub(pattern, repl, string, count=0)
# this method replaces all occurences of the pattern in string with repl,
# substituting all occurances, unless count provided.
# This method returns the modified string.
print("Search and Replace.")
string = "My name is David. Hi David."
pattern = r"David"
newString = re.sub(pattern, "Amy", string)
print(newString)
print()
'''
Output:
My name is Amy. Hi Amy.
'''


# Simple Metacharacters
# Metacharacters are what makes regular expressions more powerful than normal string methods.
# The existence of metacharacters poses a problem if you want to create a 
# regular expressions that matches a literal metacharacter, such as "$"
# We can do this by escaping the metacharacters by putting a backslash(\) in front of them.
# This can mean putting multiple backshashes in a row to do all the escaping.
# To avoid this, we use raw string, which is normal string but "r" in front of it.
# We saw this usage above.

# The first metacharacter we will look at is "." (dot)
# This matches any character, other than a new line.
# Example
# This would mean "...." would match any four letter word.
# "." also matches number, alphabetical characters, or any other character.
# Unless and untill a new line is not there, "." will match it.
print("\".\" dot(.) Metacharacter.")
pattern = r"gr.y"
if re.match(pattern, "grey"):
    print("Match 1")
if re.match(pattern, "gray"):
    print("Match 2")
if re.match(pattern, "blue"):
    print("Match 3")
if re.match(pattern, "gr4y"):
    print("Match 4")
if re.match(pattern, "gr$y"):
    print("Match 5")
print()
'''
Output:
Match 1
Match 2
Match 4
Match 5
'''

# The next metacharacters are "^" and "$".
# These match the start and end of a string respectively.
# Example
# The pattern "^gr.y$" means that the string should start wih gr, then follow any character, except a newline, and end with y.
print("^ and $ Metacharacter.")
pattern = r"^gr.y$"
if re.match(pattern, "grey"):
    print("Match 1")
if re.match(pattern, "gray"):
    print("Match 2")
if re.match(pattern, "stringray"):
    print("Match 3")
print()
'''
Output:
Match 1
Match 2
'''


# Character Classes
# Provide a at to match only one of the specific set of characters.
# A character class is created by putting the characters it matches inside square brackets
# Example
# The patthern [aeiou] in the search function matches all strings that contain any one of the characters defined.
print("Character Classes: Definition.")
pattern = r"[aeiou]"
if re.search(pattern, "grey"):
    print("Match 1")
if re.search(pattern, "qwertyuiop"):
    print("Match 2")
if re.search(pattern, "rhythm myths"):
    print("Match 3")
print()
'''
Output:
Match 1
Match 2
'''


# Character classes can also match ranges of characters
# [a-z] matches any lowercase aplhabetical character.
# [G-P] matches any uppercase character from G to P.
# the class [0-9] matches any digit.
# Multiple ranges can be included in one class.
# the class [A-Za-z] matches a letter of any case.
# Example:
# The pattern in tihs example matches strings that contain two alphabetic uppercase letters followed by a digit.
print("Character Classes: Matching values with range.")
pattern = r"[A-Z][A-Z][0-9]"
if re.search(pattern, "LS8"):
    print("Match 1")
if re.search(pattern, "E3"):
    print("Match 2")
if re.search(pattern, "1ab"):
    print("Match 3")
print()
'''
Output:
Match 1
'''


# We can place ^ at the start of a character class to invert it.
# This causes it to match any character other than the ones included.
# Other metacharacters such as "$" and ".", have no meaning within character classes.
# The metacharacter ^ has no meaning unless it is the first character in a class.
# Example
# Pattern [^A-Z] excludes uppercase strings.
# Note, that the ^ should be inside the brackets to invert the character class.
print("Character classes: Invert")
pattern = r"[^A-Z]"
if re.search(pattern, "this is all quiet"):
    print("Match 1")
if re.search(pattern, "ABsdfdsfsf"):
    print("Match 2")
if re.search(pattern, "THISISALLSHOUTING"):
    print("Match 3")
print()
'''
Output:
Match 1
Match 2
'''


# More Metacharacters
# Sore more metacharacters are "*", "+", "?" "{" and "}"
# These specify number of repetitions.
# The metacharacters * means "zero or more repititions of the previous thing".
# "*" tries to match as many repetitions as possible.
# The "previous" thing can be a single character, a class, or a group of characters in parentheses.
# Example
# The example below matches strings that start with "egg" and follow with zero or more "spam"s.
print("More Metacharacters: * Metacharacter")
pattern = r"egg(spam)*"
if re.match(pattern, "egg"):
    print("Match 1")
if re.match(pattern, "eggspamspamegg"):
    print("Match 2")
if re.match(pattern, "spam"):
    print("Match 3")
print()
'''
Output:
Match 1
Match 2
'''

# The "+" is very similar to "*", except it means "One or more repetitions", as opposed to "zero ore more repetitions"
# Example
# To Summarize:
# "*" matches 0 or more occurences of the preceding expression.
# "+" matches 1 or more occurences of the preceding expression.
print("More Metacharacters: + Metacharacter")
pattern = r"g+"
if re.match(pattern, "g"):
    print("Match 1")
if re.match(pattern, "gggggggggggggggg"):
    print("Match 2")
if re.match(pattern, "abc"):
    print("Match 3")
print()
'''
Output:
Match 1
Match 2
'''

# The Metacharacter "?" means "zeoro or one repetition"
# Example
print("More Metacharacters: ? Metacharacter")
pattern = r"ice(-)?cream"
if re.match(pattern, "ice-cream"):
    print("Match 1")
if re.match(pattern, "icecream"):
    print("Match 2")
if re.match(pattern, "sausages"):
    print("Match 3")
if re.match(pattern, "ice--ice"):
    print("Match 4")
print()
'''
Output:
Match 1
Match 2
'''


# Curly Braces
# Curly Braces can be used to represent the number of repetitions between two numbers.
# The regex {x,y} means "between x and y repetitions of something"
# Hence {0,1} is the same thing as "?".
# If the first number is missing, it is taken to be zero
# If the second number is missing, it is taken to be infinity.
# "9{1,3}$" matches string that have 1 to 3 nines.
print("More Metacharacters: Curly Braces {} Metacharacter")
pattern = r"9{1,3}$"
if re.match(pattern, "9"):
    print("Match 1")
if re.match(pattern, "999"):
    print("Match 2")
if re.match(pattern, "9999"):
    print("Match 3")
print()
'''
Output:
Match 1
Match 2
'''

# Groups
# A group can be created by surrounding part of a regular expression with parentheses.
# This means that a group can be given as an argument to metacharacters such as "*" and "?".
# Example
# (spam) represents a group in the example pattern shown above.
print("Groups: Introduction")
pattern = r"egg(spam)*"
if re.match(pattern, "egg"):
    print("Match 1")
if re.match(pattern, "eggspamspamspamegg"):
    print("Match 2")
if re.match(pattern, "spam"):
    print("Match 3")
print()
'''
Output:
Match 1
Match 2
'''


# The content of groups in a match can be accessed using group function.
# A call of group(0) or group() returns the whole match.
# A call of group(n), where n is greater than 0, returns the nth group from the left.
# The method groups(), returns all groups up from 1.
# Example
# We can see that the groups can be nested.
print("Groups: All group methods of object returned by re.match() method.")
pattern = r"a(bc)(de)(f(g)h)i"
match = re.match(pattern, "abcdefghijklmnop")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())
print()
'''
Output:
abcdefghi
abcdefghi
bc
de
('bc', 'de', 'fgh', 'g')
'''


# There are several kind of special groups.
# Two useful ones are "named group" and "non-capturing groups"
# Named groups: have format (?P<name>...), where name is the name of the group and ... is the content.
# Named group behave exactly the same as normal groups, except they can be accessed by group(name).
# Non-capturing: have the format (?:...).
# They are not accessible by the group method, so they can be added to an existing regular expression
# without breaking the numbering.
# Example:
print("Named Groups example.")
pattern = r"(?P<first>abc)(?:def)(ghi)"
match = re.match(pattern, "abcdefghi")
if match:
    print(match.group("first"))
    print(match.groups())
print()
'''
Output:
abc
('abc', 'ghi')
'''


# Metacharacters
# Another important metacharacter is "|"
# This means "or". so red|blue matches either red or blue.
# Example:
print("Metacharacter: | ")
pattern = r"gr(a|e)y"
match = re.match(pattern, "gray")
if match:
    print("Match 1")

match = re.match(pattern, "grey")
if match:
    print("Match 2")

match = re.match(pattern, "griy")
if match:
    print("Match 3")
print()
'''
Output:
Match 1
Match 2
'''


# Special sequences
# There are various special sequences you can use in regular expressions.
# They are written as a backslash followed by another character.
# One useful special sequence is a backslash and a number between 1 and 99.
# E.g. \1 or \17.
# This matches the expression of the group of that number
# Example:
# In this example, note that:
# "(.+) \1" is not the same as "(.+)(.+)", because \1 refers to the first group's subexpressions,
# which is the matched expression itself, and not the regex pattern.
print("Special Sequences: Backslash(\\)")
pattern = r"(.+) \1"

match = re.match(pattern, "word word")
if match:
    print("Match 1")

match = re.match(pattern, "?! ?!")
if match:
    print("Match 2")

match = re.match(pattern, "abc cde")
if match:
    print("Match 3")
print()
'''
Output:
Match 1
Match 2
'''


# More useful special sequences are \d, \s, and \w.
# These matches the digits, whitespace, and word characters respectively.
# In ASCII mode they are equivalent to [0-9], [\t\n\r\f\v] and [a-zA-Z0-9_]
# In Unicode mode they match certain other characters, as well. For instance, \w matches letters with accents
# Versions of these special sequences with upper case letters- \D, \S, and \W :
# mean the opposite to the lower-case versions. For instance, \D matches anything that isn't a digit.
# Example:
# (\D+\d) matches one or more non-digits followed by a digit.
print("Special Sequences: \d and \D, \s and \S, and \w and \W")
pattern = r"(\D+\d)"
match = re.match(pattern, "Hi 999!")
if match:
    print("Match 1")

match = re.match(pattern, "1, 23, 456!")
if match:
    print("Match 2")

match = re.match(pattern, " ! $?")
if match:
    print("Match 3")
print()
'''
Output:
Match 1
'''


# Special Sequences
# Additional special sequences are \A, \Z and \b.
# The sequences \A and \Z match the beginning and end of a string, respectively.
# The sequence \b matches the empty string between \w and \W character, or
# \w characters and the beginning or end of the string.
# Informally, it represents the boundary between words.
# The sequence \B matches the empty string anywhere else.
# Example
# In the example below, "\bcat\b" basically matches the work "cat" surrounded by word boundaries.
print("Special Sequences: \A, \Z, \\b and \B")
pattern = r"\b(cat)\b"

match = re.search(pattern, "The cat sat!")
if match:
    print("Match 1")

match = re.search(pattern, "We s>cat<tered")
if match:
    print("Match 2")

match = re.search(pattern, "We scattered.")
if match:
    print("Match 3")
print()
'''
Output:
Match 1
Match 2
'''


# Email Extraction:
# A basic email address consists of a word and may include dots or dashes.
# This is followed by the @ sign and the domain name (the name, a dot, and the domain name suffix.)
# [\w\.-]: matches one ore more word character, dot or dash.
# The regex above says that the string should contain a word (with dots and dashes allowed)
# followed by the @ sign, then another similar word, then a dot and another word.
# Out regex contains 3 groups
# 1- first part of the email address
# 2- demain name without the suffix.
# 3- the domain suffix.
pattern = r"([\w\.-]+)@([\w\.-])(\.[\w\.]+)"


# What is look behind assertion.
# What is look after assertion.