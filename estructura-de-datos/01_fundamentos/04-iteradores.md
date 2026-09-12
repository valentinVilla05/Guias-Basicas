# Iteradores en C++

> Un iterador es un "puntero inteligente" que sirve como puente único para recorrer cualquier contenedor (`vector`, `list`, `set`) exactamente de la misma forma, sin importar cómo guarde la memoria por dentro.


## 1. Concepto

Un **iterador** es un objeto que abstrae el comportamiento de un **puntero**. Su objetivo es dar una interfaz unificada para acceder, recorrer y modificar elementos en los contenedores de la STL.

```text
┌──────────────┐                 ┌────────────┐
│ Contenedor   │ ── Iterador ──► │ Algoritmo  │
│ (Memory)     │   (Interfaz)    │ (std::find)│
└──────────────┘                 └────────────┘
```

## El problema:
tendriamos que recorrer cada estructura de datos de forma distinta:
* En `std::vector`: Acceso por índice contiguo en memoria (`v[i]`)
* En `std::list`: Salto de nodo en nodo mediante punteors (`nodo -> siguiente`)
* En `std::set`: Recorrdio de nodos en una estructura de árbol

Perderiamos eficacia al tener que rehacer los algorítmos de búsqueda o reordenación para cada tipo de contenedor

## Como se programa un iterador:
Para entender qué hay debtri de un iterador podemos construir uo simplificado para una `Lista Enlazada` (*apartado 3 en estructuras lineales*) . Un iterador es una `clase` o `struct` que guarda la dirección de memoria actual y **sobrecarga los operadores estándar de C++ (`*`,`++`,`!=`) para simular ser un puntero

### Paso 1: Definir la estructura de nodo
```cpp
template <typename T>
struct Nodo {
    T dato;
    Nodo* siguiente;
    Nodo(T val) : dato(val), siguiente(nullptr) {}
};
```
### Paso 2: Crear la clase `Iterador`
El iterador solo necesita guardar **un puntero al nodo actual** y definir los métodos que el compilador llamará.
``` cpp
template <typename T>
class IteradorLista {
private:
    Nodo<T>* actual; // La dirección de memoria donde estamos parados

public:
    // Constructor: Recibe la dirección del nodo inicial
    IteradorLista(Nodo<T>* p) : actual(p) {}

    // 1. Sobrecarga del operador * (Dereferenciación)
    // Permite hacer '*it' para LEER o ESCRIBIR el dato del nodo
    T& operator*() {
        return actual->dato;
    }

    // 2. Sobrecarga del operador ++ (Pre-incremento)
    // Permite hacer '++it' para saltar al SIGUIENTE nodo
    IteradorLista& operator++() {
        if (actual != nullptr) {
            actual = actual->siguiente; // Mueve el puntero interno
        }
        return *this;
    }

    // 3. Sobrecarga del operador != (Comparación)
    // Permite hacer 'it != lista.end()' para saber si llegamos al final
    bool operator!=(const IteradorLista& otro) const {
        return actual != otro.actual;
    }
};
```
### Paso 3: Conectar el Iterador con el Contenedor
Nuestra lista implementa los métodos `.begin()` y `.end()` devolviendo instancias de nuestro iterador
```cpp
template <typename T>
class ListaEnlazada {
private:
    Nodo<T>* cabeza;

public:
    ListaEnlazada() : cabeza(nullptr) {}

    // Devuelve un iterador apuntando al primer nodo real
    IteradorLista<T> begin() {
        return IteradorLista<T>(cabeza);
    }

    // Devuelve un iterador apuntando a 'nullptr' (el final de la lista)
    IteradorLista<T> end() {
        return IteradorLista<T>(nullptr);
    }
    
    // ... métodos de inserción (push_front, etc.) ...
};

```
## 2. Los Métodos `begin()` y `end()`
Para delimitar el rango de recorrido, la STL utiliza un esquema de intervalo semiabierto $[begin, end)$:

* `.begin():` Devuelve un iterador apuntando al primer elemento real.

* `.end():` Devuelve un iterador apuntando a la posición inmediatamente posterior al último elemento (past-the-end).

``` text
       ┌───────────┬───────────┬───────────┐
       │  Elemento │  Elemento │  Elemento │   [ FIN / Fuera de rango ]
       └───────────┴───────────┴───────────┘
             ▲                                           ▲
             │                                           │
         c.begin()                                    c.end()
```
> Importante:
* La condición de parada del bucle debe ser it!= c.end()
* Nunca se debe usar *c.end(), porque c.end() no apunta a ningún elemento, sino a la posición que hay justo después del último elemento.

## 3. Operaciones básicas
| Operador | Acción | Descripción |
| --- | --- | --- |
| `*it` | Dereferenciación | Obtiene la referencia al valor almacenado en la posición actual |
| `it->` | Acceso a miembro | Accede a un método o atributo del objeto apuntado |
| `++it` | Pre-incremento | Avanza el iterador a la siguiente posición lógica | 
| `it != c.end()` | Comparación | Comrpueba si se ha alcanzado la posición final |


## 4. Jerarquía de Categorías

Los iteradores no ofrecen la misma capacidad de acceso en todos los contenedores. Dependiendo de la estructura , la STL clasifica los iteradores en una jerarquía de categorías

| Categoría de Iterador | Operaciones Permitidas | Complejidad de Salto | Contenedores |
| -- | -- | -- | -- |
| Forward | `*it` , `++it` | O(n) | `std::forward_list`|
| Bidirectional | `*it`, `++it` , `--it` | O(n) | `std::list`, `std::set`, `std::map` |
| Random Access | `*it`, `++it`, `--it`, `it + n`, `it[n]` | O(1) | `std::vector`, `std::deque` |

En `std::vector`, `it + 5` es una operación de tiempo constante $O(1)$ porque la **memoria es contigua**. En `std::list`, intentar usar `it + 5` produce un error de compilación, ya que la lista enlazada **requiere avanzar nodo a nodo mediante ++it**

## 5. Variantes de Iteradores
### A. Iteradores Constantes (const iterator)
Garantiza que los datos no se vayan a cambiar durante el recorrido
* Se obtiene con `.cbegin()` y `.cend()`
* Imiden la asignación de nuevos valores a través del operador `*it`
``` cpp
std::vector<int> v = {1, 2, 3};

for (std::vector<int>::const_iterator it = v.cbegin(); it != v.cend(); ++it) {
    // *it = 10; // ERROR DE COMPILACIÓN: El iterador es de solo lectura
    std::cout << *it << " ";
}
```
### B. Iteradores Inversos (reverse_iterator)
Invierten el sentido de la iteración

* `.rbegin()` apunta al último elemento real.

* `.rend()` apunta a la posición previa al primer elemento

```cpp
std::vector<int> v = {1, 2, 3};

for (auto it = v.rbegin(); it != v.rend(); ++it) {
    std::cout << *it << " "; // Muestra: 3 2 1
}
```
El operador ++it desplaza el iterador hacia atrás en el contenedor.
## 6. Recomendaciones
* **Uso de Pre-incremento**: Es preferible usar `++i` que `i++` para evitar la creación de copias termporales

* **Uso del Const**: `Debemos usar const_iterator` (`cbegin()` / `cend()`) cuando no vayamos a modificar el contenido del contenedor

* **Gestión de Borrado**: Reasignar el valor devuelto por `erase()` al iterador actual para prevenir fallos por memoria colgada

