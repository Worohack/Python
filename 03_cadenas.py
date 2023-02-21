# Divido una cadena en cada uno de los caracteres que la componen 

a, b, c, d, e, f = "Python"
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Creat subcadena

cadena = "Hola python"
subcadena1 = cadena[3:6]
subcadena2 = cadena[6:]
subcadena3 = cadena[-3]
print(subcadena1)
print(subcadena2)
print(subcadena3)

# Invertir cadena

cadena_inversa = cadena[::-1]
print(cadena_inversa)

# Seleccionar algunos caracteres

subcadena4 = cadena[0:6:2]
print(subcadena4)

# Algunas funciones dependientes del tipo de dato String
print(cadena.capitalize())
print(cadena.casefold())
print(cadena.center(20))
print(cadena.count("o"))

