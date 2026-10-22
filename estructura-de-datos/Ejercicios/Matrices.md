# Lección 5: Matrices y conjuntos de bits

> Las resoluciones de cada ejercicio se encuentran debajo del documento

**Contestar V/F las siguientes cuestiones.**
**1 [ ] El operador de asignación de la clase Matriz<T>::operator= debe siempre destruir la matriz destino de la asignación**

**2 [ ] El operador de la clase Matriz<T>::operator+= devuelve el objeto resultado por copia**

**3 [ ] La implementación de conjuntos mediante vectores realiza la intersección en tiempo lineal**

**4 [ ] El problema que poseen los conjuntos de bits es que el ID de un elemento debe ser un entero desde 0 hasta el tamaño del conjunto -1. Para convertirlo en un ID genérico se necesita otra EEDD.**

**5 [ ] Para almacenar 3841 datos en un conjunto de bits, debo crear un bufer de 480 bytes.**

**6 [ ] a.intersec(b+a) == a es correcto**

**7 [ ] El resultado de realizar esta operación: char mascara = 1 << (500 % 8); es 0000100**

## Ejercicios

1. Partiendo de esta definición del atributo m de la clase MiEstructura:
int ***m;
implementar el constructor de dicha clase para que sea:
a) una matriz (nxm) de punteros a enteros aleatorios
b) una matriz tridimensional (nxmxp) de enteros aleatorios
c) un puntero a una matriz (nxm) de enteros aleatorios

---
2. Implementar las operaciones 
```c
void Matriz2D<T>::anadirFila() y void Matriz2D<T>::anadirColumna() 
```
de la siguiente clase que implementa una matriz bidimensional:
```cpp
template<typename T>
class Matriz2D {
        int nfilas, ncolumnas;
        T** datos;
    public:
    Matriz2D(int nfilas, int ncolumnas): nfilas(nfilas), columnas(ncolumnas) {
    datos = new T*[nfilas];
    for (int f = 0; f < nfilas; ++f) {
    datos[f] = new T[ncolumnas];
    }
}
...
};
```
3. Implementar la función zoom- sobre la definición de la matriz Matriz2D anterior para que reduzca una imagen
almacenada en dicha matriz con k sucesivas compresiones de la imagen. En cada proceso de compresión, se toma
la media aritmética entera de cada 4 casillas vecinas 2x2 y se sustituye por una única casilla con ese valor medio.
Se lanza una excepción si nfilas %2^k !=0 ó ncolumnas %2^k!=0
```cpp
Matriz2D<T> Matriz2D::zoom- (k veces);
```

## Resolución

**1)**
Falso
El operador de asignación (`operator=`) no siempre destruye o libera la memoria de matriz de destino. Debe comprobar si se está realizando una **autoasignación** (evitar que a=a) y si las dimensiones de la matriz de destino coinciden con la de la matriz origen, pueden reutilizarse para copiar los nuevos datos sin destruir y volver a reservar memoria

---
**2)**
Falso
El operador `operator+=` modifica el objeto sobre el que se invoca y devuelve una referencia al propio objeto `Matriz&` y no una copia

---
**3)**
Falso
Si se implementa sobre vectores **sin ordenar** la inserción lleva un tiempo cuadrático $O(n^2)$ . Si estuviesen ordenado sería $O(n+m)$ ya que para ello tenemos que realizar una comparación elemento a elemento

---
**4)**
Verdadero

Los conjuntos de bits utilizan el índice del bit directamente como identificador del elemento, por lo que los valroes deben ser enteros consecutivos en el ango de 0 a $N-1$. Si se quierren guardar objetos complejos como claves o `string` necesitamos otra estructuras como tablas hash

---
**5)**
Falso

Para almacenar 3841 datos se necesitan 3841 bits. Como 1 byte equivale a 8 bits

$3841/8$ = 480.125 bytes

Dado que no se puede reservar fraccionamiento de bytes redondeamos hacia arriba, por lo que serían 481 bytes

---
**6)**
Veradero

b+a representa la **unión** : $b \cup a$. La intersección de cualquier conjunto $a$ con la unión de sí mismo con otro conjunto: ($a \cap (b \cup a)$) da siempre $a$ por la propiedad de la **absorción**

---
**7)**
Falso
500 (mod 8) = 4

`1<<4` desplaza el valor 1 (`0000001`) 4 posiciones a la izquierda -> (`00010000`) que equivale a 16

## Ejercicios
**1)**
a) Una matriz $(n \times m)$ de punteros a enteros aleatorios
`m` es una matriz bidimensional (un puntero doble `int***` -> array de filas de punteros `int**`)

```cpp
Matriz(int n, int m_cols) {
    // 1. Reservar array de 'n' filas de punteros a entero
    m = new int**[n];
    for (int i = 0; i < n; ++i) {
        // 2. Reservar 'm_cols' punteros a entero para cada fila
        m[i] = new int*[m_cols];
        for (int j = 0; j < m_cols; ++j) {
            // 3. Crear el entero dinámico e inicializarlo con un valor aleatorio
            m[i][j] = new int(rand());
        }
    }
}
```

b) Matriz tridimensional $(n \times m \times p)$ de enteros aleatorios

```cpp
Matriz(int n, int m_cols, int p) {
    // 1. Reservar 'n' planos (array de int**)
    m = new int**[n];
    for (int i = 0; i < n; ++i) {
        // 2. Para cada plano, reservar 'm_cols' filas (array de int*)
        m[i] = new int*[m_cols];
        for (int j = 0; j < m_cols; ++j) {
            // 3. Para cada fila, reservar 'p' enteros
            m[i][j] = new int[p];
            for (int k = 0; k < p; ++k) {
                m[i][j][k] = rand(); // Valor aleatorio
            }
        }
    }
}
```

c) Un puntero a una matriz ($n \times m$) de enteros aleatorios

```cpp
MiEstructura(int n, int m_cols) {
    // 1. Reservar espacio para el puntero principal que apuntará a la matriz
    m = new int**; 

    // 2. Reservar en *m las 'n' filas de la matriz
    *m = new int*[n];
    for (int i = 0; i < n; ++i) {
        // 3. Reservar 'm_cols' enteros para cada fila
        (*m)[i] = new int[m_cols];
        for (int j = 0; j < m_cols; ++j) {
            (*m)[i][j] = rand(); // Valor aleatorio
        }
    }
}
```

**2)**
```cpp
template<typename T>
void Matriz2D<T>::anadirFila() {
    // 1. Reservar nuevo array de filas con espacio para una fila más
    T** nuevosDatos = new T*[nfilas + 1];

    // 2. Copiar los punteros a las filas existentes
    for (int f = 0; f < nfilas; ++f) {
        nuevosDatos[f] = datos[f];
    }

    // 3. Reservar la nueva fila con 'ncolumnas' elementos (inicializados por defecto)
    nuevosDatos[nfilas] = new T[ncolumnas]();

    // 4. Liberar el array antiguo de punteros a filas y actualizar atributos
    delete[] datos;
    datos = nuevosDatos;
    nfilas++;
}

template<typename T>
void Matriz2D<T>::anadirColumna() {
    // Para añadir una columna, se debe redimensionar cada fila existente
    for (int f = 0; f < nfilas; ++f) {
        // 1. Crear nuevo array para la fila con espacio para la nueva columna
        T* nuevaFila = new T[ncolumnas + 1];

        // 2. Copiar los elementos de la fila antigua
        for (int c = 0; c < ncolumnas; ++c) {
            nuevaFila[c] = datos[f][c];
        }

        // 3. Inicializar la nueva casilla de la columna agregada
        nuevaFila[ncolumnas] = T();

        // 4. Liberar la fila antigua y asignar la nueva
        delete[] datos[f];
        datos[f] = nuevaFila;
    }

    // 5. Incrementar el contador global de columnas
    ncolumnas++;
}
```
**3)**

```cpp
#include <cmath>
#include <stdexcept>

template<typename T>
Matriz2D<T> Matriz2D<T>::zoom(int k) const {
    // 1. Calcular 2^k
    int divisor = std::pow(2, k);

    // 2. Validar que la dimensión sea divisible por 2^k
    if (nfilas % divisor != 0 || ncolumnas % divisor != 0) {
        throw std::invalid_argument("Las dimensiones de la matriz no son divisibles por 2^k");
    }

    // 3. Hacer una copia inicial de la matriz sobre la que trabajar
    Matriz2D<T> resultado = *this;

    // 4. Aplicar los k pasos sucesivos de reducción
    for (int paso = 0; paso < k; ++paso) {
        int filasActuales = resultado.nfilas;
        int colsActuales = resultado.ncolumnas;

        int nuevasFilas = filasActuales / 2;
        int nuevasCols = colsActuales / 2;

        // Crear la matriz reducida a la mitad en ambas dimensiones
        Matriz2D<T> reducida(nuevasFilas, nuevasCols);

        // Procesar cada bloque 2x2
        for (int i = 0; i < nuevasFilas; ++i) {
            for (int j = 0; j < nuevasCols; ++j) {
                // Media aritmética de las 4 casillas vecinas
                T suma = resultado.datos[2 * i][2 * j] +
                         resultado.datos[2 * i + 1][2 * j] +
                         resultado.datos[2 * i][2 * j + 1] +
                         resultado.datos[2 * i + 1][2 * j + 1];

                reducida.datos[i][j] = suma / 4;
            }
        }

        // Reemplazar el resultado actual con la versión reducida
        resultado = reducida;
    }

    return resultado;
}
```