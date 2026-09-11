# Notación Big-O

### ¿Qué es la notación Big-O?
La notación Big-O sirve para describir como aumenta el tiempo de ejecución o el uso de memoria de un algoritmo a mediad que crece la cantidad de datos de entrada

> **Punto clave:** La notación Big-O siempre mide el **peor caso posible**. Nos indica cuánto tardará el algoritmo en el escenario más desfavorable (por ejemplo, buscar un elemento y que esté en la última posición o no exista).

### ¿Por qué es necesario conocerla para la asignatura?
En estructura de datos necesitamos comprobar la eficiencia del código, programandolo con distintas estructuras puede variar el tiempo de ejecución, haciendolo más o menos eficaz.

---

### Tabla de Complejidades
| Complejidad | Ejemplo | Rendimiento |
|-------------|---------|-------------|
| **O(1)** | Acceder a un elemento de un array por índice |  Muy rápido |
| **O(log n)** | Buscar en un árbol binario equilibrado |  Rápido |
| **O(n)** | Recorrer todos los elementos de una lista |  Aceptable |
| **O(n log n)** | Ordenamiento eficiente, como Merge Sort |  Moderado |
| **O(n²)** | Comparar todos los elementos entre sí |  Lento |
| **O(2ⁿ)** | Algunos algoritmos recursivos |  Muy lento |
| **O(n!)** | Generar todas las permutaciones |  Extremadamente lento |

---
### ¿Qué indica la n?
En la notación Big-O, **$n$ representa la cantidad de datos de entrada** que va a procesar el código.

Ejemplo:
* Si le pasas a una función un vector con 10 elementos, el tamaño de entrada es **$n = 10$**.
* Si le pasas un vector con 1.000.000 de elementos, **$n = 1.000.000$**.

Es necesaria para medir cómo escala el programa: nos indica cómo aumenta el esfuerzo del algoritmo al multiplicar la cantidad de datos.

---

### ¿Cómo saber la complejidad algorítmica de nuestro código?
Para hacer una estimación es necesario aplicar el siguiente criterio:

#### 1. Ignorar las constantes
A la notación Big-O no le importan los números fijos que multiplican a la $n$. Un código que hace $2n$ operaciones se simplifica a **$O(n)$**.

#### 2. Observar el término que más crece
Si una función hace $n^2 + n + 5$ operaciones, nos quedamos solo con el término dominante: **$O(n^2)$**. Para valores grandes de $n$, el resto de términos apenas influyen.

#### 3. Sumar operaciones consecutivas
Si ejecutas instrucciones o bucles uno detrás de otro, sumas sus costes y te quedas con el mayor:
* Un bucle $O(n)$ seguido de otro bucle $O(n)$ da $O(n) + O(n) = O(2n) \rightarrow \mathbf{O(n)}$.


#### 4. Multiplicar estructuras anidadas
Si metes un bucle dentro de otro, multiplicas sus complejidades:
* Un bucle $O(n)$ dentro de otro bucle $O(n)$ da $O(n) \times O(n) = \mathbf{O(n^2)}$.

---

### Complejidad Temporal vs Complejidad Espacial

La notación big-O se aplica a dos recursos distintos e importantes de identificar.

1. **Complejidad Temporal:** mide el **tiempo/operaciones** que tarda en ejecutarse el algoritmo.

2. **Complejidad Especial:** mide la **memoria adicional** que se reserva.
    
    EJ: *variables, arreglos, llamadas recursivas...*

En el caso de que querramos crear una matriz auxiliar dentro de una función requiere una **complejidad espacial** de **O(n²)** lo que puede agotar la memoria del sistema en el caso que la entrada de datos **n** sea demasiado grande  

---

### Ejemplos con código 

#### 1. Complejidad constante -- O(1) --
Acceso directo o asignaciones. No importa cuánto crezca el vector, solo realiza una operación

```cpp
int x = 10;           // O(1)
std::cout << vec[0];  // O(1) -> Acceso directo por índice
```
#### 2. Complejidad lineal -- O(n) --
Un bucle simple que recorre un vector de inicio a fin
```cpp
for (int i = 0; i < n; i++) {
    std::cout << vec[i]; // Se ejecuta 'n' veces -> O(n)
}
```
#### 3. Complejidad cuadrática -- O(n²) --
Un bucle dentro de otro bucle (anidados).
```cpp
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        std::cout << i << ", " << j; // Se ejecuta 'n * n' veces -> O(n²)
    }
}
```
#### 4. Complejidad logarítmica -- O(log n) --
Bucles donde los datos se dividen a la mitad en cada paso
```cpp
for (int i = n; i > 0; i /= 2) {
    std::cout << i; // Divide los datos a la mitad en cada iteración -> O(log n)
}
```

#### 5. Complejidad cuasilineal -- O(n log n) --
Típica de algoritmos de ordenación eficientes (*MergeSort*). Se da cuando dividimos el problema a la mitad (O(log n)) y en cada nivel procesamos todos los elementos O(n).

```cpp

for (int i = 0; i < n; i++) {           // Se ejecuta 'n' veces
    for (int j = n; j > 0; j /= 2) {     // Se ejecuta 'log n' veces
        std::cout << vec[i];             // Total: n * log(n)
    }
}
```
#### 6. Complejidad exponencial -- O(2ⁿ) --
El tiempo de ejecución se duplica con cada nuevo elemento ($n$). Es común en algoritmos recursivos sin optimizar.
```cpp
int fibonacci(int n) {
    if (n <= 1) return n;
    // Cada llamada genera 2 llamadas más -> 2^n operaciones
    return fibonacci(n - 1) + fibonacci(n - 2); 
}
```
#### 7. Complejidad factorial -- O(n!) --
El rendimiento se desploma por completo. Ocurre cuando debemos probar todas las permutaciones posibles de un conjunto
```cpp
// Ejemplo: calcular de cuantas formas distintas se pueden sentar n personas en una mesa 
// Si n = 3 personas (A, B, C), hay 3! = 6 combinaciones.
// Si n = 4 personas, hay 4! = 24 combinaciones.
// Si n = 20 personas, hay más de 2 trillones de combinaciones

void ordenarMesa(std::string personas, std::string resultado) {
    if (personas.empty()) {
        std::cout << resultado << std::endl; // Imprime una combinación
        return;
    }
    // Genera las n! posibilidades probando todas las opciones
    for (int i = 0; i < personas.length(); i++) {
        ordenarMesa(personas.substr(0, i) + personas.substr(i + 1), resultado + personas[i]);
    }
}
```