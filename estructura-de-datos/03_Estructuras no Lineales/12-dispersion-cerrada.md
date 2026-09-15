# Dispersión Cerrada. Resolución de colisiones

La **dispersión cerrada** (o direccionamiento abierto) almacena **todos** los elementos directamente detrn de la propia tabla de dispersión sin recurrir a estructuras de datos dinámicas auxiliares como listas enlazadas (Las q usabamos en dispersión abierta)

* **Mecanismo**: Cuando ocurre una oclisión "$h(x)$" apunta a una casilla ya ocupada, el algoritmo aplica una secuencia de exploración para encontrar otra posición libre entro del vector

![disp_cerrada](../assets/img/dispersion_cerrada.gif)
### Métodos de Resolución de Colisiones (Secuencias de Exploración)
La función general de la exploración se expresa como:
> $h(x,i)= (h1(x)+f(i)) (mod t)$

$i$ representa el número de intento ($i$ = 0,1,2,3....) y t el tamaño de la tabla 

## 1. Exploración Lineal
> Formula:  $f(i) = i \implies h(x, i) = (h_1(x) + i) \pmod t$
* **Funcionamiento:** Si la posición natural está ocupada se prueba la secuencia: (+1,+2,+3....)
* **Inconveniente:** los datos tienden a aglomerarse en bloques contiguos. Las claves que colisionan y las que caen dentro del bloque compiten por los mismos huecos por lo q se reduce el rendimiento

![exploracion-lineal](../assets/img/exploracion_lineal.gif)
## 2. Exploración Cuadrática
> Formula: $f(i) = i^2 \implies h(x, i) = (h_1(x) + i^2) \pmod t$. 
* **Funcionamiento:** Modifica el salto usando la progresión cuadrática: $+1^2, +2^2, +3^2, \dots$)
* **Ventaja/Inconveniente:** Elimina el **agrupamiento primario** pero sufre **agrupamiento secundario**: Si dos claves tienen la misma posición inicial $(h(x1) = h(x2))$ seguirán la misma secuencia de prueba

![exploracion-cuadratica](../assets/img/exploracion_cuadratica.gif)
## 3. Dispersión Doble (Double Hashing)
>Fórmula: $f(i) = i \cdot h_2(x) \implies h(x, i) = (h_1(x) + i \cdot h_2(x)) \pmod t$.  
* **Funcionamiento**: El tamaño del salto está determinado por una segunda función de dispersión $h_2(x)$ independiente. $h_2(x)$ jamás debe evaluar a 0 (ej. $h_2(x) = 1 + (x \bmod q)$ con $q < t$ primo).  

* **Ventaja**: Elimina tanto el agrupamiento primario como el secundario, logrando la mejor distribución de elementos

![disp_doble](../assets/img/dispersion_doble.gif)
## Operaciones Binarias y el problema de Borrado
Dado que un elemento no puede residir en su posición "natural" por las colisiones, las operaciones deben seguir la secuencia de exploración:
* **Búsqueda**: Se calcula la posición inicial y se recorre la secuencia de exploración hasta encontrar la clave buscad o chocar con una **casilla vacía**

* **El problema de Borrado**: Si simplemente se borra un elemento dejando la casilla vacía, se interrumpe la secuencia de exploración y las **búsquedas posteriores de otros elementos colisionados fallarán**

* **Solución**: Cada casilla de la tabla debe gestionar tres estados explícitos
1. **Vacía**: Nunca ha contenido un elemento -> Detiene búsquedas
2. **Ocupada**: Contiene un elemento válido activo
3. **Disponible/Borrada**: El elemento fue eliminado (Permite insertar nuevos datos pero **no detiene las búsquedas**)

## tabla con Cubetas (Buckets)
Es una variante estructural para reducir los problemas de colisión de memoria secundaria

* **Concepto**: Cada posición de la tabla no es una única casilla, sino una **cubeta** (compartimento) con capacidad para almacenar un número fijo de elementos

* **Comportamiento**: No se genera una colisión externa hasta que la cubeta correspondiente se llene por completo

* **Desbordamiento**: Si una cubeta alcanza su capacidad máxima, las  colisiones subsiguientes se gestionan aplicando exploración lineal a otras cubetas y marcando la cubeta origen como "desbordada"

## Contenedores Dispersos en C++ STL (std::unordered_*)
Son contenedores basados en tablas de dispersión ( implementados internamente mediante cubetas)

* **Variedades**: `std::unordered_map`, `std::unordered_set`, `std::unordered_multimap`, `std::unordered_multiset`

* **Diferencias con `std::map` / `std::set`
    * Acceso en tiempo medio $O(1)$ frente a $O(log n)$
    * Los elementos **no están ordenados**
* **Métodos de Control**: Ofrecen funciones específicas de la tabla como `.load_factor()`, `.max_load_factor`, `bucket_count()`, `.rehash()` y `.reserve()`
