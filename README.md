# Raton En Laberinto

## Descripción
Este proyecto tiene como objetivo aplicar una inteligencia artificial generativa para interpretar imagenes de laberintos en distintos formatos como png o jpg,
esto mediante deteccion de colores dentro de la imagen,  posteriormente formar una matriz de binarios a la cual se le aplicara diferentes metodos de recorrido
para dar solucion al laberinto de la forma mas optima.

## Características

- **Interpretacion de imagenes**: Permite cargue dinamico de imagenes en diferentes formatos y las analiza mediante sus colores.
- **Recorridos de optimizacion**: Conocimientos como recorrido mas corto, amplitud y anchura para solucion de laberintos.
- **Interfaz grafica**: Con el objetivo de ser mas interactivo con los usuarios finales toda su funcionalidad se presenta por medio de una interfaz de usuario.

## Instalación

1. Clona este repositorio: `git clone https://github.com/FreddyOjeda/MouseInMaze.git`
2. Ingresa al directorio: `cd MouseInMaze`
3. Crea entorno Virtual: `python -m venv venv`
4. Activa el entorno: `venv/Scripts/Activate.ps1`
5. Instala las dependencias: `pip install -r requirements.txt`

## Uso

Aquí se muestra cómo utilizar esta maravillosa herramienta:

```python
import mi_modulo

resultado = mi_modulo.funcion_genial(parametro)
print(resultado)
