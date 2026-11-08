# Relación de ejercicios 1: implementación de estructuras de datos

## 1. Vectores, listas, pilas, colas

1. Implementar una función recursiva que devuelva el máximo de un array de enteros.

```cpp
#include <iostream>
#include <vector>

int maximoRecursivoAux(const std::vector<int>& array, size_t indice){
    if(indice==array.size()-1){
        return array[indice]
    }
    int maxResto = maximoRecursivoAux(array, indice + 1);
    // Devolver el mayor entre el elemento actual y el máximo del resto
    return std::max(arr[indice], maxResto);
}

int maximoRecursivo(const std::vector<int>& array){
    if(array.empty()){
        throw std::invalid_argument("El array está vacío");
    }
    return maximoRecursivo(array,0);
}
```

2. Construir una clase VAjustado que herede de la clase Vdinamico estudiada en la teoría e incluya una operación ajustar() que sustituya el array utilizado internamente como soporte por un array con el tamaño justo para contener los elementos almacenados en el vector.

```cpp
template <typename T>
class VDinamico {
protected:
    T* v;
    int tamFisico
    int tamLogico; 

public:
    VDinamico(int cap = 10) : tamFisico(cap), tamLogico(0) {
        v = new T[tamFisico];
    }

    virtual ~VDinamico() {
        delete[] v;
    }

    void insertar(const T& elem) {
        if (tamLogico == tamFisico) {
            int nuevoTam = tamFisico * 2;
            T* nuevoV = new T[nuevoTam];
            for (int i = 0; i < tamLogico; ++i) nuevoV[i] = v[i];
            delete[] v;
            v = nuevoV;
            tamFisico = nuevoTam;
        }
        v[tamLogico++] = elem;
    }

    int getTamFisico() const { return tamFisico; }
    int getTamLogico() const { return tamLogico; }
};

template <typename T>
class VAjustado : public VDinamico<T> {
public:
    void ajustar() {
        if (this->tamFisico == this->tamLogico) return;

        T* nuevoV = nullptr;
        if (this->tamLogico > 0) {
            nuevoV = new T[this->tamLogico];
            for (int i = 0; i < this->tamLogico; ++i) {
                nuevoV[i] = this->v[i];
            }
        }

        delete[] this->v;
        this->v = nuevoV;
        this->tamFisico = this->tamLogico;
    }
};
```

3. Implementar una función que devuelva los 10 valores mayores de un array y calcular su tiempo de ejecución

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <ctime>
std::vector<int> obtener10Mayores(std::vector<int> arr) {
    std::sort(arr.begin(), arr.end(), std::greater<int>());

    std::vector<int> resultado;
    int limite = (arr.size()<10) ? arr.size() : 10;
    std::vector<int> resultado;
    int limite = (arr.size() < 10) ? arr.size() : 10;

    for (int i = 0; i < limite; ++i) {
        resultado.push_back(arr[i]);
    }

    return resultado;
}

// MAIN DE PRUEBA CON EL CLOCK
int main() {
    std::vector<int> datos;
    for (int i = 0; i < 1000000; ++i) {
        datos.push_back(rand());
    }
    clock_t inicio = clock();  // aquí se inicia el clock 
    std::vector<int> mayores = obtener10Mayores(datos);

    clock_t fin = clock();  // aquí se termina el clock 
    double tiempoTotal = double(fin - inicio) / CLOCKS_PER_SEC;

    std::cout << "Los 10 mayores son: ";
    for (int i = 0; i < mayores.size(); ++i) {
        std::cout << mayores[i] << " ";
    }
    std::cout << std::endl;

    std::cout << "Tiempo de ejecucion: " << tiempoTotal << " segundos." << std::endl;
    return 0;
}
```

4. Implementar una clase TresEnRaya que utilice un vector bidimensional de 10x10 para implementar el juego tres en
raya. Las operaciones a incluir serán:
* void fichaEnColumna(int columna, char jugador): deja caer la ficha del jugador en la columna indicada. La ficha caerá hasta la primera posición vacía de la columna.

* bool ganaJugador(int jugador): Indica si el jugador ha ganado.

```cpp

class TresEnRaya{
    private:
        char tablero[10][10];
    public:
        TresEnRaya() {
        for (int i = 0; i < 10; ++i) {
            for (int j = 0; j < 10; ++j) {
                tablero[i][j] = ' ';
            }
        }
    }
    // Cae la ficha hasta la primera casilla vacía desde abajo (fila 9 a 0)
    void fichaEnColumna(int columna, char jugador) {
        int fila = 9;
        bool colocada = false;

        while (fila >= 0 && !colocada) {
            if (tablero[fila][columna] == ' ') {
                tablero[fila][columna] = jugador;
                colocada = true; 
            }
            fila--;
        }
    }
    bool ganaJugador(char jugador) {
        // 1. Horizontales (filas)
        for (int f = 0; f < 10; ++f) {
            for (int c = 0; c < 8; ++c) {
                if (tablero[f][c] == jugador && 
                    tablero[f][c+1] == jugador && 
                    tablero[f][c+2] == jugador) {
                    return true;
                }
            }
        }
        // 2. Verticales (columnas)
        for (int f = 0; f < 8; ++f) {
            for (int c = 0; c < 10; ++c) {
                if (tablero[f][c] == jugador && 
                    tablero[f+1][c] == jugador && 
                    tablero[f+2][c] == jugador) {
                    return true;
                }
            }
        }
        // 3. Diagonales principales (\)
        for (int f = 0; f < 8; ++f) {
            for (int c = 0; c < 8; ++c) {
                if (tablero[f][c] == jugador && 
                    tablero[f+1][c+1] == jugador && 
                    tablero[f+2][c+2] == jugador) {
                    return true;
                }
            }
        }
        // 4. Diagonales inversas (/)
        for (int f = 0; f < 8; ++f) {
            for (int c = 2; c < 10; ++c) {
                if (tablero[f][c] == jugador && 
                    tablero[f+1][c-1] == jugador && 
                    tablero[f+2][c-2] == jugador) {
                    return true;
                }
            }
        }

        return false;
    }
};
```
5. Implementar la clase Bicola<T> que permite realizar inserciones y borrados tanto por el comienzo como por el final de una lista en tiempo constante. Utilizad para ello la representación interna de las listas doblemente enlazadas.

```cpp
template <typename T>
class Bicola {
private:
class Nodo {
        T dato;
        Nodo* sig;
        Nodo* ant;
        Nodo(const T& d, Nodo* s = nullptr, Nodo* a = nullptr) 
            : dato(d), sig(s), ant(a) {}
    };
    Nodo* primero; // Puntero al primer elemento
    Nodo* ultimo;  // Puntero al último elemento
    int tam;       // Número de elementos en la bicola

public:
    Bicola() : primero(nullptr), ultimo(nullptr), tam(0) {}

    ~Bicola() {
        while (!esVacia()) {
            borrarPrimero();
        }
    }

    bool esVacia() const {
        return tam == 0;
    }

    int getTam() const {
        return tam;
    }

    void insertarPrimero(const T& elem) {
        Nodo* nuevo = new Nodo(elem, primero, nullptr);
        
        if (esVacia()) {
            ultimo = nuevo;
        } else {
            primero->ant = nuevo;
        }
        
        primero = nuevo;
        tam++;
    }
    void insertarUltimo(const T& elem) {
        Nodo* nuevo = new Nodo(elem, nullptr, ultimo);
        
        if (esVacia()) {
            primero = nuevo;
        } else {
            ultimo->sig = nuevo;
        }
        
        ultimo = nuevo;
        tam++;
    }
    void borrarPrimero() {
        if (esVacia()) return;

        Nodo* aBorrar = primero;
        primero = primero->sig;

        if (primero == nullptr) { // Si la lista se queda vacía
            ultimo = nullptr;
        } else {
            primero->ant = nullptr;
        }

        delete aBorrar;
        tam--;
    }
    void borrarUltimo() {
        if (esVacia()) return;

        Nodo* aBorrar = ultimo;
        ultimo = ultimo->ant;

        if (ultimo == nullptr) { // Si la lista se queda vacía
            primero = nullptr;
        } else {
            ultimo->sig = nullptr;
        }

        delete aBorrar;
        tam--;
    }
    T getPrimero() const {
        return primero->dato;
    }
    T getUltimo() const {
        return ultimo->dato;
    }
};
```

