# Tipo Test Julio 2019

**1. [F]** Todos los contenedores de STL cuentan con un iterador que sobrecarga el `operador --` pero no todos sobrecargan el operador `++`

> **Explicación**: Los contenedores unidireccionales (como forward_list) solo sobrecargan ++ pero no --, por lo que no todos admiten el operador --

**2. [V]** Una cola estática puede implementarse de forma eficiente utilizando un vector

> **Explicación**: Usando una estructura circular con dos índices (frente y final), la inserción y extracción en un vector se realiza en tiempo constante ($O(1)$)

**3. [F]** Un heap permite obtener el dato con menor prioridad en $O(1)$.(Nota escrita: $\rightarrow$ $O(1)$ si es heap con menor prioridad, sino $O(\log n)$)

> **Explicación**: En un min-heap obtener el mínimo toma $O(1)$, pero si se busca el elemento de menor prioridad en un max-heap se requiere tiempo lineal ($O(n)$)

**4. [V]** Esta definición es válida para crear una matriz de punteros a listas de enteros `vector<vector<list<int> * > > v`;

> **Explicación**: La sintaxis declara correctamente un vector cuyas filas son vectores de punteros dirigidos a objetos de tipo list<int>

**5. [V]** Cuando un índice simple es modificado, los cambios son inmediatamente reflejados en el fichero donde se guarda el índice

> **Explicación**: Los índices simples guardan referencias directas a las posiciones del fichero, por lo que cualquier cambio se actualiza inmediatamente en disco

**6. [F]** Una inserción en un árbol AVL requiere a lo sumo una única rotación simple o doble.

> **Explicación**: Una inserción en un árbol AVL requiere como máximo una única rotación (simple o doble) para rebalancear toda la estructura

**7. [F]** El agrupamiento secundario en una tabla hash se produce cuando dos claves proporcionan distintas posiciones pero coinciden en la misma secuencia de búsqueda

> **Explicación**: El agrupamiento secundario ocurre cuando claves distintas tienen la misma dirección inicial por la función hash, no por coincidir durante la secuencia de exploración

**8. [V]** Si partimos de un vector con datos ordenados de menor a mayor, el proceso recursivo que tomaría como nodo raíz el centro del vector y como hijos izquierdo y derecho los subvectores que quedan a izquierda y derecha de dicho punto central, se obtendría un árbol binario compatible con AVL

> **Explicación**: Tomar recursivamente el elemento central como raíz genera subárboles con alturas que difieren como máximo en 1, cumpliendo la condición AVL

**9. [V]** La estructura interna de un quadtree (altura del árbol) puede verse afectada al insertar un nuevo dato

> **Explicación**: Insertar un dato en un nodo saturado fuerza su división en cuatro cuadrantes, modificando directamente la altura del árbol

**10. [V]** Una vez localizado un nodo en un árbol ABB y asignado un puntero, su borrado requiere tiempo constante

> **Explicación**: Teniendo acceso directo al puntero del nodo a eliminar, el reajuste de enlaces se realiza en tiempo constante ($O(1)$)

