# Excepciones 
>Una **excepción** es una condición anómala o error que ocurre durante la ejecución de un programa (tiempo de ejecución). En lugar de que el programa se cuelgue o termine abruptamente debemos gestionar excepciones que permitan detectar los errores y transferir el control a un bloque especial de código y recuperre el error

## Cosas claves que necesitamos para excepciones:
* `try`: delimita un bloque de código que podría generar un error
* `throw`: Lanza la excepción cuando detecta una condición anómala
* `catch`: Intercepta y maneja la excepción lanzada por el bloque `try`

Ejemplo: 
```cpp
#include <iostream>
#include <stdexcept>

double dividir(double a, double b) {
    if (b == 0) {
        throw std::invalid_argument("Error: División por cero no permitida.");
    }
    return a / b;
}

int main() {
    try {
        double resultado = dividir(10.0, 0.0);
        std::cout << "Resultado: " << resultado << std::endl;
    } 
    catch (const std::invalid_argument& e) {
        std::cerr << "Excepción capturada: " << e.what() << std::endl;
    }
    catch (...) {
        std::cerr << "Captura cualquier otro tipo de excepción no especificado." << std::endl;
    }
    return 0;
}
```

## Jerarquía de Excepciones Estándar (<stdexcept>)
C++ incluye una jerarquía de clases base orientada a objetos para rperesentar errores comunes:

### Tabla Comparatica
| Clase | Descripción | Ejemplo de Uso | 
| -- | -- | -- |
| `std::invalid_argument` | Argumentos inválidos pasados a una función | Pasar un divisor igual a 0 | 
| `std::out_of_range` | Acceso a un índice fuera de los límites | Acceder a `std::vector::at(99)``en un vector de tamaño 5 |
| `std::bad_alloc` | Fallo en la asignación dinámica de memoria | Intentar reservar más RAM de la disponible con `new` |
| `std::runtime_error` | Errores detectables solo en tiempo de ejecución | Fallo de abrir un archivo o conexón de red | 

## Declaración de Clases Personalizadas
### 1. Forma Directa: Heredar de `std::runtime_error` 
Ya que gestiona el almacenamiento y retención del mensaje en formato string directamente
```cpp
#include <iostream>
#include <stdexcept>
#include <string>

// Heredamos de std::runtime_error
class ConexionBDException : public std::runtime_error {
private:
    int codigoError_;

public:
    // Pasamos el mensaje al constructor base de runtime_error
    ConexionBDException(const std::string& mensaje, int codigo)
        : std::runtime_error(mensaje), codigoError_(codigo) {}

    // Método extra para obtener datos contextuales del error
    int getCodigoError() const noexcept {
        return codigoError_;
    }
};

int main() {
    try {
        throw ConexionBDException("No se pudo conectar al servidor de base de datos", 504);
    } 
    catch (const ConexionBDException& e) {
        std::cerr << "Error BD [" << e.getCodigoError() << "]: " << e.what() << '\n';
    } 
    catch (const std::exception& e) {
        std::cerr << "Error general: " << e.what() << '\n';
    }
    return 0;
}
```

### 2. Forma Base: Heredar directamente de std::exception
```cpp
#include <iostream>
#include <exception>
#include <string>

class ArchivoNoEncontradoException : public std::exception {
private:
    std::string mensaje_;

public:
    explicit ArchivoNoEncontradoException(const std::string& nombreArchivo)
        : mensaje_("Error al abrir el archivo: " + nombreArchivo) {}

    // Sobreescritura requerida por la interfaz std::exception
    const char* what() const noexcept override {
        return mensaje_.c_str();
    }
};
```
## Buenas Prácticas:
* **Capturar por referencia constante**: Utilizar `catch  (const std::exception &e)` para evitar copias innecesarias
* **Uso del especificador `noexcept`: Indica al compilador que una función **promete no lanzar excepciones** Sirven para funciones destructoras o métodos clave que permiten optimiazaciones al compilador 
```cpp
void funcionInofensiva() noexcept {
    // Garantizado que no lanza excepciones
}
```
* **Ordenar los bloques `catch` de específico a general
```cpp
try {
    throw ConexionBDException("Timeout", 408);
}
catch (const ConexionBDException& e) {
    // 1. Captura primero la excepción más específica
}
catch (const std::runtime_error& e) {
    // 2. Luego captura clases intermedias
}
catch (const std::exception& e) {
    // 3. Finalmente la clase base general
}
```
