# Templates

> Es esencial entender el funcionamiento de las templates ya que serán usadas para muchas de las estructuras lineales por tema de eficiencia

## 1. Conceptos

Una **plantilla** (`template`) es una herramienta de C++ que permite escribir código **genérico**, es decir sin especificar el tipo de dato con el que estamos trabajando, (`int`,`float`,`std::string`,`...`)

### ¿Cómo funciona realmente?

Es un mecanismo de **metaprogramación**, lo que quiere decir que el código no se compila directamente, sino que sirve como un **"molde"** para que el compilador genere el código real cuando se utiliza

## 1.2 El problema que resuelven

Imagina que tenemos que definir dos tipos de funciones que reciben números y tiene que determinar cual es mayor de ambos, en ese caso tenemos que programar dos funciones distintas:

```cpp
//Versión de enteros
int maximo(int a, int b){
    if(a>b)
        return a;
    return b;
}

//Versión para decimales
double maximo(double a, double b){
    if(a>b)
        return a;
    return b;
}
```

En este caso las funciones son cortas pero en caso de que tengamos que escribir mucho código llega un punto en el que es más eficaz definir una **función genérica** como:

```cpp
template <typename T>
T maximo(T a, T b) {
    if (a>b)
        return a;
    return b;
}
```

### Desventajas del código especificado:

- **Mantenimiento pesado**: Cualquier cambio en lógica obliga a modificar todas las sobrecargas
- **Ineficiencia**: Si tenemos 10 tipos de datos diferentes terminamos con 10 funciones idénticas

## 2. Plantillas de Funciones

### 1. Sintaxis básica

Se utiliza la palabra clave `template` seguida de la lista de parámetros entre corchetes angulares: `< >`

Si nos fijamos en el código anterior y lo analizamos poco a poco:

- `typename T` : Declara un parámetro de tipo (o tipo de dato abstracto) llamado T. Representa un tipo de dato que concretamos más adelante (en el main)

- `T a, T b`: Indica la creación de dos parámetros de tipo `T`

- `T maximo`: La función devuelve un valor del mismo tipo `T`

---

### 2. Instancia y Deducción de Tipos

El proceso mediante el cual el compilador genera una función real a partir de la plantilla se llama `instanciación`

### A. Deducción Implícita

El compilador deduce automáticamente el tipo `T` a partir de los argumentos pasados:

```cpp
int x = maximo(5, 10);        // El compilador deduce T = int y genera maximo(int, int)
double y = maximo(3.5, 2.1);  // El compilador deduce T = double y genera maximo(double, double)
```

### B. Especificación Explícita

Si los tipos de argumentos no coinciden o si deseas forzar un tipo concreto, se indica explícitamente entre `< >`

```cpp
auto z = maximo<double>(5, 3.14); // Convierte 5 a double y usa T = double
```

---

### 3. Múltiples Parámetros de Tipo

Si los argumentos pueden ser de tipos diferentes, se declaran más parámetros de tipo:

```cpp
template <typename T, typename U>
void imprimirPar(const T &primero, const U &segundo) {
    std::cout << "(" << primero << ", " << segundo << ")\n";
}

// Uso:
imprimirPar(10, "Hola"); // T = int, U = string
```

## 3. Plantillas de Clase (`Class Templates`)

> No solo podemos definir funciones de tipo genérico si no que también podemos definir clases de tipo `template`

### 1. Definición de una Clase Genérica

Permiten crear estructuras de datos y clases que operan sobre cualquier tipo de dato

```cpp
template <typename T>
class ContenedorSimple {
private:
    T elemento;

public:
    ContenedorSimple(T val) : elemento(val) {}

    T getElemento() const {
        return elemento;
    }

    void setElemento(T val) {
        elemento = val;
    }
};
```

### 2. Uso de Clase

> Importante: A diferencia de las funciones, al instanciar una plantilla de clase **siempre es obligatorio** indicar el tipo entre `< >`

```cpp
ContenedorSimple<int> miEntero(42);
ContenedorSimple<std::string> miTexto("Estructuras de Datos");

std::cout << miEntero.getElemento() << std::endl;
std::cout << miTexto.getElemento() << std::endl;
```

## 4. Compilación de plantillas

**IMPORTANTE** : La definición (implementación) de plantillas debe ser accesible en el archivo cabecera (`h`) **NUNCA** en el `cpp`

En el caso de que la declaración se realice en el cpp saltará un error: "Undefined Reference"

## 5. Non-type Parameters

Aparte de recibir tipos de datos (`typename T`), las plantillas pueden recibir valores constantes evaluables en tiempo de compilación: (_enteros, bools, enum..._)

```cpp
template <typename T, std::size_t N>
class ArrayEstatico {
private:
    T datos[N]; // El tamaño se fija en tiempo de compilación

public:
    std::size_t getTamano() const {
        return N;
    }

    T& operator[](std::size_t indice) {
        return datos[indice];
    }
};

// Uso:
ArrayEstatico<int, 5> miArray; // Crea un array estático de 5 enteros
std::cout << "Tamaño: " << miArray.getTamano() << std::endl;
```

- Ventaja : Podemos crear estructuras con memoria estática, es decir sin necesitar `new` ni `delete`

## 6. Especialización de Plantillas

Si lo requerimos podemos implementar una plantilla que funcione genéricamente de una forma pero si le pasamos un tipo de dato específico cambie su comportamiento

**Ejemplo de su implementación:**

```cpp
// 1. Plantilla genérica
template <typename T>
class Impresor {
public:
    static void imprimir(T valor) {
        std::cout << "Valor genérico: " << valor << std::endl;
    }
};

// 2. Especialización total para el tipo 'bool'
template <>
class Impresor<bool> {
public:
    static void imprimir(bool valor) {
        std::cout << "Valor booleano: " << (valor ? "Verdadero" : "Falso") << std::endl;
    }
};

// Uso:
Impresor<int>::imprimir(100);     // Usa la plantilla genérica -> "Valor genérico: 100"
Impresor<bool>::imprimir(true);   // Usa la especialización -> "Valor booleano: Verdadero"
```

## 7. Resumen y Buenas Prácticas

1. **Escribe y prueba primero con un tipo concreto (ej. int o double)** Si estamos haciendo una función o clase compleja podemos crear la clase específica para un tipo de dato y una vez funcione se puede trasladar a template sustituyendo el tipo de dato por `T` y añadiendo `template <typename T>`

2. **Todo en el .h**: En ningún momento necesitamos el cpp

3. **Usa nombre descriptivos para los tipos:** Si usamos un solo tipo debemos especificar bien los non-type parameters y los atributos que usemos para evitar confusiones.

4. **Cuidado con la sobrecarga de código:** Cada tipo con el que instancies la plantilla (`int`,`float`,`...`) generará un bloque de código ejecutable independiente.
