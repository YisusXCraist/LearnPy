### Lambdas ###
# A lambda is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax:
# lambda arguments : expression
#

# Example:
# x = lambda a : a + 10
# print(x(5))

# Example:
# x = lambda a, b : a * b
# print(x(5, 6))

sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(5, 6))

multiply_two_values = lambda first_value, second_value: first_value * second_value
print(multiply_two_values(5, 6))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

sum_three_values_lambda = sum_three_values(5)
print(sum_three_values_lambda(5, 6))
# print(sum_three_values(5)(5, 6))

