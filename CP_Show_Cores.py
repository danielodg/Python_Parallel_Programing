import os

# Obtiene el número de cores disponibles en el sistema
# Esto incluye tanto los cores físicos como los lógicos (threads de hardware)
num_cores = os.cpu_count()

print(f"Este sistema tiene {num_cores} cores de CPU disponibles.")

# Nota: os.cpu_count() puede retornar None si la información no está disponible
if num_cores is None:
    print("No se pudo determinar el número de cores de CPU.")