# Mallas regulares y Quadtrees

## Mallas Regulares
### Definición
Una **malla regular 2D** divide un plano en una cuadrícula de regiones rectangulares , **Todas del mismo tamaño**

Funciona como una matriz 2D pero permitiendo **acceso directo a la celda/casilla correspondiente mediante una relación matemática

### Operaciones en Mallas Regulares
* **Creación**: Se define una superficie $[x_{\min}, y_{\min}][x_{\max}, y_{\max}]$  y el número de divisiones $n$

* **Recomendación**: Crear la malla con unos márgenes un pelín superiores a los datos que tenemos para evitar desbordamientos en los límites extremos

**Búsqueda**:
1. Calcular el índice de la fija $j$ e columna $i$ matemáticamente a partir de $(p_x, p_y)$
2. Realizar una búsqueda secuencial dentro de la lista interna de esa casilla

**Inserción**:
1. Obtener la casilla correspondiente
2. Añadir el dato al final de la lista de esa casilla

**Borrado**:
1. Obtener la casilla
2. Buscar el elemetno secuencialmente en la lista de la casilla y eliminarlo

**Vecino más cercano**:
1. Identificar la casilla de puntero p
2. Buscar el más cercano dentro de la propia casilla
3. Revisar las 8 casillas vecinas colindantes y quedarse con el menor de los candidatos
4. Si la casilla inicial está vacía, extendder la búsqueda a los siguientes anillos de vecinos

** Búsqueda por rangos $[x1, x2][y1, y2]$:**
1. Localizar las casillas extremas que contienen a $(x1, y1)$ y $(x2, y2)$
2. Recorrer las casillas contenidas dentro de esos límites
3. Devolver los punteros de esas casillas que satisfagan que $x1 < x < x2$ y $y1 < y < y2$.


## Implementación en C+
### Mallas Regulares
```cpp
#include <iostream>
#include <list>
#include <vector>

template<typename T>
class MallaRegular; // Declaración adelantada

template<typename T>
class Casilla {
    std::list<T> puntos;

public:
    friend class MallaRegular<T>;
    Casilla() : puntos() {}

    void insertar(const T &dato) { 
        puntos.push_back(dato); 
    }

    T *buscar(const T &dato);
    bool borrar(const T &dato);
};

template<typename T>
T* Casilla<T>::buscar(const T& dato) {
    typename std::list<T>::iterator it = puntos.begin();
    for (; it != puntos.end(); ++it) {
        if (*it == dato)
            return &(*it);
    }
    return nullptr;
}

template<typename T>
bool Casilla<T>::borrar(const T& dato) {
    typename std::list<T>::iterator it = puntos.begin();
    for (; it != puntos.end(); ++it) {
        if (*it == dato) {
            puntos.erase(it);
            return true;
        }
    }
    return false;
}
```

### Eficiencia de las Mallas Regulares
*   **Caso Óptimo**: Si los datos están uniformemente distribuidos el acceso es inmediato $O(1)$
* **Inconveniente**: No son adaptativas:
    * Si los datos están aglomerados en una zona, algunas casillas tendrán muchísimos puntos (provocando búsquedas secuenciales lentas) mientras que muchas otras quedarán completamente vacías (desperdiciando memoria)