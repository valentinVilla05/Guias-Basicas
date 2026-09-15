# Árboles AVL

> Como hemos visto en el capitulo 07-Arboles, los árboles de busqueda binaria (ABB) normal tiene el problema de la degradación (si insertamos elementos ya ordenados el árbol se vuelve una línea recta y el proceso de búsqueda será mucho más lento)

Un **Árbol AVL** es un árbol ABB que se **auto-equilibra**:
* **Regla fundamental**: La diferencia entre la altura del subárbol izquierdo y derecho de cauqluier nodo **NO** puede ser emayor que 1

**Factor Equilibrio (bal)**:

>**bal(nodo) = altura(izq) - altura(der)**

* Si bal vale -1, 0 o 1: El nodo está **equilibrado** 
* Si bal vale -2 o 2: El nodo está **desaquilibrado** y hace falta arreglarlo con **rotaciones**
### Representación en C++
```cpp
template <typename U>
class Nodo {
public:
    Nodo<U> *izq, *der;
    U dato;
    char bal; // Factor de equilibrio (-1, 0, 1)

    Nodo(U &ele) : izq(0), der(0), bal(0), dato(ele) {}
};
```

## Las 4 Rotaciones Para Reequilibrar
Cuando Insertamos un dato y este rompe el equilibrio $(bal = +- 2)$, se arregla con una rotación de coste $O(1)$.

**Hay 4 casos posibles**:

1. **Rotación Simple a la Derecha**
    * Ocurre cuando insertamos en un nodo izquierdo otro nodo izquierdo  $bal(a) = 2$, $bal(izq(a)) = 1$).
    * Solución: El nodo hijo sube a ser el padre y el padre original baja a la derecha
![arbol_AVL](../assets/img/arbol_avl.gif)

2. **Rotación Simple a la Izquierda**
    * Ocurre cuando insertamos un nodo derecho en otro nodo derecho $bal(a) = -2$, $bal(der(a)) = -1$).
    * Solución: El nodo hijo sube a ser el padre y el padre baja a la izquierda
![Rotación_izq](../assets/img/rotacion_simple_izquierda.gif)

3. **Rotación Doble Izquierda-Derecha**
    * Ocurre cuando insertamos en el hijo derecho del hijo izquierdo $bal(k_3) = 2$, $bal(k_1) = -1$)
    * Solución: tenemos que rotar a la izquierda en el hijo y luego una a la derecha en el padre
![Rot_doble](../assets/img/rotacion_doble_izq_der.gif)
4. **Rotación Doble Derecha-Izquierda**
    * Ocurre cuando insertamos en el hijo izquierdo del hijo derecho $bal(k_1) = -2$, $bal(k_3) = 1$).
    * Solución: Hacemos primero una rotación a la derecha en el hijo y luego una a la izquierda en el padre
![Rot_dob_der](../assets/img/rotacion_doble_der_izq.gif)

### Impelmentación en C++: Rotaciones y Reajuste de Balances
El clálculo para actualizar la variable `bal` de los nodos rotados sin tener que recalcular la altura completa de los subárboles se hace así:
```cpp
template<typename T>
void Avl<T>::rotIzqda(Nodo<T>* &p) {
    Nodo<T> *q = p, *r;
    p = r = q->der;
    q->der = r->izq;
    r->izq = q;

    // Reajuste matemático de factores de balance
    q->bal++;
    if (r->bal < 0) q->bal += -r->bal;
    r->bal++;
    if (q->bal > 0) r->bal += q->bal;
}

template<typename T>
void Avl<T>::rotDecha(Nodo<T>* &p) {
    Nodo<T> *q = p, *r;
    p = r = q->izq;
    q->izq = r->der;
    r->der = q;

    // Reajuste matemático de factores de balance
    q->bal--;
    if (r->bal > 0) q->bal -= r->bal;
    r->bal--;
    if (q->bal < 0) r->bal -= -q->bal;
}
```

### Proceso y programación de Inserción
1. Insertamos el nodo como en un ABB normal, hasta llegar a una hoja
2. Subimos hacia la raíz, actualizando el balance de cada nodo.
3. Si algún nodo tiene bal = +2 o -2, está desequilibrado
4. Hacemos una rotación (simple o doble) para equilibrarlo
5. El subárbol queda equilibrado y terminamos.

```cpp
template<typename T>
int Avl<T>::inserta(Nodo<T>* &c, T &dato) {
    Nodo<T> *p = c;
    int deltaH = 0;

    if (!p) {
        p = new Nodo<T>(dato);
        c = p;
        deltaH = 1;
    }

    else if (dato < p->dato) {
        if (inserta(p->izq, dato)) {
            p->bal++;

            if (p->bal == 1)
                deltaH = 1;

            // CASO 1: Rotación Simple a la Derecha
            else if (p->bal == 2 && p->izq->bal == 1) {
                rotDecha(c);
            }

            // CASO 3: Rotación Doble Izquierda-Derecha
            else if (p->bal == 2 && p->izq->bal == -1) {
                rotIzqda(p->izq);
                rotDecha(c);
            }
        }
    }

    else if (dato > p->dato) {
        if (inserta(p->der, dato)) {
            p->bal--;

            if (p->bal == -1)
                deltaH = 1;

            // CASO 2: Rotación Simple a la Izquierda
            else if (p->bal == -2 && p->der->bal == -1) {
                rotIzqda(c);
            }

            // CASO 4: Rotación Doble Derecha-Izquierda
            else if (p->bal == -2 && p->der->bal == 1) {
                rotDecha(p->der);
                rotIzqda(c);
            }
        }
    }

    return deltaH;
}

```

## **Ejemplos**:
### Insercción de `3,2,1,4,5,6`
![secuencia](../assets/img/avl_secuencia_3_2_1_4_5_6.gif)

* Al insertar `1` ; Desequilibrio en `3` (bal=2). Rotación Simple Derecha, la raíz pasa a ser `2`
* Al insertar `4`: Árbol equilibrado
* Al insertar `5`: Desequilibrio en `3`(bal=-2). Rotación Simple Izquierda en subárbol `3`
* Al insertar `6`: Desequilibrio en raíz `2` (bal = -2). Rotación Simple Izquierda (*CASO 4*) en subárbol `3`

### Inserción de `7,16,15`:
![Secuencia2](../assets/img/avl_secuencia_7_16_15.gif)
* Al insertar `7` Desequilibrio en 5 : Rotación Izquierda
* Al insertar `13` no hay ningún problema
* Al insertar `15`: Inserción en hijo izq(`15`) del hijo derecho (`16`) del nodo `7`

## Borrado en Árboles AVL
1. **Búsqueda y Eliminación**: se busca y elimina el dato como en un ABB estándar (mirar lección 7)
2. **Propagación del Desequilibrio**: Se recorre el camino hacia atrás desde el nodo eliminado hasta la raíz comprobando la condición de balance
3. **Diferencia clave con la inerción**: Mientras que la inserción se resuelve con un máximo de 1 rotación, el **borrado puede requerir muchas rotaciones en cadena** a lo largo del camino ascendente a la raíz.
4. **Caso especial de borrado**: Además de las 4 rotaciones posibles, en el borrado se contempla un caso extra donde los dos hijos del nodo hermano tienen la misma altura $(bal =0)$, el cual se resuelve con una **rotación simple**

![BorradoAVL](../assets/img/eliminacion_avl.gif)

**Análisis de Eficiencia y Conclusiones**
*   Búsqueda: O(log n)
*   Inserción: O(log n) (Búsqueda: O(log n)+ Verificación de alturas O(1)+ Máximo 1  rotación O(1))
*   Borrado: O(log n) (Búsqueda: O(log n)+ Verificación y rotaciones en cadena O(log n))

## Limitaciones del AVL:
Los recorridos recursivos tradicionales del AVL no permiten iterar de forma eficiente hacia adelante o hacia atrás elemento a elemento. Por eso librerías como la **STL** suelen implementar **Árboles Rojo-Negro** en lugar del AVL, incluyendo punteros adicionales para facilitar iteradores bidireccionales y gestionar calves repetidas
