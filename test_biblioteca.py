import time
import requests
import pytest


URL = "https://jsonplaceholder.typicode.com/posts" #JSONPlaceholder (Una API clásica de prueba para desarrollo)

def test_tiempo_respuesta_categorias_biblioteca():
    """RQ-PERF-LIBRO: El sistema de categorías por colores debe responder rápido."""
    inicio = time.perf_counter()
    
    # Hacemos la petición a la API con un límite de espera de 5 segundos
    resp = requests.get(URL, timeout=5)
    
    duracion = time.perf_counter() - inicio
    
    # Verificamos que la petición sea exitosa (código 200)
    assert resp.status_code == 200, f"Error: El servidor respondió con estado {resp.status_code}"
    
    # Verificamos el requisito de calidad: debe responder en 2 segundos o menos
    assert duracion <= 2.0, (
        f"Excede el límite de calidad: La consulta tardó {duracion:.2f}s (Máximo permitido: 2s)"
    )