import re

# Simple match example
# The example below checks if the pattern "spam" matches the string and prints "Match" if it does.
# Here pattern "pamspam" will not Match. That means the function is looking at the pattern from the start itself.
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