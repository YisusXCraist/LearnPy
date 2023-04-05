### SETS ###

my_set = set() #set() creates an empty set
my_other_set = {} #{} creates an empty dictionary

print(type(my_set)) #prints the type of the set
print(type(my_other_set)) #prints the type of the set, but it's a dictionary

my_other_set = {"Yisus", "xCraist", 1.65, 28} #creates a set with the elements specified
print(type(my_other_set)) #prints the type of the set

print(len(my_other_set)) #prints the length of the set

print(my_other_set) #prints the set

my_other_set.add("Mouse") #adds an element to the set
print(my_other_set) #prints the set, not a ordered structure

my_other_set.add("Mouse") #adds an element to the set
print(my_other_set) #prints the set, not a ordered structure

#adding a repeated element doesn't change the set
#A set is a collection of unordered elements, without duplicates

print("Yisus" in my_other_set) #prints True if the element is in the set
print("yisus" in my_other_set) #prints False if the element is not in the set
#the comparison is case sensitive, so "yisus" is not in the set
print("Clear" in my_other_set) #prints False if the element is not in the set

my_other_set.remove("Mouse") #removes an element from the set
print(my_other_set) #prints the set

my_other_set.clear() #removes all the elements from the set
print(len(my_other_set)) #prints the length of the set 

del my_other_set #deletes the set
# print(my_other_set) #prints an error because the set doesn't exist

my_set = {"Yisus", "xCraist", 1.65, 28} #creates a set with the elements specified
my_list = list(my_set) #converts the set to a list
print(my_list) #prints the list 
print(my_list[0]) #prints the first element of the list
#This type of conversion is useful when you need to access the elements of the set, but risking the order of the elements as a set is unordered

my_other_set = {"Kotlin", "Swift", "Python"}
my_new_set = my_set.union(my_other_set) #creates a new set with the union of the two sets
print(my_new_set) #prints the new set

print(my_new_set.union({"Java", "C++"})) #prints the new set with the union of the new set and the new elements

print(my_new_set.difference(my_set)) #prints the elements of the new set that are not in the first set