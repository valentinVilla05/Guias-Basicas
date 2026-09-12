# Introducción a STL: Clases vector, deque y list

Esta lección introduce la **Standar Template Library (STL)** de C++ y analiza tres de sus contenedores secuenciales principales: `std::vector`, `std::deque` y `std::list`

## Parte I: Standard Template Library (STL)
### 1. Conceptos

* **Reutilización** : Todos los compiladores de C++ la incluyen con las estructuras de datos básicas.

* **Calidad**: Ofrece una implementación eficaz y libre de errores

* **Componentes**: Incluye la clase `templates` (plantillas), algoritmos genéricos y contenedores accedidos a través de `iteradores`

### 2. Requisitos de estos contenedores
Se debe implementar **obligatoriamente**:

* **Constructores**: Por `defecto` y `copia`
* **Operador de Asignación:** `operator=`
* **Consulta de tamaño**: `size()` (num de elementos) y `empty` (comprueba si está vacío)

* **Obtención de Iteradores**: `begin()` (apunta al **primer** elemento) y `end` (apunta a la **posición después del último elemento**)

**Representación**:
``` text
begin()                                      end()
     ↓                                           ↓
  ┌──────┬──────┬──────┬──────┬──────┬──────┬─────────┐
  │  10  │  20  │  30  │  40  │  50  │  60  │ (Pasado)│
  └──────┴──────┴──────┴──────┴──────┴──────┴─────────┘
```

### Funcionalidades adicionales de secuencias STL.
También proporcionan:
* **Constructores Rango/Copia**: (`int n, T dato`) (inicia con $n$ copias) y (`iterador i, iterador j`) (copia el rango $[i,j]$)

* **Acceso a Extremos**: `front()` (accede al primer elemento) y `back()` (accede al último elemento)

* **Inserción**: `insert(pos,dato)`, `ìnsert(pos,copias,dato)` e `insert(pos,i,j)`

* **Borrado:** `erase(pos)`, `erase(i,j)` y borrado completo mediante `clear()`

----
### 3. Iteradores STL

Son objetos que actúan como abstracción de punteros para recorrer contenedores

* **Operaciones Básicas**: `operator=`, comparaciones `==` y `!=`, indirección `*it` (para leer / escribir) e incremento/decremento `++` y `--`

* **Comportamiento tras Modificaciones**:
    * Tras un `insert`, el iteraedor devuelvo o posicionado apunta al nuevo elemento insertado 
    * Tras un `erase(it)`, el iterador original queda ^invalidado** y la función devuelve un **nuevo iterador** que apunta al elemento inmediatamente posterior al eliminado  
> Aclaración:
 Cuando llamas a `erase(it)`, el nodo o posición señalada por `it` se destruye inmediatamente, haciendo que ese iterador quede invalidador (apunta a memoria liberada). Para poder continuar recorriendo el contenedor sin romper el programa, `erase` devuelve un nuevo iterador que apunta al elemento que ocupó la posición del elemento borrado (es decir, el inmediatamente posterior).

**Patrón de borrado seguro en bucle**

``` cpp
auto it = contenedor.begin();
while (it != contenedor.end()) {
    if (debeBorrarse(*it)) {
        it = contenedor.erase(it); // 'erase' avanza el iterador automáticamente
    } else {
        ++it; // Solo avanzamos manualmente si NO borramos
    }
}
```

## Parte II: El Contenedor `std::vector`
### 1. Características y Métodos Principales
Es la implementación de un **vector dinámico**
* **Acceso Aleatorio**: Implementa `operator[]` para acceso en $O(1)$ indicando el índice entre `0` y `size()-1`
* **Modificación en Extremos**:
    * `push_back()` : añade un elemento **al final**
    * `pop_back()` : elimina el elemento **del final**
        ```cpp 
        [1, 2, 3]
        push_back(4)  → [1, 2, 3, 4]
        pop_back()    → [1, 2, 3] 
        ```
* **Iteradores del Vector**: Soportan **aceso aleatorio** (aritmética de iteradores como `it+=5` o `it + 10`)

**Aritmética de Iteradores en vector**:

```cpp
#include <vector>
#include <iostream>
using namespace std;

int main() {
    vector<int> v;
    for (int c = 2; c < 100; c++) 
        v.push_back(c);

    // Acceso por posición / índice
    for (size_t c = 0; c < v.size(); c++) 
        cout << v[c] << endl;

    // Acceso mediante iteradores
    for (vector<int>::iterator i = v.begin(); i != v.end(); ++i) 
        cout << *i << endl;

    // Inserciones al principio
    v.insert(v.begin(), 1);
    v.insert(v.begin(), 0);

    // Borrado por iterador (ej. sexto elemento)
    vector<int>::iterator i = v.begin() + 5;
    v.erase(i);
}
```
## Parte III: El Contenedor `std::deque`
### 1. Definición y Estructura Interna

Un `deque` *(Double-Ended Queue)* es una evolución del vector dinámico organizada mediante un **índices de bloques de memoria**

``` text
Índice de Bloques (ibloq)
   ┌───┬───┬───┐
   │ █ │ █ │ █ │
   └───┴───┴───┘
     │   │   └─► [Bloque 3 de datos]
     │   └─────► [Bloque 2 de datos]
     └─────────► [Bloque 1 de datos]
```

* **Operaciones de Extremo en O(1)**: Admite inserciones y borrados eficientes **tanto al principio como en el final** (`push_front()`,` pop_front()`, `push_back()`, `pop_back()`)

* **Acceso Directo**: Mantiene soporte para `operator[]`

* **Limitación:** Insercciones y borrados en posiciones intermedias son **muy ineficientes**

``` cpp
#include <deque>
#include <iostream>
using namespace std;

int main() {
    deque<int> v;
    for (int c = 0; c < 100; c++) {
        v.push_back(c);
        v.push_front(c);
    }

    // Recorrido inverso con iterador
    deque<int>::iterator i = v.end();
    do {
        --i;
        cout << *i << endl;
    } while (i != v.begin());

    // Modificación de elementos
    for (auto it = v.begin(); it != v.end(); ++it) {
        *it = 0;
    }
}
```

## Parte IV: El Contenedor `std::list`
Implementa una *lista doblemente enlazada `sotisficada`
* **Gestión de Memoria Optimizada:** Solicita memoria en bloques de nodos y reutiliza nodos previamente eliminados.

* **Acceso:** **No soporta `operator[]`**. Solo se puede acceder mediante iteradores nodoa nodo , (no admite saltos de la forma `it + n`)

* **Métodos Principales**: Soporta (`push_front()`,` pop_front()`, `push_back()`, `pop_back()`)

``` cpp
#include <list>
#include <iostream>
using namespace std;

int main() {
    list<int> l;
    l.push_back(0);
    l.push_back(1);

    // Generar sucesión de Fibonacci
    auto i1 = l.begin();
    auto i2 = l.begin();
    ++i2;
    for (int c = 2; c <= 100; c++) {
        l.push_back(*i1 + *i2);
        ++i1; 
        ++i2;
    }

    // Borrado correcto de elementos impares durante recorrido
    auto it = l.begin();
    while (it != l.end()) {
        if (*it % 2 != 0) {
            it = l.erase(it); // erase devuelve el iterador al siguiente elemento
        } else {
            ++it;
        }
    }
}
```

## Parte V: Mejoras de C++11 para STL
### 1. Interferencia de Tipos con `auto`
Simplifica la declaración de tipos complejos o largos (como iteradores) deduciendo el tipo a partir de la expresión de asignación

``` cpp
// Antes (C++03):
list<int>::iterator i = l.begin();

// Con C++11:
auto i = l.begin();
```

### 2. Bucles Basados en Rango (Range-based for)
Permite iterar de forma limpia sobre cualquier contenedor que disponga de los métodos `begin()` y `end()`

```cpp
list<int> l = {1, 2, 3, 4, 5};

// Lectura/Modificación por referencia
for (int& elemento : l) {
    cout << elemento << endl;
}
```

## Comparativa de Complejidad Algorítmica y Características
| Contenedor | Acceso Aleatorio `[]` | Inserción/Borrado Incio | Insercción/Borrado Final | Inserción/Borrado Medio| Invalidación de Iteradores |
| ------ | ------- | ------- | -------- | --------- | ---- |
| `std::vector` | $O(1)$ | $O(n)$ | $O(1)$ | $O(n)$ | **Sí**: Al reasignar memoria o tras `insert / erase` (invalida desde la posición modificada)
| `std::deque` | $O(1)$ | $O(1)$ | $O(1)$| Ineficiente $O(n)$ | **Sí**: Insercones o borrados intermedios invalidan todos los iteradores
| `std::list` | No soportado $O(n)$ | $O(1)$ | $O(1)$ | $O(1)$ (con iterador) | **No**: Los iteradores existentes se mantienen válidos (Salvo el del elemento eliminado)