# Preguntas Primitivas de Julio 2019

1. **Mostrar el estado del vector de soporte para un heap (prioridad los valores menores) al realizar las siguientes operaciones: `push(25)`, `push(12)`, `push(34)`, `push(5)`, `pop()`, `push(1)`, `push(6)`, `pop()`, `pop()`, `push(10)`**

> Resolución

1. push(25)
Se inserta el 25 en la raíz
```
25
```

2. push(12)
Se inserta 12 y flota al ser menor que 25

```
    12
   /
 25
```
3. push(34)
Se inserta 34 como hijo derecho de 12
```
    12
   /  \
 25    34
```

4. push(5)Se inserta 5 a la izquierda de 25 y va hasta la raíz (5 < 25 $\rightarrow$ 5 < 12)
```
     5
   /   \
 12     34
 /
25
```

5. pop()
Se elimina la raíz (5) y sube 25. Al hundirse, se intercambia con su hijo menor (12)
```
    12
   /  \
 25    34
 ```
6. push(1)Se inserta 1 a la izquierda de 25 y va la raíz (1 < 25 $\rightarrow$ 1 < 12)

```
     1
   /   \
 12     34
 /
25
```
7. push(6)
Se inserta 6 a la derecha de 12 y cambia una posición (6 < 12)
```
       1
     /   \
    6     34
   / \
 25   12
```

8. pop()
Se elimina la raíz (1) y sube 12. Se intercambia con el menor de sus hijos (6)

```
    6
   / \
 12   34
 /
25
```

9. pop()
Se elimina la raíz (6) y sube 25. Se hunde intercambiándose con su hijo menor (12)

```
    12
   /  \
 25    34
```

10. push(10)Se inserta 10 a la izquierda de 25 y va hasta la raíz (10 < 25 $\rightarrow$ 10 < 12)
```
     10
   /    \
 12      34
 /
25
```

2. 
(a) Crear el constructor de una lista doblemente enlazada circular a partir de los datos contenidos en un vector estático manteniendo el mismo orden: `ListaDEnlazada (VEstatico<T> &ve)`;

```
Vector 've': [ A | B | C | D ]

Lista resultante:
       +-------------------------------------------------+
       |                                                 |
       v                                                 |
  +---------+   sig   +---------+   sig   +---------+   sig  
  |    A    | ------> |    B    | ------> |    C    | ---+
  | (cabeza)| <------ |         | <------ |  (cola) | <--+
  +---------+   ant   +---------+   ant   +---------+   ant 
       ^                                                 |
       |                                                 |
       +-------------------------------------------------+
```


> Resolución

```cpp
template <typename T>
class Nodo{
    T dato;
    Nodo *sig;
    Nodo *ant;
    
    Nodo(const T &dato): dato(dato),sig(nullptr),ant(nullptr){}
}

template <typename T>
class ListaDEnlazada{
    private:
        Nodo<T> *cabeza;
        Nodo<T> *cola;
    public:
        ListaDEnlazada(VDinamico<T> &ve){
            cabecera=nullptr;
            cola=nullptr;
            int n=ve.tam();
            if(n==0)
                return;
            cabeza=Nodo<T>(ve[0]);
            cola=cabeza;
            
            for(int i=1;i<n;i++){
                Nodo<T> *nuevo= new Nodo<T>(ve[i]);
                cola->sig=nuevo;
                nuevo->ant=cola;
                cola=nuevo;
            }
            cola->sig=cabeza;
            cabeza->ant=cola;
        }

};
```
(b) Crear el constructor de un árbol binario de búsqueda a partir de los datos existentes en un vector estático ordenado de menor a mayor (referenciado anteriormente) de manera que el nodo raíz toma el valor de la posición central del vector. Su hijo izquierdo tomará la posición central del sub-vector izquierdo, y del mismo modo, el hijo derecho será el central del sub-vector que queda a la derecha. El proceso se repite de forma recursiva hasta que todos los datos del vector forman parte del ABB: `Abb (VEstatico<T> &ve)`;

```
Estructura de NodoArbol:
        +-------------------+
        |       dato        |
        +---------+---------+
        |   izq   |   der   |
        +----+----+----+----+
             |         |
             v         v

Constructor recursivo dividiendo por la mitad:
Vector 've': [ 10 , 20 , 30 , 40 , 50 , 60 , 70 ]
               0    1    2    3    4    5    6

              raiz -> [ 40 ] (centro, elem 3)
                     /      \
        izq (0 a 2) v        v der (4 a 6)
                 [ 20 ]    [ 60 ]
                 /   \      /   \
               [10] [30]  [50]  [70]
```

> Resolución

```cpp
template <typename T>
class Nodo{
    T dato;
    Nodo<T> *izq;
    Nodo<T> *der;

    Nodo(const T &dato): dato(dato), izq(nullptr), der(nullptr);
}

template <typename T>
class Abb{
    Nodo<T> *raiz;

    Nodo<T>* construirAux(VEstatico<T> &ve, int inicio, int fin){
        if(inicio>fin){
            return nullptr;
        }
        int medio=(inicio + fin)/2;
        Nodo<T> *nodo= new Nodo<T>(ve[medio]);

        nodo->izq=construirAux(ve,inicio,medio-1);
        nodo->der=construirAux(ve,inicio,medio+1);
        return nodo;
    }
}

public:
    Abb(VEstatico<T> &ve){
        int n=ve.tam();
        if(n==0)
            raiz=nullptr;
        raiz=construirAux(ve,0,n-1);
    }
```

