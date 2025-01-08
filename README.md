# Proyecto de Figuras Geométricas
Este proyecto implementa varias clases para representar y manipular diferentes figuras geométricas como puntos, líneas, triángulos, rectángulos y cuadrados. Las clases están organizadas en dos paquetes principales: shape_01 y shape_02.

## Estructura del Proyecto
```bash
main_shape_01.py
main_shape_02.py
reto_05/
    __init__.py
    shape_01/
        __init__.py
        shape_01.py
    shape_02/
        __init__.py
        line.py
        point.py
        rectangle.py
        shape_02.py
        triangle.py
```
# Paquete shape_01:

## Módulo shape_01 
* `Point:` Representa un punto en el espacio 2D.
* `Rectangle:` Representa un rectángulo.
* `Square:` Representa un cuadrado.
* `Triangle:` Representa un triángulo.
* `Equilateral:` Representa un triángulo equilátero.
* `Isosceles:` Representa un triángulo isósceles.
* `Scalene:` Representa un triángulo escaleno.
* `TriRectangle:` Representa un triángulo rectángulo.

# Paquete shape_02:

## Módulo line
* `Line:` Representa una línea definida por dos puntos.

## Módulo point
* `Point:` Representa un punto en el espacio 2D.

## Módulo rectangle: 
* `Rectangle:` Representa un rectángulo.
* `Square:` Representa un cuadrado.

## Módulo shape_02
* `Shape:` Clase base para todas las figuras geométricas.

##  Módulo triangle 
* `Triangle:` Representa un triángulo.
* `Equilateral:` Representa un triángulo equilátero.
* `Isosceles:` Representa un triángulo isósceles.
* `Scalene:` Representa un triángulo escaleno.
* `TriRectangle:` Representa un triángulo rectángulo.

## Importación en main_shape_01
* En main_shape_01.py, se importan todas las clases directamente desde el módulo shape_01.py dentro del paquete shape_01. Esto significa que las clases no heredan de una clase base común dentro del paquete shape_01.

```python 
from reto_05.shape_01.shape_01 import *
```
Esta importación trae todas las clases definidas en shape_01.py (como Point, Line, Rectangle, Square, Triangle, Equilateral, Isosceles, Scalene, TriRectangle) al espacio de nombres de main_shape_01.py.

## Importación de main_shape_02
* En main_shape_02.py, se importan las clases desde varios módulos individuales dentro del paquete shape_02. Cada una de estas clases hereda de la clase base Shape definida en shape_02.py.

```python
from reto_05.shape_02.triangle import Triangle, Equilateral, Isosceles, Scalene, TriRectangle
from reto_05.shape_02.rectangle import Rectangle, Square
from reto_05.shape_02.point import Point
```
Estas importaciones traen las clases Triangle, Equilateral, Isosceles, Scalene, TriRectangle desde triangle.py, Rectangle y Square desde rectangle.py, y Point desde point.py al espacio de nombres de main_shape_02.py. Todas estas clases heredan de Shape, lo que proporciona una estructura común y métodos compartidos.
