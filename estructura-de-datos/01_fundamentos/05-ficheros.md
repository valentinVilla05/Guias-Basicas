# Ficheros 
> En las primeras prácticas nos será útil recordar el manejo de ficheros , los cuales los usamos muy poco en las asignaturas anteriores

En C++ para manejar ficheros debemos instar la librería $<fstream>$ que proporciona estas tres clases:
* **ofstream**: Para escribir en ficheros (Output Stream)
* **ifstream**: Para leer ficheros (input stream)
* **fstream**: Para leer y escribir ficheros


## 1. Cabeceras Necesarias
```cpp
#include <iostream>
#include <fstream>  // Requerido para trabajar con ficheros
#include <string>   // Recomendado para manejar cadenas
using namespace std;
```

## 2. Apertura, Cierre y Comprobación de Estado
Para trabajar con un fichero **siempre** tenemos que verificar que el canal está disponible y cerrarlo adecuadamente 

### Apertura de fichero
Se utiliza mediante el método `.open()`

```cpp
// Opción A: Mediante el constructor
ofstream archivo("datos.txt", ios::out);

// Opción B: Mediante el método .open()
ifstream archivoEntrada;
archivoEntrada.open("datos.txt", ios::in);
```

### Comprobación de Estado (`is_open`)
* `archivo.is_open()`: Devuelve `true` si el fichero se encuentra abierto y vinculado a un flujo de datos válido; devuelve `false` si la apertura falló (no existe o simplemente no hay permisos)

```cpp
if (archivo.is_open()) {
    // Operaciones con el fichero...
} else {
    cerr << "Error: No se pudo abrir el fichero." << endl;
}
```

### Cierre de Fichero (`close`) y verificación
Una vez finalizadas las operaciones de lectura/escritura, es necesario liberar los recursos con `.close()`

```cpp
archivo.close();
```

Para asegurarnos de q se cerró correctamente o para comprobar si ya no está disponible podemos evaluar con `.is_open()`

```cpp
archivo.close();

if (!archivo.is_open()) {
    cout << "El fichero se ha cerrado correctamente." << endl;
}
```

## 3. Escritura de Ficheros (`ofstream`)
### Crear / Escribir un fichero de texto

```cpp
#include <iostream>
#include <fstream>

int main() {
    // Abre (o crea) el fichero "datos.txt" para escribir
    ofstream archivo("datos.txt");

    // Verificar si se abrió correctamente
    if (!archivo.is_open()) {
        cerr << "Error al abrir el archivo." << endl;
        return 1;
    }

    // Escritura usando el operador <<
    archivo << "Primera línea de texto." << endl;
    archivo << "Segunda línea con número: " << 42 << endl;

    // Cerrar siempre el fichero
    archivo.close();
    return 0;
}
```

## 4. Lecttura de ficheros(`ifstream`)
### Lectura línea por línea (`getline`)

```cpp
#include <iostream>
#include <fstream>
#include <string>

int main() {
    ifstream archivo("datos.txt");
    string linea;

    if (!archivo.is_open()) {
        cerr << "Error al abrir el archivo." << endl;
        return 1;
    }

    // Leer hasta el final del archivo (EOF)
    while (getline(archivo, linea)) {
        cout << linea << endl;
    }

    archivo.close();
    return 0;
}
```

### Lectura palabra por palabra
```cpp
ifstream archivo("datos.txt");
string palabra;

while (archivo >> palabra) {
    cout << "Palabra: " << palabra << endl;
}
archivo.close();
```

## 5. Control de Estado y Posicionamiento
### Métodos de Comprobación de Estado /Adicionales
* `archivo.fail()`: Devuelve true si ocurrió un error durante la apertura o una operación de lectura/escritura.

* `archivo.good()`: Devuelve true si el flujo está en un estado perfecto sin ningún error.

* `archivo.eof()`: Devuelve true si se alcanzó el final del fichero (End Of File).