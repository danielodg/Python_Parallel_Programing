import asyncio
import aiohttp
import time


# -------------------------------------------------
# Ejemplo 1: Coroutine básica
# -------------------------------------------------
async def say_hello(name, delay):
    print(f"Inicio: {name}")
    await asyncio.sleep(delay)
    print(f"Fin: {name}")
    return f"Completed {name}"


async def main_basic():
    # Ejecutar secuencialmente
    await say_hello("Task 1", 2)
    await say_hello("Task 2", 1)


# -------------------------------------------------
# Ejemplo 2: Ejecutar concurrentemente con gather()
# -------------------------------------------------
async def main_concurrent():
    results = await asyncio.gather(
        say_hello("Task 1", 2),
        say_hello("Task 2", 1),
        say_hello("Task 3", 3)
    )
    print(f"Resultados: {results}")


# -------------------------------------------------
# Ejemplo 3: create_task() para más control
# -------------------------------------------------
async def main_with_tasks():
    task1 = asyncio.create_task(say_hello("Task 1", 2))
    task2 = asyncio.create_task(say_hello("Task 2", 1))
    task3 = asyncio.create_task(say_hello("Task 3", 3))

    # Esperar todos
    await task1
    await task2
    await task3


# -------------------------------------------------
# Ejemplo 4: HTTP requests asíncronos
# -------------------------------------------------
async def fetch_url(session, url):
    async with session.get(url) as response:
        content = await response.text()
        return f"Downloaded {url}: {len(content)} bytes"


async def main_http():
    urls = [
        "https://httpbin.org/get",
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://api.github.com"
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

        for result in results:
            print(result)


# -------------------------------------------------
# Ejemplo 5: as_completed() - procesar a medida que terminan
# -------------------------------------------------
async def main_as_completed():
    tasks = [say_hello(f"Task {i}", i) for i in range(1, 5)]
    for coro in asyncio.as_completed(tasks):
        result = await coro
        print(f"Completado: {result}")


# -------------------------------------------------
# EJECUCIÓN
# -------------------------------------------------
if __name__ == "__main__":

    print("\n--- Ejemplo 1: Básico ---")
    asyncio.run(main_basic())

    print("\n--- Ejemplo 2: Concurrente (gather) ---")
    asyncio.run(main_concurrent())

    print("\n--- Ejemplo 3: create_task ---")
    asyncio.run(main_with_tasks())

    print("\n--- Ejemplo 4: HTTP asíncrono ---")
    start_sync = time.time()
    # Aquí va la versión síncrona si la quieres implementar
    print(f"Tiempo síncrono: {time.time() - start_sync:.2f}s")

    start_async = time.time()
    asyncio.run(main_http())
    print(f"Tiempo asíncrono: {time.time() - start_async:.2f}s")

    print("\n--- Ejemplo 5: as_completed ---")
    asyncio.run(main_as_completed())
