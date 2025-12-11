# Python_Parallel_Programing

Estos son los ejemplos de la exposición sobre programación paralela en python

# Thread_Pool
Este script demuestra la concurrencia basada en hilos (Thread Pool Executor) para optimizar tareas ligadas a Entrada/Salida (I/O-bound), como las descargas web.
Compara la ejecución secuencial de varias solicitudes HTTP con la ejecución concurrente utilizando concurrent.futures.ThreadPoolExecutor,tanto con submit() como con map().

# CP_Show_Cores.py

Descripción: Un script simple que utiliza la librería os de Python para obtener y mostrar el número de cores de CPU disponibles en el sistema. Es útil para determinar el valor óptimo de max_workers para cargas de trabajo ligadas a la CPU (CPU-bound) en el módulo multiprocessing.


# CP2_Process_Pool_CP_bound.py

Descripción: Demuestra el uso de un ProcessPoolExecutor para paralelizar una tarea intensiva en CPU (CPU-bound): encontrar números primos en un rango grande. Muestra la ganancia de rendimiento (speedup) al dividir el trabajo entre múltiples procesos, uno por core de CPU, superando la limitación del GIL (Global Interpreter Lock) de Python.

# Multiprocessing_Pool.py
Este ejemplo ilustra las diversas funcionalidades del módulo estándar de Python multiprocessing

Incluye cuatro ejemplos fundamentales de la librería:

1. *Pool.map()* : Paraleliza la aplicación de una función a una colección de datos de manera simple.

2. *Pool.starmap()*: Permite la aplicación paralela de una función que requiere múltiples argumentos, en este ejemplo para una base y su exponente.

3. *Process individual y Queue*: Demuestra la creación, inicio y finalización manual de procesos separados (Process), y cómo estos procesos se comunican y devuelven resultados utilizando una cola (Queue).

4. *Pool.apply_async()*: Muestra cómo enviar tareas de manera asíncrona a un grupo de procesos,conocido como Pool, permitiendo un control más fino y la obtención de resultados bajo demanda.

# CP4_asyncio_para_io.py

Descripción: Ilustra la concurrencia basada en asyncio (programación asíncrona) para tareas ligadas a Entrada/Salida (I/O-bound). 
Contiene ejemplos que muestran:
        - gather() para ejecutar coroutines concurrentemente.
        - create_task() para un mayor control de las tareas.
        - Uso de aiohttp para realizar múltiples solicitudes HTTP asíncronas, destacando cómo asyncio permite que el programa "espere" por las respuestas de I/O             sin bloquear el hilo principal.

# Threading_GIL.py
Estos tres ejemplos son sobre el modulo estandar threading de python:

*Thread Básico* : 
Demuestra la creación, inicio (t.start()) y espera (t.join()) de múltiples hilos que realizan tareas simples con sleeps simulados.

Condición de Carrera y Lock:
Muestra una condición de carrera (race condition) donde el conteo de una variable global falla cuando varios hilos la modifican simultáneamente sin protección.
Muestra la solución a este problema utilizando un objeto de sincronización threading.Lock (dentro de un with statement) para garantizar la integridad de los datos.

Demostración del GIL:
Compara el tiempo de ejecución de una tarea intensiva en CPU (suma grande) en un hilo único versus múltiples hilos. El resultado demuestra que el tiempo de ejecución es casi idéntico (speedup cercano a 1x), confirmando que el Global Interpreter Lock (GIL) impide el paralelismo real en tareas CPU-bound incluso con threading.
