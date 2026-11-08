# Memoria III

# EXAMEN EEDD Y ESTRUCTURAS DE DATOS — PREGUNTAS Y RESOLUCIONES

---

# Pregunta 1: Árbol Binario de Búsqueda y AVL

## Estructura del árbol

```text
       (5)
      /   \
    (4)   (9)
    /    /   \
  (1)  (7)   (17)
       /    /    \
     (6)  (13)   (19)
```

## Enunciado

Indica cuáles de las siguientes sentencias son ciertas:

- Es ABB.
- Si fuera AVL, el nodo 9 tiene factor de equilibrio -1.
- Era un AVL antes de insertar el dato 10.

## Respuestas correctas

- Es ABB.
- Si fuera AVL, el nodo 9 tiene factor de equilibrio -1.
- Era un AVL antes de insertar el dato 10.

## Explicación

El árbol cumple las propiedades de ordenación de un Árbol Binario de Búsqueda (ABB).

Además, en el diseño del ejercicio se considera la estructura previa a la inserción del dato 10 y el factor de equilibrio del nodo 9 bajo la variante de cálculo de la corrección del test.

---

# Pregunta 2: Operaciones y Rotaciones en Árboles AVL

## Estructura del árbol

```text
       (5)
      /   \
    (4)   (9)
    /    /   \
  (1)  (7)   (17)
       /    /    \
     (6)  (13)   (19)
```

## Enunciado

Indica cuáles de las siguientes sentencias son ciertas:

- Si inserto un 2, el nodo que se desequilibra es el 4 y el tipo de rotación es la 2.
- Si inserto un 16, el tipo de rotación es tipo 4 sobre el nodo 5.
- Si borro el 6 e inserto el 12, el tipo de rotación es tipo 3.

## Respuestas correctas

- Inserción del 2: nodo desequilibrado 4, rotación Tipo 2.
- Inserción del 16: rotación Tipo 4 sobre el nodo 5.
- Borrado del 6 e inserción del 12: rotación Tipo 3.

## Explicación

### Inserción del dato 2

Al insertar 2, se desequilibra el nodo 4:

`FE = +2`

La trayectoria es Izquierda-Derecha, por lo que corresponde una rotación doble de Tipo 2.

### Inserción del dato 16

Al insertar 16, se provoca un desequilibrio con raíz en el nodo 5 que requiere la rotación Tipo 4 (Derecha-Izquierda / Doble).

### Eliminación del 6 e inserción del 12

Al eliminar 6 e insertar 12, la reestructuración de alturas sobre las ramas desequilibradas activa una rotación de Tipo 3.

---

# Pregunta 3: Recorridos en Árboles Binarios

## Estructura del árbol

```text
       (5)
      /   \
    (4)   (9)
    /    /   \
  (1)  (7)   (17)
       /    /    \
     (6)  (13)   (19)
          /
        (10)
```

## Enunciado

Indica cuáles de las siguientes sentencias son ciertas:

- El recorrido en Postorden es el correcto para implementar el destructor.
- Para obtener la secuencia de datos ordenada de mayor a menor, lo que debo hacer es intercambiar los parámetros de las llamadas recursivas `(p->izq)` por `(p->der)` en el método de recorrido en Inorden.
- El recorrido en Postorden da la secuencia: `1, 4, 6, 7, 10, 13, 19, 17, 9, 5`.

## Respuestas correctas

- El recorrido en Postorden es el correcto para implementar el destructor.
- El recorrido Inorden inverso permite obtener los datos ordenados de mayor a menor.
- El recorrido en Postorden produce la secuencia `1, 4, 6, 7, 10, 13, 19, 17, 9, 5`.

## Explicación

### Recorrido Postorden

El Postorden libera primero los subárboles hijos antes que la raíz, siendo el estándar para destructores.

El orden de recorrido es:

1. Izquierda.
2. Derecha.
3. Raíz.

### Recorrido Inorden inverso

El Inorden inverso (Derecha, Raíz, Izquierda) procesa la secuencia en sentido descendente, de mayor a menor.

Para conseguirlo, se intercambia el orden de las llamadas recursivas.

**Inorden normal:**

```cpp
recorrer(p->izq);
procesar(p);
recorrer(p->der);
```

**Inorden inverso:**

```cpp
recorrer(p->der);
procesar(p);
recorrer(p->izq);
```

### Secuencia del recorrido Postorden

El Postorden evaluado secuencialmente en este árbol produce exactamente:

```text
1, 4, 6, 7, 10, 13, 19, 17, 9, 5
```

---

# Pregunta 4: Conversión a Lista Doblemente Enlazada Circular

## Estado inicial y estado circular

```text
Estado Inicial:              Estado Circular:

 [cab|cola]                     [cab|cola]
   |   |                          |   |
  (7)<->(9)                      (7)<--->(9)
  null  null                   ^           ^
  (ant) (sig)                  |___________|
```

## Enunciado

Indicad cómo convertir la lista en doblemente enlazada y circular conservando la cabecera y cola:

- `cola->sig = cab;`
- `cab->ant = cola;`
- `cola->ant->sig->sig = cab;`
- `cola->ant->ant = cola;`

## Respuestas correctas

Las cuatro sentencias son correctas.

### Primera forma

```cpp
cola->sig = cab;
cab->ant = cola;
```

### Segunda forma

```cpp
cola->ant->sig->sig = cab;
cola->ant->ant = cola;
```

## Explicación

En una lista circular doblemente enlazada con 2 nodos, el puntero `sig` de `cola` (nodo 9) debe apuntar al nodo `cab` (nodo 7), y el puntero `ant` de `cab` debe apuntar a `cola`.

Ambos bloques de sentencias realizan los enlaces cruzados de cierre de forma directa o navegada.

---

# Pregunta 5: Inserción por el Final en Lista Doblemente Enlazada

## Estado inicial y estado final

```text
 [cab|cola]                     [cab|cola]
    |    |                         |    |
   [  7  ]          -->           [ 7 ]<--->[ 9 ]
  null  null                     null        null
```

## Enunciado

Indicad las sentencias que insertan correctamente un dato por el final:

### Primera implementación

```cpp
cola->sig = new Nodo(cola, 9, nullptr);
cola->sig->ant = cola;
cola = cola->sig;
```

### Segunda implementación

```cpp
Nodo *p = new Nodo(cab, 9, nullptr);
p->ant->sig = p;
cola = p;
```

## Respuestas correctas

Ambos fragmentos son correctos.

## Explicación

Ambos fragmentos crean el nuevo nodo asignando como anterior el nodo previo (`cola` o `cab`, al haber un único elemento inicial), enlazan el puntero `sig` del nodo previo hacia el nuevo nodo 9 y actualizan el puntero `cola` hacia la nueva terminación.

---

# Pregunta 6: Liberación de Memoria / Eliminación Completa de la Lista

## Estructura inicial

```text
 [cab|cola]
   |   |
  (7)<->(8)<->(9)
```

## Enunciado

Indicad la forma correcta de eliminar todos los nodos de esta lista o de cualquier otra con un número indeterminado de datos.

## Respuestas correctas

### Primera implementación

```cpp
Nodo<T> *nodoAnt, *nodo = cab;

while (nodo != 0) {
    nodoAnt = nodo;
    nodo = nodo->sig;
    delete nodoAnt;
}
```

### Segunda implementación

```cpp
Nodo<T> *nodo = cab;

while (nodo != 0) {
    nodo = nodo->sig;
    delete cab;
    cab = nodo;
}
```

## Explicación

Ambos algoritmos recorren secuencialmente la lista almacenando la referencia al nodo actual/siguiente en un puntero auxiliar antes de invocar `delete`, garantizando que nunca se acceda a memoria destruida (dangling pointer).

---

# Pregunta 7: Eliminación de un Nodo Central

## Estructura inicial

```text
 [cab|cola]
   |   |
  (7)<->( 8 )<->(9)
          ^
          |
         (p)
```

## Enunciado

Indicad la forma correcta de eliminar el nodo apuntado por `p` en el caso genérico de que `p` apunte a un nodo central.

## Respuesta correcta

**Opción B.**

```cpp
p->ant->sig = p->sig;
p->sig->ant = p->ant;
delete p;
```

## Explicación

Se "puentea" el nodo `p` conectando el puntero `sig` de su predecesor (`p->ant`) directamente a su sucesor (`p->sig`), y el puntero `ant` de su sucesor (`p->sig`) hacia su predecesor (`p->ant`).

Una vez desacoplado del flujo bidireccional, se libera su memoria con:

```cpp
delete p;
```

---

# Pregunta 8: Implementación de Atributo Asociativo (UML a C++)

## Diagrama UML

```text
+-------------------+       relAB *      +-------------------+
|      claseA       |◆-------------------|      claseB       |
+-------------------+ 1     relBA        +-------------------+
|-claveA: Integer   |<-------------------| -claveB: Integer  |
+-------------------+                    +-------------------+
```

## Enunciado

Dado el UML, indicad las formas correctas de definir el atributo `relAB` si el contenedor asociativo elegido es un mapa.

## Respuesta correcta

**Opción C.**

```cpp
map<int, claseB> relAB;
```

## Explicación

Al tratarse de una relación de composición (rombo negro), los objetos componentes son gestionados directamente dentro del contenedor por valor (`claseB`), utilizando el identificador entero (`claveB`) como clave asociativa (`int`).

---

# Pregunta 9: Requisitos y Propiedades de `set<claseB>` en Composición

## Enunciado

Dado el diagrama UML y la elección `set<claseB> relAB;`, indicad todas aquellas respuestas que sean verdaderas.

## Respuestas correctas

### Opción A

También se podría hacer esta definición con un mapa del modo:

```cpp
map<int, ClaseB>
```

### Opción D

Esta definición es correcta, pero la clase `ClaseB` necesita definir el `operator<`.

## Explicación

### Opción A

Un `std::map<int, claseB>` representa adecuadamente la relación asociativa `1 → *`.

### Opción D

`std::set` implementa un árbol binario de búsqueda interno, por lo que exige que los elementos de tipo clase personalizada (`claseB`) tengan sobrecargado el operador de comparación `operator<` para ordenarlos e identificarlos.

---

# Pregunta 10: Definición de Atributo de Navegabilidad Inversa (`relBA`)

## Enunciado

Indicad la/s forma/s correcta/s de definir el atributo `relBA` dentro de `claseB`.

## Respuesta correcta

**Opción A.**

```cpp
claseA *relBA;
```

## Explicación

`relBA` representa una relación de asociación a 1 desde `claseB` hacia `claseA`.

En C++, la navegación simple a un objeto con ciclo de vida independiente se modela mediante un puntero al tipo de la clase destino (`claseA*`).

---

# Pregunta 11: Definición Genérica de Atributo Multiplicidad * (EEDD en UML)

## Enunciado

Dado el UML, indicad las formas válidas de definir el atributo `relAB` (sin restringirse a un contenedor específico de la STL o usando punteros nativos).

## Respuestas correctas

### Primera alternativa

```cpp
map<int, claseB*> relAB;
```

### Segunda alternativa

```cpp
claseB** relAB;
```

## Explicación

`map<int, claseB*>` permite almacenar una colección asociativa de punteros a instancias dinámicas de `claseB`.

`claseB**` representa la estructura nativa en C++ de un arreglo dinámico de punteros a objetos `claseB`.

---

# Pregunta 12: Gestión de Destrucción y Memoria en Composición con `std::vector`

## Estructura proporcionada

```cpp
class claseA {
    int claveA;
    std::vector<claseB*> relAB;
};

class claseB {
    int claveB;
    claseA *relBA;
};
```

## Enunciado

Indicad la opción correcta respecto a la gestión del espacio en memoria de las EEDD.

## Respuesta correcta

**No defino destructor ni en `claseA` ni en `claseB`.**

## Explicación

Según las especificaciones de diseño y las reglas estrictas asignadas en esta pregunta del examen, la respuesta marcada como correcta en el sistema es no definir destructor explícito en ninguna de las dos clases.
