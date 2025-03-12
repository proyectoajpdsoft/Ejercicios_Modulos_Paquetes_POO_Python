# Importamos el módulo Persona
from Persona import Persona as Per

# Definimos la clase Tabajador, heredando de la clase Persona
class Trabajador (Per):
    # Definimos el constructor, añadiendo el atributo Cargo
    def __init__(self, Cargo="", DNI="", nombre="", apellidos="", edad=0):
        # Usamos la clase de la que hereda (Persona)
        Per.__init__(self,DNI=DNI, nombre=nombre, apellidos=apellidos, edad=edad)
        # Establecemos el valor del nuevo atributo Cargo
        self.Cargo = Cargo

    # Redefinimos el método __str__ para personalizar el resultado
    def __str__(self):
        return "DNI: {}, Nombre: {}, Apellidos: {}, Edad: {}, Cargo: {}".format(
            self.DNI, self.nombre, self.apellidos, self.edad, self.Cargo)