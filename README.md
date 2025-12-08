# Python_Parallel_Programing

Estos son los ejemplos de la exposición sobre programación paralela en python

# CP_Show_Cores.py

    Descripción: `Un script simple que utiliza la librería os de Python para obtener y mostrar el número de cores de CPU disponibles en el sistema. Es útil para determinar el valor óptimo de max_workers para cargas de trabajo ligadas a la CPU (CPU-bound) en el módulo multiprocessing.`

# CP2_Process_Pool_CP_bound.py

    Descripción: `Demuestra el uso de un ProcessPoolExecutor para paralelizar una tarea intensiva en CPU (CPU-bound): encontrar números primos en un rango grande. Muestra la ganancia de rendimiento (speedup) al dividir el trabajo entre múltiples procesos, uno por core de CPU, superando la limitación del GIL (Global Interpreter Lock) de Python.`

CP4_asyncio_para_io.py

    Descripción: `Ilustra la concurrencia basada en asyncio (programación asíncrona) para tareas ligadas a Entrada/Salida (I/O-bound). Contiene ejemplos que muestran:
        gather() para ejecutar coroutines concurrentemente.
        create_task() para un mayor control de las tareas.
        Uso de aiohttp para realizar múltiples solicitudes HTTP asíncronas, destacando cómo asyncio permite que el programa "espere" por las respuestas de I/O sin bloquear el hilo principal.`
