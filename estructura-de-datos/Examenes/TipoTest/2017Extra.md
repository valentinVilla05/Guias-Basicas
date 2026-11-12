# Tipo Test Julio 2017

**1. [V]** Los dos fragmentos de código mostrados a continuación reservan memoria para 10000 enteros pero el primero lo hace de una manera más rápida que el segundo.

```cpp
a) int* a = new int[10000];
b) int* a[100];
   for (int i = 0; i < 100; ++i) a[i] = new int[100];
```

> **Explicación**: Verdadero: los dos reservan 10000 enteros, pero a) hace UNA sola asignación de un bloque contiguo, mientras que b) hace 100 asignaciones pequeñas dispersas en memoria, con más overhead de gestión. Por eso el primero es más rápido.

**2. [V]** La siguiente implementación de `insertarFinal()` en un vector dinámico es correcta:

```cpp
void VectorDin<T>::insertarFinal(const T& dato) {
    if (tamLog == tamFis) {
        tamFis *= 2;
        T* tmp = new T[tamFis];
        for (int c = 0; c < tamLog; ++c) tmp[c] = mem[c];
        delete[] mem;
        mem = tmp;
    }
    mem[tamLog++] = dato;
}
```

> **Explicación**: Verdadero: comprueba si el vector está lleno (`tamLog == tamFis`), duplica `tamFis`, reserva un bloque nuevo, copia solo los `tamLog` elementos válidos, libera el bloque viejo con `delete[]` y finalmente añade el dato. Es la ampliación clásica correcta (ampliar, copiar, liberar lo viejo, insertar).

**3. [F]** Dadas dos listas simplemente enlazadas l1 y l2 de enteros ordenados de menor a mayor, es posible construir una lista también ordenada con todos los elementos de l1 y l2 en tiempo $O(n)$.

> **Explicación**: Así está marcada en la hoja del examen, pero ojo con esta: fusionar dos listas ya ordenadas es un recorrido lineal, $\mathcal{O}(n)$ (el mismo merge de mergesort, tomando siempre la menor de las dos cabezas). Es una duda razonable para preguntar en clase.

**4. [F]** Implementar un conjunto de enteros para el rango 100-100000 mediante un bitset requiere 1238 bytes.

> **Explicación**: Falso: el rango 100-100000 son 99901 enteros, es decir 99901 bits ≈ 12488 bytes ($99901 / 8$). Los 1238 bytes serían diez veces menos.

**5. [F]** La operación para determinar la hoja con mayor profundidad en un ABB no se puede implementar iterativamente.

> **Explicación**: Falso: sí se puede. Cualquier recorrido de árbol, incluido el que busca la hoja más profunda, se implementa con una pila explícita en lugar de la pila de llamadas del sistema.

**6. [V]** Dado el siguiente subárbol de un árbol AVL, para decidir si hay que realizar una rotación a izquierdas a nivel del nodo a (y el tipo, simple o doble) tras insertar un dato por su derecha es necesario conocer el factor de equilibrio del nodo a y el valor del dato almacenado en el nodo b.

> **Explicación**: Verdadero: el factor de equilibrio de a indica si la inserción deja el árbol como estaba (si estaba en 0 la altura no sube y no rota) o lo desequilibra (pasa a -2 y hay que rotar), y comparando el dato con el valor de b se ve por qué rama entra: por la izquierda de b haría una rotación doble, por su derecha una simple.

**7. [F]** El tipo de ordenación existente en los nodos en un ABB y en un heap es la misma. La diferencia es que los nodos del segundo se empaquetan en un vector en lugar de crearse individualmente en memoria dinámica.

> **Explicación**: Falso: el orden no es el mismo. En el ABB cada nodo separa los menores (izquierda) de los mayores (derecha); en el heap el orden es de PRIORIDAD entre padre e hijos (la raíz es la extrema) y no hay orden entre hermanos. Son propiedades distintas, más allá de la representación en vector o con punteros.

**8. [V]** Las operaciones de borrado e inserción a posteriori no deterioran una tabla de dispersión abierta, en contraste con lo que ocurre en las de dispersión cerrada.

> **Explicación**: Verdadero: en la abierta (encadenamiento) cada clave vive en la lista de su posición y borrar solo modifica esa lista: las búsquedas posteriores no se alargan. En la cerrada, los borrados dejan celdas BORRADO que hay que ir saltando en cada sondeo, y eso deteriora las búsquedas.

**9. [V]** Supongamos que utilizamos una rejilla regular para indexar espacialmente los restaurantes y bares de una ciudad, utilizando celdas de tamaño 500 m. Localizar los establecimientos situados a 100 m. a la redonda de la posición actual $(x, y)$ de un usuario se reduce a filtrar todos aquellos elementos situados en la celda que contiene la posición $(x, y)$ situados a una distancia menor de 100 m. de esta posición.

> **Explicación**: Verdadero: con celdas de 500 m y un radio de búsqueda de 100 m, la consulta queda circunscrita a la celda que contiene $(x,y)$: basta examinar esa celda y filtrar por distancia, sin recorrer la malla entera.

**10. [F]** Una búsqueda de un registro utilizando un índice simple es más eficiente que utilizando un árbol B.

> **Explicación**: Falso: el índice simple de búsqueda secuencial es $\mathcal{O}(n)$; el árbol B descarta niveles enteros en cada paso y se resuelve en $\mathcal{O}(\log n)$, además con muchos menos accesos a disco. El árbol B es el más eficiente de los dos.
