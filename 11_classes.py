### Classes ###
#Classes are a way to take a grouping of functions and data and place them inside a container so you can access them with the . (dot) operator. 

class MyEmptyPerson: #camel case is used for class names.
    pass

print(MyEmptyPerson) # This will print the class definition.
print(MyEmptyPerson()) # This will print the class instance.

class MyPerson:
    def __init__(self, name, surname, age, alias = "The Dude"):
        self.name = name
        self.surname = surname
        self.age = age
        self.alias = alias
    
    def walk(self):
        print(f"{self.name} is walking. Let's go {self.alias}")

my_person = MyPerson("John", "Doe", 35)
print(my_person.name) # This will print the class instance.
my_person.walk() # This will print the class instance.

my_other_person = MyPerson("Jane", "Doe", 30, "The Lady")
print(my_other_person.name) # This will print the class instance.
my_other_person.walk() # This will print the class instance.
my_other_person.age = 31
print(my_other_person.age) # This will print the class instance.



########## Exercise ##########
class MyPerson2:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def get_full_name(self):
        return self.name + " " + self.surname
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

my_person2 = MyPerson2("John", "Doe", 35)
#print(my_person2.get_full_name()) # This will print the class instance.