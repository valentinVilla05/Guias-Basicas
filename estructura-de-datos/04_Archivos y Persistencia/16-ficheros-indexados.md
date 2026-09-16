# Ficheros indexados

## 1. Motivación e Indexación de Ficheros
Mantener grandes volúmenes de datos completamente en memoria (como un catálogo de 100,000 libros) es practicamente imposible. La indexación resuelve esto utilizando una estructura ligera en memoria principal (RAM) que apunta al fichero de datos almacenado en disco

### Funciones Principales de un Índice
* **Localización eficiente:** Permite encontrar un registro a partir de su clave sin leer todo el fichero.  
* **Comprobación rápida:** Determina si un registro existe o no.  
* **Listado ordenado:** Permite recorrer los registros de forma ordenada por clave sin necesidad de ordenarlos físicamente en disco.  
**Bajo Consumo**: El tamaño del índice en memoria es considerablemente menor que el del fichero completo.

![ficheros_indexados](../assets/img/ficheros_indexados.gif)
## 2. Índices Simples o Primarios
Un índice primario se construye sobre la clave primaria (un identificador único por registro, como el ISBN). Consiste en una lista ordenada en memoria de tuplas (`Clave`, `Posición`)

### Estructuras de Datos Utilizadas
Para implementar el índice en memoria se puede usar:
    * **Vectores dinámicos ordenados**
    * **Mapas basados en Árboles Binarios de Búsqueda (`std::map`)**
    * **Tablas de dispersión / Hash (`std::unordered_map`)

### Operaciones Básicas
* **Buscar:** Se busca la clave en el índice (RAM) para obtener la posición exacta y realizar un solo acceso a disco.  
* **Insertar:** Se escribe el registro en el fichero de datos, se obtiene su posición (`tellp()`) y se añade el par (`clave, posición`) al índice  
* **Borrar:** Se localiza la clave en el índice, se elimina su entrada y se realiza el borrado lógico en el fichero de datos

### Persistencia y Marca de Actualización
Como construir el índice desde cero recorriendo el fichero de datos registro a registro es lento, se guarda en un **fichero de índices** (ej. `.idx`).  

* Para evitar inconsistencias si el programa falla antes de guardar, se incluye una **marca de actualización** (`V` o `E`) al inicio del archivo 

* Si el fichero tiene la marca en falso al arrancar, significa que quedó desactualizado y se reconstruye recorriendo el fichero de datos

## 3. Índices Secundarios
Los **índices secundarios** permiten realizar búsquedas por campos que no son la clave primaria (ej. buscar por `Autor`)

### Diferencias con el índice Primario

| Características | Índice Primario | Índice Secundario | 
| -- | -- | -- | 
| **Clave** | Única (Clave primaria / ISBN) | Puede repetirse (ej: varios libros del mismo autor) | 
| **Valor Asociado** | La **La posición física** (byte) en el fichero de dato | La **clave primaria** (ISBN) del registro |
|

### Alternativas de Implementación
* **Claves repetidas:** Usando `std::multimap<ClaveSec, ClavePrim>` 
* **Listas de ocurrencias (Listas Invertidas):** Usando `std::map<ClaveSec, list<ClavePrim>>`

### Proceso de Búsqueda Secundaria
1. Se consulta el índice secundario para obtener la lista de claves primarias asociadas Ej: Obtener los ISBNs del autor
2. Por cada clave primaria, se consulta el úndice primario para obtener la pos física en el disco
3. Se lee registro directamente desde el fichero de datos

## 4. Comparativa de Implementaciones en C++
```cpp
// Estructura de un Índice Primario en memoria
std::map<string, long> indPrimario; // <ISBN, Posicion_en_Fichero>

// Estructura de un Índice Secundario (Lista Invertida)
std::map<string, list<string>> indSecundario; // <Autor, Lista_de_ISBNs>
```

## 5. Conclusiones y Limitaciones
* **Ventaja:** Técnica sencilla y extremadamente rápida para consultar y gestionar ficheros de datos sin realizar accesos masivos a disco  

* **Limitación:** Todo el índice debe caber en la memoria RAM. Si el fichero es muy grande, la memoria se satura 

**Siguiente paso:** Para ficheros masivos donde el índice no cabe en RAM, se utilizan estructuras jerárquicas en disco como los Árboles B **(aptd 17)**
