### Dictionaries ###

my_dict = dict() #dict() creates an empty dictionary
my_other_dict = {} #creates an empty dictionary

print(type(my_dict)) #prints the type of the dictionary
print(type(my_other_dict)) #prints the type of the dictionary

my_other_dict = {"Name":"Yisus", "Surname":"xCraist", "Age":28, "Height":1.65} #creates a dictionary with the elements specified, relation between keys and values
print(my_other_dict) #prints the dictionary

my_dict = {
    "Name":"Yisus",
    "Surname":"xCraist",
    "Age":28,
    "Height":1.65,
     1 : "One",
    "Lenguajes" : {"Kotlin", "Swift", "Python"}
}

print(my_dict) #prints the dictionary

print(len(my_dict)) #prints the length of the dictionary

#Dictonaries are unordered, so the order of the elements is not guaranteed
#Dictionaries are mutable, so you can change the values of the elements

print(my_dict["Name"]) #prints the value of the key "Name"

my_dict["Name"] = "Jesus" #changes the value of the key "Name"
print(my_dict["Name"]) #prints the value of the key "Name"

print(my_dict[1]) #prints the value of the key 1

del my_dict[1] #deletes the element with the key 1
print(my_dict) #prints the dictionary

print("Yisus" in my_dict) #prints False, because the value "Yisus" is not a key in the dictionary
print("Name" in my_dict) #prints True, because the key "Name" is in the dictionary

print(my_dict.items()) #prints the items of the dictionary
print(my_dict.keys()) #prints the keys of the dictionary
print(my_dict.values()) #prints the values of the dictionary
print(my_dict.fromkeys(my_dict)) #creates a new dictionary with the keys specified and the values None
