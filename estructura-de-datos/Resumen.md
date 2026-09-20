# Comparación de la complejidad dependiendo de la estructura de datos
## 1- Vectores Estáticos y Dinámicos
| Categoría | Función / Algoritmo | Complejidad Temporal | Condición / Explicación del Mecanismo |
|---|---|---|---|
| Acceso Directo | Lectura/Escritura por índice `v[i]` | $\mathcal{O}(1)$ | Acceso a memoria contigua por cálculo de puntero base + desplazamiento. |
| Búsqueda | Búsqueda Secuencial / Lineal | $\mathcal{O}(n)$ | Recorre el vector elemento por elemento. Funciona en vectores desordenados. |
| Búsqueda | Búsqueda Binaria | $\mathcal{O}(\log_2 n)$ | Divide el espacio a la mitad en cada paso. Requiere que el vector esté previamente ordenado. |
| Inserción / Borrado | Inserción / Eliminación al Final (`push_back` / `pop_back`) | $\mathcal{O}(1)$ amortizado | Es $\mathcal{O}(1)$ constante casi siempre; pasa a $\mathcal{O}(n)$ solo en el caso de redimensión automática (duplicado de tamaño). |
| Inserción / Borrado | Inserción / Eliminación al Inicio / Medio | $\mathcal{O}(n)$ | Desplazamiento contiguo obligatorio de los $k$ elementos posteriores hacia la derecha o izquierda. |
| Redimensión | Ampliación por Duplicado (`capacity * 2`) | $\mathcal{O}(n)$ | Ocurre cuando `tamal == tamaf`. Reserva nuevo bloque en Heap, copia $n$ elementos y libera el bloque antiguo (`delete[]`). |
| Redimensión | Reducción por Tercio (Estrategia $\frac{1}{3}$) | $\mathcal{O}(n)$ | Reduce la capacidad a la mitad cuando `tamal <= tamaf / 3` para evitar creaciones/destrucciones continuas. |
| Ordenación | Algoritmos Eficientes (Merge Sort, QuickSort medio, HeapSort) | $\mathcal{O}(n \log n)$ | Métodos por división y conquista. Preparan el vector para poder aplicar Búsqueda Binaria. |
| Ordenación | Algoritmos Básicos (Burbuja, Inserción, Selección) | $\mathcal{O}(n^2)$ | Bucles anidados comparando y desplazando elementos contiguos. |

---
### Recordatorio 
### ¿Cuándo USAR un Vector?
* **Acceso por índice $\mathcal{O}(1)$:** Cuando necesitas consultar o modificar posiciones conocidas inmediatamente (`v[i]`)
* **Inserciones/Borrados al final $\mathcal{O}(1)$:** Para construir secuencias o pilas agregando elementos al final
* **Búsquedas binarias $\mathcal{O}(\log_2 n)$:** Cuando los datos se mantienen ordenados y se busca con frecuencia

### ¿Cuándo EVITAR un Vector?
* **Inserciones/Borrados en medio o al inicio $\mathcal{O}(n)$:** Desplazar elementos es muy costoso. *(Usa **Listas Enlazadas**)*
* **Búsquedas frecuentes en datos desordenados $\mathcal{O}(n)$:** Recorrer todo el vector es ineficiente. *(Usa **Tablas Hash**)*
* **Memoria muy restringida:** El duplicado de capacidad (`tamaf`) puede desperdiciar memoria no utilizada

## 2- Matrices y Conjuntos de Bits

| Estructura | Función / Operación | Complejidad Temporal | Detalle / Mecanismo |
| :--- | :--- | :---: | :--- |
| **Matriz** | **Acceso por coordenadas** `m(i, j)` | $\mathcal{O}(1)$ | Cálculo directo de índice o desreferencia de puntero `mat[i][j]`. |
| **Matriz** | **Multiplicación de matrices** | $\mathcal{O}(n \cdot m \cdot p)$ | Bucle triple anidado para calcular el producto escalar. |
| **Matriz Dinámica** | **Reserva / Liberación de memoria** | $\mathcal{O}(n)$ | Bucle para hacer `new[]` / `delete[]` por cada una de las $n$ filas. |
| **Bitset** | **Inserción** (`inserta`) | $\mathcal{O}(1)$ | Máscara de bits con desplazamiento y `OR`: `arr[n/8] \|= (1 << n%8)`. |
| **Bitset** | **Eliminación** (`elimina`) | $\mathcal{O}(1)$ | Máscara de bits con `AND` y `NOT`: `arr[n/8] &= ~(1 << n%8)`. |
| **Bitset** | **Comprobación de pertenencia** (`contiene`) | $\mathcal{O}(1)$ | Máscara de bits con `AND`: `(arr[n/8] & (1 << n%8)) != 0`. |
| **Bitset** | **Unión / Intersección / Resta** | $\mathcal{O}(n)$ | Operación lógica a nivel de byte (`\|`, `&`, `~`) donde $n$ es el nº de bytes. |
| **Conjunto en Vector** | **Inserción / Borrado / Pertenencia** | $\mathcal{O}(n)$ | Búsqueda lineal previa para evitar duplicados o localizar elemento. |
| **Conjunto en Vector** | **Unión / Intersección** | $\mathcal{O}(n^2)$ | Bucles anidados de comprobación elemento a elemento. |
---
### Recordatorio
### ¿Cuándo USAR una Matriz?
* **Acceso bidimensional inmediato $\mathcal{O}(1)$:** Para consultar o modificar datos en rejillas mediante coordenadas `[i][j]`
* **Modelado matemático y gráfico:** Excelente para representar tablas, imágenes, juegos (ej. ajedrez, tres en raya) y grafos (matrices de adyacencia).
* **Velocidad:** Alta localidad espacial al almacenar filas en bloques contiguos de memoria

### ¿Cuándo USAR un Bitset?
* **Pertenencia a conjuntos de enteros $\mathcal{O}(1)$:** Para comprobar si un entero no negativo pertenece a un grupo cerrado
* **Ahorro masivo de memoria:** Reduce el consumo hasta **8 veces** respecto a un arreglo de booleanos/enteros (1 byte = 8 elementos)
* **Operaciones de conjuntos a nivel de Hardware $\mathcal{O}(n)$:** Operaciones de Unión, Intersección y Diferencia ultra eficientes con instrucciones nativas del procesador (`AND`, `OR`, `NOT`)

### ¿Cuándo EVITARLOS?
* **Evitar Matrices cuando:** El tamaño cambia frecuentemente o los datos están muy dispersos (mayoría de ceros $\rightarrow$ usar *Listas de Adyacencia* o *Matrices Dispersas*)
* **Evitar Bitset cuando:** Necesitas almacenar objetos complejos, cadenas de texto o números flotantes/negativos sin rango acotado

## 3- Listas enlazadas (Linked Lists)
| Función / Operación | Complejidad Temporal | Detalle / Mecanismo Interno |
| :--- | :---: | :--- |
| **Acceso por índice** | $\mathcal{O}(n)$ | Recorrido secuencial enlace a enlace desde la `cabecera`. |
| **Búsqueda por valor** | $\mathcal{O}(n)$ | Recorrido lineal comparando `nodo->dato`. |
| **Búsqueda Binaria** | *No viable* | Requiere acceso aleatorio $\mathcal{O}(1)$, impracticable en listas. |
| **Inserción al Inicio** (`insertarInicio`) | $\mathcal{O}(1)$ | Reasigna el puntero `cabecera` inmediatamente. |
| **Borrado al Inicio** (`borrarInicio`) | $\mathcal{O}(1)$ | Elimina el primer nodo y avanza `cabecera = cabecera->sig`. |
| **Inserción al Final** (`insertarFinal`) | $\mathcal{O}(1)$ | Acceso directo usando el puntero `cola`: `cola->sig = nuevo`. |
| **Borrado al Final** (`borrarFinal`) | $\mathcal{O}(n)$ | Obliga a un bucle para buscar el penúltimo nodo y actualizar `cola`. |
| **Inserción/Borrado en Medio** | $\mathcal{O}(1)$ *(con iterador)* / $\mathcal{O}(n)$ *(sin iterador)* | Reorganización de punteros en $\mathcal{O}(1)$ tras posicionar el iterador. |
---
### Recordatorio
### ¿Cuándo USAR una Lista Enlazada?
* **Inserciones/Borrados frecuentes al inicio $\mathcal{O}(1)$:** Ideal para implementar Pilas (LIFO) o Colas simples
* **Inserciones/Borrados iterativos en medio $\mathcal{O}(1)$:** Cuando ya estás posicionado en el nodo con un iterador y quieres modificar la lista sin mover bloques de memoria
* **Memoria fragmentada o impredecible:** Para añadir elementos nodo a nodo en el Heap sin necesidad de reservar un tamaño fijo o contiguo

### ¿Cuándo EVITAR una Lista Enlazada?
* **Acceso por índice $\mathcal{O}(n)$:** Si necesitas consultar elementos por posición (`v[i]`) constantemente
* **Búsquedas binarias o algoritmos de ordenación por índices:** Ineficiente porque exige avanzar enlace a enlace
* **Borrado frecuente en el final $\mathcal{O}(n)$:** Borrar el último nodo requiere recorrer la lista para buscar el penúltimo. *(Para esto se usa la Lista Doblemente Enlazada)*
* **Se necesita velocidad:** Los nodos dispersos en memoria no aprovechan la velocidad de la caché del procesador.

## 4- Listas Doblemente Enlazadas

| Estructura | Función / Operación | Complejidad Temporal | Detalle / Mecanismo Interno |
| :--- | :--- | :---: | :--- |
| **Lista Doblemente Enlazada** | **Acceso por índice** | $\mathcal{O}(n)$ | Recorrido secuencial desde la cabecera o cola. |
| **Lista Doblemente Enlazada** | **Inserción / Borrado al Inicio o Final** | $\mathcal{O}(1)$ | Actualización directa de punteros `cabecera` o `cola` (elimina la limitación del borrado al final de las simples). |
| **Lista Doblemente Enlazada** | **Inserción / Borrado con Iterador** | $\mathcal{O}(1)$ | Desconexión y reconexión inmediata de los punteros `sig` y `ant`. |
| **Lista Circular** | **Acceso al Primer / Último elemento** | $\mathcal{O}(1)$ | El puntero `cola` apunta al final y `cola->sig` al inicio. |
| **Lista Circular** | **Recorrido / Búsqueda** | $\mathcal{O}(n)$ | Iteración lineal hasta volver a coincidir con el nodo inicial. |
| **Lista Circular** | **Inserción / Borrado en Extremos** | $\mathcal{O}(1)$ | Inserción directa en `cola->sig` o en `cola`. |
| **Matriz Dispersa** | **Consulta / Modificación `valor(i, j)`** | $\mathcal{O}(k)$ | $k$ es el número de elementos no nulos en la fila. Requiere búsqueda en listas. |
| **Matriz Dispersa** | **Inserción de Elemento no nulo** | $\mathcal{O}(k)$ | Busca la fila y la posición de la columna para enlazar el nodo. |
---

### Recordatorio:
### ¿Cuándo USAR estas Estructuras?
* **Lista Doblemente Enlazada:** Necesitas recorrer datos hacia adelante y atrás, o hacer **borrados frecuentes al final o en cualquier punto en $\mathcal{O}(1)$** disponiendo de un iterador/puntero
* **Lista Circular:** Necesitas procesamiento en bucle continuo (planificación *Round-Robin* en SO, turnos de juegos, estructuras cíclicas) y acceso instantáneo a inicio y fin con un solo puntero (`cola`)
* **Matriz Dispersa:** Representas tablas de grandes dimensiones donde la inmensa mayoría de celdas son $0$ (imágenes comprimidas, grafos gigantes), ahorrando memoria masivamente

### ¿Cuándo EVITARLAS?
* **Evita Listas Dobles cuando:** El consumo de memoria sea crítico (almacenas 2 punteros por nodo: `sig` y `ant`)
* **Evita Listas Circulares cuando:** Requieras acceso por índice directo $\mathcal{O}(1)$ o si hay riesgo de dejar bucles infinitos por mal control de parada
* **Evita Matrices Dispersas cuando:** La matriz esté llena o densa (perderás la velocidad $\mathcal{O}(1)$ de las matrices normales y añadirás sobrecoste de punteros)

## 5- STL
| Contenedor | Acceso Aleatorio `[]` | Inserción / Borrado Inicio | Inserción / Borrado Final | Inserción / Borrado Medio | Invalidación de Iteradores |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **`std::vector`** | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ amortizado | $\mathcal{O}(n)$ | **Sí**: Invalida todos al redimensionar en Heap, o desde la posición modificada. |
| **`std::deque`** | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ | **Sí**: Inserciones o borrados intermedios invalidan todos los iteradores. |
| **`std::list`** | *No soportado* ($\mathcal{O}(n)$) | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ *(con iterador)* | **No**: Los iteradores se mantienen válidos (salvo el del nodo eliminado). |
---
### Recordatorio

### ¿Cuándo USAR cada contenedor?
* **`std::vector` (Por defecto):** Quieres **acceso por índice $\mathcal{O}(1)$**, rendimiento máximo de caché y la mayoría de tus inserciones o borrados son al final (`push_back` / `pop_back`)
* **`std::deque`:** Necesitas **acceso directo $\mathcal{O}(1)$** y requieres insertar/borrar de forma ultrarrápida $\mathcal{O}(1)$ **tanto al principio como al final** (`push_front` / `push_back`)
* **`std::list`:** Realizas **inserciones y borrados constantes en posiciones intermedias $\mathcal{O}(1)$** con un iterador, o necesitas mantener la validez de los iteradores sin importar las modificaciones

### ¿Cuándo EVITARLOS?
* **Evita `std::vector` cuando:** Realices inserciones o borrados frecuentes al principio o en medio $\mathcal{O}(n)$
* **Evita `std::deque` cuando:** Vayas a insertar/borrar en medio $\mathcal{O}(n)$ o necesites un bloque de memoria 100% contiguo (para interoperar con código C antiguo)
* **Evita `std::list` cuando:** Necesites acceder por índice (`v[i]`), hacer búsquedas binarias o maximizar el rendimiento de la memoria caché


## 6- Pilas-Colas

| Estructura | Implementación Interna | Inserción (`push`) | Extracción (`pop`) | Consulta (`top` / `front`) |
| :--- | :--- | :---: | :---: | :---: |
| **Pila** | Vector Dinámico / Lista Enlazada | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |
| **Cola** | Vector Circular / Lista Enlazada | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |
| **Cola con Prioridad** | Lista Enlazada Ordenada | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |
| **Cola con Prioridad** | Vector de Listas *(rango acotado)* | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |
| **Cola con Prioridad** | Montículo / Árbol (*Heap*) | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(1)$ |
---

| Adaptador STL | Encabezado | Contenedor por Defecto | Contenedores Permitidos | Método de Consulta |
| :--- | :---: | :---: | :--- | :---: |
| **`std::stack`** | `<stack>` | `std::deque` | `std::vector`, `std::list` | `top()` |
| **`std::queue`** | `<queue>` | `std::deque` | `std::list` | `front()` / `back()` |
| **`std::priority_queue`** | `<queue>` | `std::vector` | `std::deque` | `top()` |

--- 
### Recordatorio
### ¿Cuándo USAR cada estructura?
* **Pila (`Pila` / `std::stack`):** Estrategia **LIFO** *(Last In, First Out)*. Para deshacer acciones (Ctrl+Z), evaluar expresiones sintácticas, recorridos DFS o **eliminar la recursividad**
* **Cola (`Cola` / `std::queue`):** Estrategia **FIFO** *(First In, First Out)*. Para listas de espera, gestión de recursos por orden de llegada, colas de impresión o recorridos BFS
* **Cola con Prioridad (`ColaPrioridad` / `std::priority_queue`):** Para procesar elementos según su **prioridad o relevancia** (no el orden de llegada).

### ¿Cuándo EVITARLAS?
* **Evita estas estructuras si:** Necesitas consultar o modificar elementos intermedios o iterar sobre la estructura, ya que **no soportan iteradores ni acceso por índice/posición**


## 7- Árboles
### Complejidad 
| Caso de Árbol | Búsqueda | Inserción | Eliminación | Altura del Árbol ($h$) |
| :--- | :---: | :---: | :---: | :---: |
| **Caso Promedio / Equilibrado** | $\mathcal{O}(\log_2 n)$ | $\mathcal{O}(\log_2 n)$ | $\mathcal{O}(\log_2 n)$ | $h \approx \log_2 n$ |
| **Peor Caso / Degenerado (Lista)** | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $h = n$ |

### Tipo de Recorrido

| Recorrido | Orden de Procesamiento | Propósito / Caso de Uso Principal |
| :--- | :---: | :--- |
| **Preorden** | **Raíz** $\rightarrow$ Izquierda $\rightarrow$ Derecha | Copiar o duplicar la estructura exacta del árbol. |
| **Inorden** | Izquierda $\rightarrow$ **Raíz** $\rightarrow$ Derecha | Obtener los elementos **ordenados de menor a mayor**. |
| **Postorden** | Izquierda $\rightarrow$ Derecha $\rightarrow$ **Raíz** | Liberar/destruir memoria del árbol de abajo hacia arriba. |

### Estrategia de eliminación en los ABB
| Caso de Borrado | Comportamiento / Mecanismo Interno | Complejidad |
| :--- | :--- | :---: |
| **0 Hijos (Hoja)** | Elimina el nodo directamente y pone el puntero del padre a `nullptr`. | $\mathcal{O}(1)$ *post-búsqueda* |
| **1 Hijo** | Reconecta al padre directamente con el único hijo del nodo borrado. | $\mathcal{O}(1)$ *post-búsqueda* |
| **2 Hijos** | Sustituye el dato por el **mínimo del subárbol derecho** (o máximo del izquierdo) y elimina la hoja duplicada. | $\mathcal{O}(\log_2 n)$ |

---
### Recordatorio
### ¿Cuándo USAR un Árbol Binario de Búsqueda (ABB)?
* **Búsquedas, Inserciones y Borrados dinámicos rápidos en $\mathcal{O}(\log_2 n)$:** Cuando necesitas la velocidad de la búsqueda binaria de un vector ordenado, pero con la flexibilidad de inserción/borrado de una lista
* **Mantenimiento de datos ordenados automáticamente:** Al recorrer el árbol en **Inorden**, obtienes todos los elementos ordenados de menor a mayor sin coste adicional
* **Modelado de jerarquías:** Representación de directorios de archivos, sintaxis de código (árboles sintácticos) o esquemas de decisión

### ¿Cuándo EVITAR un ABB?
* **Datos de entrada ya ordenados sin mecanismo de balanceo:** Si insertas elementos en orden secuencial (1, 2, 3, 4...), el árbol degenera en una lista enlazada con rendimiento $\mathcal{O}(n)$. *(Usa árboles autobalanceados como **AVL** o **Rojo-Negro**)*.
* **Acceso directo por índice $\mathcal{O}(1)$:** Un ABB requiere navegar nodo a nodo desde la raíz $\mathcal{O}(\log n)$. *(Usa **Vectores**)*

##  8- Árboles AVL
| Operación | Complejidad Temporal | Detalle / Mecanismo Interno |
| :--- | :---: | :--- |
| **Búsqueda** | $\mathcal{O}(\log_2 n)$ | Mapeo rápido garantizado por la altura óptima del árbol. |
| **Inserción** | $\mathcal{O}(\log_2 n)$ | Búsqueda $\mathcal{O}(\log n)$ + ajuste de balances y **máximo 1 rotación** $\mathcal{O}(1)$. |
| **Borrado** | $\mathcal{O}(\log_2 n)$ | Búsqueda y eliminación $\mathcal{O}(\log n)$ + **posibles rotaciones en cadena** hasta la raíz. |
| **Rotación (Simple/Doble)** | $\mathcal{O}(1)$ | Intercambio local de punteros y reajuste aritmético de variables `bal`. |

### ¿Cuándo USAR un Árbol AVL?
* **Entornos con búsquedas intensivas $\mathcal{O}(\log_2 n)$:** Cuando la lectura/consulta es la operación más frecuente y se requiere la mínima altura posible garantizada
* **Prevención absoluta de degradación:** Cuando los datos de entrada pueden venir ordenados o parcialmente ordenados y un ABB normal degeneraría en $\mathcal{O}(n)$

### ¿Cuándo EVITAR un Árbol AVL?
* **Inserciones y borrados masivos muy frecuentes:** Las reestructuraciones mediante rotaciones constantes añaden sobrecoste (el borrado puede encadenar múltiples rotaciones hasta la raíz). *(Suele preferirse **Árboles Rojo-Negro** como en `std::map`)*
* **Acceso por índice directo $\mathcal{O}(1)$:** No permite saltos por posición *(Usar vectores)*


## 9- Heaps y Conjuntos
| Estructura | Implementación / Operación | Consulta (`top` / `buscar`) | Inserción (`push`) | Extracción / Unión (`pop` / `unir`) |
| :--- | :--- | :---: | :---: | :---: |
| **Heap** | Vector Contiguo (Min/Max Heap) | $\mathcal{O}(1)$ | $\mathcal{O}(\log_2 n)$  | $\mathcal{O}(\log_2 n)$ *(Hundido)* |
| **Union-Find** | Vector Simple de Representantes | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ *(crear)* | $\mathcal{O}(n)$ *(unir requiere actualizar array)* |
| **Union-Find** | Bosque + Rango + Compresión | $\mathcal{O}(\alpha(n)) \approx \mathcal{O}(1)$ | $\mathcal{O}(1)$ *(crear)* | $\mathcal{O}(\alpha(n)) \approx \mathcal{O}(1)$ |
---
### Recordatorio
### ¿Cuándo USAR estas Estructuras?
* **Heaps (Montículos):** Ideal para implementar **Colas de Prioridad**, el algoritmo de ordenación **HeapSort**, o cuando necesitas obtener de forma continua el valor máximo o mínimo en tiempo constante $\mathcal{O}(1)$.
* **Conjuntos Disjuntos (Union-Find):** Necesitas gestionar **agrupaciones/particiones de elementos**, detectar ciclos en grafos no dirigidos (Algoritmo de **Kruskal** para Árbol de Recubrimiento Mínimo) o comprobar si dos nodos están en la misma componente conexa.

### ¿Cuándo EVITARLAS?
* **Evita Heaps cuando:** Necesites buscar un elemento arbitrario o recorrer los datos de forma ordenada. Búsquedas por valor cuestan $\mathcal{O}(n)$ al no tener orden entre hermanos
* **Evita Union-Find cuando:** Necesites **desunir o separar conjuntos previamente fusionados** (es una estructura de fusión incremental)

## 10- Conjuntos-mapas-STL


### Clasificación de Contenedores
| Contenedor | Formato del Dato | Admite Claves Duplicadas | Acceso por `operator[]` | Retorno de `insert()` |
| :--- | :---: | :---: | :---: | :--- |
| **`std::set`** | Clave es el Dato | **NO** | No soportado | `std::pair<iterator, bool>` |
| **`std::multiset`** | Clave es el Dato | **SÍ** | No soportado | `iterator` |
| **`std::map`** | Pareja `std::pair<Clave, Dato>` | **NO** | **SÍ** (`m[clave]`) | `std::pair<iterator, bool>` |
| **`std::multimap`** | Pareja `std::pair<Clave, Dato>` | **SÍ** | No soportado | `iterator` |


### Complejidad
| Operación | Complejidad Temporal | Detalle / Mecanismo Interno |
| :--- | :---: | :--- |
| **Búsqueda** (`find`, `count`) | $\mathcal{O}(\log_2 n)$ | Búsqueda binaria jerárquica sobre el Árbol Rojo-Negro. |
| **Inserción** (`insert`) | $\mathcal{O}(\log_2 n)$ | Localiza la posición en $\mathcal{O}(\log n)$ y reequilibra el árbol. |
| **Borrado** (`erase`) | $\mathcal{O}(\log_2 n)$ | Elimina el nodo y aplica rotaciones/recoloreo de balanceo. |
| **Búsqueda por Rango** (`lower_bound`) | $\mathcal{O}(\log_2 n)$ | Devuelve un iterador al primer elemento no menor que la clave dada. |
| **Recorrido Secuencial** | $\mathcal{O}(n)$ | Recorrido en **Inorden** utilizando los punteros al nodo padre. |

---
### Recordatorio
### ¿Cuándo USAR estos Contenedores Asociativos?
* **`std::set` / `std::multiset`:** Cuando necesitas mantener una colección de elementos **ordenados automáticamente** y sin duplicados (`set`) o permitiendo duplicados (`multiset`)
* **`std::map` / `std::multimap`:** Cuando necesitas una estructura clave-valor (diccionario) que **mantenga las claves siempre ordenadas** para realizar búsquedas, inserciones y borrados en $\mathcal{O}(\log_2 n)$
* **Búsquedas por rango:** Ideal si necesitas consultar subrangos de datos con `lower_bound()` o `upper_bound()`

### ¿Cuándo EVITARLOS?
* **Búsquedas ultrarrápidas en $\mathcal{O}(1)$:** Si el orden no te importa y solo buscas velocidad máxima por clave, utiliza contenedores no ordenados basados en Hash (`std::unordered_map` / `std::unordered_set`)
* **Acceso por índice numérico directo:** No soportan acceso por posición `v[i]`. Su acceso por `[]` en `std::map` es por clave

## 11- Dispersión Abierta
### Complejidad
| Operación / Métrica | Caso Promedio / Óptimo ($\lambda \le 0.7$) | Peor Caso (Degenerado) | Detalle / Mecanismo Interno |
| :--- | :---: | :---: | :--- |
| **Búsqueda** | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ | Mapeo directo por clave + recorrido corto en la lista enlazada. |
| **Inserción** | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ | Inserta al inicio o final de la lista enlazada de la celda. |
| **Borrado** | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ | Localiza la celda en $\mathcal{O}(1)$ y desconecta el nodo de la lista. |
| **Factor de Carga ($\lambda$)** | $\lambda = \frac{n}{t}$ | $-$ | Mide la saturación de la tabla ($\lambda > 0.7$ requiere **Redispersión**). |
| **Redispersión (Rehash)** | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | Duplica el tamaño $t$ y reinserta todos los elementos al superar $\lambda > 0.7$. |

---
### Recordatorio
### ¿Cuándo USAR Dispersión Abierta?
* **Búsquedas, inserciones y borrados inmediatos $\mathcal{O}(1)$ promedio:** Cuando la velocidad absoluta es prioritaria frente al mantenimiento de un orden entre elementos
* **Número de elementos impredecible:** El uso de listas enlazadas dinámicas en cada celda permite almacenar más elementos que el tamaño físico $t$ de la tabla sin saturarse completamente
* **Factor de carga alto ($\lambda > 0.7$):** Soporta mejor la acumulación de datos que la dispersión cerrada sin colapsar

### ¿Cuándo EVITAR Dispersión Abierta?
* **Necesidad de datos ordenados:** Las funciones Hash distribuyen las claves de forma pseudoaleatoria. No permite recorridos en inorden ni búsquedas por rango (`lower_bound`)
* **Sistemas con memoria muy limitada:** Las listas enlazadas en cada posición añaden un sobrecoste de memoria por nodo para almacenar los punteros `sig`
* **Velocidad:** Los nodos dispersos en las listas rompen la localidad espacial de la CPU

## 12- Dispersión cerrada

### Tipo de Exploración
| Método de Exploración | Fórmula de Salto ($f(i)$) | Ventajas | Inconvenientes / Limitaciones |
| :--- | :---: | :--- | :--- |
| **Exploración Lineal** | $f(i) = i$ | Muy fácil de implementar y aprovecha al máximo la Caché de la CPU. | **Agrupamiento Primario:** Forma grandes bloques de casillas ocupadas contiguas. |
| **Exploración Cuadrática** | $f(i) = i^2$ | Elimina el agrupamiento primario variando la longitud del salto. | **Agrupamiento Secundario:** Claves con la misma posición inicial siguen la misma secuencia. |
| **Dispersión Doble** | $f(i) = i \cdot h_2(x)$ | **Elimina agrupamientos primarios y secundarios** (mejor distribución). | Exige calcular una segunda función $h_2(x)$ que jamás devuelva 0. |

### Gestión del Borrado
| Estado de Casilla | ¿Contiene Dato Válido? | ¿Permite Insertar Aquí? | ¿Detiene el Bucle de Búsqueda? |
| :--- | :---: | :---: | :---: |
| **Vacía** | NO | SÍ | **SÍ** *(Llega al final de la secuencia)* |
| **Ocupada** | SÍ | NO | NO *(Compara la clave)* |
| **Borrada / Disponible** | NO | SÍ | **NO** *(Continúa buscando hacia adelante)* |

### Tabla Comparativa: `std::map` vs `std::unordered_map` (C++ STL)

| Característica | `std::map` / `std::set` | `std::unordered_map` / `std::unordered_set` |
| :--- | :---: | :---: |
| **Estructura Interna** | Árbol Rojo-Negro (Balanceado) | Tabla Hash (Basada en Cubetas / Buckets) |
| **Complejidad Acceso / Búsqueda** | $\mathcal{O}(\log_2 n)$ garantizado | **$\mathcal{O}(1)$ promedio** ($\mathcal{O}(n)$ peor caso) |
| **Orden de los Elementos** | **Ordenados automáticamente** por clave | **Sin orden definido** (desordenados) |
| **Métodos de Control de Tabla** | *No aplican* | `.load_factor()`, `.bucket_count()`, `.rehash()`, `.reserve()` |

---
### Resumen
### ¿Cuándo USAR Dispersión Cerrada?
* **Rendimiento crítico de memoria Caché:** Todos los datos se almacenan en un **vector contiguo** sin listas externas ni sobrecoste de punteros dinámicos.
* **Número máximo de elementos conocido y acotado ($n \le t$):** La tabla tiene un tamaño fijo $t$, por lo que la cantidad de elementos $n$ **nunca puede superar el tamaño de la tabla** ($\lambda \le 1.0$).
* **Ahorro de sobrecoste de memoria:** No requiere instanciar nodos ni reservar memoria dinámica en el Heap por cada inserción.

### ¿Cuándo EVITAR Dispersión Cerrada?
* **Factor de carga alto ($\lambda > 0.7$):** El rendimiento cae drásticamente debido a las colisiones y las secuencias de exploración largas.
* **Borrados masivos y frecuentes:** Requiere marcar casillas como *Borrada/Disponible*, lo que ensucia la tabla y alarga las secuencias de búsqueda hasta requerir una reorganización/rehash.
* **Volumen de datos altamente variable e impredecible:** Si la tabla se llena ($n = t$), fallará o requerirá un rehash completo a un vector mayor.

## 13- Grafos

| Operación / Recorrido | Matriz de Adyacencia | Lista de Adyacencia |
| :--- | :---: | :---: |
| **Espacio en memoria** | $\mathcal{O}(\vert V \vert^2)$ | $\mathcal{O}(\vert V \vert + \vert E \vert)$ |
| **Comprobar si existe arista $(u, v)$** | $\mathcal{O}(1)$ | $\mathcal{O}(\text{Grado}(u))$ |
| **Insertar arista** | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ |
| **Obtener vecinos de un nodo $u$** | $\mathcal{O}(\vert V \vert)$ | $\mathcal{O}(\text{Grado}(u))$ |
| **Recorrido completo (DFS / BFS)** | $\mathcal{O}(\vert V \vert^2)$ | $\mathcal{O}(\vert V \vert + \vert E \vert)$ |

*Donde $\vert V \vert$ es el número de vértices y $\vert E \vert$ el número de aristas.*

## 14- Quadtrees
### Matriz Comparativa: Mallas Regulares vs. Quadtrees

| Característica | Malla Regular | Quadtree |
| :--- | :---: | :---: |
| **Tipo de Estructura** | Matricial 2D (Fija / No adaptativa) | Árbol Jerárquico de Orden 4 (Adaptativo) |
| **Cálculo de Posición** | Directo por fórmula $\mathcal{O}(1)$ | Descendiente desde la raíz $\mathcal{O}(\log_4 n)$ |
| **División del Espacio** | Rejilla de tamaño uniforme | 4 cuadrantes ortogonales (NO, NE, SO, SE) |
| **Criterio de Subdivisión** | Fijo desde la inicialización | Dinámico al superar `MAX_PUNTOS_CAJA` |
| **Uso de Memoria en Zonas Vacías** | Alto (asigna casillas vacías igualmente) | Mínimo (nodos sin dividir) |
| **Extensión Tridimensional** | Malla Regular 3D | **Octree** (Subdivisión en 8 octantes) |


### Tabla Completa de Complejidad Temporal

| Operación | Malla Regular (Caso Óptimo - Uniforme) | Malla Regular (Peor Caso - Aglomerado) | Quadtree (Promedio / Esperado) | Quadtree (Peor Caso - Desequilibrado) |
| :--- | :---: | :---: | :---: | :---: |
| **Acceso / Localizar Casilla** | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(\log_4 n)$ | $\mathcal{O}(n)$ |
| **Búsqueda / Inserción** | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ | $\mathcal{O}(\log_4 n)$ | $\mathcal{O}(n)$ |
| **Borrado** | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ | $\mathcal{O}(\log_4 n)$ | $\mathcal{O}(n)$ |
| **Reestructuración Escalar** | *No aplica* | *No aplica* | $\mathcal{O}(1)$ local *(División / Fusión)* | $\mathcal{O}(n)$ *(Reorganización profunda)* |

### ¿Cuándo USAR una Malla Regular?
* **Distribución de datos uniforme:** Los objetos se reparten de forma homogénea por la superficie (sin grandes aglomeraciones ni zonas vacías).
* **Acceso directo ultrarrápido $\mathcal{O}(1)$:** Deseas calcular la posición exacta de la casilla mediante una simple fórmula matemática sin recorrer estructuras jerárquicas.
* **Búsquedas de vecinos cercanos en rango fijo:** Mallas donde el tamaño de celda coincide con el radio de búsqueda deseado.

### ¿Cuándo USAR un Quadtree?
* **Distribución de datos no uniforme (Aglomeraciones):** Los objetos se agrupan en regiones concretas (ej. mapa de una ciudad con alta densidad en el centro y vacíos en la periferia).
* **Estructura adaptativa requerida:** Necesitas que la resolución espacial se ajuste dinámicamente según la cantidad de datos sin desperdiciar memoria.
* **Aplicaciones espaciales compuestas:** Compresión de imágenes, detección de colisiones 2D o representación de mapas con diferentes niveles de detalle (LOD).
