# Primitivas de Junio de 2012

**1. Indicar de que manera evolucionaría un árbol binario de búsqueda de enteros durante la inserción/borrado de los siguientes datos: I(6), I(2), I(4), I(10), I(1), I(15), I(14), I(3), I(5), I(8), B(15), B(6). Mostrar el estado del árbol cada 3 operaciones**

**Estado 1: `I(6)`, `I(2)`, `I(4)`**

```text
    6
   /
  2
   \
    4

```

**Estado 2: `I(10)`, `I(1)`, `I(15)`**
```text
      6
     / \
    2   10
   / \    \
  1   4    15
```

**Estado 3: `I(14)`, `I(3)`, `I(5)`**
```text
        6
       / \
      2   10
     / \    \
    1   4    15
       / \   /
      3   5 14
```

**Estado 4: Tras `I(8)`, `B(15)`, `B(6)`**

> EN ESTE PODEMOS TOMAR 2 OPCIONES

**Opción A: Sustituyendo la raíz por el mayor de los menores (el 5) (Criterio más habitual):**
```text
        5
       / \
      2   10
     / \  / \
    1   4 8  14
       /
      3
```

**Opción B: Sustituyendo la raíz por el menor de los mayores (el 8):**
```text
        8
       / \
      2   10
     / \    \
    1   4    14
       / \
      3   5
```
----

**2. Dada la siguiente definición de una tabla de dispersión cerrada de enteros con función de dispersión por división y resolución de colisiones mediante exploración lineal, implementar la operación existe(), que devuelve true si el dato existe en la tabla**

```cpp
#define TAM_TABLA 1003
struct PosicionEnt {
    int dato;
    char estado; // Puede ser "D" (disponible), "B" (borrado), "S" (borrado especial)
};
class DispCerradaEnt {
    PosicionEnt tabla[TAM_TABLA];

    int hash(int dato) { return pos% TAM_TABLA; }
public:
    bool existe(int dato);
    ...
};
```

> Resolución

```cpp
bool DispCerrada::existe(int dato){
    int posInicial=hash(dato);
    int pos=posInicial;

    do{
        // Si encontramos un hueco que nunca ha sido ocupado ponemos D
        if (tabla[pos].estado=="D"){
            return false;
        }
        // Si la celda está ocupada (O o cualquier estado que no sea D ni B o S y coincide con el dato, entonces lo hemos encontrado)
        if(tabla[pos].estaod!='B' && tabla[pos].estado!='S' && tabla[pos].dato==dato){
            return true;
        }
        // Avanzamos a la siguiente pos
        pos = (pos +1 ) % TAM_TABLA
        // TENEMOS QUE HACER EL RESTO MODULAR PARA QUE NO SE SALGA DE LA ESTRUCTURA CIRCULAR
    }while (pos != posInicial);
    return false;
}
```