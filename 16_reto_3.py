'''
#2: LA SUCESIÓN DE FIBONACCI
DIFÍCIL | Publicación: 10/01/22 | Resolución: 17/01/22
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
 '''

def fibonacci(numeros):

    for j  in numeros:
        if j==0:
            lista = [numeros[j], numeros[j+1], numeros[j] + numeros[j+1]]
        else:
            lista.append(lista[j] + lista[j+1])
    print(lista)

# El rango lo establezco en 48 porque los dos primeros valores son fijos: 0 y 1

listado_numeros = range(48)
fibonacci(listado_numeros)

'''
Otra posible forma
'''
def fibo():
    
    prev = 0
    next = 1

    for index  in range(0,50):
        print(prev)
        fib = next + prev
        prev = next
        next = fib

fibo()
