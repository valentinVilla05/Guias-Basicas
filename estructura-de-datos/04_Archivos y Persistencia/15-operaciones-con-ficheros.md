# Conceptos y operacionesfundamentales con ficheros

## 1. Introducción
En las aplicaciones informáticas, la información almacenada en estrucuras de datos en memoria principal (RAM) debe transferirse a un almacenamiento secundario (ficheros) por tres razones
* **Persistencia**: Para evitar tener q alimentar continuamente de datos a la aplicación cada vez que la ejecutamos
* **Capacidad**: Porque la cantidad total de información puede superar a la cantidad de memoria principal
* **Tipos de datos**: Para almacenar datos no textuaels como fotos

### Necesidad de Almacenamiento Masivo
En el ciclo de vida de una aplicación, los dicheros se utilizan para mantener datos de entrada, guardar datos de salida/resultados y albergar datos temporales o intermedios. Cuando la información no cabe en memoria RAM tenemos q recurrir a estruturas de datos integradas en ficheros

## 2. Dispositivos de Almacenamiento y Tipos de Acceso
Los dispositivos de almacenamiento secundario son periféricos que guardan información de forma permanente

### Tipos de Dispositivos
* **Magnéticos (ya no se usan)**: discos divididos en pistas lineales o concéntricas (ej: cintas, discos..)
* **Ópticos (en sustitución)**: Pistas dispuesas en espiral (CV,DVD, Blu-Ray)
* **Memorias Flash**: Estructura matricial basada en transistores derivados de las memorias EEPROM , sin partes móviles, silenciosas y de bajo consumo (SSD, SD, MicroSD)

> **Recordatorio de EDI:** las memorias EEPROM son memorias no volátil de borrado eléctrico y accceso a nivel de byte 

### Tipos de Acceso (Dispositivos Ópticos / Mecánicos)
En dispositivos con partes mecánicas , el timepo de acceso total es la suma de:
1. **Tiempo de desplazamiento**: Mover el brazo mecánico hasta cilindro/pista adecuada
2. **Retraso por rotación**: Tiempo que tarda el disco en girar hasta situar el sector bajo la cabeza lectora
3 **Tiempo de transferencia**: Depende del volumen de bytes a transmitir

## 3. Tamaños de Bloque y Organización Interna
El acceso a disco es mucho más lento q a la RAM. El objetivo principal de cualquier sistema de ficheros es **minimizar el número de accesos a disco** (idealmente menos que 10 accesos por operación)

* **Bloque de Ficheros**: Es la unidad mínima de información que se transfiere en una operación de lectura o escritura entre memoria principal y el fichero. Su tamaño depende del SO y del dispositivo
* **Cubetas**: Las estructuras de datos agrupan varios registros en "cubetas" cuyo tamaño se adapta al bloque del sistema para aprovechar cada operación de entrada salida

## 4. Estructura y Formato de los Ficheros
Para organizar la información dentro de un fichero, se emplean tres niveles conceptuales:

* **Campo**: unidad básica de información (ej: `dni`, `nombre`,`edad`)
* **Registro**: Colección de campos relacionados que forman una entidad (ej registro `Empleado`)
* **Fichero**: Colección de Registros

### Formatos de Ficheros
| Formato | Características Principales | Ventaja / Desventaja | 
| -- | -- | -- |
| **Texto** | Codificado en ASCII /UFT-8....Legible con editores | + Porátil e interoperable , - Requiere conversión al cargarse en RAM | 
| **Binario** | Guarda los bytes tal cual están en la memoria RAM | + Operaciones L/E my rápidas (sin conversión) y más compacto - No es legible directamente y es menos transportable | 
| 


### Tipos de Cmapos y Registros
* **Campos / Registros de Longitud Fija**: Ocupan siempre un tamaño fijo predeterminado en bytes. Aunq pueden desperdiciar espacio, son muy sencillso y rápidos de manipular en código
* **Campos / Registros de Longitud Variable**: Se adaptan al tamaño del dato. Ahorran espacio, pero requieren delimitaciones (marcas como `|` o `$`), indicandores de tamaño o indices exernos para procesarse

## 5. Operaciones Fundamentales en C++ (Clase `FicheroLibro`)
Basado en una estructtura de registros de longitud fija (como la clase `Libro`), se implementan las siguientes operaciones

### serialización (Lectura y Escritura)
Para guardar o leer objetos en ficheros binarios se utilizan las funciones `write()` y `read()` sobre los bytes del objeto:

```cpp
// Escritura en flujo binario
stSal.write(titulo, sizeof(titulo));
stSal.write((char*) &anio, sizeof(anio));

// Lectura en flujo binario
stEnt.read(titulo, sizeof(titulo));
stEnt.read((char*) &anio, sizeof(anio));
```

### Principales Funciones y Desplazamientos
* `seekg()` / `seekp()`: Mueven los punteros de **lectura** (get) y **escritura** (put)
* `tellg()` / `tellp()`: Obtienen la posición acttual de los punteros de lectura y escritura

```cpp
// Abrir o crear fichero binario
f.open(name.c_str(), fstream::binary | fstream::in | fstream::out);

// Obtener el tamaño del fichero moviendo el puntero al final
f.seekg(0, ios::end);
tam = f.tellg();
```

## 6. Gestión de Altas, Modificaciones y Bajas
### Inserción y Modificación
* **Inserción al final**: Es una operación rápida que requiere de un solo acceso a disco posicionando el puntero al final mediante `f.seekp(0,ios_base::end)`

* **Modificación**: Es los registros de longitud fija, basta con sobreescribir la posición conocida con `f.seekp(pos)`. En registros de longitud variable es más complejo, ya que un dato más grande no cabría en el espacio previo

### Borrado Lógico y Reutilización de Espacio
El borrado físico (eliminar y reorganizar todo el archivo) es inviable por su alto coste en operaciones de E/S. Se utiliza el borrado lógico, que consiste en escribir una marca especial (ej. `MARCA_BORRADO`) sobre el registro

Para no hacer crecer el archivo indefinidamente, se implementa una Pila de Borrados en el propio fichero:

1. La cabecera (posición 0) almacena la dirección del último hueco libre disponible.

2. Cada registro borrado guarda la dirección del siguiente registro libre (apuntando con `-1` al final de la pila).

3. Al **insertar**, se reutiliza primero el último hueco de la pila en lugar de escribir al final del archivo, requiriendo solo 2 accesos a disco.

## 7. Búsquedas, Ordenación e Iteración
* **Búsqueda y Ordenación Directa:** Mantener un fichero de datos ordenado en disco ante continuas altas y bajas requiere un coste de $O(n)$ accesos, lo cual es inasumible. Incluso la búsqueda binaria (aprox. 20 accesos para $10^6$ datos) resulta ineficiente si el archivo cambia con frecuencia.
* **Iteración:** Se implementa mediante clases iteradoras (ej. `IteradorLibro`) que recorren el fichero omitiendo automáticamente los registros marcados como borrados.

