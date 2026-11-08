# Test lecciones 10-11 Árboles

### 1. En un árbol binario de búsqueda (ABB), un recorrido en inorden produce la secuencia de elementos ordenada de menor a mayor.

**Verdadero**

> **Explicación**: Por la propiedad fundamental de un ABB, el subárbol izquierdo contiene elementos menores que la raíz y el derecho elementos mayores. El recorrido en inorden procesa primero el subárbol izquierdo, luego la raíz y finalmente el subárbol derecho, produciendo siempre los elementos en secuencia estrictamente ascendente.

---

### 2. En un árbol de expresión binario, un recorrido en postorden permite obtener la notación posfija (polaca inversa) de la expresión.

**Verdadero**

> **Explicación**: El recorrido en postorden evalúa primero el hijo izquierdo, luego el hijo derecho y finalmente el nodo raíz (operador). Esto genera exactamente la notación en posfijo, donde los operandos preceden a sus respectivos operadores.

---

### 3. En un árbol AVL, la condición de equilibrio se calcula evaluando el número total de nodos a la izquierda y a la derecha de cada nodo.

**Falso**

> **Explicación**: La condición de equilibrio en un árbol AVL se evalúa atendiendo exclusivamente a la **altura** (profundidad máxima) de los subárboles izquierdo y derecho ($|FE| = |h_{izq} - h_{der}| \le 1$), y no al número total de nodos o descendientes que contenga cada subárbol.

---

### 4. Dado el siguiente árbol AVL, la inserción de 10 requiere una rotación doble a derecha.

```txt
    11
   /  \
  5    15
 / \   / \
1   8 12  20
     \
      9
```
**Falso**

> **Explicación**: Tras insertar el elemento **10** a la derecha del 9, el desequilibrio local se produce en el subárbol con raíz en el nodo **8** (camino Derecha-Derecha: $8 \rightarrow 9 \rightarrow 10$). Este desequilibrio se soluciona mediante una **rotación simple a la izquierda sobre el nodo 8**, dejando el árbol completamente equilibrado sin requerir una rotación doble.

---

### 5. Al insertar la siguiente secuencia en un ABB: {4, 3, 7, 12, 2, 6, 5, 13}, el borrado del 12 implica una llamada a la función borraMin()

**Falso**

> **Explicación**: El nodo **12** solo tiene un hijo (el nodo **13** a su derecha), ya que su subárbol izquierdo está vacío. Para eliminar un nodo con un solo hijo no se requiere buscar el mínimo con `borraMin()`; simplemente se reenlaza el padre (el nodo 7) directamente con su único nieto (el nodo 13).

---

### 6. En un árbol AVL tras una inserción el proceso de ajuste requiere a lo sumo una única rotación simple o doble.

**Verdadero**

> **Explicación**: A diferencia del borrado, al reestructurar un árbol AVL tras una inserción, una única rotación (simple o doble) restablece la altura del subárbol afectado a su valor previo a la inserción, garantizando que no se propaguen desequilibrios hacia la raíz.

---

### 7. Se pueden listar los datos de un árbol AVL o ABB en orden inverso a su definición sin necesidad de añadir un puntero al padre.

**Verdadero**

> **Explicación**: Basta con realizar un recorrido en inorden inverso (Derecha $\rightarrow$ Raíz $\rightarrow$ Izquierda) usando recursividad o una pila explícita (*stack*). La pila de llamadas mantiene el contexto de los ascendentes sin requerir punteros directos al padre.

---

### 8. Todo recorrido recursivo que opere sobre un ABB se puede resolver de forma iterativa mediante una pila de punteros a nodos de tipo ABB.

**Verdadero**

> **Explicación**: Cualquier algoritmo recursivo sobre árboles se puede transformar en iterativo simulando la pila de llamadas del sistema (*call stack*) mediante una estructura de datos de tipo pila (*stack*) que almacene los punteros a los nodos.

---

### 9. Para recorrer un árbol binario por niveles se necesita una cola. Este recorrido pasaría primero por la raíz, luego por raíz->izq, luego por raíz->der, raíz->izq->izq, raíz->izq->der, etc...

**Verdadero**

> **Explicación**: El recorrido por niveles (o búsqueda en anchura, BFS) requiere una **cola** (FIFO) para garantizar que se procesen los nodos en orden de profundidad, visitando de izquierda a derecha todos los nodos de un nivel antes de descender al siguiente.

---

### 10. Es posible que exista una secuencia de datos que al ser insertada en un árbol AVL no provoque rotaciones.

**Verdadero**

> **Explicación**: Si los datos se insertan en un orden tal que el árbol se mantiene naturalmente equilibrado en todo momento (por ejemplo, insertando la raíz mediana y luego progresivamente las medianas de los subárboles), el factor de equilibrio $|FE|$ nunca superará 1 y no se ejecutará ninguna rotación.

---

### 11. No es posible que un árbol AVL tenga un nodo hoja a una profundidad 4 y otra a profundidad 8.

**Falso**

> **Explicación**: Al acumularse los desequilibrios de altura permitidos ($|FE| \le 1$) a lo largo de ramas de distinta densidad, la profundidad entre distintas hojas del árbol puede diferir en más de un nivel en ramas lejanas, siendo posible tener hojas a profundidad 4 y 8 en un mismo AVL.

---

### 12. Dos árboles ABB equivalentes pueden tener diferente altura, raíz y hojas.

**Verdadero**

> **Explicación**: Dos ABB son equivalentes si contienen el mismo conjunto de datos (mismo inorden). Sin embargo, la topología del árbol (raíz, hojas y altura) depende exclusivamente del orden en el que se hayan insertado dichos elementos.

---

### 13. Los recorridos recursivos Preorden, Inorden y Postorden permiten iterar sobre los árboles hacia delante y detrás.

**Falso**

> **Explicación**: Los recorridos recursivos estándar son unidireccionales y siguen un orden estricto fijado por la secuencia de la pila. Para iterar en ambos sentidos (hacia adelante y hacia atrás) se necesitan iteradores bidireccionales explícitos o estructuras adicionales como árboles hilvanados (*threaded trees*).

---

### 14. En los árboles AVL las rotaciones garantizan que el número de descendientes por la izquierda y derecha de un nodo difiere a lo sumo en 1.

**Falso**

> **Explicación**: Las rotaciones AVL equilibran la **altura** (profundidad máxima del subárbol), no la cantidad total de **descendientes** o nodos a cada lado. Un subárbol puede tener muchos más nodos que otro si uno está lleno y el otro es ralo.

---

### 15. Si se introducen datos ordenados de forma ascendente en un AVL, el tipo de rotación que se realizaría siempre sería el caso 4.

**Verdadero**

> **Explicación**: Insertar elementos en orden estrictamente creciente genera desequilibrios continuos en el subárbol derecho (caso Derecha-Derecha), requiriendo repetidamente una rotación simple a la izquierda (clasificada académicamente como Caso 4 o Derecha-Derecha).

---

### 16. Conocer la altura de un ABB da información sobre el número de datos que contiene.

**Falso**

> **Explicación**: Al no estar balanceado por definición, conocer solo la altura $h$ de un ABB no permite determinar el número de nodos $N$, ya que un árbol de altura $h=4$ puede estar totalmente desequilibrado (lista con 5 nodos) o totalmente lleno (31 nodos).