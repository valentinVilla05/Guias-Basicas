# Listas Doblemente Enlazadas, Circulares y Matrices Dispersas
En esta lección se abordan tres estructuras lineales avanzadas: **las listas doblemente enlazadas**, **las listas circulares** y **las matrices dispersas** (implementadas mediante listas de listas).

## Parte I: Listas Doblemente Enlazadas
### 1. Definición
Una lista **doblemente enlazada** es una estructuras de datos secuencial donde cada nodo almacena el elemento de dato y dos punteros: uno al nodo posterior (`sig`) y otro al anterior (`ant`)

```text 
         LISTA DOBLEMENTE ENLAZADA

        ant          dato          sig
         ↓             ↓             ↓
     ┌─────────┬───────────┬─────────┐
     │   NULL  │    45     │  0x2000 │
     └─────────┴───────────┴─────────┘
         ↑                         ↓
         │                         │
     ┌─────────┬───────────┬─────────┐
     │  0x1000 │    12     │  0x3000 │
     └─────────┴───────────┴─────────┘
         ↑                         ↓
         │                         │
     ┌─────────┬───────────┬─────────┐
     │  0x2000 │    89     │  0x4000 │
     └─────────┴───────────┴─────────┘
         ↑                         ↓
         │                         │
     ┌─────────┬───────────┬─────────┐
     │  0x3000 │    33     │  NULL   │
     └─────────┴───────────┴─────────┘
                                   ↑
                                  FIN
```

* **Ventajas claves**
    * Permite **iteración bidireccional**
    * Garantiza tiempo constante $O(1)$ para la inserción y el borrado en cualquier posición (siempre q se tenga referencia o iterador a dicho nodo)

### 2. Estructura del Nodo e Iterador en C++
#### Estructura del Nodo
``` cpp
template <class T>
class Nodo {
public:
    T dato;
    Nodo *ant, *sig;

    Nodo(T &aDato, Nodo *aAnt, Nodo *aSig)
        : dato(aDato), ant(aAnt), sig(aSig) {}
};
```

#### Iterador Bidireccional
``` cpp
template <class T>
class Iterador {
    Nodo<T> *nodo;
    friend class ListaDEnlazada<T>;

public:
    Iterador(Nodo<T> *aNodo) : nodo(aNodo) {}

    bool hayAnterior() { return nodo->ant != 0; }
    bool haySiguiente() { return nodo->sig != 0; }

    void anterior() { nodo = nodo->ant; }
    void siguiente() { nodo = nodo->sig; }

    T& dato() { return nodo->dato; }
};
```

### 3. Operaciones Principales de Inserción y Borrado
``` cpp
// Inserción al principio: O(1)
template <class T>
void ListaDEnlazada<T>::insertarInicio(T &dato) {
    Nodo<T> *nuevo = new Nodo<T>(dato, 0, cabecera);
    if (cola == 0) cola = nuevo;          // Lista previamente vacía
    if (cabecera != 0) cabecera->ant = nuevo;
    cabecera = nuevo;
}

// Inserción en medio (antes del nodo p): O(1)
template <class T>
void ListaDEnlazada<T>::insertar(Iterador<T> &i, T &dato) {
    Nodo<T> *p = i.nodo;
    Nodo<T> *nuevo = new Nodo<T>(dato, p->ant, p);
    if (p->ant != 0) p->ant->sig = nuevo;
    p->ant = nuevo;
}

// Borrado del primer nodo: O(1)
template <class T>
void ListaDEnlazada<T>::borrarInicio() {
    if (cabecera == 0) return;
    Nodo<T> *borrado = cabecera;
    cabecera = cabecera->sig;
    
    if (cabecera != 0) cabecera->ant = 0;
    else cola = 0;                       // La lista quedó vacía
    
    delete borrado;
}
``` 

## Parte 2: Listas Circulares
### Definición y Características
Una lista circular es una variante de lista enlazada (simple o doble) donde el último nodo no apunta a nulo (`0`), sino que su puntero `sig` regresa al primer nodo de la lista

``` text
        LISTA CIRCULAR

       ┌──────────────────────────────────────────────────┐
       │                                                  ▼
 ┌───────────┐     ┌─────────┐     ┌─────────┐     ┌─────────┐
 │   Cola    ├────►│ dato 1  ├────►│ dato 2  ├────►│ dato 3  │
 └───────────┘     └─────────┘     └─────────┘     └─────────┘
                        ▲                               │
                        └───────────────────────────────┘

```

* **Representación en memoria:** Basta con mantener únicamente un puntero al último elemento (`cola`). El primer elemennto se obtiene como: `cola -> sig`
* **Casos de uso típico:**
    * Planifiación de procesos en S.O
    * Representación de figuras geométricas cerradas

## Parte 3: Matrices Dispersas
Una **matriz dispersa** es una matriz de grandes dimensiones $(n \times m)$ en la que la mayoría de sus celdas son 0

Almacenar esta estructura es inefciciente en memoria. La solución óptima es la representación mediante **listas de listas**, guardando exclusivamente las celdas con valores **no** nulos

``` text
                    MATRIZ DISPERSA

              Columna
               0   1   2   3
             ┌───┬───┬───┬───┐
       Fila 0│ 0 │ 5 │ 0 │ 0 │
             ├───┼───┼───┼───┤
             │ 0 │ 0 │ 0 │ 8 │
       Fila 1├───┼───┼───┼───┤
             │ 3 │ 0 │ 0 │ 0 │
       Fila 2├───┼───┼───┼───┤
             │ 0 │ 0 │ 7 │ 0 │
       Fila 3└───┴───┴───┴───┘


        Solo almacenamos los valores ≠ 0

        Memoria
          │
          ▼
     ┌───────────────┐
     │ Fila: 0       │
     │ Col:  1       │
     │ Valor: 5      │
     └───────────────┘
             │
             ▼
     ┌───────────────┐
     │ Fila: 1       │
     │ Col:  3       │
     │ Valor: 8      │
     └───────────────┘
             │
             ▼
     ┌───────────────┐
     │ Fila: 2       │
     │ Col:  0       │
     │ Valor: 3      │
     └───────────────┘
             │
             ▼
     ┌───────────────┐
     │ Fila: 3       │
     │ Col:  2       │
     │ Valor: 7      │
     └───────────────┘

```

### 2. Implementación en C++ (Listas de Listas)

``` cpp
#include <iostream>
// Utiliza una plantilla de ListaEnlazada de forma interna

class ColMatrizDispersa {
public:
    int col;
    float val;
    ColMatrizDispersa(int aCol, float aVal) : col(aCol), val(aVal) {}
};

class FilaMatrizDispersa {
    ListaEnlazada<ColMatrizDispersa> columnas;
    Iterador<ColMatrizDispersa> buscar(int columna);

public:
    int fila;
    FilaMatrizDispersa(int aFila) : fila(aFila), columnas() {}
    float valor(int columna);
    void cambiarValor(int columna, float valor);
};

class MatrizDispersa {
    int maxFilas, maxColumnas;
    ListaEnlazada<FilaMatrizDispersa> filas;
    Iterador<FilaMatrizDispersa> buscar(int fila);

public:
    MatrizDispersa(int filas, int columnas)
        : maxFilas(filas), maxColumnas(columnas) {}

    float valor(int fila, int columna);
    void cambiarValor(int fila, int columna, float valor);
    int getNumFilas() const { return maxFilas; }
    int getNumColumnas() const { return maxColumnas; }
};
```

## Ventajas Y Desventajas
### Listas Doblemente Enlazadas

#### Ventajas
- **Recorrido bidireccional:** Facilita la navegación en ambas direcciones mediante los punteros `sig` y `ant`.
- **Borrado O(1) en cualquier nodo:** Permite eliminar el nodo actual en tiempo constante sin necesidad de recorrer la lista para localizar el nodo previo.

#### Desventajas
- **Mayor consumo de memoria:** Cada nodo requiere dos punteros en lugar de uno.
- **Complejidad de punteros:** Las inserciones y borrados exigen actualizar hasta 4 punteros de forma coordinada.

---

### Listas Circulares

#### Ventajas
- **Sin punteros nulos:** Todo nodo tiene un sucesor válido, simplificando los algoritmos cíclicos.
- **Ahorro de referencia:** Solo requieren el puntero `cola` para acceder tanto al final como al inicio en `O(1)`.

#### Desventajas
- **Riesgo de bucles infinitos:** Si no se gestiona correctamente la condición de parada durante las iteraciones, se pueden producir bucles sin fin.

---

### Matrices Dispersas

#### Ventajas
- **Ahorro masivo de memoria:** Minimiza el espacio requerido al guardar únicamente los valores no nulos.

#### Desventajas
- **Acceso O(n):** El tiempo para consultar o modificar una casilla `M[i][j]` ya no es inmediato `O(1)`, pues requiere realizar búsquedas sobre las listas de filas y columnas.

## Comparativa de Complejidad Algorítmica

| Operación | Listas Dobles | Listas Circulares | Matrices Dispersas |
|---|---|---|---|
| **Acceso por posición** | `O(n)` | `O(n)` | `O(elementos no nulos en fila)` |
| **Inserción / Borrado en Extremos** | `O(1)` | `O(1)` (con puntero `cola`) | `O(búsqueda de posición)` |
| **Inserción / Borrado con Iterador** | `O(1)` | `O(1)` | `O(1)` |
| **Consumo de Memoria** | Alto (`2 punteros / nodo`) | Bajo-Medio (`1–2 punteros / nodo`) | Mínimo en datos dispersos |
