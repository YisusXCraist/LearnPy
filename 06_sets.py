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