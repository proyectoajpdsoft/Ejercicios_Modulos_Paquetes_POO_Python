# Para obtener hora actual
import datetime as fechas
# Para obtener ruta y versión del ejecutable de Python
import sys
import os.path

# Obtener la hora, minuto y segundo y mostrar por pantalla
# en formato HH:MM:SS
hora = fechas.datetime.now().hour
minuto = fechas.datetime.now().minute
segundo = fechas.datetime.now().second
print(f"La hora actual es: {hora}:{minuto}:{segundo}")

# Mostrar por pantalla la ruta del ejecutable de Python
ruta = os.path.realpath(sys.executable)
print("La ruta del ejecutable de Python es: ", ruta)

# Mostrar por pantalla la versión de Python actual
print("La versión de Python es: ", sys.version)