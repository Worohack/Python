import re

mi_cadena = "Esta es la lección número 7: Lección de Expresiones Regulares: Primera parte"
mi_otra_cadena = "Esta no es la lección número 6: Manejo de ficheros"

# match

print("--------", "match", "----------")
resultado1 = re.match("Esta es la lección", mi_cadena)
resultado2 = re.match("Esta es la Lección", mi_otra_cadena)
print("En \"mi_cadena\": ", resultado1 )
print("En \"mi_otra_cadena\": ", resultado2)
print(resultado1.span())

# search

print("--------", "search", "----------")
resultado3 = re.search("Lección número", mi_cadena, re.I)
print(resultado3)

# findall

print("--------", "findall", "----------")
resultado4 = re.findall("lección", mi_cadena, re.I)
print(resultado4)

# split

print("--------", "split", "----------")
resultado5 = re.split(":",mi_cadena)
print(resultado5)

#sub

print("--------", "sub", "----------")
resultado6 = re.sub("Expresiones", "expresionesssssss", mi_cadena)
print(resultado6)
resultado6 = re.sub("lección", "bloque", mi_cadena)
print(resultado6)
resultado6 = re.sub("lección|Lección", "lecciones", mi_cadena)
print(resultado6)

# Patrones

print("--------", "Patrones", "----------")
patron = r"[lL]ección"
print(re.findall(patron, mi_cadena))

patron = r"^[a-z0-9_]+@[a-z]+\.[com|es|org|net]+$"
email = "fjmunozruano@gmail.com"
print(re.match(patron, email))
print(re.search(patron, email))
print(re.findall(patron, email))

print("-----------------------------")

email = "fjmunozruano@gmail"
print(re.match(patron, email))
print(re.search(patron, email))
print(re.findall(patron, email))
