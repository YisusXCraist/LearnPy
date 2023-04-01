### Lists ###

my_list = [1, 2, 3, 4, 5] #array, arreglo, lista
print(my_list)

my_second_list = list()
print(my_second_list)

my_third_list = []
print(my_third_list)
print(len(my_list))

print(len(my_second_list))

my_list = [35, 22, 14, 65, 58, 47, 77, 82, 20]

print(my_list)
print(len(my_list))

my_other_list = [28, 1.65, "Gerardo","Rauda"]

print(type(my_other_list))
print(my_other_list)

#Lists are not the same as arrays, they are mutable and can be changed in place, arrays are not mutable and cannot be changed in place

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
#print(my_other_list[4]) #IndexError: list index out of range
#print(my_other_list[-5]) #IndexError: list index out of range

print(my_other_list.count(28)) #count the number of times an element appears in the list

age, height, name, last_name = my_other_list #unpacking
print(name)

print(my_list + my_other_list) #concatenation

my_list = "Hola Python"
print(my_list)
print(type(my_list))

my_list = list("Hola Python asas")
print(my_list) 

my_other_list.append("Ouroboros")
print(my_other_list) #append adds an element to the end of the list

my_other_list.insert(0, "Python") 
print(my_other_list) #insert adds an element to the list in the position specified

my_other_list.remove("Python")
print(my_other_list) #remove removes the first element that matches the value specified

my_list.pop() #pop removes the last element of the list
print(my_list)
print(my_list.pop(0)) #pop can also remove an element in a specific position
my_pop = my_list.pop(0)
print(type(my_pop)) #pop returns the element that was removed

#YisusxCraist!

del my_list[2] #del removes an element in a specific position
print(my_list)
print(my_list[2])