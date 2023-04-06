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