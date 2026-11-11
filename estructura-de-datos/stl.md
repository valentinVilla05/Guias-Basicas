# STL de C++ 

> Explicaciones sobre algunas de las funciones más importantes sobre las stl para el examen
> Referencia: [cplusplus.com/reference/stl/](https://cplusplus.com/reference/stl/)

---

## Índice

1. [¿Qué es y de qué se compone?](#1-qué-es-y-de-qué-se-compone)
2. [Métodos comunes a (casi) todos los contenedores](#2-métodos-comunes-a-casi-todos-los-contenedores)
3. [Contenedores secuenciales](#3-contenedores-secuenciales)
4. [Adaptadores de contenedor](#4-adaptadores-de-contenedor)
5. [Contenedores asociativos (ordenados por clave)](#5-contenedores-asociativos-ordenados-por-clave)
6. [Contenedores no ordenados (hash)](#6-contenedores-no-ordenados-hash)
7. [Iteradores: el pegamento de la STL](#7-iteradores-el-pegamento-de-la-stl)
8. [Algoritmos básicos (\<algorithm\>)](#8-algoritmos-básicos-algorithm)
9. [Tabla de retornos: qué devuelve cada operación](#9-tabla-de-retornos-qué-devuelve-cada-operación)
10. [Detalles importantes para el examen](#10-detalles-importantes-para-el-examen)
11. [¿Qué contenedor elijo?](#11-qué-contenedor-elijo)

---

## 1. ¿Qué es y de qué se compone?

La STL es una biblioteca de plantillas reutilizable que trae todo compilador C++. Se compone de tres pilares:

* **Contenedores** (`containers`): guardan objetos (`vector`, `list`, `map`...).
* **Iteradores** (`iteradores`): "punteros genéricos" que recorren los contenedores (`begin()`, `end()`).
* **Algoritmos** (`algorithms`): funciones genéricas (`sort`, `find`, `copy`...) que trabajan sobre
  rangos de iteradores `[inicio, fin)`.

### 1.1 Cabeceras de contenedor

| Cabecera | Contenedores que trae |
| -- | -- |
| `<array>` | `array` (estático, tamaño fijo) |
| `<vector>` | `vector` |
| `<deque>` | `deque` |
| `<list>` | `list` |
| `<forward_list>` | `forward_list` (C++11) |
| `<stack>` | `stack` |
| `<queue>` | `queue`, `priority_queue` |
| `<set>` | `set`, `multiset` |
| `<map>` | `map`, `multimap` |
| `<unordered_set>` | `unordered_set`, `unordered_multiset` (C++11) |
| `<unordered_map>` | `unordered_map`, `unordered_multimap` (C++11) |

> **Ojo:** `sort()` y compañía viven en `<algorithm>`, **no** en las cabeceras de contenedor.
> `pair` vive en `<utility>` (se incluye automáticamente con `<map>`).

### 1.2 Clasificación de contenedores

* **Secuenciales** — guardan los elementos en el orden en que se insertan:
  `array`, `vector`, `deque`, `list`, `forward_list`.
* **Adaptadores** — envuelven otro contenedor y limitan su interfaz:
  `stack`, `queue`, `priority_queue`.
* **Asociativos** — ordenados por clave, búsqueda $\mathcal{O}(\log n)$:
  `set`, `multiset`, `map`, `multimap`.
* **No ordenados (unordered)** — con tabla hash, búsqueda promedio $\mathcal{O}(1)$:
  `unordered_set`, `unordered_map` y sus versiones *multi*.

---

## 2. Métodos comunes a (casi) todos los contenedores

| Método | Descripción | Retorna |
| -- | -- | -- |
| `empty()` | Comprueba si está vacío | `bool` |
| `size()` | Número de elementos | `size_type` (entero sin signo) |
| `max_size()` | Máximo número de elementos que puede guardar | `size_type` |
| `clear()` | Borra **todos** los elementos | `void` |
| `begin()` / `end()` | Iterador al primer elemento / al **después del último** | iterador |
| `cbegin()` / `cend()` | Igual pero con iteradores **constantes** (solo lectura) | `const_iterator` |
| `rbegin()` / `rend()` | Iterador inverso: recorre desde el último al primero | iterador inverso |
| `erase(...)` | Borra elementos | **iterador al siguiente al borrado** |
| `swap(c2)` | Intercambia todo el contenido con `c2` | `void` |
| `operator=` | Copia o mueve el contenido | `*this` |
| `emplace(...)` | **Construye** el elemento in situ (C++11) | `iterator` al nuevo elemento |
| `insert(...)` | Inserta una copia del elemento | `iterator` (varía según contenedor) |

### 2.1 Detalle importante: `erase` devuelve un iterador

```cpp
for (auto it = v.begin(); it != v.end(); ) {
    if (*it % 2 == 0)
        it = v.erase(it);   // hay que REASIGNAR el iterador
    else
        ++it;
}
```

* Si se ignora el valor de retorno (`v.erase(it); ++it;`), el comportamiento es **indefinido**
  (el iterador apunta a memoria ya liberada).
* `erase` devuelve **el iterador que apuntaba al elemento siguiente** al borrado.
* También se puede borrar un rango: `erase(inicio, fin)` borra `[inicio, fin)`
  (el elemento apuntado por `fin` **no** se borra).

---

## 3. Contenedores secuenciales

### 3.1 `vector<T>` — arreglo dinámico

**Internamente:** memoria **contigua**, como un array pero que crece solo.

| Método | Retorna | Notas |
| -- | -- | -- |
| `push_back(x)` | `void` | Añade al final. Coste amortizado $\mathcal{O}(1)$ |
| `pop_back()` | `void` | Quita el último. **No devuelve nada** |
| `v[i]` | `T&` | **No comprueba límites** (más rápido) |
| `v.at(i)` | `T&` | Lanza `std::out_of_range` si `i >= size()` |
| `front()` / `back()` | `T&` | Primer / último elemento |
| `data()` | `T*` | Puntero a la memoria contigua |
| `reserve(n)` | `void` | Reserva memoria para `n` elementos (**no cambia `size()`**) |
| `capacity()` | `size_type` | Cuántos elementos caben sin reservar más memoria |
| `resize(n)` | `void` | Cambia el **tamaño** (rellena con `T()` o trunca) |
| `clear()` | `void` | `size() = 0`, pero **`capacity()` no baja** |
| `insert(pos, x)` | `iterator` | Inserta antes de `pos`; desplaza a la derecha, $\mathcal{O}(n)$ |
| `erase(pos)` | `iterator` | Borra y devuelve el siguiente |

**Aspectos a tener en cuenta:**

* `size()` devuelve un tipo **sin signo**; en C++ conviene usar `size_t` o iteradores en los bucles.
* `push_back` es $\mathcal{O}(1)$ **amortizado**: al llenarse, el vector duplica su capacidad;
  copiar cuesta $\mathcal{O}(n)$, pero el promedio por inserción es constante.
* `reserve(n)` **no** hace que `size()` valga `n`; `resize(n)` sí.
* Para pasar un vector a una función: `const vector<T>& v` (solo lectura) o `vector<T>& v` (modificar).
* `vector<bool>` es una **especialización rara**: guarda bits, no `bool` contiguos
  (por eso no existe `data()` y `operator[]` no devuelve `bool&`).
* Inicialización típica: `vector<int> v(5, 0);` → cinco ceros · `vector<int> v{1,2,3};` → tres valores.

### 3.2 `deque<T>` — doble cola

Similar a `vector`, pero **no** usa memoria contigua: es una cola de bloques (*chunks*). Por eso:

* `push_front(x)` y `pop_front()` también son $\mathcal{O}(1)$ (en `vector` **no existen**).
* `push_back` / `pop_back` → $\mathcal{O}(1)$.
* Acceso aleatorio `v[i]` y `v.at(i)` → $\mathcal{O}(1)$ (un poco más lento que en `vector`
  por la doble indirección).
* `insert` / `erase` en medio → $\mathcal{O}(n)$.

### 3.3 `list<T>` — lista doblemente enlazada

Cada elemento guarda puntero al anterior y al siguiente, por lo que **insertar y borrar en
cualquier sitio cuesta $\mathcal{O}(1)$** si ya se tiene el iterador.

| Método | Retorna | Notas |
| -- | -- | -- |
| `push_front(x)` / `push_back(x)` | `void` | Ambos $\mathcal{O}(1)$ |
| `pop_front()` / `pop_back()` | `void` | $\mathcal{O}(1)$ |
| `insert(pos, x)` | `iterator` al insertado | **No desplaza nada** → $\mathcal{O}(1)$ |
| `erase(pos)` | `iterator` al siguiente | $\mathcal{O}(1)$ |
| `remove(x)` | `size_type` | Borra **todos** los que valen `x` y devuelve cuántos |
| `remove_if(pred)` | `size_type` | Borra los que cumplen el predicado |
| `sort()` | `void` | **Tiene método propio** (merge sort, $\mathcal{O}(n \log n)$) |
| `unique()` | `void` | Elimina los consecutivos iguales (para no consecutivos, ordenar antes) |
| `merge(lista2)` | `void` | Fusiona `lista2` en `*this`; ambas deben estar **ordenadas** |
| `reverse()` | `void` | Invierte la lista, $\mathcal{O}(n)$ |
| `splice(pos, lista2)` | `void` | **Mueve** nodos de `lista2` a `*this` sin copiarlos → $\mathcal{O}(1)$ |
| `front()` / `back()` | `T&` | No tiene `operator[]` (no hay acceso aleatorio) |

**Aspectos a tener en cuenta:**

* No existe `v[i]` ni `v.at(i)`: solo se recorre con iteradores.
* `list::sort()` es **estable** y no necesita acceso aleatorio; en cambio
  `std::sort(v.begin(), v.end())` **no compila** con `list`.
* `splice` traslada **nodos**, no copia elementos → coste constante.

### 3.4 `forward_list<T>` — lista simplemente enlazada

Solo guarda puntero al **siguiente**, así que:

* Usa menos memoria, pero **no tiene `size()`** (costaría $\mathcal{O}(n)$), ni `back()`, ni `pop_back()`.
* No tiene `insert` / `erase` normales: usa **`insert_after(pos, x)`** y **`erase_after(pos)`**,
  porque no se puede insertar *antes* de un nodo si solo se conoce el siguiente.
* `push_front`, `pop_front` y `front` sí existen.
* `before_begin()` devuelve un iterador "falso" anterior al primero, útil para `insert_after`.

### 3.5 `array<T, N>` — array estático (C++11)

* Tamaño **fijo en tiempo de compilación**: `array<int, 5> a;`
* Se guarda **en la pila** (*stack*), no en el *heap*: más rápido, pero no puede crecer.
* Dispone de `a[i]`, `a.at(i)`, `a.front()`, `a.back()`, `a.data()`, `a.size()`, `a.fill(x)`.
* **No tiene** `push_back`, `pop_back`, `insert`, `erase` ni `reserve`.
* Se puede inicializar con `= {1,2,3}` y, a diferencia del array C (`int a[5]`), **sí se puede
  copiar** con `=` y pasar a funciones.
* Al ser contiguo, `std::sort(a.begin(), a.end())` funciona perfectamente.

### 3.6 Tabla resumen de complejidades

| Operación | `array` | `vector` | `deque` | `list` | `forward_list` |
| -- | -- | -- | -- | -- | -- |
| Acceso `v[i]` | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | No existe | No existe |
| Insertar / borrar al **final** | No existe | $\mathcal{O}(1)$* | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | No existe |
| Insertar / borrar al **principio** | No existe | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |
| Insertar / borrar **en medio** (con iterador) | No existe | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |
| Recorrer entero | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ |
| `size()` | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | No existe ($\mathcal{O}(n)$) |

\* Coste amortizado.

---

## 4. Adaptadores de contenedor

No son contenedores propiamente dichos: **envuelven** otro (por defecto `deque` para `stack` y
`queue`, y `vector` para `priority_queue`) y solo exponen una interfaz reducida. Por eso
**no tienen iteradores** ni `begin()` / `end()`.

### 4.1 `stack<T>` — LIFO (pila)

```cpp
stack<int> s;
s.push(10);      // void
s.top();         // T&  → referencia al tope
s.pop();         // void → NO devuelve el valor; hay que leer top() antes
s.empty();       // bool
s.size();        // size_type
```

* **Detalle clave:** `pop()` es `void`. Para "sacar y devolver" hay que hacer
  `int x = s.top(); s.pop();`.
* Sin `begin()` / `end()` y sin `clear()` (hay que vaciar con un bucle de `pop()`).
* Costes: `push`, `pop`, `top`, `empty`, `size` → todos $\mathcal{O}(1)$.

### 4.2 `queue<T>` — FIFO (cola)

```cpp
queue<int> q;
q.push(10);      // void → al final
q.front();       // T& → primero en salir
q.back();        // T& → último en entrar
q.pop();         // void → quita el PRIMERO (no el último)
q.empty(); q.size();
```

* **Trampa clásica:** en `queue`, `pop()` quita el **`front`** (lo primero que se puso);
  en `stack` quita el tope.
* Costes: todos $\mathcal{O}(1)$.

### 4.3 `priority_queue<T>` — cola de prioridad (heap binario)

```cpp
priority_queue<int> pq;              // por defecto: el MÁXIMO arriba (max-heap)
pq.push(5); pq.top();                // T& → el elemento de mayor prioridad
pq.pop();                            // void → extrae el máximo
pq.empty(); pq.size();

// min-heap:
priority_queue<int, vector<int>, greater<int>> minPQ;
```

* **No es una cola ordenada:** solo garantiza que `top()` es el de mayor prioridad;
  el resto está desordenado (es un heap).
* No tiene iteradores.
* Costes: `push` y `pop` → $\mathcal{O}(\log n)$; `top` → $\mathcal{O}(1)$.
* Para usar structs hay que sobrecargar `operator<` o pasar un comparador personalizado.

---

## 5. Contenedores asociativos (ordenados por clave)

Cabeceras: `<set>` y `<map>`. Internamente suelen ser **árboles rojo-negro**,
por lo que todo está ordenado y los costes son logarítmicos.

### 5.1 `set<T>` / `multiset<T>`

```cpp
set<int> s = {5, 1, 3, 1};   // = {1, 3, 5}  → NO admite duplicados
s.insert(2);                 // pair<iterator,bool> → bool = si realmente se insertó
s.count(3);                  // 1 si existe, 0 si no  (en multiset: nº de repeticiones)
s.find(3);                   // ITERADOR al elemento, o s.end() si NO existe
s.erase(3);                  // size_type → nº de elementos borrados
s.empty(); s.size(); s.clear();
s.lower_bound(3);            // primer elemento >= 3
s.upper_bound(3);            // primer elemento > 3

// Existencia:  count(10) == 0   equivale a   find(10) == s.end()
```

**Aspectos a tener en cuenta:**

* `insert` en `set` devuelve **`pair<iterator, bool>`**: el `bool` indica si se insertó (`true`)
  o si la clave ya existía (`false`). En `multiset` devuelve solo `iterator` (siempre inserta).
* `find` devuelve un **iterador**, no un `bool`. Para comprobar existencia:
  `s.find(x) != s.end()`.
* `count` en `set` / `map` cuesta $\mathcal{O}(\log n)$ pero **solo devuelve 0 o 1**;
  sirve como consultas de "¿existe?".
* `lower_bound` y `upper_bound` devuelven **iteradores**; si no hay candidatos, devuelven `end()`.
  * `lower_bound(x)` → primer elemento **≥ x**.
  * `upper_bound(x)` → primer elemento **> x**.
  * Elementos iguales a `x`: `upper_bound(x) - lower_bound(x)` (también vale `count(x)`).
* `set` **no permite** modificar los elementos (son claves): `*it = 10;` no compila.
* El orden por defecto es ascendente; se cambia con `set<int, greater<int>> s;`.

### 5.2 `map<K,V>` / `multimap<K,V>`

```cpp
map<string,int> m;
m["ana"] = 20;               // inserta o crea
m.insert({"luis", 15});      // pair<iterator,bool>
m.emplace("eva", 12);        // construye el pair in situ
m.at("ana");                 // int& → lanza out_of_range si no existe
m.find("ana");               // iterator (m->second da el valor)
m.count("ana");              // 0 o 1
m.erase("ana");              // size_type
m.lower_bound("b");          // primer elemento con clave >= "b"
```

**La trampa más importante: `m["clave"]`**

* `m[k]` **inserta** la clave `k` con valor por defecto (`V()`) si no existía → tiene
  **efectos secundarios**.
* `m.at(k)` **lanza excepción** `std::out_of_range` si no existe.
* Por eso, para **consultar** sin modificar nada, conviene `find()` o `at()`; el `[]`
  se reserva para inserción o modificación.

```cpp
if (m.find("luis") != m.end()) { /* existe */ }   // consultar
m["luis"] += 1;                                    // crear / modificar
int v = m.at("luis");                              // consultar (excepción si falta)
```

* `map` está **ordenado por clave** → recorrerlo con un iterador da las claves en orden.
* Recorrido típico: `for (auto& p : m) cout << p.first << " = " << p.second;`
* `multimap` permite claves repetidas: `insert` devuelve solo `iterator`, `count` puede ser
  mayor que 1 y `erase(k)` borra **todas** las repeticiones.
* `multimap` **no tiene** `operator[]` (sería ambiguo con claves repetidas).

---

## 6. Contenedores no ordenados (hash)

Cabeceras: `<unordered_set>` y `<unordered_map>`. Internamente usan **tablas de hash**.

| | Asociativos (`set` / `map`) | Unordered (`unordered_set` / `unordered_map`) |
| -- | -- | -- |
| Orden | Sí, siempre ordenados | **No**, ningún orden |
| Búsqueda | $\mathcal{O}(\log n)$ | $\mathcal{O}(1)$ **promedio**, $\mathcal{O}(n)$ peor caso |
| Estructura interna | Árbol rojo-negro | Tabla hash |

* Ofrecen las mismas operaciones básicas: `insert`, `find`, `count`, `erase`,
  además de `bucket_count` y `load_factor`.
* **No tienen** `lower_bound` / `upper_bound` (no existe orden).
* `unordered_map` **sí** tiene `operator[]` (con el mismo efecto de insertar si falta).
* `erase` cuesta $\mathcal{O}(1)$ promedio, frente a $\mathcal{O}(\log n)$ en `map`.
* Se usan cuando **no hace falta orden** y se quiere buscar más rápido.

---

## 7. Iteradores: el pegamento de la STL

* `begin()` apunta al **primer** elemento; `end()` apunta a la posición **después del último**
  (por eso el bucle usa `it != end()` y nunca `<=`).
* Tipos: `iterator` (lee y escribe), `const_iterator` (solo lee), `reverse_iterator`
  (recorre al revés).
* Categorías: *input*, *output*, *forward*, *bidirectional* (`list`, `set`, `map`),
  *random access* (`vector`, `deque`, `array`).
  * Solo los *random access* permiten `it + 5`, `v[i]`, `it2 - it1` y les va bien `std::sort`.
* `++it` es más eficiente que `it++` (el prefijo no devuelve copia) → conviene usar prefijo.
* Funciones útiles: `std::advance(it, n)` (salta `n` posiciones) y `std::distance(a, b)`
  (distancia entre dos iteradores).

### 7.1 Invalidación de iteradores

| Operación | `vector` | `deque` | `list` |
| -- | -- | -- | -- |
| `push_back` | Invalida si realoca | Invalida si realoca al final | No invalida |
| `push_front` | No existe | Invalida si realoca al principio | No invalida |
| `insert` / `erase` en medio | Invalida **todos** desde ahí | Invalida desde ahí | Solo los borrados |

* En `list`, al ser enlazada, borrar un nodo **no** afecta a los demás iteradores →
  por eso el patrón `it = l.erase(it)` es seguro y eficiente.

---

## 8. Algoritmos básicos (`<algorithm>`)

```cpp
sort(v.begin(), v.end());                 // O(n log n); requiere acceso aleatorio
sort(v.begin(), v.end(), greater<int>()); // orden descendente
stable_sort(...);                          // estable (respeta los empates)
reverse(v.begin(), v.end());               // O(n)
find(v.begin(), v.end(), x);              // ITERADOR o end()
count(v.begin(), v.end(), x);             // nº de apariciones
binary_search(v.begin(), v.end(), x);     // bool → requiere que v esté ORDENADO
lower_bound(v.begin(), v.end(), x);       // primer elemento >= x
accumulate(v.begin(), v.end(), 0);        // suma (está en <numeric>)
copy, fill, remove, unique, min_element, max_element, ...
```

* `find` y `lower_bound` devuelven **iteradores**; `binary_search` devuelve `bool`.
* Antes de usar `binary_search` o `lower_bound`, el contenedor debe estar **ordenado**.
* `remove` + `erase` = **erase-remove idiom**: `remove` no borra de verdad, solo recoloca
  los elementos; hay que llamar a `erase` para que desaparezcan.
* Si el contenedor tiene su propio método (`list::sort`, `map::find`), **conviene usarlo**:
  suele ser más rápido y a veces es el único que funciona.

---

## 9. Tabla de retornos: qué devuelve cada operación

| Operación | Retorna | Detalle |
| -- | -- | -- |
| `v.push_back(x)` | `void` | |
| `v.pop_back()` | `void` | No devuelve el elemento |
| `s.pop()` (stack) | `void` | Leer `top()` antes de hacer `pop()` |
| `q.pop()` (queue) | `void` | Quita el `front` |
| `v[i]` | `T&` | Sin comprobar límites |
| `v.at(i)` | `T&` | Lanza `out_of_range` |
| `m["k"]` | `T&` | **Inserta** si no existe |
| `m.at("k")` | `T&` | Excepción si no existe |
| `set::insert(x)` | `pair<it,bool>` | `bool` = ¿se ha insertado? |
| `set::find(x)` | `iterator` | `end()` si no existe |
| `set::count(x)` | `size_type` | 0 o 1 (en *multi*: nº de repeticiones) |
| `set::erase(x)` | `size_type` | Nº de elementos borrados |
| `v.erase(it)` | `iterator` | Siguiente al borrado |
| `v.insert(pos,x)` | `iterator` | Al elemento insertado |
| `lower_bound(x)` | `iterator` | Primer elemento **≥ x** |
| `upper_bound(x)` | `iterator` | Primer elemento **> x** |
| `list::remove(x)` | `size_type` | Nº de elementos borrados |
| `list::splice(...)` | `void` | Mueve nodos sin copiar |

---

## 10. Detalles importantes para el examen

* **`erase` devuelve un iterador** → patrón de borrado seguro dentro de un bucle.
* **`m[k]` inserta** si la clave no existe → efecto secundario silencioso (clásica pregunta
  de "¿qué imprime este programa?").
* **`pop()` no devuelve nada** en `stack`, `queue` y `priority_queue`.
* **`list::sort()` existe y `std::sort` no sirve** para listas (no hay acceso aleatorio).
* **`splice` mueve nodos en $\mathcal{O}(1)$** → fusionar listas sin copiar elementos.
* **`vector` duplica su capacidad** al crecer → `push_back` amortizado $\mathcal{O}(1)$;
  `reserve` evita copias innecesarias.
* **`size()` de un vector es `size_t` (sin signo)** → `v.size() - 1` es peligroso si el
  vector está vacío (desborda a un número enorme).
* **`deque` permite `push_front`**, `vector` no (borrar delante de un vector cuesta $\mathcal{O}(n)$).
* **`forward_list` no tiene `size()`** ni `back()` ni `[]`; usa `insert_after` / `erase_after`.
* **`priority_queue` es un heap**, no una cola ordenada: solo `top()` está garantizado.
* **`set` y `map` están siempre ordenados** → recorrerlos es recorrer en orden;
  `unordered_*` no.
* **`count` en `set` / `map` solo vale 0 o 1**; para contar repeticiones hace falta
  `multiset` o la diferencia `upper_bound - lower_bound`.
* **`unique()` solo elimina consecutivos** (el nombre engaña): conviene ordenar antes.
* **`clear()` no libera memoria** en `vector` (sigue valiendo `capacity()`); para liberar:
  `vector<int>(v).swap(v);` (truco clásico).

---

## 11. ¿Qué contenedor elijo?

* Necesito **acceso aleatorio rápido** y crecer solo al final → **`vector`**.
* Necesito **insertar o quitar mucho por los extremos** → **`deque`**.
* Necesito **insertar o borrar en medio** manteniendo el orden y recorrer en ambos sentidos
  → **`list`**.
* Es **pequeño y de tamaño fijo** → **`array`**.
* Solo necesito **último en entrar, primero en salir** → **`stack`**.
* **Primero en entrar, primero en salir** → **`queue`**.
* Siempre tengo que coger **el más prioritario** → **`priority_queue`**.
* Quiero **buscar por clave** sin duplicados → **`set`**; con valor asociado → **`map`**.
* Quiero **permitir duplicados** → `multiset` / `multimap`.
* Solo quiero **buscar rápido sin importar el orden** → **`unordered_set`** / **`unordered_map`**.

---

> Fuente de referencia a la que es recomendable echarle un vistazo para profundizar más sobre el tema: [cplusplus.com/reference/stl/](https://cplusplus.com/reference/stl/) ·
> [vector](https://cplusplus.com/reference/vector/vector/) ·
> [map](https://cplusplus.com/reference/map/map/) ·
> [set](https://cplusplus.com/reference/set/set/) ·
> [list](https://cplusplus.com/reference/list/list/) ·
> [stack](https://cplusplus.com/reference/stack/stack/) ·
> [queue](https://cplusplus.com/reference/queue/queue/) ·
> [priority_queue](https://cplusplus.com/reference/queue/priority_queue/)
