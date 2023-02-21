# Una posibilidad

def producto(producto1, producto2):
    return suma(producto1 * producto2)

def suma(sumatorio):
    return sumatorio + 15

print(producto(3,9))

# Otra posibilidad

def producto_a(producto1, producto2):
    resultado = producto1 * producto2
    return suma_a(resultado)

def suma_a(sumatorio):
    return sumatorio + 25

print(producto_a(4,10))

# Una función pasada como argumento a otra función

def suma(valor1, valor2, funcion):
    return funcion(valor1+valor2)

def resta(valor):
    return 15 - valor

print(suma(7,5,resta))

####### Closures ########

def sum_ten():
    def anade(valor):
        return valor + 10
    return anade

nuevo_closure = sum_ten()
print(nuevo_closure(9))

# Llamada a funciones anidadas

def sum_ten(valor1):
    valor1 += 100
    def anade(valor):
        return valor + 10 + valor1 
    return anade

nuevo_closure = sum_ten(2)
print(nuevo_closure(9))

# Otra forma de hacer llamadas a funciones anidadas
def sum_ten(valor1):
    valor1 += 100
    def anade(valor):
        return valor + 10 + valor1 
    return anade

print(sum_ten(7)(16))

####### Buit-in Higher Order Functions #######

##### Map

def multiplica(numero):
    return numero * 2

numeros = [2, 5, 10, 21]

resultado = list(map(multiplica, numeros))
resultado1 = list(map(lambda x: x * 3, numeros))
print(resultado, resultado1)

##### Filter

def filtrado(numero):
    if numero % 2 == 0:
        return True
    return False

numeros = [5,1,4,6,3,8]
resultado = filter(filtrado, numeros)
print(list(resultado))

##### Reduce

from functools import reduce

numeros = [5,1,4,6,3,8]

def sumavalores(valor1, valor2):
    return valor1 + valor2

print(reduce(sumavalores, numeros))
