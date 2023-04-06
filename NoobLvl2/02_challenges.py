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

'''
Count Vowels
Write a function that takes a string and returns the number (count) of vowels contained in it.
'''

def count_vowels(s):
    count = 0
    for i in s:
        if i in "aeiou":
            count += 1
    return count

print(count_vowels("Hello World"))

'''
Fibonacci
Write the Fibonacci series up to n
'''

def fibonacci(n):
    a = 0 # first number
    b = 1 # second number
    for i in range(n): # loop n times
        print(a) # print first number
        a, b = b, a + b # set first number to second number, second number to first number + second number


fibonacci(10)

'''
Is a prime number
Write a function that takes a number and returns True if the number is prime. from 1 to 100
'''

def is_prime(n):
    for i in range(2, n): # loop from 2 to n
        if n % i == 0: # if n is divisible by i
            return False # return false
    return True # else return true

for i in range(1, 101): # loop from 1 to 100
    if is_prime(i): # if i is prime
        print(i) # print i
