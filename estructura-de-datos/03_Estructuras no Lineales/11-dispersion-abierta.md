# Dispersión Abierta
El objetivo de la dispersión (también conocida como hashing) es lograr operaciones de búsqueda, inserción y borrado en un tiempo constante **O(1)**, superando la complejidad $O (\log n)$ de esttructuras asociativas basadas en árboles como los ALV

Mecanimos: Usa un vector de tamaño t como contenedor base. Una función de dispersión $h(x)$ calcula directamente la posición en el vector correspondiente **a una clave**

![dispersión_abierta](../assets/img/open_hashing_dark.gif)

## Funciones de Dispersión $h(x)$
Transforman una clave de caulquier tipo y rango en un índice dentro del intervalo $[0,t-1]$ de la tabla (como siempre recorremos los arrays)

### Requisitos:
* **Bajo coste computacional**: debe ser rápido
* **Determinismo**: La misma clave siempre debe devolver **el mismo índice**
* **Uniformidad**: Debe repetir las claves homogéneamente por todo el rango de la tabla 

### Técnicas de Dispersión Comunes
### 1. Método de División
#### **¿Cómo funciona?**
Calcula el resto de dividir la clave $x$ entre el tamaño de la tabla $t$ con la operación de módulo (`%`). Es recomendable que el tamaño $t$ sea un número primo para distribuir mejor los datos

#### Ejemplo:
* **Datos**: Clave x=4567 , tamaño de la tabla = 101.
* **Cálculo**: 4567 / 101 = 45 y el resto es 22
* **Resultado**: h(4567) = 4567%101 = 22 ( se guardará en la posición 22 del vector)

---
### 2. Método de Plegamiento
#### **¿Cómo funciona?**
Toma una clave larga, la parte en trozos con la misma longitud ( es decir con el mismo núm de dígitos), suma esos trozos y al resultado final se le aplica el módulo del tamaño de la tabla $(t)$

#### Ejemplo:
* **Datos**: Clave = 23911984. Tamaño de la tabla = 100
* **Paso 1 (Dividir):** Se separan en grupos de 2 , entonces : $[23] [91] [19] [84]$.
* **Paso 2 (Sumar):** 23 + 91 + 19 + 84 = 217
* **Paso 3 (Ajustar al tamaño):** 217%100 = 17
* **Resultado** h(23911984) = 17 (se guardará la posición 17)

---
### 3. Método de la mitad del Cuadrado
#### **¿Cómo funciona?**
Eleva la clave al cuadrado $(x²)$ y exxtrae los dígitos que quedan justo en el centro del resultado

#### Ejemplo:
* **Datos**: Clave = 4567, Tamaño de tabla t=100 (como tiene 2 ceros necesitamos extraer 2 dígitos)
* **Paso 1 (Cuadrado)**: 4567² = 20857489
* **Paso 2 (Extraer centro)**: De la cifra 20857489 tomamos como dígitos centrales **57**
* **Resultado**: h(4567) = **57** (se guardará en la posción 57)


---
### 4. Método para Cadenas de Texto
#### **¿Cómo funciona?**
Si la clave es un texto (como un nombre o un DNI en formato `string`), no basta consumar los valores de las letras (ASCII) porque palabras con la mismas letras en distinto orden (`"CASA"` `"SACA"`) darían la misma posición -> `colisión` . Aplicamos algorítmos como el de `djb2` que multiplican el alor acumulado en cada paso para romper esa simetría usando el desplazamiento de bits

#### Ejemplo:
* Empieza con un número semilla (se suele usar el `5381`)
* Por cada letra `c` de la cadena hace:
    > hash = (hash * 33 ) + c
* Puesto en código, multiplicar por 33 se expresa como:
    > ((hash << 5) + hash) + c ya que hash<< 5 equivale a hash *2^5= hash * 32
---
### Factor de Carga y Dimensionamiento
> El **factor de carga** se define como $ \lambda = n/t $, donde $n$ es el núm de elementos y $t$ el tamaño de la tabla
* **Zona óptima**: Para 0.0 <= $\lambda$ <= 0.7, el tiempo de acceso se mantiene constante $O(1)$

* **Degradación**: Si $\lambda$ > 0.7, el núm de colisiones incrementa notablemente el tiempo de procesamiento

* **Regla General**: La tabla debe dimensionarse para ser al menos $1/3$ más grande q el total de elementos a almacenar

---
### Dispersión Abierta (Encadenamiento Separado)
Estrategia para gestionar **colisiones** (cuando dos valores se almacenan en la misma posición en memoria) , formalmente como h(x1) = h(x2) pero x1 != x2

* **Estructura:** El contenedor base es un vecor cuyo elemento en cada celda es una lista enlazada (`std::list`) que almacena todas las entradas cuya clave dió la misma posición en la función dispersión

* **Operaciones**
* **Inserción:** Se añade la entrada al final de la lista correspondiente a la celda $h(clave)$
* **Búsqueda/Borrado**: Se calcula $h(clave)$ y se recorre linealmente la lista en esa posición para encontrar la coincidencia

```cpp
template<class T>
class DispAbierta {
    struct Entrada { long clave; T dato; };
    std::vector<std::list<Entrada>> tabla; // Vector de listas enlazadas
    long fDisp(int clave) { return clave % tabla.size(); }
};
```
---
### Redispersión
Ocurre cuando la cantidad de datos almacenados sobrepasa el límite óptimo ($\lambda$ > 0.7)
* **Proceso**: Se cra una tabla nueva (normalmente del **doble del tam anterior**) para minimizar reorganizaciones futuras y se re-insertan todos los elementos aplicando la función de módulo (`%`)

* también se puede aplicar en caso de un decrecimient drástico en el núm de datos guardados

