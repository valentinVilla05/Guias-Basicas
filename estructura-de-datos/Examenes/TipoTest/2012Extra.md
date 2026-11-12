# Tipo Test Septiembre 2012

**1. [V]** Una lista doblemente enlazada y circular puede considerarse una eedd lineal, de acceso secuencial y dinámica.

> **Explicación**: Verdadero: es lineal porque todos los datos están en un mismo nivel (uno detrás de otro), de acceso secuencial porque para llegar a un dato hay que pasar por los anteriores, y dinámica porque los nodos se crean y se borran en tiempo de ejecución sin reservar la capacidad por adelantado.

**2. [F]** Un dato almacenado en una lista dinámica nunca cambia en su ubicación en memoria, aunque se inserten o eliminen más datos en dicha lista.

> **Explicación**: Así está marcada en la hoja, pero ojo con esta: en una lista enlazada cada nodo vive en su propio sitio y al insertar o eliminar otros datos los nodos existentes no se mueven, así que la frase parece Verdadero. Es una duda razonable para preguntar en clase.

**3. [F]** Si la clase A tiene como atributo un vector de punteros a objetos tipo B, entonces entre ellos sólo puede existir una relación de asociación.

> **Explicación**: Falso: el vector de punteros no impide que la relación sea de COMPOSICIÓN. Si es la clase A la que crea y destruye los objetos B (el vector los almacena y A gestiona su ciclo de vida), hay composición. La palabra "sólo" es la que hace falsa la frase.

**4. [F]** Si P y Q son dos conjuntos de bits de tamaños 7 y 15 respectivamente, entonces P∪Q puede tener tamaño 10.

> **Explicación**: Falso: la unión contiene todos los elementos de Q, así que como mínimo tiene el tamaño del conjunto mayor, 15 (y como máximo 22). Nunca puede quedarse en 10.

**5. [F]** La operación pop() de un heap montado sobre un vector se puede mejorar eligiendo una lista de listas para dicha implementación del heap.

> **Explicación**: Falso: el vector ya permite localizar los hijos de cualquier posición i en O(1) con los índices 2i+1 y 2i+2. Con una lista de listas habría que recorrerla para llegar a cada hijo, así que pop() no mejoraría sino que empeoraría.

**6. [F]** Borrar un nodo de un árbol ABB de tamaño 1000 puede llegar a tener tan sólo un coste de T(1000)=2, es decir, visitando tan sólo 2 nodos.

> **Explicación**: Falso: T(1000) es el coste en el PEOR caso de borrar sobre 1000 nodos. Borrar exige localizar el nodo desde la raíz y, si tiene dos hijos, ir a buscar sucesor; con datos que degeneran el árbol en lista se recorren los 1000 nodos. Visitar 2 nodos no es el coste T(1000), sería como mucho un caso particular.

**7. [V]** Elisa lleva razón cuando dice que no va a usar una tabla hash para su aplicación porque, aunque necesita realizar búsquedas eficientes, también necesita realizar listados ordenados de datos.

> **Explicación**: Verdadero: la hash reparte las claves con su función de dispersión y no mantiene ningún orden. Cada listado ordenado obligaría a recorrer la tabla entera y ordenar el resultado (o a mantener una estructura adicional). Si los listados ordenados son habituales en la aplicación, la hash no le sirve sola y Elisa acierta en descartarla.

**8. [V]** Un grafo que representa carreteras nacionales puede considerarse un grafo ponderado, no dirigido y posiblemente cíclico.

> **Explicación**: Verdadero: cada arco puede llevar un peso (kilómetros, tiempo o peaje), se puede recorrer en ambos sentidos (no dirigido) y es posible que existan ciclos (rondas, retornos, encrucijadas). La palabra "puede" se cumple con claridad.

**9. [V]** Las posiciones de las gasolineras sobre un mapa se van a representar utilizando un Kd-tree. La búsqueda de dichas gasolineras en un rango [x1,y1][x2,y2] puede implicar la visita de nodos tanto a la izquierda como a la derecha del nodo raíz.

> **Explicación**: Verdadero: un Kd-tree parte el espacio con planos de división. Si el rectángulo de consulta cruza el plano que divide la raíz (el rango abarca ambos lados), hay que explorar los dos subárboles desde el principio, izquierda y derecha de la raíz.

**10. [V]** Un árbol B de orden 5 y altura 3 puede indexar 100 datos.

> **Explicación**: Verdadero: con orden 5 cada nodo admite hasta 5 claves y con altura 3 hay hasta 5³ hojas, es decir una capacidad máxima del orden de 5⁴ = 625 registros. 100 datos caben de sobra y, como la pregunta sólo dice "puede", basta con que exista esa configuración.
