def mi_funcion ():
    print("Esto es una función")

mi_funcion()

def suma(valor1, valor2):
    print(valor1 + valor2)

suma(9, 13)

def resta(valor1, valor2):
    return valor1 - valor2

resultado = resta(10, 8)
print(resultado)

'''
Voy a crear una función con dos parámetros a la que luego voy a llamar
cambiando el orden de los parámetros
'''
def imprime_datos(nombre_recibido, apellidos_recibido):
    print(f"{nombre_recibido} {apellidos_recibido}")

imprime_datos(apellidos_recibido = "Muñoz Ruano", nombre_recibido = "Francisco Javier") 

'''
 Creo función con un parámetro con un valor por defecto. Y también he añadido al 
 valor por defecto el caracter \" para incluir las " en la impresión del valor
'''

def funcion_con_parametro_con_valor_defecto(nombre, apellidos, alias = "\"Sin alias\""):
    print(f"{nombre} {apellidos} {alias}")

# Aquí no paso el tercer parámetro en la llamada

funcion_con_parametro_con_valor_defecto("Emilio", "Sánchez Lozano")

# Aquí paso el tercer parámetro en la llamada

funcion_con_parametro_con_valor_defecto("Emilio", "Sánchez Lozano", "Lozi")

# Creo una función a la que pasarle un número indefinido de parámetros

def funcion_con_parametros_indefinidos (*textos):
    print(textos)

# LLamo a la función anterior pasándole un solo parámetro

funcion_con_parametros_indefinidos("Hola")

# LLamo a la función anterior pasándole varios parámetros

funcion_con_parametros_indefinidos("Hola", "Francisco Javier", "Eres Worome?")

