### Functions ###
# Functions are a way to organize code into reusable blocks. They are a way to
# break up your code into logical chunks that can be used over and over again.
# Functions are also a way to make your code more readable and easier to
# understand.

# Functions are defined using the def keyword. For example:
def my_function():
    print("Hello from a function")

# To call a function, use the function name followed by parenthesis:
my_function ()

def sum_two_values (first_value, second_value):
    return first_value + second_value
# Note: The return statement is used to exit a function and return a value.

print(sum_two_values (5, 10))
#print(sum_two_values ("Hola ", "mundo!")) # This will cause an error if the function is not defined to accept strings or concatenation.
print(sum_two_values (1.4, 1.5))

def sum_two_values_wreturn (first_value, second_value):
    return first_value + second_value
# Note: The return statement is used to exit a function and return a value.

sum_two_values_wreturn (5, 10) # This will not print anything because the function does not have a print statement.
print(sum_two_values_wreturn (5, 10)) # This will print the return value of the function.

my_return = sum_two_values_wreturn (5, 10)
print(my_return)

def print_name (name, surname):
    print(f"Hello {name} {surname}") # This is a f-string. It is a way to format strings in Python 3.6+.

print_name ("John", "Doe") # This will print "Hello John Doe".

def print_name_wdefault (name, surname, alias = "The Dude"):
    print(f"Hello {name} {surname}, alias {alias}") # This is a f-string. It is a way to format strings in Python 3.6+.

print_name_wdefault ("John", "Doe") # This will print "Hello John Doe, alias The Dude".
print_name_wdefault ("John", "Doe", "The Big Lebowski") # This will print "Hello John Doe, alias The Big Lebowski".

# This is a function that accepts an arbitrary number of arguments.
def print_upper_texts(*texts): #*text is a tuple of arguments.
    for text in texts:
        print(text.upper())

print_upper_texts("Hello", "World", "This", "Is", "A", "Test")