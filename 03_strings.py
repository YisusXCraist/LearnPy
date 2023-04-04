### Strings ###

my_string = "Hello World"
my_other_string = 'Hello World 2'

print(len(my_string)) # 11
print(len(my_other_string)) # 13

print(my_string + "" + my_other_string) # Hello WorldHello World 2

my_new_line_string = "Este es un String\ncon un salto de línea"
print(my_new_line_string) 

my_new_tab_string = "\tEste es un String con tabulacion"
print(my_new_tab_string) 

my_new_scaped_string = "\\tEste es un String \\nescapado"
print(my_new_scaped_string) 

### formateo de strings ###

name, surname, edad = "Gerardo", "Rauda", 28

print("Hola me llamo %s %s y tengo %d años" % (name, surname, edad)) #%s string, %d int, %f float
print("Hola me llamo {} {} y tengo {} años".format(name, surname, edad)) # python 3.6
print(f"Hola me llamo {name} {surname} y tengo {edad} años") # python 3.6


# desempaquetado de caracteres
language = "Python"
a, b, c, d, e, f = language
print(a) # P
print(e) # y

# División de strings

language_slice = language[1:]
print(language_slice) # yh

language_slice = language[-2]
print(language_slice) # o

# reverse string
reversed_language = language[::-1] # [start:end:step]
print(reversed_language) # nohtyP

language_slice = language[0:6:2] # [start:end:step]
print(language_slice) # Pto 

# Funciones

print(language.upper()) # PYTHON
print(language.lower()) # python
print(language.capitalize()) # Python
print(language.title()) # Python
print(language.swapcase()) # pYTHON
print(language.count("P")) # 1
print("i".isnumeric()) # False
print("i".isalpha()) # True
print(language.startswith("P")) # True
