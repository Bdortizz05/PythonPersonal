# Variables

my_string_variable = "My variable of text "
print(my_string_variable)

my_int_variable = 954253361233
print(my_int_variable)
print(type(my_int_variable))


my_bool_number = True
print(my_bool_number)

"""
Cambio de variables
of integer to text 
"""

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# of text to integer

my_str_to_int_variable = int(my_int_to_str_variable)
print(my_str_to_int_variable)
print(type(my_str_to_int_variable))

# Concatenacion  de variable en un Print

print(my_bool_number, my_str_to_int_variable, my_int_variable)

# len "funcion para validar el tamaño de la variable"
print(len(my_string_variable))

# Variable en una sola línea

name, surname, alias, age = "Brayan", "Ortiz", "Dani", 26

print("Me llamo", name, "Mi apellido es", surname, "Y me dicen", alias, "my age", age)

# Inputs pruebas

name = input("cuale es tu nombre?")
surname = input("cuale es tu surname?")
age = input("cuale es tu edad?")

print("nombre", name, "Apellido", surname, "Edad", age)
