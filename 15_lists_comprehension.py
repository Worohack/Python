# CReo una lista normal

lista_normal = [12,3,45,561,0]

# A partir de la lista normal, genero una lista comprimida

lista_comprimida = [i for i in lista_normal]
print(lista_comprimida)

# Creo una nueva lista comprimida desde cero

lista_comprimida1 = [i for i in range(5)]
print(lista_comprimida1)

'''
# Creo una nueva lista comprimida desde cero pero haciendo operaciones sobre los elementos que se van
a guardar en ella
'''

lista_comprimida2 = [(i * 7) + 5 for i in range(5)]
print(lista_comprimida2)

'''
# Creo una nueva lista comprimida desde cero pero haciendo operaciones sobre los elementos que se van
a guardar en ella, pero usando una función
'''

def operacion(numero):
    return numero + 7

lista_comprimida3 = [operacion(i) for i in range(5)]
print(lista_comprimida3)
