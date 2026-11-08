# Preguntas de Autoevaluación sobre STL (Lecciones  8-13)

### 1. El contenedor list<T> de STL implementa el operador [] para acceder directamente al dato almacenado en una posición arbitraria.

**Falso**

> **Explicación**: `std::list` está implementada como una lista doblemente enlazada y no admite acceso aleatorio, por lo que no incluye el operador `[]` ni el método `.at()`. Para acceder a una posición arbitraria hay que recorrerla elemento a elemento ($O(n)$).

---

### 2. Se ha pensado en implementar una matriz para almacenar todos los jugadores convocados en todos los partidos de todas las jornadas de la liga de fútbol. Esta sería una posible estructura de datos para crear dicha tabla: `vector<vector<vector<Jugador> > > jugadores;`

**Verdadero**

> **Explicación**: La estructura anidada de tres niveles permite organizar la información en tres dimensiones dinámicas: jornada `jugadores[i]`, partido de esa jornada `jugadores[i][j]` y lista de convocados `jugadores[i][j][k]`.

---

### 3. Para simular una lista circular doblemente enlazada (p.e. procesos de un S.O) en el que los datos entran siempre por el mismo lugar pero salen en cualquier momento es igualmente eficiente utilizar una lista (list) que un vector de STL

**Falso**

> **Explicación**: Borrar elementos en posiciones intermedias o arbitrarias de un `std::vector` requiere desplazar los elementos posteriores ($O(n)$), mientras que en `std::list` el borrado en un nodo dado se realiza desenlazando en tiempo constante ($O(1)$).

---

### 4. Se ha utilizado la siguiente estructura de datos para implementar un editor de texto interactivo: `list<vector<char> > texto;` La implementación de la operación pulsarTecla(char c) sería la siguiente: `i->insert(i->begin() + pos, c)`, siendo i un iterador de la lista que apunta a la línea donde se encuentra el cursor y pos un entero positivo que indica la posición del cursor en dicha línea.

**Verdadero**

> **Explicación**: Al usar el iterador `i`, se accede a un elemento de tipo `std::vector<char>`. Como los iteradores de `vector` son de acceso aleatorio, la expresión `i->begin() + pos` es totalmente válida e inserta el carácter en la posición del cursor dentro de la línea.

---

### 5. Sean dos conjuntos a y b de palabras, implementados usando dos vectores de STL instanciados al tipo string. Entonces obtener el vector c = a ∩ b (palabras que están en ambos conjuntos) requiere un tiempo cuadrático.

**Verdadero**

> **Explicación**: Al no estar los vectores ordenados, para cada elemento del primer vector de tamaño $n$ se requiere una búsqueda lineal en el segundo vector de tamaño $m$, acumulando un tiempo total de $O(n \times m) = O(N^2)$.

---

### 6. La inserción de un dato d al principio de un vector v de STL mediante v.insert(v.begin(), d) requiere tiempo O(1)

**Falso**

> **Explicación**: Insertar al principio de un `std::vector` obliga a desplazar todos sus elementos una posición hacia la derecha para hacer hueco en la memoria contigua, lo que requiere un tiempo lineal $O(n)$.

---

### 7. Un vector estático puede implementar eficientemente a pilas y colas estáticas

**Verdadero**

> **Explicación**: En una pila estática se controla el tope mediante un índice ($O(1)$) y en una cola estática se utiliza una estructura circular con dos índices (frente y final) evitando desplazamientos ($O(1)$).

---

### 8. Una lista simplemente enlazada puede implementar eficientemente a pilas y colas dinámicas.

**Verdadero**

> **Explicación**: En las pilas se inserta y elimina siempre por la cabeza ($O(1)$), y en las colas se inserta por el puntero al final (*rear*) y se elimina por la cabeza (*front*), logrando $O(1)$ en ambas operaciones.

---

### 9. Una deque puede implementar eficientemente a pilas y colas dinámicas.

**Verdadero**

> **Explicación**: `std::deque` está optimizado para inserciones y eliminaciones eficientes tanto por el principio como por el final ($O(1)$ amortizado), por lo que es la estructura por defecto usada por `std::stack` y `std::queue`.

---

### 10. Se usa una pila para resolver aquellos procesos recursivos que agotan la pila.

**Verdadero**

> **Explicación**: Convertir una recursión en un algoritmo iterativo mediante una pila explícita traslada la asignación de memoria desde el marco del sistema (*stack overflow*) a la memoria RAM dinámicamente gestionada (*heap*).

---

### 11. Una cola con prioridad siempre tendrá un push() en O(1) independientemente de la implementación concreta (vectores, vector de listas o listas de listas)

**Falso**

> **Explicación**: La complejidad de `push()` cambia según la estructura elegida; si la estructura interna se mantiene ordenada al insertar para agilizar las extracciones, el coste del borrado o inserción pasa a ser $O(n)$ u $O(\log n)$.

---

### 12. Una stack o una queue se implementa por defecto sobre un std:list pero se puede cambiar en ambos casos el contenedor

**Falso**

> **Explicación**: En la librería estándar de C++, el contenedor subyacente por defecto para ambos adaptadores es `std::deque`, no `std::list`.

---

### 13. Para hacer que una priority_queue de STL considere como dato más prioritario al mayor, se debe definir con el operator greater

**Verdadero**

> **Explicación**: En la plantilla de corrección oficial del examen se marca como verdadera asociando la palabra "mayor" al comparador `greater`. *(Nota de estándar C++: En C++ real, `priority_queue` es un Max-Heap por defecto usando `less`, mientras que `greater` genera un Min-Heap).*

---

### 14. Necesito una pila para eliminar la recursividad de la sucesión de Fibonacci: `int fibonacci(int n){ if(n==1 || n==2) return 1; else return fibonacci(n-1)+fibonacci(n-2); }`

**Falso**

> **Explicación**: La sucesión de Fibonacci se puede transformar a versión iterativa de forma óptima utilizando simplemente dos variables acumuladoras en un bucle ($O(n)$ en tiempo y $O(1)$ en memoria), sin necesidad de usar una pila.