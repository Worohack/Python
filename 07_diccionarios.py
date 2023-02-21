# Defino dos diccionarios de distinta forma

mi_diccionario = dict()
mi_otro_diccionario = {}

# Doy valores al diccionario

mi_otro_diccionario = {"Nombre" : "Francisco Javier", "Apellidos" : "Muñoz Ruano", "Edad" : 56, 
    "Domicilio" : "C/. Marathon, 5"}

# Muestro el diccionario completo
print(mi_otro_diccionario)

#Agrego valores a mi_diccionario, incluyendo un set como un valor de una de sus claves.

mi_diccionario = {
    "Nombre" : "Francisco Javier", 
    "Apellidos" : "Muñoz Ruano", 
    "Edad" : 56, 
    "Domicilio" : "C/. Marathon, 5", 
    "Lenguajes" : {"Python", "C#", "Basic","Java"}
    }

print(mi_diccionario)

# Muestro un solo elemento dependiendo del nombre de la clave que se ponga como índice

print(mi_otro_diccionario["Nombre"])

# Modifico el valor de la clave "Domicilio"

mi_diccionario["Domicilio"] = "Pza. de Riofrío, 6"
print(mi_diccionario)

# Añado una nueva clave al diccionario

mi_diccionario["DNI"] = "27324343J"
print(mi_diccionario)

# Borro una de las claves del diccionario
del mi_diccionario["DNI"]
print(mi_diccionario)

mi_diccionario.clear()
print(mi_diccionario)
mi_diccionario = mi_otro_diccionario.copy()
print(mi_diccionario)
print(mi_otro_diccionario)

# Muestro los items de un diccionario

print(mi_diccionario.items())

# Muestro las claves de un diccionario

print(mi_diccionario.keys())

# Muestro los valores de un diccionario

print(mi_diccionario.values())

#Creo un nuevo diccionario con valores a cero

otro_diccionario_mas = dict.fromkeys(("Clave", "Clave 2"))

print(otro_diccionario_mas)