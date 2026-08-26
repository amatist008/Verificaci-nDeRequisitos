# 📚 Sistema de Biblioteca - Optimización y Calidad de Software

Este repositorio contiene el proyecto académico desarrollado para la materia de **Programación Web II / Ingeniería de Requisitos y Calidad de Software**, enfocado en resolver problemas de usabilidad y organización en una biblioteca tradicional.

---

## 🛑 El Problema
En la biblioteca actual, los libros solo se encuentran organizados por código o por orden alfabético estricto. Esto genera los siguientes inconvenientes:
* La búsqueda física de los títulos es lenta y tediosa para los usuarios.
* Los visitantes nuevos dependen casi por completo de la ayuda del bibliotecario.
* Se pierde mucho tiempo recorriendo los estantes y existe una alta probabilidad de reubicar un libro en la sección equivocada.

---

## 💡 Nuestra Solución
Para solucionar el problema de orientación y mejorar la experiencia de búsqueda, implementamos un sistema de **marcado visual por colores según la categoría** de cada libro, facilitando que los usuarios se guíen visualmente dentro de los estantes de forma rápida e intuitiva.

---

## 🧪 Verificación de Calidad (Pruebas Automatizadas)
Siguiendo los estándares de calidad de software vistos en clase (ISO/IEC 25010), se automatizó la verificación de un requisito de rendimiento clave para asegurar que el sistema responda de manera óptima al usuario[cite: 1]:

* **Requisito evaluado (RQ-PERF-LIBRO):** El tiempo de respuesta del sistema al consultar las categorías y catálogos de la biblioteca debe ser **menor o igual a 2 segundos**.
* **Herramientas utilizadas:** Python, `pytest` y `requests`.

### 🚀 ¿Cómo ejecutar la prueba localmente?

1. Clona el repositorio y abre la terminal en la carpeta del proyecto.
2. Crea y activa tu entorno virtual de Python:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate