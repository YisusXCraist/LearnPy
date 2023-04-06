### Error Types ###

### SyntaxError
# print("Hello World") # Missing parentheses

#print "Hello World" # Error
print("Hello World") # Correct

### NameError
variable_name = "Hello World" # Delete the # to remove the error
print(variable_name) # variable_name is not defined

### IndexError
my_list = ["Python", "Java", "C++", "C#", "JavaScript"] 
print(my_list[0])
print(my_list[4])
print(my_list[-1])
#print(my_list[5]) # list index out of range, because the list has 5 elements and the index starts at 0
#Remove the # above to see the error

### ModuleNotFoundError

#import maths # ModuleNotFoundError: No module named 'maths' >>>> descomentar para ver el error
import math # No error

### AttributeError
print(math.pi) # No error
#print(math.pie) # AttributeError: module 'math' has no attribute 'pie' >>>> descomentar para ver el error

### KeyError
my_dict = {"name": "John", "age": 36, "country": "USA"}
print(my_dict["name"])
print(my_dict["age"])

#print(my_dict["city"]) # KeyError: 'city' >>>> descomentar para ver el error

### TypeError
#print("Hello World" + 5) # TypeError: can only concatenate str (not "int") to str >>>> descomentar para ver el error
print("Hello World" + str(5)) # No error


### ImportError
#from math import pie # ImportError: cannot import name 'pie' from 'math' >>>> descomentar para ver el error
from math import pi # No error
print(pi)

### ValueError
#print(int("Hello World")) # ValueError: invalid literal for int() with base 10: 'Hello World' >>>> descomentar para ver el error


### ZeroDivisionError
#print(5 / 0) # ZeroDivisionError: division by zero >>>> descomentar para ver el error
print(5 / 1) # No error