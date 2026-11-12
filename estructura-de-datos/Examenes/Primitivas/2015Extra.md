# Primitivas examen 2015

**1. Dado el siguiente árbol B de orden 3, indicar la configuración del árbol tras la inserción/borrado de cada una de las siguientes claves: I(10), B(3), B(9), B(11), B(5).**

```text
    1|5|_
     / \
  1|3|_ 5|9|11
```
**1. `I(10)`**

```text
       1|5|10
      /  |   \
  1|3|_ 5|9|_ 10|11|_
```

**2. `B(3)`**
```text
      1|10|_
      /    \
  1|5|9   10|11|_
```

**3. `B(9)`**
```text
       1|10|_
      /    \
  1|5|_   10|11|_
```

**4. `B(11)`**

```text
1|5|10
```
**5. `B(5)`**

```text
1|10|_
```
**2. Implementar las siguientes operaciones de estructuras de datos, incluyendo todo el código necesario (no asumir llamadas a operaciones cuyo código no se detalle aquí).**   

**a) La operación void ListaEnlazada<T>::insertarFinal(VDinamico<T>& v) que inserta todos los elementos del vector $v$ al final de una lista simplemente enlazada** 

```cpp
template <typename T>
class NodoLista{
    public:
        T dato;
        NodoLista<T>* sig;
        NodoLista<T>* ant;

        NodoLista(T& d, NodoLista<T>* s=0, NodoLista<T>* a=0):
        dato(d),sig(s),ant(a){}
};
template <typename T>
class VDinamico{
    private:
        T* vec;
        int atm;
    public:
        int tamlog(){
            return tam;
        }
        T& operator[](int pos){
            return vec[pos];
    }
};

template <typename T>
class ListaEnlazada{
    private:
        NodoLista<T>* cabecera;
        NodoLista<T>* cola;
    public:
        ListaEnlazada(): cabecera(0), cola(0){}

        T& inicio(){
            return cabecera->dato;
        }

        void insertaFinal(T &dato{
            NodoLista<T>* nuevo=new NodoLista<T>(dato,0,cola);

            if(cabecera==0){
                cabecera=cola=nuevo;
            }else{
                cola->sig=nuevo;
                cola=nuevo;
            }
        }
        void insertaFinal(VDinamico<T>& v){
            for(int i=0;i<v.tamlog();++i){
                NodoLista<T>* nuevo= new NodoLista<T>(v[i],0,cola);

                if(cabecera==0){
                    cabecera=cola=nuevo;
                }else{
                    cola->sig=nuevo;
                    cola=nuevo;
                }
            }
        }
};
```

**b) La operación void MultiABB::insertar(T &dato) en un árbol binario de búsqueda que admite datos repetidos. Para soportar tal funcionalidad la clase nodo tiene la implementación indicada a continuación, que permite guardar todas las datos asociados a la misma clave. A la hora de comparar un dato con los contenidos en el nodo, usar cualquiera de la lista (e. g. el primero del todos)**

```cpp
template<class T>
class Nodo {
public:
    Nodo<T> *izq, *der;
    ListaEnlazada<T> datos;
    Nodo(T &ele): izq(0), der(0), datos()
        { datos.insertarFinal(ele); }
};
```

```text
o->5->5
    /   \
 o->3  o->9->9
          \
         o->10
```