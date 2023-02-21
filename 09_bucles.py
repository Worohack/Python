# Bucle while

mi_condicion = 0
otro_valor = 10
un_valor_mas = 3
ademad_otro_valor = 1000

while mi_condicion < 10:
    print(mi_condicion)
    mi_condicion += 1
    if mi_condicion == 5:
        print("he llegado a la mitad")
        break
    otro_valor -= 1
    print(otro_valor)
    un_valor_mas *= 2
    print(un_valor_mas)
    ademad_otro_valor /= 10
    print(ademad_otro_valor)

# Bucle For

mi_lista=[12,14,16,18,20]

for elemento in mi_lista:
    print(elemento)

