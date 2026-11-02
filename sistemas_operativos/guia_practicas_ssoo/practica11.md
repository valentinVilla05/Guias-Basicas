# Práctica 11: Cadenas

## 1. Expansión de Parámetros (Manipulación de Cadenas)
La expansión de parámetros es un conjunto de herramientas integradas en la shell para analizar, modificar y extraer partes de cadenas de texto sin necesidad de recurrir a comandos externos (como `sed`, `awk` o `cut`)

### 1.1 Longitud de una Cadena: `${#variable}`
Devuelve la cantidad total de caracteres contenidos en la variable

```bash
var="hola mundo"
echo ${#var}   # Devuelve: 10
```

### 1.2 Extracción e Eliminación de Patrones
```text
TABLA DE ELIMINACIÓN DE PATRONES
 ┌────────────────────────────────────────────────────────────────────────┐
 │                                                                        │
 │   Principio  ──>   ${var#patrón}   (Elimina coincidencia MÁS CORTA)    │
 │   de cadena  ──>   ${var##patrón}  (Elimina coincidencia MÁS LARGA)    │
 │                                                                        │
 │   Final de   ──>   ${var%patrón}   (Elimina coincidencia MÁS CORTA)    │
 │   cadena     ──>   ${var%%patrón}  (Elimina coincidencia MÁS LARGA)    │
 │                                                                        │
 └────────────────────────────────────────────────────────────────────────┘
```

### A. Eliminación desde el FINAL (`%` y `%%`)

* `${var%patrón}`: Elimina la subcadena más corta desde el final que coincida con el patrón

* `${var%%patrón}`: Elimina la subcadena más larga desde el final que coincida con el patrón

```bash
var="Toronto"

echo ${var%o*}   # Devuelve "Toront" (elimina la 'o' final)
echo ${var%%o*}  # Devuelve "T"      (elimina desde la primera 'o' hasta el final)
```

**Uso práctico común (Obtener el directorio de una ruta):**

```bash
fichero="/usr/bin/calendar"
echo ${fichero%/*}  # Devuelve: "/usr/bin" (elimina desde la última '/' hasta el final)
```

### B. Eliminación desde el PRINCIPIO (`#` y `##`)
* `${var#patrón}`: Elimina la subcadena más corta desde el principio que coincida con el patrón

* `${var##patrón}`: Elimina la subcadena más larga desde el principio que coincida con el patrón

```bash
var="Toronto"

echo ${var#*o}   # Devuelve "ronto" (elimina desde el inicio hasta la primera 'o')
echo ${var##*o}  # Devuelve ""      (cadena vacía, elimina desde el inicio hasta la última 'o')
```

**Uso práctico común (Obtener el nombre o extensión de un archivo):**
```bash
fichero="/usr/bin/calendar"
echo ${fichero##*/}  # Devuelve: "calendar" (elimina desde el inicio hasta la última '/')

archivo="documento.tar.gz"
echo ${archivo##*.}  # Devuelve: "gz"     (extensión final)
echo ${archivo#*.}   # Devuelve: "tar.gz" (extensión completa)
```

### 1.3 Búsqueda y Reemplazo
| Sintaxis | Descripción | Ejemplo (contrasena="aJds34.$") | Resultado |
|---|---|---|:---:|
| `${var/patrón/cadena}` | Reemplaza la primera ocurrencia del patrón. | `${contrasena/?/*}` | `*Jds34.$` |
| `${var//patrón/cadena}` | Reemplaza todas las ocurrencias del patrón. | `${contrasena//?/*}` | `********` |

> Usar comillas dobles al sustituir por `*` (*ej. `"${var//?/*}"`*) para evitar que la shell lo expanda como los archivos del directorio actual

### 1.4 Extracción de Subcadenas por Posición: `${var:inicio:tamaño}`
Extrae una porción de texto indicando la posición inicial (base 0) y el número de caracteres a tomar

```bash
dato="abc123"

echo ${dato:2:3}  # Extrae 3 caracteres desde la posición 2 -> Devuelve: "c12"
echo ${dato:3:1}  # Extrae 1 carácter desde la posición 3   -> Devuelve: "1"
```

### 1.5 Cambio de Mayúsculas y Minúsculas
| Sintaxis | Operación | Ejemplo (`dato="hola mundo"`) | Resultado |
|---|---|---|---|
| `${var^}` | Primera letra a mayúscula | `${dato^}` | `Hola mundo` |
| `${var^^}` | Todas las letras a mayúsculas | `${dato^^}` | `HOLA MUNDO` |
| `${var,}` | Primera letra a minúscula | `${dato,}` (con `"HOLA"`) | `hOLA` |
| `${var,,}` | Todas las letras a minúsculas | `${dato,,}` (con `"HOLA"`) | `hola` |

**Ejemplo: Manipulación de Rutas y Correos**
```bash
#!/bin/bash
# Extracción de componentes de ruta y correo electrónico

if [ $# -ne 2 ]; then
    echo "Uso: $0 <ruta> <email>"
    exit 1
fi

ruta="$1"      # Ej: /home/usuario/documento.txt
email="$2"     # Ej: usuario@dominio.com

# Extracción de componentes
directorio="${ruta%/*}"               # /home/usuario
nombre_completo="${ruta##*/}"         # documento.txt
nombre_sin_extension="${nombre_completo%.*}" # documento
extension="${nombre_completo##*.}"    # txt

usuario_email="${email%%@*}"          # usuario
dominio_email="${email##*@}"          # dominio.com

echo "Directorio: $directorio"
echo "Archivo: $nombre_completo"
echo "Sin ext: $nombre_sin_extension | Ext: $extension"
echo "Usuario Email: $usuario_email | Dominio: $dominio_email"
```

## 2. Formateo de Mensajes con printf
A diferencia de `echo`, la orden `printf` permite formatear cadenas, alinear texto, definir anchos de columna y dar formato numérico preciso

### 2.1 Sintaxis Base
```bash
printf "cadena_de_formato" argumento1 argumento2 ...
```

### 2.2 Especificadores de Formato y Secuencias de Escape
### Especificadores Principales
* `%s`: Cadena de caracteres (string)
* `%d`: Número entero (decimal)
* `%f`: Número con coma flotante / real (float)

### Secuencias de Escape Comunes
* `\n`: Salto de línea
* `\t`: Tabulador horizontal
* `\\`: Imprime una barra invertida `\`


### 2.3 Especificación de Tamaño y Alineación
```bash
# Alineación a la DERECHA (por defecto):
printf "%6s\n" hola     # Imprime: "  hola" (rellena con espacios a la izquierda)

# Alineación a la IZQUIERDA (usando '-'):
printf "%-8s:%s\n" hola mundo  # Imprime: "hola    :mundo"
```

### Formato Decimal en Números Reales (`%AnchoTotal.Decimales f`)
```bash
printf "%10.3f\n" 1234,45433
# Resultado: "  1234,454" (Ancho total 10 caracteres, 3 decimales)
```

### Formato en Cadenas de Texto (`%AnchoMínimo.MáximoCaracteres s`)

```bash
printf "%10.3s %8.2s\n" hola mundo
# Resultado: "       hol       mu"
# Explicación:
# - "%10.3s": Ancho total de 10, pero solo toma los 3 primeros caracteres ("hol").
# - "%8.2s" : Ancho total de 8, pero solo toma los 2 primeros caracteres ("mu").
```

### 2.4 Guardar el Salida Formateada en una Variable: `printf -v`

La opción `-v` permite asignar el resultado del formateo directamente a una variable en lugar de imprimirlo por pantalla

```bash
printf -v res "%10.3f\n" 1234,45433
echo "${res}"  # Muestra: "  1234,454"
```

**Ejemplo: Generación de Pirámide de Asteriscos**

Este script utiliza variables dinámicas dentro del especificador de formato de `printf` (`%${ancho}.${tam}s`)

```bash
#!/bin/bash
# Imprime una pirámide simétrica de asteriscos.

# 1. Validar argumento único y numérico
if [ ${#} -ne 1 ] || [[ ${1} = *[^0-9]* ]]; then
    echo "Error: Debe proporcionar solo un argumento numérico entero."
    exit 1
fi

# 2. Validar tamaño máximo
if [ ${1} -gt 20 ]; then
    echo "Error: El número no puede ser mayor que 20."
    exit 2
fi

cad="********************"  # Cadena de 20 asteriscos de referencia
i=1

while [ ${i} -le ${1} ]
do
    # Explicación del especificador de formato:
    # %${1}.${i}s  -> Alineado a la derecha, ancho total $1, muestra $i asteriscos
    # %-${1}.${i}s -> Alineado a la izquierda, ancho total $1, muestra $i asteriscos
    printf "%${1}.${i}s%-${1}.${i}s\n" "${cad}" "${cad}"
    i=$(( i + 1 ))
done
```

**Ejemplo de salida para `./piramide.sh 5`**

```text
    **    
   ****   
  ******  
 ******** 
**********
```