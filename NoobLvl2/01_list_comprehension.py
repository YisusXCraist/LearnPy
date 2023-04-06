### List Comprehension ###
# List comprehension is a way to create a list in a single line of code.
# It is a very powerful tool that can be used to create lists in a very
# efficient way.
# The syntax is:
# [expression for item in list] # This will create a list with the expression applied to each item in the list.
#
# Example:
# numbers = [1, 2, 3, 4, 5]
# squares = [number ** 2 for number in numbers]
# print(squares) # [1, 4, 9, 16, 25]
#

my_original_list = [1, 2, 3, 4, 5] # This is a list of numbers
my_new_list = [number ** 2 for number in my_original_list] # This is a list comprehension that creates a new list with the squares of the numbers in the original list

print(my_new_list) # [1, 4, 9, 16, 25]

my_range = range(8)
print(list(my_range)) # [0, 1, 2, 3, 4, 5, 6, 7]

my_other_list = [i for i in range(1, 10)] # This is a list comprehension that creates a new list with the numbers from 1 to 5
print(my_other_list) # [1, 2, 3, 4, 5]

# List comprehension can also be used to create a list of strings.
# Example:
names = ["John", "Bob", "Mosh", "Sarah", "Mary"]
usernames = [name.lower() for name in names]
print(usernames) # ["john", "bob", "mosh", "sarah", "mary"]

# List comprehension can also be used to create a list of booleans.
# Example:
numbers = [1, 2, 3, 4, 5]
is_even = [number % 2 == 0 for number in numbers]
print(is_even) # [False, True, False, True, False]

# List comprehension can also be used to create a list of lists.
# Example:
numbers = [1, 2, 3, 4, 5]
numbers2 = [6, 7, 8, 9, 10]
numbers3 = [11, 12, 13, 14, 15]
numbers4 = [16, 17, 18, 19, 20]
numbers5 = [21, 22, 23, 24, 25]
numbers6 = [26, 27, 28, 29, 30]

numbers_list = [numbers, numbers2, numbers3, numbers4, numbers5, numbers6]
print(numbers_list) # [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]

numbers_list = [[number for number in numbers], [number for number in numbers2], [number for number in numbers3], [number for number in numbers4], [number for number in numbers5], [number for number in numbers6]]
print(numbers_list) # [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]

# List comprehension can also be used to create a list of dictionaries.
# Example:
names = ["John", "Bob", "Mosh", "Sarah", "Mary"]
usernames = ["johnsmith", "bobsmith", "moshmosh", "sarahsarah", "marymary"]
users = [{"name": name, "username": username} for name, username in zip(names, usernames)]

print(users)