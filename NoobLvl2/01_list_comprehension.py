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