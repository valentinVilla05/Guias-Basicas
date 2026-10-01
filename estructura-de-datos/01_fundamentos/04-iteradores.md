# Iteradores en C++

> Un iterador es un "puntero inteligente" que sirve como puente único para recorrer cualquier contenedor (`vector`, `list`, `set`) exactamente de la misma forma, sin importar cómo guarde la memoria por dentro

## 1. Concepto

Un **iterador** es un objeto que abstrae el comportamiento de un **puntero**. Su objetivo es dar una interfaz unificada para acceder, recorrer y modificar elementos en los contenedores de la STL

```text
┌──────────────┐                 ┌────────────┐
│ Contenedor   │ ── Iterador ──► │ Algoritmo  │
│ (Memory)     │   (Interfaz)    │ (std::find)│
└──────────────┘                 └────────────┘
```
### Definición de un iterador
```cpp
     Contenedor<Tipo> :: TipoIterador   Nombre   =  Valor Inicial;
    └───────────────────────────────┘  └──────┘    └─────────────┘
     std::vector<int> :: iterator       it      =   v.begin();
```
**Partes:**
* `std::vector<int>`: Indica sobre qué contenedor vamos a trabajar:
    * Tipo de dato: `int` (va dentro de `< >`) debe coincidir con el contenedor
* `iterator`: Indicq el tipo de estructura que vamos a usar. Otros Iteradores:
    * `iterator` (Lectura y escritura)
    * `const_iterator` (Solo Lectura)
    * `reverse_iterator` (Inverso de derecha a izquierda)
* `v.begin()`: Asigna la posición inicial (métodos: `.begin()`,`.cbegin()`,`.rbegin()`...)
## El problema:

tendriamos que recorrer cada estructura de datos de forma distinta:

- En `std::vector`: Acceso por índice contiguo en memoria (`v[i]`)
- En `std::list`: Salto de nodo en nodo mediante punteors (`nodo -> siguiente`)
- En `std::set`: Recorrido de nodos en una estructura de árbol

Perderiamos eficacia al tener que rehacer los algorítmos de búsqueda o reordenación para cada tipo de contenedor

## Como se programa un iterador:

Para entender qué hay dentro de un iterador podemos construir lo simplificado para una [`Lista Enlazada`](https://github.com/valentinVilla05/Guias-Basicas/blob/master/estructura-de-datos/02_Estructuras%20Lineales/03-listas-enlazadas.md) (_apartado 3 en estructuras lineales_) . Un iterador es una `clase` o `struct` que guarda la dirección de memoria actual y sobrecarga los operadores estándar de C++ (`_`,`++`,`!=` y `->`) para simular ser un puntero

### Paso 1: Definir la estructura de nodo

```cpp
template <typename T>
struct Nodo {
    T dato;
    Nodo* siguiente;
    Nodo(T val) : dato(val), siguiente(nullptr) {}
};
```

### Paso 2: Crear la clase `Iterador` para una Lista Enlazada

El iterador solo necesita guardar **un puntero al nodo actual** y definir los métodos que el compilador llamará.

```cpp
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
    // 4. Métodos para obtener el principio y el final de una lista enlazada 
    bool fin() { return actual == 0; }
    void siguiente() {actual = actual->sig; }

    // 5. Método para asignar un dato
    T &dato() { return actual->dato; }

};
```
### Otros ejemplos de uso
**Imprimir los datos de una lista de enteros**

```cpp
Iterador<int> i=lista.iterador();
while(!i.fin()){
    cout<<i.dato<<endl;
    i.siguiente();
}
```

**Escribir 0 en todas las posiciones de la lista**
```cpp
Iterador<int> i=lista.iterador();
while(!i.fin()){
    i.dato()=0;
    i.siguiente();
}
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

- `.begin():` Devuelve un iterador apuntando al primer elemento real.

- `.end():` Devuelve un iterador apuntando a la posición inmediatamente posterior al último elemento (past-the-end).

```text
       ┌───────────┬───────────┬───────────┐
       │  Elemento │  Elemento │  Elemento │   [ FIN / Fuera de rango ]
       └───────────┴───────────┴───────────┘
             ▲                                           ▲
             │                                           │
         c.begin()                                    c.end()
```

> Importante:

- La condición de parada del bucle debe ser it!= c.end()
- Nunca se debe usar \*c.end(), porque c.end() no apunta a ningún elemento, sino a la posición que hay justo después del último elemento.

## 3. Operaciones básicas

| Operador        | Acción           | Descripción                                                     |
| --------------- | ---------------- | --------------------------------------------------------------- |
| `*it`           | Dereferenciación | Obtiene la referencia al valor almacenado en la posición actual |
| `it->`          | Acceso a miembro | Accede a un método o atributo del objeto apuntado               |
| `++it`          | Pre-incremento   | Avanza el iterador a la siguiente posición lógica               |
| `it != c.end()` | Comparación      | Comprueba si se ha alcanzado la posición final                  |

## 4. Jerarquía de Categorías

Los iteradores no ofrecen la misma capacidad de acceso en todos los contenedores. Dependiendo de la estructura , la STL clasifica los iteradores en una jerarquía de categorías

| Categoría de Iterador | Operaciones Permitidas                   | Complejidad de Salto | Contenedores                        |
| --------------------- | ---------------------------------------- | -------------------- | ----------------------------------- |
| Forward               | `*it` , `++it`                           | O(n)                 | `std::forward_list`                 |
| Bidirectional         | `*it`, `++it` , `--it`                   | O(n)                 | `std::list`, `std::set`, `std::map` |
| Random Access         | `*it`, `++it`, `--it`, `it + n`, `it[n]` | O(1)                 | `std::vector`, `std::deque`         |

En `std::vector`, `it + 5` es una operación de tiempo constante $O(1)$ porque la **memoria es contigua**. En `std::list`, intentar usar `it + 5` produce un error de compilación, ya que la lista enlazada **requiere avanzar nodo a nodo mediante ++it**

## 5. Variantes de Iteradores

### A. Iteradores Constantes (const iterator)

Garantiza que los datos no se vayan a cambiar durante el recorrido

- Se obtiene con `.cbegin()` y `.cend()`
- Impiden la asignación de nuevos valores a través del operador `*it`

```cpp
std::vector<int> v = {1, 2, 3};

for (std::vector<int>::const_iterator it = v.cbegin(); it != v.cend(); ++it) {
    // *it = 10; // ERROR DE COMPILACIÓN: El iterador es de solo lectura
    std::cout << *it << " ";
}
```

### B. Iteradores Inversos (reverse_iterator)

Invierten el sentido de la iteración (es decir de derecha a izquierda)

- `.rbegin()` apunta al último elemento real.

- `.rend()` apunta a la posición previa al primer elemento

* El operador `++it` desplaza el iterador hacia atrás en el contenedor.

**Representación**
```text
[ Fuera de rango ]    ┌──────────┬──────────┬──────────┐
                      │    10    │    20    │    30    │
                      └──────────┴──────────┴──────────┘
           ▲                                       ▲
           │                                       │
        v.rend()                               v.rbegin()
  (Antes del primero)                      (Último elemento)
```

```cpp
std::vector<int> v = {1, 2, 3};

for (auto it = v.rbegin(); it != v.rend(); ++it) {
    std::cout << *it << " "; // Muestra: 3 2 1
}
```
---
### Fallos Comunes en Iteradores
Un iterador es como una nota con la **dirección de memoria** de un elemneto. Si modificamos la lista mientras la recorremos esa dirección puede **dejar de existir**

**ERROR**
```cpp
for(auto it=v.begin(); it != v.end();++i) // Es un simple bucle que va desde el comienzo al final del vector
    if(*it==5){
        v.erase(it); //Este ya no es válido 
    }
````

**SOLUCIÓN**
```cpp
for(auto it= v.begin();it!=v.end();){ // NO PONEMOS ++i o i++
    if(*it==5){
        it=v.erase(it);
    }else{
        ++it; // Avanzamos solo si no se ha borrado
    }
}
```
---
### Uso de `++it` en lugar de `it++`
* `++it` (**Pre-incremento**): Mueve el iterador y te lo da. Es más rápido y directo
* `it++` (**Post-incremento**): Crea una copia temporal del iterador viejo, avanza al real y devuelve la copia

> En ocasiones que usamos tipos de datos como **int** no pasaría nada usar **it++** pero cuando usamos Templates u otros datos malgastamos mucha memoria en copias

### Funciones útiles: `std::advance` y `std::distance`
A veces queremos avanzar $N$ posiciones o saber la cantidad de leementos entre dos iteradores sin hacer bucles

```cpp
#include <iterator>
std::advance(it,3); // Avanza 3 posiciones hacia delante
int distancia=std::distance(v.begin(),it); // Saber cuantos elementos hay entre inicio y donde estamos
```

## 6. Aritmética de Iteradores (Saltos de memoria)
Al igual que con los punteros normales, con algunos iteradores podemos **sumar o restar números** para saltar varios elementos de golpe sin tener que ir uno con uno con `++`

**Explicación con un ejercicio:**
```text
Vector de ejemplo:   ┌────┬────┬────┬────┬────┐
                     │ 10 │ 20 │ 30 │ 40 │ 50 │
                     └────┴────┴────┴────┴────┘
```
#### **1. Operaciones con Iteradores Normales**
Los saltos se calculan siempre de **izquierda a derecha**

* `v.begin() + N` -> Salta $N$ posiciones a la derecha: 
```text
 ┌────┬────┬────┬────┬────┐
 │ 10 │ 20 │ 30 │ 40 │ 50 │
 └────┴────┴────┴────┴────┘
   ▲              ▲
   │ ─── +3 ────► │
begin()       begin() + 3  ──►  *(begin() + 3) vale 40
```

* `v.end() - N`-> Retrocede $N$ posiciones a la izquierda 
. Empieza desde la casilla que no contiene ningún dato y vuelve hacia atrás

```text
 ┌────┬────┬────┬────┬────┐  [ end() ]
 │ 10 │ 20 │ 30 │ 40 │ 50 │
 └────┴────┴────┴────┴────┘      ▲
                    ▲            │
                    │ ◄── -2 ─── │
                 end() - 2  ──────►  *(end() - 2) vale 40
```
#### **2. En Iteradores Inversos**
* `v.rbegin() + N` -> Salta $N$ posiciones hacia la izquierda 
```text
 ┌────┬────┬────┬────┬────┐
 │ 10 │ 20 │ 30 │ 40 │ 50 │
 └────┴────┴────┴────┴────┘
        ▲              ▲
        │ ◄─── +3 ──── │
   rbegin() + 3     rbegin()  ──►  *(rbegin() + 3) vale 20
```
* `v.rend() - N` -> Retrocede $N$ posiciones hacia la derecha
```text
[ rend() ]    ┌────┬────┬────┬────┬────┐
              │ 10 │ 20 │ 30 │ 40 │ 50 │
              └────┴────┴────┴────┴────┘
     ▲          ▲         ▲
     │ ── -1 ──►│         │
     │ ─────── -3 ───────►│
     │
  v.rend()
```
## Consideraciones 
Las operaciones Aritméticas no se pueden usar en todas las estructuras de datos

* **Si pueden usarlo** (`Random Access`): `std::vector`,`std::array`,`std::deque`. Como sus elementos están **CONTIGUOS** en memoria saltan en tiempo constante

* **No pueden usarlo**: `std::list`, `std::set`, `std::map`: Como están dispersos por la memoria mediante nodos / punteros darán error de compilación. 
    * **Alternativa**: Podemos usar `++i` o usar `std::advance(it,X)` (siendo X el número de posiciones)

## 7. Recomendaciones

- **Uso de Pre-incremento**: Es preferible usar `++i` que `i++` para evitar la creación de copias termporales

- **Uso del Const**: `Debemos usar const_iterator` (`cbegin()` / `cend()`) cuando no vayamos a modificar el contenido del contenedor

- **Gestión de Borrado**: Reasignar el valor devuelto por `erase()` al iterador actual para prevenir fallos por memoria colgada
