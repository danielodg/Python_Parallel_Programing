from concurrent.futures import ProcessPoolExecutor
import time
from multiprocessing import cpu_count


# ----------------------------------------
# Función CPU-intensive
# ----------------------------------------
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes_in_range(start, end):
    primes = []
    for n in range(start, end):
        if is_prime(n):
            primes.append(n)
    return primes


# Wrapper(envoltorio) para evitar usar lambda
def run_range(r): #! r es una tupla (start, end)
    return find_primes_in_range(r[0], r[1])


# ----------------------------------------
# Protección obligatoria en Windows/Linux 
# garantizando que el codigo de subprocesos no se ejecute al importar sino solo al ejecutar el script directamente
# ----------------------------------------
if __name__ == "__main__": 

    RANGE_END = 100000

    # Secuencial
    start_seq = time.time()
    result = find_primes_in_range(1, RANGE_END)
    time_seq = time.time() - start_seq

    print(f"Encontrados {len(result)} primos")
    print(f"Tiempo secuencial: {time_seq:.2f}s")

    # Paralelo
    start_parallel = time.time()

    cores = cpu_count()
    chunk_size = RANGE_END // cores

    # Crear lista de tuplas (start, end) para cada proceso
    starts = list(range(1, RANGE_END, chunk_size))
    ranges = [(i, min(i + chunk_size, RANGE_END)) for i in starts]



    with ProcessPoolExecutor(max_workers=cores) as executor:
        results = executor.map(run_range, ranges)
        #results es un iterador de listas de primos devueltas por cada proceso
    

    all_primes = []
    for r in results:
        all_primes.extend(r)

    time_parallel = time.time() - start_parallel

    print(f"Encontrados {len(all_primes)} primos")
    print(f"Tiempo con procesos: {time_parallel:.2f}s")
    print(f"Speedup: {(time_seq / time_parallel):.2f}x")  #Aceleracion(MR) = Tiempo secuencial / Tiempo paralelo