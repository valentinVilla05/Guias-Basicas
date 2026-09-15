# Conjuntos y mapas de STL

## Parte I: Contenedores asociados de STL
Los contenedores asociativos de la biblioteca de Plantillas Estándar (STL) están diseñados para almacenar datos organizados por **claves** permitiendo operaciones eficiendes de inserción, búsqueda y borrado

* **Estructura Interna**: Están implementados internamente mediante **árboles Rojo-Negro**
* **Complejidad Temporal**: Garantizan un tiempo de ejecución de O(log n) para dichas operaciones
* **Iteración**: Los nodos incorporan un puntero a su nodo padre, lo q permite realizar recorridos secuenciales en $Inorden$ eficientemente usando iteradores

### Clasificación de los contenedores Asociativos
Se diferencian en dos aspectos : si el dato tiene la clave misma o si está separado , y si se admiten claves duplicadas

| Contenedor | Tipo de Almacenamiento | Claves Duplicadas | Ejemplo de uso |
| -- | -- | -- | -- |
| `std::set` | Clave==Dato | NO | Códigos postales de una provincia |
| `std::multiset` | Clave==Dato | Sí | Fechas de examenes de una carrera | 
| `std::map` | Pareja `std::pair<Clave,Dato>` | NO | Enviar notas a estudiantes usando como clave el correo |
| `std::multimap` | Pareja `std::pair<Clave,Dato> | Sí | Reservas de un restaurante agrupadas por fecha |

## Detalles de cada tipo de Contenedor
## 1. Conjuntos
> Se tiene que incluir la cabecera <set>

* `std::set`:
    * `insert(t)` : Devuelve un `std::pair<iterator,bool>`. El valor booleano indica `true` si se ha podido insertar o `false` si ya existía
    * `erase(t)`: Elimina el elemento especificado
    * Operaciones matemáticas: Permite aplicar la teoría de conjuntos con `<algorithm>` como `set_union`, `set_intersection` y `set_difference`

        ![std::set](../assets/img/std_set_dark.gif)
* `std::multiset`:
    * `insert(t)`: Retorna directamente un `iterador` hacia el nodo insertado.
    * `erase(t)`: elimina **todas** las ocurrencias del valor en el conjunto
        ![multiset](../assets/img/std_multiset_insert_erase_dark.gif)
## 2. Mapas
> Hace falta la cabecera <map>
* `std::map`
    * Cada elemento es un `std::pair<Tclave,Tdato>. Se accede con `.first` (clave) y `.second` (dato)
    * Soporta el operador de acceso indexado `operator[]` tanto para lecttura como para escritura mediante clave.

        ![map](../assets/img/std_map_dark.gif)

* `std::multimap`:
    * No soporta el `operator[]` ya q las claves **no** pueden estar duplicadas 
    * Podemos usar la función `count(clave)` para devolver la cantidad de elementos asociavos a esa clave

        ![multimap](../assets/img/std_multimap_dark.gif)

## Operaciones Principales de búsqueda
* `find(t)`: Devuelve un iterador al elemento si existe, y si no `.end()`
* `lower_bound(t)`: Retorna un iterador al primer elemento que no sea menor que t (es decir, mayor o igual)
* `Clases de Comparación Personalizadas (Functores):` Si se desea un criterio distinto (por ejemplo, de mayor a menor con `std::greater<T>`): Si se desea un criterio distinto (por ejemplo de mayor a menor con `std::greater<T>` o lógica propia) se define con la sobrecarga del operador : `operator ()`

```cpp
class ComparadorPunto {
public:
    bool operator()(const Punto &p1, const Punto &p2) const {
        return (p1.leeY() > p2.leeY() || 
               (p1.leeY() == p2.leeY() && p1.leeX() > p2.leeX()));
    }
};

// Declaración aplicando el comparador personalizado:
std::map<Punto, int, ComparadorPunto> puntos;
```