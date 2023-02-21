# Defino dos tuplas de distinta forma

mi_tupla = tuple()
mi_otra_tupla = ()

# Doy valores a las tuplas

mi_tupla=(28, 45, 56, 100, 115)
mi_otra_tupla =  ("Luís", "Carmen", "Raquel", "Pedro")

# Muestro el elemento 56

print(mi_tupla[2])

# Muestro en qué posiición se encuentra el elemento 45

print(mi_tupla.index(45))

# Concateno dos tuplas

una_tupla_mas = mi_tupla + mi_otra_tupla
print(una_tupla_mas)