# Declaro mi edad como un entero

mi_edad = 55

# Declaro mi altura como un float

mi_altura = 1.65

# Declaro un número complejo

numero_complejo = 1 + 3j

# Solicito la base y la altura de un triángulo

base = input("Dime la base del triángulo: ")
altura = input("Dime la altura del triángulo: ")

# Calculo el área del triángulo

area = (int(base) * int(altura)) / 2
print(area)

# Solicito las longitudes de los lados de un triángulo

lado1 = int( input("Dime el tamaño del lado 1: "))
lado2 = int( input("Dime el tamaño del lado 2: "))
lado3 = int( input("Dime el tamaño del lado 3: "))

# Calculo el perímetro del triángulo

perimetro = lado1 + lado2 + lado3
print(perimetro)

# Pido el largo y el ancho de un rectángulo

largo = int(input("Dime el largo de un rectangulo: "))
ancho = int(input("Dime el ancho de un rectangulo: "))

# Calculo su área

area = largo + ancho
print(area)

# Calculo su perímetro
perimetro = 2 * (largo + ancho)
print(perimetro)

# Pido el radio de un círculo

radio = int(input("Dime el radio de un círculo: "))

# Calculo el área

area = 3.14 * (radio ** 2)
print(area)

# Calculo la circunferencia

circunferencia = 2 * 3.14 * radio
print(circunferencia)

# Pido un valor para averiguar otro
x = int(input("Dime el valor de X: "))

# Calculo y en función del valor de x

y = (x ** 2) + (6 * x) + 9
print(y)

# Calculo la longitud de "Dragón" y de "Python"

Longitud1 = len("Dragon")
Longitud2 = len("Python")

# Genero una comparación falsa

print(Longitud1 > Longitud2)

# Convierto la longitud de "Python" a flotante

print(float(Longitud2))

# Convierto la longitud de "Python" a cadena

print(str(Longitud2))

# Compruebo si un número es par

numero = int(input("Dime un número: "))
resto = numero / 2
if resto != 0:
    print("El número es impar")
else:
    print("El número es par")

print("Fin If")
