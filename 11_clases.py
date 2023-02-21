# Defino una clase vacía. Al estar sin código, para que no de error, escribo el comando pass

class PersonaVacia:
    pass

# Defino otra clase con propiedades:
class Persona:
    def __init__(self):

        # Hago privada la propiedad p_nombre

        self.__p_nombre = ""
        self.p_apellidos = ""
        self.p_edad = ""
        self.p_domicilio = ""
        self.p_telefono = ""
        self.p_nif = ""
    
    def imprime_datos(self):
        print(f"{self.p_nombre} {self.p_apellidos} {self.p_nif}")

    # CReo la función que devolverá el valor de la propiedad p_nombre

    def get_nombre(self):
        return self.__p_nombre
    def set_nombre(el_nombre):
        self.__p_nombre = el_nombre

# Creo un objeto a partir de la clase Persona

mi_objeto = Persona()
mi_objeto.p_domicilio = "Calafate"
print(mi_objeto.p_domicilio)
print(mi_objeto.p_nif)
print(mi_objeto.get_nombre())
mi_objeto.p_nombre = "1 Javier"
mi_objeto.p_apellidos="Muñoz"
mi_objeto.p_nif = "27458298J"
# print(mi_objeto.p_nombre)
# mi_objeto.set_nombre("Fernando")
print(mi_objeto.get_nombre())

# Llamo a la función definida en la clase

mi_objeto.imprime_datos()
