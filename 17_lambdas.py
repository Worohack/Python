# Creo la lambda

mi_funcion_lambda = lambda valor1, valor2: valor1 * valor2

# Llamo a la lambda

print(mi_funcion_lambda(3,5))

#  CReo una lambda dentro de una función

def suma(valor1):
    
   return lambda producto1, producto2: (producto1 * producto2) + valor1

print(suma(3)(4,5))