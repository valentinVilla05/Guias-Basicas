# Examen de Julio 2022

2. Definid una función de dispersión cuadrática para una tabla de dispersión de tamaño 13 para insertar (I) / borrar (B) los siguientes datos:
`I(33), I(21), I(7), I(27), I(0), I(22), I(13), I(14), B(0), B(22), I(18), B(7), B(33), I(2)`.   Dibujad paso a paso el proceso (se pueden agrupar varios si no hay colisiones) dejando claro el estado de cada casilla. Determinar el valor de $\lambda$ máximo alcanzado y el dato con más colisiones 

> Resolución:

* **Tamaño de la tabla ($M$)**: $13$ (índices del 0 al 12)   

* **Función Hash inicial:** $h(x) = x \bmod 13$

* **Resolución de colisiones**: Dispersión cuadrática $\rightarrow$ Posición $k$-ésima = $(h(x) + k^2) \bmod 13$ (donde $k = 0, 1, 2, \dots$)

---
Paso 1:
`I(33)` $\rightarrow 33 \bmod 13 = 7$ (Sin colisión)

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---| ---| ---|---|---|---|---|---|---|---|----|----|----| 
| - | - | - | - | - | - | - | 33 | - | - | -  | - | - |

Paso 2:
`I(21)` -> 21mod13=8 (Sin colisión)

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---| ---| ---|---|---|---|---|---|---|---|----|----|----| 
| - | - | - | - | - | - | - | 33 | 21 | - | -  | - | - |

Paso 3: 
`I(7)` -> 7mod13=7
* Colisión en $7 + 1^2 = 8$ ($k=1$) $\rightarrow$ Ocupado por 21

* Prueba $7 + 2^2 = 11$ ($k=2$) $\rightarrow$ Libre

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---| ---| ---|---|---|---|---|---|---|---|----|----|----| 
| - | - | - | - | - | - | - | 33 | 21 | - | -  | 7  | - |


Paso 4: 
`I(27)` $\rightarrow 27 \bmod 13 = 1$ (Sin colisión)

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---| ---| ---|---|---|---|---|---|---|---|----|----|----| 
| - | 27 | - | - | - | - | - | 33 | 21 | - | -  | 7  | - |

Paso 5:
`I(0)` $\rightarrow 0 \bmod 13 = 0$ (Sin colisión)

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---| ---| ---|---|---|---|---|---|---|---|----|----|----| 
| 0 | 27 | - | - | - | - | - | 33 | 21 | - | -  | 7  | - |

Paso 6: 
`I(22)` $\rightarrow 22 \bmod 13 = 9$ (Sin colisión)

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---| ---| ---|---|---|---|---|---|---|---|----|----|----| 
| 0 | 27 | - | - | - | - | - | 33 | 21 | 22 | -  | 7  | - |

Paso 7:
`I(13)` $\rightarrow 13 \bmod 13 = 0$
* Colisión en 0 ($k=0$) $\rightarrow$ Ocupado por 0   

* Colisión en $0 + 1^2 = 1$ ($k=1$) $\rightarrow$ Ocupado por 27   

* Prueba $0 + 2^2 = 4$ ($k=2$) $\rightarrow$ Libre 

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---| ---| ---|---|---|---|---|---|---|---|----|----|----| 
| 0 | 27 | - | - | 13 | - | - | 33 | 21 | 22 | -  | 7  | - |

Paso 8:
`I(14)` $\rightarrow 14 \bmod 13 = 1$
* Colisión en 1 ($k=0$) $\rightarrow$ Ocupado por 27   

* Prueba $1 + 1^2 = 2$ ($k=1$) $\rightarrow$ Libre

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---| ---| ---|---|---|---|---|---|---|---|----|----|----| 
| 0 | 27 | 14 | - | 13 | - | - | 33 | 21 | 22 | -  | 7  | - |

**Punto de $\lambda_{\max}$: Aquí la tabla alcanza su ocupación máxima con 8 elementos: $\lambda_{\max} = \frac{8}{13} \approx 0,615$**

Paso 9:
`B(0)` $\rightarrow$ Borra el dato 0 en posición 0

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---| ---| ---|---|---|---|---|---|---|---|----|----|----| 
| `X` | 27 | 14 | - | 13 | - | - | 33 | 21 | 22 | -  | 7  | - |

Paso 10:
`B(22)` $\rightarrow$ Borra el dato 22 en posición 9

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---| ---| ---|---|---|---|---|---|---|---|----|----|----| 
| `X` | 27 | 14 | - | 13 | - | - | 33 | 21 | `X` | -  | 7  | - |

Paso 11:
`I(18)` $\rightarrow 18 \bmod 13 = 5$ (Sin colisión)

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---| ---| ---|---|---|---|---|---|---|---|----|----|----| 
| `X` | 27 | 14 | - | 13 | 18 | - | 33 | 21 | `X` | -  | 7  | - |

Paso 12:
`B(7)` $\rightarrow$ Borra el dato 7 en posición 11

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---| ---| ---|---|---|---|---|---|---|---|----|----|----| 
| `X` | 27 | 14 | - | 13 | 18 | - | 33 | 21 | `X` | -  | `X` | - |

Paso 13:
`B(33)` $\rightarrow$ Borra el dato 33 en posición 7

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---| ---| ---|---|---|---|---|---|---|---|----|----|----| 
| `X` | 27 | 14 | - | 13 | 18 | - | `X` | 21 | `X` | -  | `X` | - |

Paso 14: 
`I(2)` $\rightarrow 2 \bmod 13 = 2$
* Colisión en 2 ($k=0$) $\rightarrow$ Ocupado por 14   
* Prueba $2 + 1^2 = 3$ ($k=1$) $\rightarrow$ Libre

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---| ---| ---|---|---|---|---|---|---|---|----|----|----| 
| `X` | 27 | 14 | 2 | 13 | 18 | - | `X` | 21 | `X` | -  | `X` | - |


3. (a) Dada la definición de un árbol AVL<T> devolver el dato con el valor máximo albergado en dicho árbol en tiempo $O(\log n)$:

`T AVL<T>::datoMax ();`

> Resolución:

```cpp
template<typename T>
T AVL<T>::datoMax(){
    if(raiz==nullptr)
        throw std::invalid_argument("El árbol está vacío");

    Nodo *actual=raiz;
    while(actual){
        actual=actual->der; 
    }
    return actual->dato;
}
```
(b) Insertar un nuevo dato ndato en una lista doblemente enlazada con datos ordenados de forma ascendente para que mantenga este orden. La lista admite repetidos y se supone que ya está ordenada, por lo que no hay que comprobarlo de forma explícita, pero si se detectara que no lo está, se debería lanzar la excepción `NON_SORTED_LIST()`. **(Aviso: no deben usarse iteradores)**

`void ListaEnlazada<T>::insertaOrdenado (T &ndato);`


```cpp

template<typename T>
void ListaEnlazada<T>::insertaOrdenado(T &dato){
    // CASO 1 Lista vacía
    if(!cabecera){
        cabecera=new Nodo(ndato);
        return;
    }
    if(ndato<=cabecera->dato){
        Nodo *nuevo= new Nodo(ndato,cabecera,nullptr);
        cabecera->ant=nuevo;
        cabecera=nuevo;
        return;
    }
    Nodo *actual=cabecera;
    while(actual->sig != nullptr && actual->sig->dato < ndato){
        // Comprobamos si está desordenada
        if( actual-> dato > actual->sig->dato){
            throw NON_SORTED_LIST();
        }
        actual=actual->sig;
    }
    // Comprobación de orden final por si nos paramos antes de terminar
    if (actual->sig != nullptr && actual->dato > actual->sig->dato) {
        throw NON_SORTED_LIST();
    }
    // 4. Creamos e insertamos el nodo entre actual y actual->sig
    Nodo* nuevo = new Nodo(ndato, actual->sig, actual);

    if (actual->sig != nullptr) {
        actual->sig->ant = nuevo;
    }
    actual->sig = nuevo;
}
```
