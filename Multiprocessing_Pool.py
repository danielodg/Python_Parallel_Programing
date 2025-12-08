from multiprocessing import Pool, Process, Queue, cpu_count
import time
import os

# Ejemplo 1: Pool.map()
def square(x):
   return x * x
if __name__ == '__main__':
    numbers = range(1, 1000)
    # Con Pool.map()
    with Pool(processes=4) as pool:
        results = pool.map(square, numbers)
    print(f"Primeros resultados: {results[:10]}")


# Ejemplo 2: Pool.starmap() - múltiples argumentos
def calculate_power(base, exponent):
    return base ** exponent
if __name__ == '__main__':
    args = [(2, 10), (3, 5), (4, 3), (5, 2)]
    with Pool(processes=4) as pool:
        results = pool.starmap(calculate_power, args)
    print(f"Resultados: {results}")


# Ejemplo 3: Process individual
def worker_function(name, queue):
    print(f"Worker {name} (PID: {os.getpid()}) iniciado")
    result = sum(range(1000000))
    queue.put(result)
    print(f"Worker {name} terminado")

if __name__ == '__main__':
    queue = Queue()
    # Crear procesos
    processes = []
    for i in range(4):
        p = Process(target=worker_function, args=(f"W{i}", queue))
        processes.append(p)
        p.start()
    # Esperar a que terminen
    for p in processes:
        p.join()
    # Obtener resultados
    results = []
    while not queue.empty():
        results.append(queue.get())
    print(f"Resultados: {results}")


# Ejemplo 4: apply_async() para control fino
def heavy_computation(x):
    time.sleep(1)
    return x * x

if __name__ == '__main__':
   with Pool(processes=4) as pool:
        # Enviar tareas asíncronamente
        async_results = [pool.apply_async(heavy_computation, (i,)) for i in range(10)]
        # Obtener resultados cuando estén listos
        results = [ar.get() for ar in async_results]
   print(f"Resultados: {results}")