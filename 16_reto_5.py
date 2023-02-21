'''
#6: INVIRTIENDO CADENAS
FÁCIL | Publicación: 07/02/22 | Resolución: 14/02/22
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
'''

def invierte_cadena(cadena):
    
    longitud_texto = len(cadena)
    texto_nuevo = ""
        
    while longitud_texto > 0:
        texto_nuevo += cadena[longitud_texto - 1]
        longitud_texto -= 1

    return texto_nuevo

print(invierte_cadena("Hola mundo"))

'''
Otra posibilidad.
'''

def reverse(text):

    text_len = len(text)
    reversed_text = ""
    for index in range(0,text_len):
        reversed_text += text[text_len - index - 1]

    return reversed_text

print(reverse("Hola mundo"))