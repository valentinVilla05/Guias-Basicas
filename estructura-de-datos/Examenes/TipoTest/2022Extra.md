# Tipo Test de Julio 2022

**1. [V]** Las siguientes sentencias definen y crean un vector estático de punteros a enteros.
```cpp
int **p;
*p = new int [100];   
```

> **Explicación**: La variable p se declara en la pila (estática) como un doble puntero (`int**`), pero luego almacena la dirección de un bloque de memoria reservado en el heap (dinámico) con `new`

**2. [V]** Jesús ha tenido una buena idea al utilizar una matriz dispersa para establecer una correspondencia V/F entre todos los aeropuertos comerciales del planeta que tienen vuelos directos.   

> **Explicación**: La inmensa mayoría de aeropuertos del mundo no tienen conexión directa entre sí. Como casi todas las casillas estarían vacías, usar una matriz dispersa evita malgastar memoria frente a una matriz tradicional

**3. [V]** Esta sentencia tiene sentido que se incluya en la primitiva que elimina el nodo siguiente al apuntado por p en una lista simplemente enlazada:
```cpp
p->sig = p->sig->sig;
```

> **Explicación**: Al cambiar el puntero sig de p para que apunte al nodo que está dos posiciones por delante, se "salta" y desvincula directamente el nodo intermedio para eliminarlo

**4. [F]** Esta sentencia es correcta usando STL y produce los resultados esperados:
```cpp
list<int> l;
....
l.insert(l.begin() + 1, 100);   
```

> **Explicación**: Los iteradores de std::list son de acceso bidireccional, no aleatorio. Al no permitir aritmética de punteros, la expresión + 1 da error de compilación (habría que usar `std::next()`)

**5. [V]** Para recorrer árboles sin recursividad, se debería utilizar una pila para realizar un recorrido en postorden y una cola para hacer un recorrido por niveles o anchura.   

> **Explicación**: El recorrido por niveles (anchura) procesa nodos por orden de llegada mediante una cola (FIFO), mientras que el postorden requiere guardar nodos pendientes en una pila (LIFO) para procesar los hijos antes que el padre

**6. [V]** Una cola con prioridad puede ofrecer $O(n)$ en la inserción y $O(1)$ en el borrado.

> **Explicación**: Si se implementa internamente sobre una lista enlazada o vector ordenado, insertar requiere buscar la posición correcta en $O(n)$, pero borrar el elemento de mayor prioridad (el primero o el último) se hace en tiempo constante $O(1)$

**7. [F]** Los agrupamientos secundarios ocurren cuando $h(x1) \neq h(x2)$ y luego compiten por las mismas posiciones.

> **Explicación**: El agrupamiento secundario ocurre precisamente cuando dos claves distintas tienen el mismo valor hash inicial ($h(x1) = h(x2)$), lo que provoca que compartan toda la secuencia

**8. [F]** Un quadtree es por definición, un árbol de orden 4 equilibrado en altura.

> **Explicación:** Que sea un Quadtree solo garantiza que cada nodo interno tenga 4 hijos (orden 4), pero no exige que esté equilibrado; su altura depende de cómo se repartan los datos en el espacio

**9. [F]** Si se introducen datos ordenados de forma ordenada ascendente en un AVL, el tipo de rotación que se realizaría será siempre 3 o 4.

> **Explicación:** Al insertar datos en orden ascendente, el árbol se descompensa siempre hacia la derecha, por lo que solo se aplican rotaciones simples a la izquierda (que corresponden al caso 4, no al 3)

**10. [F]** No es posible albergar un millón de datos en un árbol B de orden 64 con tan solo 3 niveles (altura 2) pero sí con orden igual a 128

> **Explicación**: La capacidad máxima con orden $m$ y 3 niveles es $m^3 - 1$. Para $m=64$ es $64^3-1 = 262.143$ (no llega al millón) y para $m=128$ es $128^3-1 = 2.097.151$ (lo supera). Sin embargo, es falsa porque la pregunta evalúa la capacidad mínima garantizada por la regla del factor de carga ($m/2$) en árboles B, con la cual $128$ tampoco asegura alojar un millón en solo 3 niveles

