### Regular Expressions ###
# Regular expressions are a powerful tool for string manipulation.
# They are a domain specific language for describing patterns in text.
# They are used in many programming languages, and are a standard feature of Python.
# Regular expressions are a huge topic, and this is just a brief introduction.

# Regular expressions are written in a special syntax.
# The syntax is not the same as normal Python syntax, so we need to tell Python
# that we want to use a regular expression by putting an r in front of the string.
# This makes sure that the backslashes in the regular expression are not treated
# as escape characters.

# The re module provides regular expression support.

import re

my_string = "The quick brown fox jumps over the lazy dog."
my_other_string = "The sun is shining."


# match() checks for a match only at the beginning of the string

match = re.match("The quick brown fox", my_string, re.I) # match the string with the regular expression, ignore case
print(match) # returns a match object if there is a match, otherwise None


start, end = match.span() # get the start and end positions of the match
print(my_string[start:end]) # print the matched text

print(re.match("The quick brown fox", my_string)) # match the string with the regular expression
print(re.match("The quick brown fox", my_other_string)) # no match, because the string doesn't start with "The quick brown fox"
#match = print(re.match("jumps over the lazy dog.", my_other_string)) # no match, activate this line to see what happens


if match != None:
    print("Match found: ", match.group()) # get the matched text
else:
    print("No match was found")

# search() checks for a match anywhere in the string

search = re.search("jumps over the lazy dog", my_string, re.I) # search the string for the regular expression, ignore case
print(search) # returns a match object if there is a match, otherwise None

start, end = search.span() # get the start and end positions of the match
print(my_string[start:end]) # print the matched text

# findall() finds all the substrings where the regular expression matches, and returns them as a list

findall = re.findall("The", my_string, re.I) # find all substrings where the regular expression matches, ignore case
print(findall) # returns a list of all matches

# split() splits the string where there is a match, and returns a list of the results

split = re.split(" ", my_string) # split the string where there is a match for the regular expression
print(split) # returns a list of the results

# sub() replaces all occurrences of the pattern in the string with the replacement string

sub = re.sub("The", "A", my_string) # replace all occurrences of "The" with "A"
print(sub) # returns the modified string



#>>> Patterns
# regex101.com is a great resource for testing regular expressions.

pattern = r"[t|T]he" # match "the" or "The" at the beginning of a word
print(re.findall(pattern, my_string)) # returns a list of all matches

pattern = r"[t|T]he|over" # match "the" or "The" at the beginning of a word
print(re.findall(pattern, my_string)) # returns a list of all matches

pattern = r"[a-z]" # match any lowercase letter
print(re.findall(pattern, my_string)) # returns a list of all matches