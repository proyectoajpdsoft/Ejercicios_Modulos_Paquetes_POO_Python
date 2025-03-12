# Definimos la clase Persona, que no hereda de otras (object)
class Persona (object):
    # Definimos el constructor, creando los atributos en su definición
    def __init__(self, DNI="", nombre="", apellidos="", edad=0):
        self.DNI = DNI
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        
    # Redefinimos el método __str__ para personalizar 
    # los datos devueltos de los atributos de la clase
    def __str__(self):
        return "DNI: {}, Nombre: {}, Apellidos: {}, Edad: {}".format(
            self.DNI, self.nombre, self.apellidos, self.edad)