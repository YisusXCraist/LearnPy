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

