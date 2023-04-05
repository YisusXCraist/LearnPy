### Modules ###
# A module is a file containing Python definitions and statements.
# The file name is the module name with the suffix .py appended.
# Within a module, the module’s name (as a string) is available as the value of the global variable __name__.

#import module

from module import sum_values, print_values

#print(module.sum_values(1, 2, 3, 4, 5))
#module.print_values(1, 2, 3, 4, 5)

print(sum_values(1, 2, 3, 4, 5))
print_values(1, 2, 3, 4, 5)