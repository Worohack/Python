# Reto 0: EL FAMOSO "FIZZ BUZZ”
'''
FÁCIL | Publicación: 27/12/21 | Resolución: 03/01/22
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
 '''

i = 1
while i < 101:
    #print("\n", i)
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
    i += 1

# Otra posibilidad

print ("******** OTRA POSIBILIDAD **********")
def fizbuz():
    #  Se pone (1, 101) para que incluya ambos números en la impresión
    for indice in range(1, 101):
        # Comprobamos primero si el número es múltiplo de 3 y de 5 porque es el caso más restrictivo
        if indice % 3 == 0 and indice % 5 == 0:
            print("fizzbuzz")
        elif indice % 3 == 0:
            print("fizz")
        elif indice % 5 == 0:
            print("buzz")
        else:
            print(indice)

fizbuz()
