### Loops ###

#>>>>> While loop

# While loop is used to execute a block of code repeatedly until a given condition is satisfied. 
#And when the condition becomes false, the line immediately after the loop in the program is executed. 
#The while loop falls under the category of indefinite iteration.

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:  
    print("my_condition is no longer less than 10")
# Note: The condition is checked before the loop is executed.

print("End of the first while loop")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("my_condition is 15")
        break
    print(my_condition)
# Note: The condition is checked before the loop is executed.

print("End of the second while loop")

#>>>>> For loop
# The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects.
# Iterating over a sequence is called traversal.
# For loop falls under the category of definite iteration.
# The for loop does not require an indexing variable to set beforehand.
# The for loop can iterate over any sequence type.

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list: #for each element in the list, where element is the variable name, you can use any name
    print(element) #print each element of the list

my_tuple = (35, 24, 62, 52, 30, 30, 17)

for element in my_tuple: #for each element in the tuple, where element is the variable name, you can use any name
    print(element) #print each element of the tuple

my_set = {35, 24, 62, 52, 30, 30, 17}

for element in my_set: #for each element in the set, where element is the variable name, you can use any name
    print(element) #print each element of the set

my_dictionary = {"name": "John", "age": 36, "country": "Norway"}

for key in my_dictionary: #for each key in the dictionary, where key is the variable name, you can use any name
    print(key) #print each key of the dictionary

    #to access the values in the dictionary, you can use the key as an index
    #print(my_dictionary[key])

for element in my_dictionary:
    print(element)
    if element == "age":
        break
else:
    print("End of the for loop")

for element in my_dictionary:
    print(element)
    if element == "age":
        continue
else:
    print("End of the for loop")