'''
#3: ¿ES UN NÚMERO PRIMO?
MEDIA | Publicación: 17/01/22 | Resolución: 24/01/22
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
'''

def is_primo(numero):
    
    resultado_is_primo = True

    i = 2
    while i <= numero:
        
        resultado = numero % i
        if resultado == 0 and numero != i:
            resultado_is_primo = False
        break
        i += 1
        

    return resultado_is_primo

def imprime_primos():
    
    for teorico_primo in range(2,100):
        for dividendo in range(2,200):
            if teorico_primo % dividendo == 0 and teorico_primo != dividendo:
                break
            elif teorico_primo % dividendo == 0 and teorico_primo == dividendo:
                print(teorico_primo)
                break

if is_primo(int(input("Introduce un número: "))):
    print("El número es primo")
else:
    print("El número no es primo")

imprime_primos()