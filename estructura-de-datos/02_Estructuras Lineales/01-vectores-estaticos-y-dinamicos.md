# Vectores Estáticos y Dinámicos

En este capítulo analizaremos una de las estructuras de datos lineales más básicas y utilizadas en programación: los **arrays o vectores**, tanto estáticos como dinámicos

> Es importante comprender bien su funcionamiento, ya que muchas otras estructuras de datos se basan en ellos

## 1. Memoria Contigua

Un **vector (array)** es una colección finita de elementos del **mismo tipo**, almacenados en posiciones de memoria **contiguas**, es decir, una posición justo después de la otra.

### Representación en memoria

Por ejemplo, si tenemos un vector de `int`:

```text
Índice:          [0]      [1]      [2]      [3]
Dirección:     0x1000    0x1004   0x1008   0x100C
              ┌────────┬────────┬────────┬────────┐
Valor:        │   45   │   12   │   89   │   33   │
              └────────┴────────┴────────┴────────┘
```
### ¿Por qué es útil?
Como conocemos la dirección del primer elemento y el tamaño de cada elemento para obtener un dato no necesitamos recorrer todos los elementos anteriores para encontrar v[i] 

---
### 2. Complejidad Algorítmica

| Operación | Array | Vector |
|-------------|---------|-------------|
| Acceso por índice | O(1) | O(1)|
| Búsqueda (Desordenada) | O(n) | O(n)
| Insercción / Borrado al Final | No permitido | O(1)
| Inserción / Borrado al Inicio o Medio | No permitido | O(n) (tiene que desplazar elementos)
|

---

### 3. Array Estático vs Array Dinámico
Se diferencian en dónde y cuándo se reserva la memoria

* **Array Estático (Stack):** Tamaño fijo definido en tiempo de compilación
``` cpp
int notas[5] = {8, 9, 7, 10, 6}; // Reserva fija de 5 enteros
```

* **Array Dinámico (Heap):** Tamaño variable definido en tiempo de ejecución.
``` cpp
int tamano = 10;
int* arreglo = new int[tamano]; // Reserva en el Heap

// Liberación obligatoria al terminar
delete[] arreglo;
arreglo = nullptr;
```
---
### 4. Tamaño Lógico (tamal) vs. Tamaño Físico (tamaf)
En los vectores dinámicos debemos diferenciar dos conceptos:

* **Tamaño Físico (`tamaf` / `capacity`)**: Número total de posiciones reservadas en memoria RAM.

* **Tamaño Lógico (`tamal` / `size`)**: Es el número de datos que el usuario ha introducido y el que realmente se usa

Ejemplo:
``` text
V: [ 56 | 18 | 22 | 89 |    |    |    |    ]
   └─── tamal = 4 ────┘
   └─────────────── tamaf = 8 ──────────────┘
``` 

---
### 5. Redimensión Automática
Cuando el vector dinámico se llena (`capacity == size`) y queremos insertar un nuevo elemento:

1. **Ampliación (Duplicado)** : Creamos un nuevo bloque de memoria en el Heap con el doble de su capacidad **`capacity*2`**
2. **Copia**: Se transladan los datos del bloque antiguo al nuevo
3. **Liberación**: Se elimina el bloque antiguo con `delete[]`
4. **Inserción**: Se añade el nuevo elemento.

>Estrategia del $1/3$ para reducir el vector:
Para evitar estar creando y destruyendo memoria continuamente en el Heap cuando se inserta y borra consecutivamente al final, el vector solo reduce su capacidad a la mitad cuando el tamaño lógico baja a la tercera parte ($1/3$) del tamaño físico.
---
### 6. ¿Cuándo debemos usar un Vector?
Debemos usar los vectores cuando:
* Conozcamos el índice y queramos accesos inmediatos *O(1)*
* Las insercciones y borrados sean mayoritariamente al final *O(1)*
* Tengamos los datos ordenados y hagamos **búsquedas binarias** frecuentes *O(log n)*

Debemos **evitarlos** cuando:
* Necesitamos realizar constantes inserrciones y borrados en posiciones intermedias. En ese caso **Listas enlazadas**

---
### 7. Búsqueda Binaria
Es un algoritmo super eficiente para encontrar elementos en un vector pero exige una **condición: que el vector esté ordenado previamente**

#### Funcionamiento
En lugar de recorrer el vector de principio a fin **O(n)** aplica:
1. Compara el valor busado con el elemento del medio
2. Si coincide termina
3. Si es menor, descarta toda la mitad derecha y se queda con la izquierda
4. Si es mayor, descarta toda la mitad izquierda y se queda con la derecha
5. Repite el proceso hasta encontrarlo

Complejidad: **O(log2 (n))**
``` cpp
int busquedaBinaria(const int v[], int tamano, int datoBuscado) {
    int inf = 0;               // Límite inferior
    int sup = tamano - 1;      // Límite superior
    int medio;

    while (inf <= sup) {
        medio = (inf + sup) / 2; // Calculamos la posición central

        if (v[medio] == datoBuscado) {
            return medio; // ¡Encontrado! Retorna el índice
        } 
        else if (v[medio] < datoBuscado) {
            inf = medio + 1; // Buscar en la mitad derecha
        } 
        else {
            sup = medio - 1; // Buscar en la mitad izquierda
        }
    }

    return -1; // No encontrado
}
``` 