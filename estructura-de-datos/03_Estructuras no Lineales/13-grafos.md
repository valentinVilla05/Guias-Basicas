# Grafos
## 1. Conceptos Fundamentales
* **Definición de Grafo**: Es un conjunto $G = (V,E)$ donde $V$ son los vértices (nodos) y $E$ son las aristas

* **Tipos de Grafos**:
    * **No dirigido**: Las aristas no tienen dirección especificada; es decir
    > e = (u,v) = (v,u)
    * **Dirigido (Digrafo)**: Las aristas tienen un sentido de origen a destino 
    > (u,v) != (v,u)
    * **Ponderado**: Cada arista tiene un costo o peso asociado (ej distancia en km)
* **Propiedades**:
    * **Camino**: Secuencia de vértices unidos por aritas
    * **Camino Simple**: No repite vértices
    * **Ciclo**: Camino simple q empieza y termina en el mismo vértice
    * **Grafo Conexo**: Existe un camino para conectar cualquier par de vértices
    * **Árbol**: Grafo conexo y sin ciclos
    * **Grado**: Núm de aristas que inciden en un vértice. En los digrafos se divide en grado de entrada y grado de salida

## 2. Representación Interna en Memoria
| Estructura | Descripción | Ventajas / Inconvenientes |
| -- | -- | -- | 
| **Matriz de Adyacencia** | Matriz $m * n$ donde matAd[i][j] vale 1 si existe la arista y 0 si no. Es simétrica en grafos no dirigidos | **Rápida** para consultar si existe un eje entre $i$ y $j$. Consume más espacio en grafos dispersos
| **Lista de Adyacencia** | Vector de listas en el que cada posición almacena únicamente sus nodos adyacentes | **Eficiente en espacio** para grafos con pocos ejes (grafos dispersos). Insertar un eje toma tiempo $O(1)$

## 3. Algorítmo de Recorrido 
### Recorrido en Profundidad (DFS- Depth First Search)
* Análogo al recorrido en preorden de un árbol
* Explora el camino lo más lejos posible antes de retroceder (backtracking)
* Se implementa de forma **recursiva** marcando el estado en cada nodo (ej: Blanco para visitado y gris para no visitado, negro para visitado)
```cpp
// Esquema conceptual de DFS recursivo
void DFS_Visitar(int u, vector<vector<int>>& adj, vector<bool>& visitado) {
    visitado[u] = true;
    // Procesar nodo u

    for (int v : adj[u]) {
        if (!visitado[v]) {
            DFS_Visitar(v, adj, visitado);
        }
    }
}
```
### Recorrido en Anchura (BFS- Breadth First Search)
* Análogo al recorrido por niveles de un árbol
* Visita primero todos los vecinos inmediatos de un nodo antes de descender al siguiente nivel
* Se implementa de forma **iterativa** utilizando una **cola** (`deque` o `queue`) y un vector de visitados


```cpp
#include <iostream>
#include <vector>

using namespace std;

class GrafoMatriz {
    int V;
    vector<vector<int>> matAd;

public:
    GrafoMatriz(int V) : V(V), matAd(V, vector<int>(V, 0)) {}

    void insertarArista(int u, int v, int peso = 1) {
        matAd[u][v] = peso;
        // matAd[v][u] = peso; // Descomentar si el grafo fuera no dirigido
    }

    bool existeArista(int u, int v) {
        return matAd[u][v] != 0;
    }
};
```

## 4. Implementación en C++
### Matriz de Adyacencia
```cpp
#include <iostream>
#include <vector>

using namespace std;

class GrafoMatriz {
    int V;
    vector<vector<int>> matAd;

public:
    GrafoMatriz(int V) : V(V), matAd(V, vector<int>(V, 0)) {}

    void insertarArista(int u, int v, int peso = 1) {
        matAd[u][v] = peso;
        // matAd[v][u] = peso; // Descomentar si el grafo fuera no dirigido
    }

    bool existeArista(int u, int v) {
        return matAd[u][v] != 0;
    }
};
```

### Lista de Adyacencia
```cpp
#include <iostream>
#include <vector>

using namespace std;

class GrafoLista {
    int V;
    vector<vector<int>> adj; // Vector de vectores para la lista de adyacencia

public:
    GrafoLista(int V) : V(V), adj(V) {}

    void insertarArista(int u, int v) {
        adj[u].push_back(v);
        // adj[v].push_back(u); // Descomentar si el grafo fuera no dirigido
    }

    // Para obtener todos los vecinos inmediatos de u
    const vector<int>& obtenerVecinos(int u) {
        return adj[u];
    }
};
```