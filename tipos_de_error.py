# Syntax error
#print "Hola mundo"
# en este caso el error que daría sería:
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print("Hola mundo")

# NameError
# name_error = lis([3,4,5])
# El error que da es:
# NameError: name 'lis' is not defined. Did you mean: 'list'?
name_error = list([3, 4, 5])

# IndexError
lenguajes = ["C#", "Basic", "Cobol", "Java"]
print(lenguajes[1])
#print(lenguajes[7])  # Esto va a provoca rel error porque no hay nada más que cuatro elementos.

# ModuleNotFoundError

# import maths # Esto produce error porque el módulo es "math"
import math

# AttributeError
# print(math.PI) # esto da error porque el atributo es "pi"
print(math.pi)

# KeyError
mi_diccionario = {"Nombre":"Luís", "Apellidos":"González" }
#print(mi_diccionario["Apelidos"]) # Esto produce el error
print(mi_diccionario["Apellidos"])

# TypeError
# suma = 1 + "ggg" # Esto da error

# ImportError
