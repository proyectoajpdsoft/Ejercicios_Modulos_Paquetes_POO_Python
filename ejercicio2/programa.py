# Importamos los módulos Persona y Trabajador
from Persona import Persona as Per
from Trabajador import Trabajador as Trab

# Instanciamos la clase Persona, pasándole unos valores de ejemplo a los atributos
per = Per(DNI="5252525K", nombre="Alonso", apellidos="Proyecto A", edad= 49)
# Mostramos por consola los datos
# al usar "per" sin nada más, se está llamando al método __str__
print("La persona es: ", per)

# Instanciamos la clase Trabajador, pasándole unos valores de ejemplo a los atributos
trab = Trab(DNI="45555555K", nombre="Javier", apellidos="Proyecto A", edad=55, Cargo="Desarrollador")
# Mostramos por consola los datos
# al usar "trab" sin nada más, se está llamando al método __str__
print("El trabajador es: ", trab)