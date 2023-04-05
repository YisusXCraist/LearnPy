### Tuples ###

my_tuple = tuple() #tuple() creates an empty tuple

my_other_list = ()  #() creates an empty tuple

my_tuple = (28, 1.65, "Yisus", "xCraist", "Yisus") #tuple() creates a tuple with the elements specified

print(my_tuple) #prints the tuple
print(type(my_tuple)) #prints the type of the tuple

print(my_tuple[0]) #prints the first element of the tuple
print(my_tuple[-1]) #prints the first element of the tuple
#print(my_tuple[-6]) # prints an error because the tuple has only 4 elements // index error

print(len(my_tuple)) #prints the length of the tuple

print(my_tuple.count("Yisus")) #prints the number of times that the element "Yisus" appears in the tuple
print(my_tuple.index("xCraist")) #prints the index of the first element "Yisus" in the tuple

#my_tuple[1] = 1.80 #prints an error because tuples are immutable // type error
#print(my_tuple) #prints the tuple

### !!! Lists are mutable, tuples are immutable !!! ###

my_other_tuple = (28, 29, 30)
my_sum_tuple = my_tuple + my_other_tuple #creates a new tuple with the elements of the two tuples
print(my_sum_tuple) #prints the new tuple

print(my_sum_tuple[3:6]) #prints the elements of the tuple from the index 3 to the index 5 

## Tuples are immutable, but you can convert them into lists and then change them ##

my_tuple = list(my_tuple) #converts the tuple into a list
print(type(my_tuple)) #prints the type of the tuple

my_tuple[4] = "Mouse" #changes the element in the index 4 of the tuple
my_tuple.insert(1, "Azul") #inserts an element in the index 1 of the tuple

my_tuple = tuple(my_tuple) #converts the list into a tuple
print(type(my_tuple)) #prints the type of the tuple
print(my_tuple) #prints the tuple

#del my_tuple[2] #prints an error because tuples are immutable // type error

del my_tuple #deletes the tuple from memory
#print(my_tuple) #prints an error because the tuple was deleted from memory // name error