# Las variables son utilizadas para almacenar datos en memoria que pueden ser utilizados posteriormente.
# Ejemplos: type(), print(), input(), etc.

# La nomenclatura de las variables es importante, ya que nos permite identificarlas fácilmente y saber qué tipo de dato contienen.

# Variables
# Nomenclatura camel_case: nombre_variable
my_variable = "Mi variable de tipo Str"
# Nomenclatura PascalCase: NombreVariable
MyVariable = "Mi variable de tipo Str con nomenclatura PascalCase en su definición"

# Utilizaremos esta Nomenclatura para las variables
# Nomenclatura snake_case: nombre_variable

# Definición de variables
my_string = "Mi variable de tipo Str con nomenclatura snake_case en su definición"
my_int_variable = 1
my_bool_variable = True
my_int_to_str_variable = str(my_int_variable)

# Imprimir variables
print(MyVariable)
print(my_int_variable)
print(my_bool_variable)
print(type(my_int_to_str_variable))

# Concatenación de variables en print
print(my_string, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string))

# Variables en una sola línea
name, sur_name, alias, age = "Gerardo", "Rauda", "YxC", 28
print(name, sur_name, alias, age)

# Este tipo de definiciones de variables es útil cuando se trabaja con bases de datos y se requiere asignar los valores de las columnas a variables.
# Pero también puede hacer que el código sea más difícil de leer y mantener, por lo que se recomienda utilizarlo solo cuando sea necesario.

name = input("Ingresa tu nombre: ")
age = input("Ingresa tu edad: ")

print("Hola", name, "tu edad es:", age)

#Cambiamos su tipo de dato
name = 35
age = "Canelo"
print("Hola", name, "tu edad es:", age) # Imprime: Hola 35 tu edad es: Canelo

#Python no tiene un tipado fuerte, por lo que podemos cambiar el tipo de dato de una variable en cualquier momento.

# forzamos el tipo?
name: str = "Gerardo"
age: int = 28
print(type(name), type(age)) #R:// No.