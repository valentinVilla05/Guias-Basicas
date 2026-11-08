# Test lecciones 12-13 Heaps, Cjtos. y Mapas

### 1. Un heap es un árbol binario que también está equilibrado en altura.

**Verdadero**

> **Explicación**: Un montículo (*heap*) se define estructuralmente como un **árbol binario completo** (o casi completo), lo que significa que todos los niveles están completamente llenos excepto posiblemente el último, que se llena de izquierda a derecha. Por construcción, la diferencia de altura entre cualquier par de ramas es como máximo **1**, por lo que satisface de forma estricta la condición de estar equilibrado en altura.

### 2. La siguiente sentencia: v["María"] = dato; es válida si v representa a un deque.

**Falso**

> **Explicación**: El contenedor `std::deque` en C++ es una secuencia lineal de acceso aleatorio que solo admite enteros como índices de posición (`v[0]`, `v[1]`, etc.). La sintaxis de indexación por clave asociativa mediante una cadena de texto (como `"María"`) requiere un contenedor asociativo (como `std::map` o `std::unordered_map`), por lo que no es una instrucción válida sobre un `deque`.

### 3. Si esta sentencia es válida:
```cpp 
int nuevoValor = 7; 
it=micontainer.find(clave); 
(*it).second[i] = &nuevoValor; 
```
Entonces micontainer puede tener esta definición: map <int, vector<int> >micontainer;

**Falso**

> **Explicación**: En el código se asigna `&nuevoValor` (que es la **dirección de memoria** o puntero a `int`, de tipo `int*`) a un elemento de `(*it).second[i]`. Si la definición fuera `map<int, vector<int>>`, el vector contendría valores de tipo `int` y no punteros `int*`, lo que provocaría un error de compilación por incompatibilidad de tipos. Para que la sentencia sea válida, la definición debería ser `map<int, vector<int*>>`.

### 4. Un heap permite obtener o leer el dato con menor prioridad en O(1).

**Verdadero**

> **Explicación**: En una implementación de montículo (*min-heap*), el elemento con la menor prioridad (o menor valor) se almacena siempre en la raíz de la estructura. Por lo tanto, consultar la raíz mediante la operación `top()` / `front()` permite obtener dicho elemento de forma directa e instantánea en tiempo constante $\mathcal{O}(1)$.

### 5. Si la clase ClassA tiene el siguiente atributo: map<string, *ClassB> atributo; entonces necesariamente la relación entre ClassA y ClassB es de asociación.

**Falso**

> **Explicación**: El uso de un puntero (`ClassB*`) como valor en una estructura de datos no determina de forma exclusiva una relación de **asociación**. En el diseño orientado a objetos, esta implementación también puede representar una relación de **agregación** (donde `ClassB` tiene vida independiente) o de **composición** (donde `ClassA` gestiona el ciclo de vida de los objetos dinamicos `ClassB` mediante dicho puntero). Al no ser *necesariamente* de asociación, la afirmación es falsa.

### 6. Si en el caso anterior el operator< ya está usándose para otro tipo de ordenación sobre ClaseA, entonces se puede usar la definición: set<ClaseA, comparaClaseA>, siendo comparaClaseA una clase de comparación para ClaseA

**Verdadero**

> **Explicación**: El contenedor `std::set` acepta un segundo parámetro de plantilla (*functor* o clase de comparación) que define el criterio de ordenación sin depender del `operator<` por defecto de la clase. Al pasar `comparaClaseA` (que implementa el operador `operator()` para la comparación estricta de dos objetos `ClaseA`), el `set` utiliza ese functor específico para ordenar los elementos, permitiendo aplicar un criterio de orden alternativo.

### 7. El contenedor de STL más adecuado para albergar las reservas de un restaurante para tener acceso a éstas por fecha es un mapa de la siguiente forma: multimap <Fecha, Reserva>

**Verdadero**

> **Explicación**: El contenedor `std::multimap` almacena los pares clave-valor automáticamente ordenados por la clave (`Fecha`) y permite asociar **múltiples reservas** a una misma fecha u hora. Esto facilita el acceso de búsqueda eficiente en tiempo $\mathcal{O}(\log n)$ y permite iterar sobre las reservas en rango cronológico directo.

### 8. El objecto mc se define como: map <int, miClase> mc; ¿se podría realizar la siguiente operación sobre mc? map<int, miClase>:: iterator it = mc. begin(); *(it).first = 5;

**Falso**

> **Explicación**: Hay dos errores conceptuales y sintácticos en la operación:
> 1. Las claves de un `std::map` son **constantes** (`std::pair<const Key, T>`) para evitar que se altere el orden del contenedor asociativo, por lo que no es posible modificar la clave a través de un iterador.
> 2. El operador de desreferencia `*` devuelve la pareja `std::pair`, por lo que el acceso correcto a sus miembros se realiza mediante `it->first` o `(*it).first`. La sintaxis `*(it).first` intenta desreferenciar erróneamente el miembro `first`.

### 9. La operación pop() es más eficiente en un heap que en una cola con prioridad montada mediante una lista de listas.

**Falso**

> **Explicación**: Si la **lista de listas** mantiene sublistas ordenadas por nivel de prioridad (o punteros directos a la sublista de mayor prioridad en la cabeza de la estructura), la extracción del elemento con mayor prioridad (`pop()`) se realiza en tiempo constante **$\mathcal{O}(1)$**. En cambio, en un **heap** la eliminación de la raíz requiere desencadenar un proceso de reajuste (*heapify* o hundimiento) a lo largo de la altura del árbol, lo que toma tiempo logarítmico **$\mathcal{O}(\log n)$**. Por tanto, la operación `pop()` en la lista de listas es más eficiente ($\mathcal{O}(1)$) que en el heap ($\mathcal{O}(\log n)$).

### 10. Implementar un heap mediante nodos y punteros al igual que el resto de árboles binarios tiene dos graves inconvenientes: consume mucha más memoria y la inserción en la siguiente posición libre del último nivel (durante los push) o el borrado de la última posición del último nivel (durante los pop) no podría implementarse en tiempo constante.

**Verdadero**

> **Explicación**: La representación secuencial en un vector (*array*) aprovecha las relaciones numéricas de los índices (hijo izquierdo a $2i+1$, hijo derecho a $2i+2$, padre a $\lfloor(i-1)/2\rfloor$) sin gastar memoria en punteros explícitos. Si un *heap* se implementara dinámicamente con nodos y punteros:
> 1. Consumiría sustancialmente **más memoria** por los punteros a hijo izquierdo, hijo derecho y padre de cada nodo.
> 2. Localizar el nodo padre de la **siguiente posición libre** para una inserción (`push`) o encontrar la **última hoja** para su borrado (`pop`) requeriría navegar por la estructura del árbol con un coste logarítmico $\mathcal{O}(\log n)$, a diferencia del acceso directo e instantáneo $\mathcal{O}(1)$ que permite el final de un vector.

### 11. La unión de dos conjuntos disjuntos de tamaños n y m puede llevarse a cabo mediante una operación en O(1)

**Verdadero**

> **Explicación**: Utilizando la estructura de datos para **Conjuntos Disjuntos** (*Disjoint Set Union* / *Union-Find*), la operación de unión entre dos conjuntos representados por árboles se realiza haciendo que la raíz de un árbol apunte a la raíz del otro. Si se cuenta con los punteros directos a los representantes/raíces de ambos conjuntos, la vinculación entre ellos consiste simplemente en actualizar un puntero, lo cual tiene un coste de tiempo constante $\mathcal{O}(1)$ independientemente de los tamaños $n$ y $m$ de los conjuntos.

### 12. La correspondiente definición de una matriz dispersa en STL según la Lección 7 es: vector <list <int> > matrizDis;

**Falso**

> **Explicación**: La definición `vector<list<int>>` solo almacenaría listas de enteros por cada fila, sin guardar la posición de la **columna** asociada a cada valor no nulo. Una representación válida de una matriz dispersa mediante contenedores de la STL debe almacenar explícitamente la columna y el valor (por ejemplo, utilizando un vector de mapas `vector<map<int, T>>` o un vector de listas de pares `vector<list<pair<int, T>>>`), o bien una clave compuesta para las coordenadas `map<pair<int, int>, T>`. Por tanto, `vector<list<int>>` es insuficiente e incorrecta para implementar una matriz dispersa.

### 13. La siguiente tabla referente a la eficiencia de las distintas implementaciones de una cola con prioridad es correcta (n es el número de datos y p el número de valores de prioridad distintos):

| Implementación | push | pop |
|---|---|---|
| vector de listas | $O(1)$ | $O(p)$ |
| lista de listas | $O(p)$ | $O(1)$ |
| heap | $O(\log n)$ | $O(\log n)$ |

**Verdadero**

> **Explicación**: La tabla refleja con precisión las complejidades temporales para cada estructura:
> - **Vector de listas**: Acceso indexado en $\mathcal{O}(1)$ por valor de prioridad para insertar al final de la lista correspondiente (`push`), y búsqueda lineal de la primera lista no vacía en el vector de $p$ prioridades ($\mathcal{O}(p)$) para extraer el elemento (`pop`).
> - **Lista de listas**: Requiere recorrer o mantener ordenada la lista de prioridades para la inserción ($\mathcal{O}(p)$), pero permite extraer directamente el primer elemento de la cabeza con máxima prioridad en $\mathcal{O}(1)$ (`pop`).
> - **Heap**: Tanto el ajuste tras la inserción (`push`) como la reestructuración tras el borrado de la raíz (`pop`) requieren recorrer la altura del árbol binario completo, ofreciendo una complejidad logarítmica $\mathcal{O}(\log n)$.

### 14. La operación busca() en conjuntos disjuntos es O y Ω(1)

**Falso**

> **Explicación**: La operación de búsqueda (`find` / `busca`) en una estructura de Conjuntos Disjuntos (*Disjoint Set*) no es estrictamente $\mathcal{O}(1)$ ni $\Omega(1)$ en el peor caso. Sin optimizaciones, el árbol representativo puede degenerar en un camino lineal de altura $n$, dando una complejidad de peor caso de $\mathcal{O}(n)$. Incluso al emplear las dos optimizaciones conjuntas de **unión por rango/tamaño** y **compresión de caminos**, la complejidad amortizada por operación es de $\mathcal{O}(\alpha(n))$, donde $\alpha$ es la función inversa de Ackermann, que aunque crece extremadamente despacio, matemáticamente no es una constante estricta $\mathcal{O}(1)$.

### 15. Un map definido como: <int, ClaseA> puede sustituirse por un set<ClaseA> si la clave entera forma parte de la clave ClaseA y esta tiene sobrecargado el operator< para realizar comparaciones por dicha clave

**Verdadero**

> **Explicación**: El contenedor `std::map<int, ClaseA>` organiza los pares clave-valor según el orden de la clave entera. Si el atributo entero de tipo clave ya está integrado dentro de la estructura/clase `ClaseA`, y `ClaseA` proporciona la sobrecarga del operador `operator<` comparando a través de dicha clave, un `std::set<ClaseA>` mantendrá exactamente el mismo ordenamiento estricto, unicidad de elementos y complejidad de búsqueda $\mathcal{O}(\log n)$, haciendo que la sustitución sea funcionalmente equivalente y más eficiente en memoria.