#Las variables son las funciones importantes que ya vienen en Python, y que nos permiten almacenar datos en memoria para poder utilizarlos posteriormente.
#Ejemplos: type(), print(), input(), etc.

#La nomeclatura de las variables es importante, ya que nos permite identificarlas facilmente, y saber que tipo de dato contiene.

#Variables
#nomencatura camelCase: nombreVariable
myVariable = "Mi variable de tipo Str"
#nomencatura PascalCase: NombreVariable
MyVariable = "Mi variable de tipo Str con nomencatura PascalCase en su definicion"

#Utilizaremos esta Nomencatura para las variables#
#nomencatura snake_case: nombre_variable

#definicion de variables
my_string = "Mi variable de tipo Str con nomencatura snake_case en su definicion"

my_int_variable = 1

my_bool_variable = True

my_int_to_str_variable = str(my_int_variable)

#Imprimir variables
print(MyVariable)
print(my_int_variable)
print(my_bool_variable)
print(type(my_int_to_str_variable))

#concatenacion de variables en print
print(my_string, my_int_to_str_variable, my_bool_variable)

print("Este es el valor de:", my_bool_variable)

#print(type(print(my_string, my_int_to_str_variable, my_bool_variable)))
#<class 'NoneType'>

# Algunas funciones del sistema

print (len(my_string))

# Variables en una sola linea
name, sur_name, alias, age = "Gerardo", "Rauda", "YxC", 28

print(name, sur_name, alias, age)

#Este tipo de definiciones de variables es muy util cuando se trabaja con bases de datos, y se requiere asignar los valores de las columnas a variables.
#Pero tambien ocasiona que el codigo sea mas dificil de leer y dar mantenimiento, por lo que se recomienda utilizarlo solo cuando sea necesario.

name = input("Ingresa tu nombre: ")
age = input("Ingresa tu edad: ")

print("Hola", name, "tu edad es:", age)
