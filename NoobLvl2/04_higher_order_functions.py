### Higher Order Functions ###
# A function that takes a function as an argument is called a higher order function.
# A function that returns a function is also called a higher order function.
#
# Example:
# def sum_two_values(first_value, second_value):
#     return first_value + second_value
#
# def multiply_two_values(first_value, second_value):
#     return first_value * second_value
#
# def sum_or_multiply_two_values(first_value, second_value, function):
#     return function(first_value, second_value)
#
# print(sum_or_multiply_two_values(5, 6, sum_two_values))

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_one(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_one(5, 6, sum_one))
print(sum_two_values_and_one(5, 6, sum_five))

### Closures ###
# A closure is a function that remembers the values from the enclosing lexical scope even when the program flow is not in the enclosing scope.
# A closure is a function that returns another function.

def sum_ten():
    def add(value):
        return value + 10
    return add

add_closure = sum_ten()
print(add_closure(5))

### Built-in Higher Order Functions ###

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map() function
# map() function returns an iterator that applies the given function to each item of the given iterable.

def multiply_by_two(number):
    return number * 2

print(list(map(multiply_by_two, numbers))) # normal function
print(list(map(lambda number: number * 2, numbers))) # lambda function

# filter() function
# filter() function returns an iterator that contains only the elements that satisfy the given condition.

def filter_greater_than_five(number):
    if number > 5:
        return True
    return False

print(list(filter(filter_greater_than_five, numbers))) # normal function
print(list(filter(lambda number: number > 5, numbers))) # lambda function

# reduce() function
# reduce() function returns a single value after applying the given function to the items of the given iterable.
