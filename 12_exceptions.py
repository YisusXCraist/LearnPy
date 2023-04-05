#### Exception Handling ####
# Exceptions are errors that occur during execution of a program
# Exceptions are handled with try and except statements

number_one, number_two = 1, 0

print(number_one + number_two) # This will print the class instance.

#print a line to separate the output
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

number_two = "Dos"

#print(number_one + number_two) # Error: TypeError: unsupported operand type(s) for +: 'int' and 'str'

try:
    print(number_one + number_two)
    print("There was no error.")
except:
    print("There was a type error!")
    print("Make sure you add two integers together.")
else:
    print("There was no error.") # This will not print if there is an error.
finally:
    print("This will print no matter what.") # This will print no matter what.

# exceptios for specific errors

try:
    print(number_one + number_two)
    print("There was no error.")
except TypeError as error:
    # This will only run if there is a TypeError
    print("There was a type error!")
    print(error)
except ValueError as error:
    # This will only run if there is a ValueError
    print("There was a value error!")
    print(error)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")