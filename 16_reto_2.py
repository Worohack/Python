#1: ¿ES UN ANAGRAMA?

'''

MEDIA | Publicación: 03/01/22 | Resolución: 10/01/22
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */

'''
def anagrama_si_no(palabra1, palabra2):
    '''
     Primero comparo si las dos palabras son iguales, por que si lo son, no son un anagrama.
     Pero también tengo que tener en cuenta que la comparación la tengo que hacer o con todas las
     letras en mayúsculas o en minúsculas, porque si comparo algo en mayúsculas y en minúsculas,
     Python considera que son distintas
    '''

    if palabra1.lower() == palabra2.lower():
        return False
        ''' 
        Como un anagrama es que dos palabras tienen dos letras. Vamos a ordenar alfabéticamente las letras de cada palabra
        para luego compararlas.
        '''
    print(sorted(palabra1.lower()))
    print(sorted(palabra2.lower()))
    if sorted(palabra1.lower()) == sorted(palabra2.lower()):
        return True
    else:
        return False


print(anagrama_si_no("hola","Alho"))