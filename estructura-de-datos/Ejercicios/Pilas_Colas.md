# Lección 9: Listas, Colas y Colas con Prioridad

## Test
Test de comprensión
Contestar V/F las siguientes cuestiones.
**1 [ ] Un vector estático puede implementar eficientemente a pilas y colas estáticas.**

> **Verdadero**
Un vector o array estático permite implementar pilas (insertado y eliminando al final con un entero como tope) y colas (mediante un vector circular) de forma eficiente en tiempo $O(1)$

**2 [ ] Una lista simplemente enlazada puede implementar eficientemente a pilas y colas dinámicas.**

> **Verdaero**
En una lista simplemente enlaza se puede insertar y borrar al principio en $O(1)$ (lo que permite implementar una pila) y manteniendo un puntero al último nodo , se puede insertar al final y borrar al principio en $O(1)$ (lo que permite una cola)

**3 [ ] Una deque puede implementar eficientemente a pilas y colas dinámicas.**


> **Verdadero**
El contenedor `deque` en la STL permite inserciones y borrados tanto por el principio como por el final en tiempo constante $O(1)$, por eso pilas y colas son una buena alternativa
 
**4 [ ] Se usa una pila para resolver aquellos procesos recursivos que agotan la pila.**

> **Verdadero**
La recursividad consume la pila de llamadas del sistema. Cuando se agota (provoca stack overflow), la solución habitual es transofmrar el algoritmo recursivo en iterativo, gestionando manualmente la pila de datos

**5 [ ] Una cola con prioridad siempre tendrá un push() en O(1) independientemente de la implementación concreta (vectores, vector de listas o listas de listas)**

> **Falso**
La complejidad de **push()** depende de la estructura interna. Por ejemplo, en una lista ordenada o vector ordenado, insertar un elemento manteniendo la prioridad requiere buscar su posición correcta, lo que toma tiempo lineal $O(n)$ en el pero de los casos

**6 [ ] Una stack o una queue se implementa por defecto sobre un std:list pero se puede cambiar en ambos casos el contenedor.**

> **Falso**
Por defecto en la STl, los adaptadores **std::stack** y **std::queue** se implementan sobre el contenedor **std::deque**, no sobre **std::list** (aunque se podría cambiar)

**7 [ ] Para hacer que una priority_queue de STL considere como dato más prioritario al mayor, se debe definir con el operator greater**

> **Falso**
Por defecto, **std::priority_queue** utiliza **std::less** (situa el elemento **mayor** en la cima (máxima prioridad)). Para hacer que el dato más prioritario sea el **menor**

**8 [ ] Necesito una pila para eliminar la recursividad de la sucesión de Fibonacci (Ejercicio 1)**

> **Falso**
Para eliminar la recursividad de Fibonacci no hace falta una pila S epuede cambiar a una función iterativa que mantenga los dos últimos valroes calculados utilizando solo dos o tres variables


## Ejercicios
**1. Eliminar recursividad al cálculo de la sucesión de Fibonacci:**
```cpp
int fibonacci(int n){
    if(n==1 || n==2)
        return 1;
    else
        return fibonacci(n-1)+fibonacci(n-2);
    }
```

**MODIFICACIÓN**
```cpp
int fibonacci(int n) {
    if (n <= 0) return 0;
    if (n == 1 || n == 2) return 1;

    int prev2 = 1; // Representa fibonacci(n-2)
    int prev1 = 1; // Representa fibonacci(n-1)
    int actual = 0;

    for (int i = 3; i <= n; ++i) {
        actual = prev1 + prev2;
        prev2 = prev1;
        prev1 = actual;
    }

    return actual;
}
```

**2. Usar una std:stack para mostar en pantalla los datos de una std:queue en orden inverso**

Transformamos de **FIFO** (First in , first out) a **LIFO** (last in , first out)

```cpp
#include <iostream>
#include <queue>
#include <stack>

void mostrarInverso(std::queue<int> cola) { // Pasada por copia para no modificar la original
    std::stack<int> pila;

    // Desapilamos de la cola y empujamos a la pila
    while (!cola.empty()) {
        pila.push(cola.front());
        cola.pop();
    }

    // Al extraer de la pila, saldrán en orden inverso
    while (!pila.empty()) {
        std::cout << pila.top() << " ";
        pila.pop();
    }
    std::cout << std::endl;
}
```

**3. Implementar la siguiente función que evalúa una expresión postfija devolviendo su valor usando una pila. En una expresion postfija el operador ocupa la posición después de los operandos. Un ejemplo de expresión infija es: (2+(3*4)) = x y su expresión postfija es 2 3 4 * + x = float evaluaPostfija(string &exp)**

Se recorre la expresión carácter a carácter, si es un número lo guardamos en la pila, si es un operador extraemos los dos últimos operandos , realizamo la operación y guardamos el resultado de nuevo

```cpp
#include <iostream>
#include <string>
#include <stack>

float evaluaPostfija(string &exp) {
    stack<float> pila;

    for (int i = 0; i < exp.length(); i++) {
        char c = exp[i];

        // Si es un espacio, lo ignoramos y seguimos
        if (c == ' ') {
            continue;
        }

        // Si es un número (entre '0' y '9')
        if (c >= '0' && c <= '9') {
            // Convertimos el char a número restándole '0'
            pila.push(c - '0');
        } 
        // Si es un operador (+, -, *, /)
        else {
            // Sacamos los dos últimos números de la pila
            float op2 = pila.top();
            pila.pop();
            
            float op1 = pila.top();
            pila.pop();

            // Hacemos la operación y guardamos el resultado
            if (c == '+') pila.push(op1 + op2);
            if (c == '-') pila.push(op1 - op2);
            if (c == '*') pila.push(op1 * op2);
            if (c == '/') pila.push(op1 / op2);
        }
    }

    // El resultado final es el único número que queda en la pila
    return pila.top();
}
```


**4. La clase Empleado, definida a continuación, establece una jerarquía en la empresa, de manera que un empleado tiene categorías del 1 al 5 para indicar al director general (categoría 1) y al empleado de mantenimiento (categoría 5). El resto de trabajadores poseen categorías intemedias. Un empleado también tiene un número de empleado que se les asígnó de forma correlativa según iban siendo contratados por la empresa desde sus inicios. Un empeado de contabilidad es el más antiguo actualmente con NumEmpl = 5 mientras que el director general es el 22. Definid la función de comparación CategorizarEmpleado para la gestión de los pedidos mensuales de material de oficina de modo que priorice en primer lugar a la categoría profesional y en segundo lugar al número de empleado.**

```cpp
class Empleado{
    int CatProf;
    int NumEmpl;
    };
    priority_queue <Empleado, CategorizarEmpleado> pedidos;
```


```cpp
#include <iostream>
#include <queue>

class Empleado {
public:
    int CatProf;
    int NumEmpl;

    Empleado(int cat, int num) : CatProf(cat), NumEmpl(num) {}
};

// Functor de comparación para la cola con prioridad
struct CategorizarEmpleado {
    bool operator()(const Empleado &a, const Empleado &b) const {
        // Si tienen distinta categoría, el de categoría mayor TIENE MENOS PRIORIDAD
        if (a.CatProf != b.CatProf) {
            return a.CatProf > b.CatProf;
        }
        // A igual categoría, el de mayor NumEmpl (menos antiguo) TIENE MENOS PRIORIDAD
        return a.NumEmpl > b.NumEmpl;
    }
};

// Declaración requerida en el ejercicio:
// std::priority_queue<Empleado, std::vector<Empleado>, CategorizarEmpleado> pedidos;
```