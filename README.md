![CI Status](https://github.com/jhonnz18/mi-proyecto-automatizacion/actions/workflows/python-app.yml/badge.svg)

# Python Automation & CI/CD Pipeline 🚀
Este proyecto demuestra un flujo de trabajo profesional para el procesamiento de datos, utilizando contenedores y validación automatizada.

## 🛠️ Tecnologías
* **Python 3.9** (Pandas para manipulación de datos)
* **Pytest** (Pruebas unitarias robustas)
* **Docker** (Contenedores para consistencia de entorno)
* **GitHub Actions** (CI/CD Pipeline para despliegue seguro)

## 🏗️ Arquitectura de Calidad
Cada vez que se realiza un `push`, el pipeline de **GitHub Actions**:
1. Levanta un entorno virtual limpio.
2. Instala las dependencias necesarias.
3. Ejecuta la suite de pruebas unitarias con **Pytest**.
4. Valida que la lógica de limpieza de datos (Data Cleaning) sea 100% correcta antes de permitir el despliegue.

## 🚀 Cómo ejecutar localmente
```bash
docker build -t mi-automatizacion .
docker run mi-automatizacioncls