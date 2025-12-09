from concurrent.futures import ThreadPoolExecutor
import time
import requests
# Función para descargar URL
def download_url(url):
    response = requests.get(url)
    return f"Downloaded {url}: {len(response.content)} bytes"
# Lista de URLs
urls = [
'https://www.google.com/',
'https://httpbin.org/get',
'https://www.wikipedia.org/',
'http://www.python.org',
'http://www.github.com'
]
# Versión secuencial
start = time.time()
for url in urls:
    result = download_url(url)
    print(result)
print(f"Tiempo secuencial: {time.time()- start:.2f}s")

# Versión con ThreadPoolExecutor
start = time.time()
with ThreadPoolExecutor(max_workers=5) as executor:
    # submit() - retorna Future objects
    futures = [executor.submit(download_url, url) for url in urls]
    # Obtener resultados
    for future in futures:
        print(future.result())

print(f"Tiempo con threads: {time.time()- start:.2f}s")

# Alternativa con map()
start = time.time()
with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(download_url, urls)
    for result in results:
        print(result)
print(f"Tiempo con map(): {time.time()- start:.2f}s")