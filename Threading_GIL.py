import threading
import time


# Ejemplo 1: Thread básico
def worker(name, delay):
    print(f"Thread {name} iniciado")
    time.sleep(delay)
    print(f"Thread {name} terminado")

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(f"T{i}", i+1))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
    
# Ejemplo 2: Race condition y Lock
counter = 0
counter_lock = threading.Lock()
def increment_without_lock():
    global counter
    for _ in range(100000):
        counter += 1
def increment_with_lock():
    global counter
    for _ in range(100000):
       with counter_lock:
            counter += 1

# Sin lock (race condition)

counter = 0
threads = [threading.Thread(target=increment_without_lock) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"Counter sin lock: {counter} (esperado: 1000000)")


# Con lock
counter = 0
threads = [threading.Thread(target=increment_with_lock) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"Counter con lock: {counter}")


# Ejemplo 3: Demostrar el GIL
def cpu_bound_task():
    total = 0
    for i in range(10000000):
        total += i
    return total

# Single thread
start = time.time()
result = cpu_bound_task()
single_time = time.time()- start
print(f"Single thread: {single_time:.2f}s")


# Multiple threads (NO más rápido por el GIL)
start = time.time()
threads = [threading.Thread(target=cpu_bound_task) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()
multi_time = time.time()- start
print(f"Multiple threads: {multi_time:.2f}s")
print(f"Speedup: {single_time/multi_time:.2f}x (esperado ~1x por GIL)")