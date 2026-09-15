# Heaps y Conjuntos disjuntos

## Parte I: Heaps (Montículos)
### 1. Definiciones y Conceptos
* Un **heap** es una estructura de datos basada en un **árbol binario completo** diseñada para gestionar colas con prioridad de forma eficiente

* **Árbol Binario Completo**: Es perfececto en todos su niveles excepto quizás en el último donde los nodos deben estar agrupados totalmente a la izquierda

* **Propiedad de Orden del Heap**:
    * **Min-Heap**: El padre es **menor o igual** que sus hijos. Es decir **la raíz contiene el valor mínimo**
    * **Max-Heap**: El padre es **mayor o igual** que sus hijos. Es decir **la raíz contiene el valor máximo**

![Representación Heaps](../assets/img/heap_min_max_dark.gif)
### 2. Implementación sobre Vectores(Arrays)
Al ser un árbol completo compactado, **no usa punteros** ; se guarda directamente en un vector contiguo. Para un nodo de índice $i$:
* **Hijo Izquierdo** : 2 * i+1
* **Hijo Derecho**: 2 * i+2
* **Padre**: [(i-1)/2]

![Implementacion_en_vectores](../assets/img/heap_array_index_dark.gif)
### 3. Operaciones Claves del Heap
* `push` **(Inserción / Flotado)**:
    * Inserta el nuevo elemento al final del vector
    * **Flotado (Percolate UP)**: Compara el elemento con su padre y los intercambia mientras sea mayor(en Max-Heap) o menor (en Min-Heap)
* `pop` **Extracción/Hundido**:
    * Guarda y extrae el elemento de la raíz (`arr[0]`)
    * Mueve el último elemento del vector a la raíz
    * **Hundido (Percolate Down)**: Compara la nueva raíz con sus hijos y la intercambia con el hijo mayor/menor según corresponda, bajando por el árbol hasta restaurar la propiedad de orden

![op](../assets/img/heap_push_pop_dark.gif)
#### Implementación:
```cpp
template <class T>
class Heap {
    T *arr;
    int tamal, tamaf;
    inline void swap(int a, int b);

public:
    Heap(int MaxTama = 500);
    
    void push(const T &item) {
        if (tamal == tamaf) throw HeapSinEspacio();
        int actual = tamal++;
        arr[actual] = item;
        int padre = (actual - 1) / 2;
        
        while (actual > 0 && arr[actual] > arr[padre]) { // Flotado (Max-Heap)
            swap(actual, padre);
            actual = padre;
            padre = (actual - 1) / 2;
        }
    }

    T pop() {
        if (tamal == 0) throw HeapVacio();
        T resultado = arr[0];
        arr[0] = arr[--tamal];
        int actual = 0, hijoMax = 1;
        
        while (hijoMax < tamal) { // Hundido
            if (hijoMax + 1 < tamal && arr[hijoMax] < arr[hijoMax + 1]) ++hijoMax;
            if (arr[actual] < arr[hijoMax]) {
                swap(actual, hijoMax);
                actual = hijoMax;
                hijoMax = 2 * actual + 1;
            } else break;
        }
        return resultado;
    }
};
```


### Complejidad Temporal (HEAP)
* **Insertar (`push`):** O(log n) peor caso
* **Extraer(`pop`):** O(log n) garantizado
* **Consultar raíz (`top`):** O(1)

## Parte II: Conjuntos Disjuntos (Union-Find)
Esta estructura administra una partición de $n$ elementos repartidos en subconjuntos disjuntos
>Recordatorio: Un conjunto disjutno es aquel en el q ningún elemento pertenece a más de un subconjunto

### 1. Operaciones Básicas
* `crearConjunto(x)`: Crea un subconjunto **unitario** de un elemento $x$
* `buscar(x)`: Devuelve el representante/raíz del conjunto al que pertence $x$
* `unir(x,y)`: Fusiona en un solo conjunto los subconjuntos donde están $x$ e $y$

### 2. Implementaciones y Operadores
### A: Implementación con un Vector Simple
* El vector `rep[i]` guarda directamente el identificador del conjunto.
* **Desventaja**: `buscar` es O(1), pero la operación `unir` es ineficiente y cuesta $O(n)$ porque debe actualizar todo el array

### B: Implementación con Bosque de Árboles
* cada subconjunto se represntamediante un árbol donde cada nodo apunta a su padre 
* la raíz es el identificador del conjunto y se cumple que `rep[i]==i
* ara evitar errores de  que los árboles se vuelvan muy profundos se aplican estas dos optimizaciones:
    * **Unión por Altura / Rango**: Al unir dos árboles, el de menor profundiad pasa a ser subárbol del de mayor profundidad
    * **Compresión de Caminos**: Durante `buscar(x)` , todos los nodos visitados en el trayecto se reconecttan diretamente a la raíz
    

### Búsqueda de Caminos
```cpp
int buscar(int x) {
    int r = x;
    while (rep[r] != r) r = rep[r]; // 1. Encontrar la raíz
    
    int a, s = x;
    while (rep[s] != r) {           // 2. Comprimir el camino
        a = s;
        s = rep[s];
        rep[a] = r;
    }
    return r;
}
```