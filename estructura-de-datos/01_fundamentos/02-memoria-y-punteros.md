# Memoria y Punteros en C++

### 1. La Memoria RAM

Es necesario entender el funcionamiento de la memoria ram para poder manejar correctamente punteros y memoria dinámica.

- La memoria RAM se divide en celdas donde se almacenan los distintos valores con su tipo de dato correspondiente, _int, float, double, char, string.._
- Cada casillero tiene un número de dirección único (por ejemplo, `0x7ffc82`).
- Cuando creas una variable, el sistema reserva uno de esos casilleros y le asigna el nombre de tu variable.

```text
  Dirección de Memoria       Variable      Valor Guardado
  ┌──────────────────┐      ┌─────────┐    ┌──────────┐
  │     0x7ffc81     │ ---> │  edad   │ -->│    20    │
  ├──────────────────┤      └─────────┐    └──────────┘
  │     0x7ffc82     │ ---> │  precio │ -->│   15.99  │
  └──────────────────┘      └─────────┘    └──────────┘
```

También es importante entender que no todos los tipos de dato ocupan el mismo espacio en memoria.

### 2. Tipos de datos y memoria

| Tipo de dato | ¿Qué almacena?                        | Memoria  |
| ------------ | ------------------------------------- | -------- |
| `int`        | Números enteros                       | 4 bytes  |
| `long`       | Números enteros grandes               | 8 bytes  |
| `float`      | Números decimales                     | 4 bytes  |
| `double`     | Números decimales con mayor precisión | 8 bytes  |
| `char`       | Un carácter Unicode                   | 2 bytes  |
| `bool`       | `true` o `false`                      | 1 bit    |
| `string`     | Texto                                 | Variable |

### 3. Operadores

**Operador dirección (&)**: Se coloca delante de una variable existente para obtener su dirección de memoria en formato hexadecimal. Significa "¿dónde está guardada esta variable?".

**Operador de desreferencia / indirección (\*)**: Se coloca delante de un puntero para acceder al contenido real ubicado en la dirección que este almacena. Significa "¿qué valor hay dentro de esa dirección?".

```text
& = Ubicación ("Encuentra la dirección").
* = Contenido ("Ve a la dirección y lee/modifica lo que hay dentro").
```

---

### 4. ¿Qué es un puntero?

Un puntero no es más que una variable cuyo valor es una dirección de memoria de otra variable

Si una variable entera guarda el número 42, un puntero guardará algo como 0x7ffc82.

Para declarar un puntero se coloca un asterisco \* entre el tipo de dato y el nombre del puntero:

```cpp
C++
int x = 20;       // Variable normal
int* ptr = &x;    // 'ptr' guarda la dirección de memoria de 'x'
```

#### Punteros nulos

Un puntero no inicializado contiene **basura de memoria** es decir apunta a una dirección aleatoria. Siempre que creemos un puntero sin asignarle una variable debemos incializarlo a `nullptr`

```cpp
int* p = nullptr; // Puntero seguro que apunta a 'nada'

if (p != nullptr) {
    std::cout << *p << std::endl; // Evitamos que pueda lanzar una excepción
}
```

#### Punteros Colgantes

Ocurre cuando un puntero apunta a una dirección de memoria que ya ha sido previamente eliminada

---

### 5. La organización de memoria : Estática vs Stack vs Heap

Hay tres zonas principales de memoria en c++

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│                                MEMORIA RAM                                   │
├─────────────────────────┬─────────────────────────┬──────────────────────────┤
│    MEMORIA ESTÁTICA     │       STACK (Pila)      │     HEAP (Montículo)     │
│ - Se asigna al compilar │ - Gestionado por CPU    │ - Gestionado a mano      │
│ - Variables globales    │ - Tamaño fijo y rápido  │ - Tamaño flexible        │
│ - Dura todo el programa │ - Estructura LIFO       │ - Acceso con punteros    │
└─────────────────────────┴─────────────────────────┴──────────────────────────┘
```

| Característica    | Memoria Estática                                    | El Stack (Pila)                                     | El Heap (Montículo)                            |
| ----------------- | --------------------------------------------------- | --------------------------------------------------- | ---------------------------------------------- |
| Gestión           | Automática por el sistema al arrancar el programa   | Automática por el compilador                        | Manual por el programador                      |
| Velocidad         | Muy rápida                                          | Extremadamente rápido                               | Más lento                                      |
| Duración de datos | Viven durante **toda** la ejecución del programa    | Viven solo mientras dure su función/ámbito          | Viven hasta que tú los elimines explícitamente |
| Asignación        | Variables fuera del `main` o marcadas como `static` | Variables locales declaradas normalmente (`int x;`) | Memoria dinámica reservada con `new`           |

### 6. Memoria dinámica

La Memoria Dinámica nos permite **reservar espacio en el Heap durante el tiempo de ejecución** (por ejemplo, cuando no sabemos de antemano cuántos elementos va a ingresar el usuario)

#### Reservar y Liberar Memoria Individual

```cpp
// 1. Reservar un entero en el Heap
int* p = new int(50); // Se crea el dato en el Heap y 'p' guarda su direccion

std::cout << *p << std::endl; // Imprime 50

// 2. Liberar la memoria cuando ya no se necesite
delete p;
p = nullptr; // Buena practica para evitar punteros colgantes
```

#### Reservar y Liberar Arrays Dinámicos

```cpp
int tamano = 5;
int* arreglo = new int[tamano]; // Reserva espacio para 5 enteros contiguos en el Heap

for (int i = 0; i < tamano; ++i) {
    arreglo[i] = (i + 1) * 10;
}

// Para liberar un array se usa delete[] con corchetes
delete[] arreglo;
arreglo = nullptr;
```

**Fugas de Memoria (Memory Leaks)** : Si usamos `new` sin poner `delete`, la memoria quedará bloqueada en la RAM hasta que se cierre la aplicación, lo que puede agotar toda la memoria del sistema

### 7. Paso por Valor vs. Paso por Referencia

Tenemos 3 maneras distintas

```cpp
#include <iostream>

// 1. Paso por VALOR: Se crea una COPIA. Modificar 'a' no afecta a la variable original.
void porValor(int a) {
    a = 5;
}

// 2. Paso por PUNTERO: Pasa la dirección. Modifica el valor original.
void porPuntero(int* a) {
    if (a != nullptr) {
        *a = 5;
    }
}

// 3. Paso por REFERENCIA (&): Alias directo a la variable original. Más limpio y seguro.
void porReferencia(int& a) {
    a = 5;
}

int main() {
    int x = 10;

    porValor(x);
    std::cout << x << std::endl; // Imprime 10 (sin cambios)

    porPuntero(&x);
    std::cout << x << std::endl; // Imprime 5

    porReferencia(x);
    std::cout << x << std::endl; // Imprime 5
}
```

---
