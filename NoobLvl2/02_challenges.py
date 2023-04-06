### Challenges ###

'''
FizzBuzz
Write a program that prints the numbers from 1 to 100. 
But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
For numbers which are multiples of both three and five print "FizzBuzz".
'''
def fizbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
# fizbuzz()
fizbuzz() # This is the solution

'''
Is Anagram
Write a function that takes two strings and returns True if they are anagrams.
'''

def is_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower() # replace spaces and make lower case
    s2 = s2.replace(" ", "").lower() # replace spaces and make lower case
    return sorted(s1) == sorted(s2) # sort and compare, returns boolean

print(is_anagram("dog", "god"))
