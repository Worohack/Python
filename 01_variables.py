# Defino varias variables:

cadena_de_caracteres = "Variable de tipo string"
variable_entera = 9
variable_bool = True

# Imprimo en la consola los valores de las variables

print(cadena_de_caracteres)
print(variable_entera)
print(variable_bool)

# También puedo imprimir todos los valores de una vez

print(cadena_de_caracteres,variable_entera,variable_bool)

# Cambio del valor de "variable_entera" a string y la guardo en una nueva variable

nueva_variable_string = str(variable_entera)
print("La cadena es: ", nueva_variable_string, " y su tipo es: ", type(nueva_variable_string) )

# Imprimo la longitud del contenido de la variable "cadena_de_caracteres"

print(len(cadena_de_caracteres))

# Definición de variables en una sola línea

nombre, apellido, alias, edad = "Juan", "López", "Wisconsin", 19
print(nombre, apellido,  ", alias:", alias, ", de edad:", edad) 

# Uso de la función input

nombre = input("Dime tu nombre: ")
apellido = input("Ahora dime tu apellido: ")
alias = input("Y tu alias?:")
edad = input("Por último, dime tu edad:")
print(nombre, apellido,  ", alias:", alias, ", de edad:", edad) 
