# Sobre Carga de operadores
> Es esencial el manejo de operadores ya que necesitaremos programarlos apropiadamente, recordemos que C++ por defecto crea sus propios operadores en caso de que nosotros no lo programemos personalmente, sin embargo estos pueden dar conflico y simplemente no funcionar apropiadamente cuando estamos  tratando con memoria dinámica, por lo tanto es esencial programarlos correctamente

## ¿Qué es la sobrecaga de operadores?
Por defecto, C++ sabe cómo sumar dos números (5 + 3), pero no sabe cómo sumar dos objetos tuyos (por ejemplo, puntuacion1 + puntuacion2)

La sobrecarga consiste en escribir un método o función dentro de la clase usando la palabra clave operator seguida del símbolo que quieres programar

## Sintaxis General
```cpp
TipoRetorno operatorSímbolo(const TipoParametro& parametro) {
    // Código con la lógica personalizada
}
```

* `Tipo de Retorno`: Lo quedevuelve la operación (por ejemplo, `bool` para comparaciones u otro objeto para sumas)
* `operator`: palabra reservada **obligatoria**
* `Símbolo`: El operador q estamos sobrecargando (ej: `+`, `-`,`[]`,`==`..)

## Clasificación de Operadores
### 1. Operador de Comparación (`==`)
Sirve para definir cuando dos objetos de tu clase se consideran iguales

```cpp
class Punto {
public:
    int x, y;

    Punto(int x = 0, int y = 0) : x(x), y(y) {}

    // Sobrecarga de ==
    bool operator==(const Punto& otro) const {
        return (this->x == otro.x && this->y == otro.y);
    }
};

// Uso:
Punto p1(5, 10);
Punto p2(5, 10);

if (p1 == p2) { // Internamente ejecuta: p1.operator==(p2)
    // Se cumple porque x e y son iguales
}
```

> **Recordatorio:** Cuando estamos pasando parámetros por la cabecera si estos son grandes como clases, strings y demás debemos pasarlo como const tipodedato &parametro

### 2. Operador de Asignación (`=`)
Define como se copian los datos de un objeto a otro. **Es fundamental cuando la clase maneja memoria dinámica (punteros)** para evitar copias superficiales

```cpp
class Texto {
private:
    char* contenido;

public:
    // Sobrecarga del operador =
    Texto& operator=(const Texto& otro) {
        // 1. Evitar auto-asignación (ejemplo: t1 = t1)
        if (this == &otro) return *this;

        // 2. Liberar memoria previa
        delete[] contenido;

        // 3. Copiar los datos del nuevo objeto
        contenido = new char[strlen(otro.contenido) + 1];
        strcpy(contenido, otro.contenido);

        // 4. Retornar el objeto actual por referencia
        return *this;
    }
};
```

### 3. Operador de Acceso por Índice (`[]`)
Permite que un objeto se comporte como un arreglo o lista, accediendo a sus elementos mediante corchetes

```cpp
class Vector3D {
private:
    float coords[3]; // 0: X, 1: Y, 2: Z

public:
    Vector3D(float x, float y, float z) {
        coords[0] = x;
        coords[1] = y;
        coords[2] = z;
    }

    // Lectura y escritura: permite hacer miVector[0] = 5.0;
    float& operator[](int indice) {
        return coords[indice];
    }
};

// Uso:
Vector3D v(1.0, 2.0, 3.0);
v[0] = 10.5; // Cambia la coordenada X a 10.5
```

### 4. Operadores Aritméticos (`+`,`-`)
Permiten realizar operaciones matematicas entre instancias de clases
```cpp
class Contador {
public:
    int valor;

    Contador(int v) : valor(v) {}

    // Sobrecarga de +
    Contador operator+(const Contador& otro) const {
        return Contador(this->valor + otro.valor);
    }
};

// Uso:
Contador c1(10), c2(20);
Contador c3 = c1 + c2; // c3.valor será 30
```

### 5. Operador de Flujo / Salida (<<)
Para imprimir directamente tu objeto con `std::cout`, este operador se declara como una función `friend` (amiga) dentro de una clase

```cpp
#include <iostream>

class Persona {
    std::string nombre;
    int edad;

public:
    Persona(std::string n, int e) : nombre(n), edad(e) {}

    // Permite acceder a miembros privados e integrarse con cout
    friend std::ostream& operator<<(std::ostream& os, const Persona& p) {
        os << "Nombre: " << p.nombre << ", Edad: " << p.edad;
        return os;
    }
};

// Uso:
Persona p("Carlos", 25);
std::cout << p << std::endl; // Imprime: Nombre: Carlos, Edad: 25
```
### 6.  Operadores de Comparación relacionales (`<`, `>`, `!=`, `<=`, `=>`)
Para sobrecargas los oepradores relacionales de una clase, se retorna un valor booleano (`bool`). La práctica recomendada es marcar la función como `const` para garantizar q no se alteren sus datos

```cpp
class Persona {
public:
    int edad;

    Persona(int e) : edad(e) {}

    // Menor que (<)
    bool operator<(const Persona& otra) const {
        return this->edad < otra.edad;
    }

    // Mayor que (>)
    bool operator>(const Persona& otra) const {
        return this->edad > otra.edad;
    }

    // Menor o igual que (<=)
    bool operator<=(const Persona& otra) const {
        return this->edad <= otra.edad;
    }

    // Mayor o igual que (>=)
    bool operator>=(const Persona& otra) const {
        return this->edad >= otra.edad;
    }

    // Diferente de (!=)
    bool operator!=(const Persona& otra) const {
        return this->edad != otra.edad;
    }
};

// Uso práctico:
Persona p1(20), p2(30);

if (p1 < p2) {  // Imprime true porque 20 < 30
    // Lógica cuando p1 es menor que p2
}
```

## Sobrecarga Miembro vs Función Amiga (`friend`)
Existen dos formas de sobrecargar operadores en C++. La principal diferencia radica en quien es el operando de la izquierda en la expresión

### A. Como Función Miembro (Dentro de la Clase)
El objeto a la izquieda del operador es la instancia que llama al método (`this`), y el objeto a la derecha pasa como argumento

```cpp
class Numero {
public:
    int valor;
    Numero(int v) : valor(v) {}

    // Sobrecarga como MÉTODO MIEMBRO:
    // Toma 1 parámetro explícito (el de la derecha)
    Numero operator+(const Numero& otro) const {
        return Numero(this->valor + otro.valor);
    }
};

// Uso:
Numero n1(5), n2(10);
Numero n3 = n1 + n2; // Equivale a: n1.operator+(n2)
```

### B. Como Función Amiga (`friend`)
La función no pertenece al objeto, pero recibe permiso explícito para acceder a sus atributos privados o protegidos. **Toma dos parámetros**: el operando izquierdo y el operando derecho

#### ¿Cuando es obligatoria una función `friend`?
Cuando el lazo izquierdo del operador **no es un objeto de tu clase** 

```cpp
class Numero {
private:
    int valor;

public:
    Numero(int v) : valor(v) {}

    // Permite escribir: 10 + n1 (el número entero va a la izquierda)
    friend Numero operator+(int numeroIzquierda, const Numero& objDerecha) {
        return Numero(numeroIzquierda + objDerecha.valor);
    }

    // Permite usar cout << miObjeto
    friend std::ostream& operator<<(std::ostream& os, const Numero& obj) {
        os << obj.valor;
        return os;
    }
};

// Uso:
Numero n1(5);
Numero n2 = 10 + n1;  // Funciona gracias a la función friend (10 está a la izquierda)
std::cout << n2;       // Imprime: 15
```