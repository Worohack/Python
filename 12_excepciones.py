numero_uno = 5
numero_dos = 1
print(numero_uno + numero_dos)

''' 
El resultado de las líneas anteriores sería la suma de los dos números
pero si, por ejemplo, a numero_dos le doy como valor una cadena, la suma 
provocaría un error porque no se puede sumar un número y un string.
'''
numero_dos = "1"
# print(numero_uno + numero_dos) # Ahora esto provocaría un error

# Para controlar el error

try:
    print(numero_uno + numero_dos)
except:
    print("ALgo has hecho mal")

# Otro control añadiendo else

numero_dos = 3

try:
    print(numero_uno + numero_dos)
except:
    print("ALgo has hecho mal")
else:
    print("Enhorabuena. NO ha habido un error")

# Por último añadiendo finally

numero_dos = 10

try:
    print(numero_uno + numero_dos)
except:
    print("ALgo has hecho mal")
else:
    print("Enhorabuena. NO ha habido un error")
finally:
    print("pase lo que pase, hago otro cálculo: ")
    numero_dos = 7
    print(numero_uno + numero_dos)

    # Controlo los errores y obtengo más información dentro del except

    numero_dos = "9"
try:
    print(numero_uno + numero_dos)
except TypeError as e:
    print("ALgo has hecho mal:", e)
else:
    print("Enhorabuena. NO ha habido un error")
finally:
    print("pase lo que pase, hago otro cálculo: ")
    numero_dos = 7
    print(numero_uno + numero_dos)