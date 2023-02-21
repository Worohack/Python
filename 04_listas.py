# Creación de listas

mi_lista = list(["oreja", "de", "qué", "te", "quejas"])
print(mi_lista)
mi_otra_lista = [10, 5, 93, 5, 45, 5]

# Impresión del número de elementos de la lista

print(len(mi_otra_lista))

# Impresión del contenido de la lista

print(mi_otra_lista)

# Lista con elementos de difeerentes tipos de datos

mi_lista = [35, 1.77, "Árbol"]
print(mi_lista)

# Muestro un elemento determinado de la lista

print(mi_lista[2])
print(mi_lista[-2])

# Cuento cúantas veces se repite el valor 5 en la lista

print(mi_otra_lista.count(5))

# Asigno a variables los elementos de mi_lista

edad, altura, cosa = mi_lista
print(edad)
print(altura)
print(cosa)

# Concateno las dos listas

lista_unida = mi_lista + mi_otra_lista
print(lista_unida)

# Añado un elemento al final de la lista
mi_lista.append("Baobab")
print(mi_lista)

""" 

Añado o inserto un nuevo elemento en la posición que indico como primer argumento 
de la función insert

"""

mi_lista.insert(1, "Madagascar")
mi_lista.insert(3, 63)
print(mi_lista)

# Elimino un elemento de la lista

mi_lista.remove("Árbol")
print(mi_lista)

# Cambio un elemento por otro (cambio el 10 por "Cambiazo")

lista_unida[3] = "Cambiazo"
print(lista_unida)

# Invierto el orden de los elementos de la lista

lista_unida.reverse()
print(lista_unida)
