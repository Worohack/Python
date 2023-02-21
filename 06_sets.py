# Creo un set

mi_set = set()
mi_otro_set ={}

print(type(mi_set))
print(type(mi_otro_set))

# Asigno valores al set

mi_otro_set = {"Carmen", "José", 2, "Javier", "Jose Antonio", "Riofrío, 6"}

print(mi_otro_set)

# Añado un elemento

mi_otro_set.add("Familia")
print(mi_otro_set)

# Compruebo si un eemento dado existe en el set

print("Riofrío, 6" in mi_otro_set)

# Elimino el elemento 2

mi_otro_set.remove(2)
print(mi_otro_set)

# Uno dos sets de dos formas distintas pero usando "union" 
mi_set = {"C#", "Java", "Visual Basic"}
print(mi_set)
print(mi_otro_set)
nuevo_set = mi_otro_set.union(mi_set)
print(nuevo_set)
nuevo_set = nuevo_set.union({10, 8})
print(nuevo_set)

otro_set = {"vacío", "lleno", "glp", "gasoil"}
otro_set_mas = {"vacío", "lleno", "glp", "gasolina"}
print(otro_set.difference(otro_set_mas))