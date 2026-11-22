# Práctica 10: Aritmética y Bucles

## 1. Operaciones Aritméticas en Shell Script

Por defecto, la shell **trata todas las variables y valores como cadenas de texto (strings)**

```bash
# Intento de suma sin sustitución aritmética:
resultado=1+2
echo $resultado  # Imprime la cadena "1+2", no el número 3
```

### Sustitución Aritmética: `$(( expresión ))`

Para forzar al intérprete a tratar los datos como números enteros, se utiliza la sintaxis `$(( expresión ))`

```bash
resultado=$(( 1+2 ))
echo $resultado  # Imprime 3
```

> Dentro de `$(( ))`, **no es necesario** anteponer el símbolo `$` a los nombres de las variables

```bash
var1=2
resultado=$(( var1 * 3 ))  # Equivale a $(( $var1 * 3 )) -> Resultado: 6
```

## Operadores Aritméticos Soportados

Todos los operadores ejecutan **operaciones numéricas enteras** (sin decimales)

| Operador | Descripción                       |     Ejemplo     | Resultado |
| :------: | --------------------------------- | :-------------: | :-------: |
|   `+`    | Suma                              | `$(( 5 + 2 ))`  |    `7`    |
|   `-`    | Resta / Negación                  | `$(( 5 - 2 ))`  |    `3`    |
|   `*`    | Multiplicación                    | `$(( 5 * 2 ))`  |   `10`    |
|   `/`    | División entera (sin decimales)   | `$(( 1 / 3 ))`  |    `0`    |
|   `%`    | Módulo (resto de la división)     | `$(( 7 % 3 ))`  |    `1`    |
|   `**`   | Exponenciación                    | `$(( 2 ** 4 ))` |   `16`    |
|   `&`    | AND a nivel de bits               | `$(( 6 & 3 ))`  |    `2`    |
|   `\|`   | OR a nivel de bits                | `$(( 6 \| 3 ))` |    `7`    |
|   `^`    | XOR a nivel de bits               | `$(( 6 ^ 3 ))`  |    `5`    |
|   `~`    | Complementario a nivel de bits    |   `$(( ~2 ))`   |   `-3`    |
|   `<<`   | Desplazamiento a izquierda (× 2ⁿ) | `$(( 2 << 2 ))` |    `8`    |
|   `>>`   | Desplazamiento a derecha (÷ 2ⁿ)   | `$(( 8 >> 1 ))` |    `4`    |

## 2. El Mecanismo de Indirección `${!var}`

**La indirección** permite acceder al contenido de una variable cuyo nombre está guardado dentro de otra variable (puntero a variable)

### Sintaxis y Funcionamiento

```bash
hola=3
nvar=hola

# Intento incorrecto: ${${nvar}} dará error de sintaxis en bash.
# Uso correcto: ${!nvar}
echo ${hola} ${nvar} ${!nvar}
# Salida: 3 hola 3
```

1. `${nvar}` obtiene el texto `"hola"`
2. `${!nvar}` busca el valor de la variable llamada `"hola"`, devolviendo `3`

## Indirección aplicada a Parámetros Posicionales

Es especialmente útil para acceder a parámetros del script de forma dinámica dentro de un bucle

### 1. Parámetro posicional simple

Si el parámetro `$2` tiene el valor `"fconde"`:

```bash
i=2
echo ${2} ${i} ${!i}
# Salida: fconde 2 fconde
```

### 2. Acceso al último argumento recibido: ${!#}

La variable `$#` almacena el **número total de argumentos**. Por lo tanto, `${!#}` devuelve el **valor del último argumento**

```bash
# Si el script se ejecuta con: ./script.sh archivo1.txt archivo2.txt /tmp/destino
# $# vale 3
echo ${!#}  # Muestra: /tmp/destino
```

## 3. Bucles de Control: while y until

### Bucle `while`

Ejecuta el bloque de código **mientras la condición sea verdadera**

```bash
while condición
do
    # Instrucciones a ejecutar
done
```

> Ejemplo: Contar de 1 a 10

```bash
i=1
while [ ${i} -le 10 ]
do
    echo "${i}"
    i=$(( i + 1 ))  # Es obligatorio actualizar la variable de control
done
```

### Bucle `until`

Ejecuta el bloque de código **hasta que la condición sea verdadera** (se ejecuta mientras la condición sea falsa)

```bash
until condición
do
    # Instrucciones a ejecutar
done
```

**Ejemplo: Contar de 1 a 10**

```bash
i=1
until [ ${i} -gt 10 ]
do
    echo "${i}"
    i=$(( i + 1 ))
done
```

### Criterio de Selección de Bucles

```text
                            ¿Qué estructura usar?
                                     │
         ┌───────────────────────────┴───────────────────────────┐
         ▼                                                       ▼
¿Tienes una lista fija                                ¿Tienes una condición
de elementos a recorrer?                              de prueba a evaluar?
         │                                                       │
         ▼                                                       ▼
 Usar bucle FOR                                           Usar bucle WHILE / UNTIL
 (ej. archivos de un dir)                                (ej. contador, lectura de línea)
```

## 4. Lectura Avanzada de Archivos y Procesos con `while`

El bucle `while` es la estructura idónea para procesar flujos de texto línea a línea

### Estructura Robusta de Lectura: `IFS= read -r linea`

```bash
archivo="datos.txt"

while IFS= read -r linea
do
    echo "Línea leída: ${linea}"
done < "${archivo}"
```

### Componentes Clave:

- `IFS=` (Internal Field Separator nulo): Evita que `read` elimine los espacios o tabuladores iniciales/finales de cada línea

- `read -r`: Desactiva la interpretación de la barra invertida (`\`), permitiendo leer caracteres de escape literalmente

- `< "${archivo}"`: Redirección de entrada que alimenta el bucle con el contenido del archivo

### Procesamiento de Comandos mediante Process Substitution `<( comando )`

Para procesar la salida de un comando línea por línea sin crear archivos temporales:

```bash
while IFS= read -r archivo
do
    echo "Archivo encontrado: ${archivo}"
done < <(ls)
```

## 5. El Filtro `cut`

El comando `cut` permite extraer partes/columnas de cada línea de un texto delimitado por un carácter específico

### Sintaxis Principal

```bash
cut -d'delimitador' -f'campo(s)'
```

- `-d` **(delimiter)**: Especifica el carácter delimitador (ej. `-d`:, `-d','`). Si se omite, usa tabulador por defecto

- `-f` **(fields)**: Indica el número de campo o rango de campos a extraer

### Ejemplos Prácticos

Dada la cadena: `"aa:bb:cc:dd"`

| Comando                               | Resultado  | Explicación                             |
| ------------------------------------- | :--------: | --------------------------------------- |
| `echo "aa:bb:cc:dd" \| cut -d: -f3`   |    `cc`    | Extrae únicamente el 3. er campo.       |
| `echo "aa:bb:cc:dd" \| cut -d: -f1,3` |  `aa:cc`   | Extrae el 1. er y 3. er campo.          |
| `echo "aa:bb:cc:dd" \| cut -d: -f2-4` | `bb:cc:dd` | Extrae desde el 2.º hasta el 4.º campo. |

## 6. Scripts Complejos de Ejemplo

### Script 1: Copia de N-1 Elementos al Último Directorio

Copia los primeros $N-1$ argumentos dentro del directorio especificado en el argumento $N$

```bash
#!/bin/bash
# Descripción: Copia n-1 archivos/directorios al directorio destino (último argumento).

# 1. Validación de cantidad mínima de argumentos
if [ ${#} -lt 2 ]; then
    echo "Error: Se deben proporcionar al menos 2 argumentos."
    exit 1
fi

# 2. Validación de que el último argumento es un directorio existente (usando indirección)
if [ ! -d ${!#} ]; then
    echo "Error: El último argumento (${!#}) no es un directorio válido."
    exit 2
fi

# 3. Recorrido de los n-1 primeros argumentos
i=1
while [ ${i} -le $(( $# - 1 )) ]
do
    # Comprobar si el elemento existe usando indirección (${!i})
    if [ -e ${!i} ]; then
        cp -r ${!i} ${!#}
    fi
    i=$(( i + 1 ))  # Incrementar contador
done
```

### Script 2: Verificación de Existencia de Usuario en `/etc/passwd`

Busca un nombre de usuario recibido por parámetro dentro del fichero `/etc/passwd` del sistema

```bash
#!/bin/bash
# Descripción: Comprueba la existencia de un usuario mediante /etc/passwd.

if [ ${#} -ne 1 ]; then
    echo "Error: Debe proporcionar exactamente 1 argumento (nombre de usuario)."
    exit 1
fi

# Lectura de /etc/passwd línea a línea
while IFS= read -r linea
do
    # /etc/passwd usa ':' como separador. El primer campo es el nombre de usuario.
    usuario=$(echo "${linea}" | cut -d: -f1)

    if [ "${1}" = "${usuario}" ]; then
        echo "El usuario '${1}' existe en el sistema."
        exit 0
    fi
done < /etc/passwd

echo "El usuario '${1}' NO existe en el sistema."
exit 3
```

## Ejercicios

1. Escribe un shell script que reciba como argumento un número, el UID de un usuario y que compruebe si existe en el sistema un usuario con ese UID. Si existe debe comprobar además si ese usuario tiene el mismo UID y GID. Debe usar el fichero de cuentas de usuario /etc/passwd.

```bash
#!/bin/bash

# Autor: Valentin Villa

# Poner los colores es COMPLETAMENTE opcional
ROJO='\e[0;31m'
MAGENTA='\e[0;35m'
BLANCO='\e[0;37m'


if [ $# -lt 1 ]; then
    echo -e "${ROJO}Error: Debes pasar un argumento"
    exit 1
fi

# existe=$(cat /etc/passwd | grep "$1")

# De esta manera usamos expresiones regulares para buscar el numero pasado siempre que esté en la tercera columna. Así evitamos falsos positivos
existe=$(grep -E "^[^:]+:[^:]+:${1}:" /etc/passwd)

if [ -z "${existe}" ]; then
    echo -e "${MAGENTA} El UID especificado \"${1}\" no pertenece a ningún usuario"
    exit 1
fi

# Cuidado al usar nombres de variables. Palabras como UID son palabras reservadas del sistema
userID=$(echo "${existe}" | cut -d: -f3)
groupID=$(echo "${existe}" | cut -d: -f4)


if [[ ${userID} == ${groupID} ]]; then
    echo -e "${BLANCO} El usuario con el UID \"$1\" tiene el mismo GID."
else
    echo -e "${BLANCO} El usuario con el UID \"$1\" no tiene el mismo GID."
fi
```

2. Escribe un shell script que saque una lista por pantalla de aquellos usuarios del sistema que están bloqueados y el número de cuentas bloqueadas. Recuerda que un usuario bloqueado tiene en el archivo `/etc/shadow` un signo ! al principio del campo de la contraseña (passwd -l y usermod -L lo añaden delante de la contraseña cifrada). Recuerda que para acceder a `/etc/shadow` hay que tener privilegios de administrador (sudo).

```bash
#!/bin/bash

#Autor: Valentin Villa

ROJO='\e[0;31m'
MAGENTA='\e[0;35m'
BLANCO='\e[0;37m'

archivo="/etc/shadow"

# Comprobamos si tenemos permisos de lectura (necesita sudo)
if [ ! -r "${archivo}" ]; then
    echo -e "${ROJO}Error: No tienes permisos para leer ${archivo}. Ejecuta el script con sudo.${RESET}"
    exit 1
fi

vectorBloqueados=()

while IFS= read -r linea; do
    vectorBloqueados+=($(echo "${linea}" | grep -E "^[^:]+:!" | cut -d: -f1))
done < "${archivo}"

echo -e "Lista de usuarios bloqueados: "

for usuario in "${vectorBloqueados[@]}"; do
    echo -e "--> ${usuario} <--"
done

# Estructura con while:
# i=0
# while [ $i -lt ${#vectorBloqueados[@]} ]; do
#     echo "${vectorBloqueados[$i]}"
#     ((i++))
# done

```

3. Escribe un shell script que busque, en todos los directorios que cuelgan del directorio base del usuario que ejecuta el script, si hay algún archivo que tenga como nombre `core` y que borre todos los archivos `core` encontrados. Al final del script se debe imprimir el número de archivos `core` borrados. Recuerda que la orden find con la opción `-name nombrearchivo` permite buscar archivos en el disco. Para más información consulta la sintaxis de la orden find. (Pista: Asegúrate de buscar únicamente ficheros de tipo regular usando `-type f` y realiza pruebas seguras, como mostrar por pantalla la orden con echo rm, antes de ejecutar el borrado definitivo).

```bash
#!/bin/bash

# Autor: Valentin Villa

contador=0

# Metodo WHILE
while IFS= read -r archivo; do
    rm "${archivo}"
    echo -e "${archivo} eliminado."
    ((contador++))
done < <(find "$HOME" -type f -name "core")

echo "Total borrados: ${contador}"

# Con metodo 'for'


# old_IFS=${IFS}
# IFS=$'\n'
# archivos=($(find "$HOME" -type f -name "core")) # Encontramos todos los archivos
# IFS=${old_IFS}

# Formato for:
# for archivo in "${archivos[@]}"; do
#     rm "${archivo}"
#     echo -e "${archivo} eliminado..."
#     ((contador++))

# done
```

4. El archivo `/etc/group` tiene una línea por cada grupo que exista en el sistema. Investiga el formato de este archivo y escribe un script que escriba por pantalla cuáles son los grupos que tienen usuarios asignados. Ten en cuenta que el cuarto campo solo enumera los miembros secundarios (por ejemplo, el grupo principal de un usuario puede aparecer con el cuarto campo vacío, ya que solo lista los miembros adicionales). Al final deberá escribir el número de grupos que tienen usuarios asignados. Debes recorrer todo el archivo línea a línea.

```bash
#!/bin/bash

# Autor: Valentin Villa

contador=0

archivo="/etc/group"

grupos=()

while IFS= read -r linea; do
    tieneUsuarios=$(echo "${linea}" | cut -d: -f4)

    if [ -n "${tieneUsuarios}" ]; then
        ((contador++))
        grupos+=($(echo "${linea}" | cut -d: -f1))
    fi
done < "${archivo}"

echo -e "Hay ${contador} grupos que tienen usuarios."

echo -e "Grupos que tienen usuarios: "
for grupo in "${grupos[@]}"; do
    echo -e "${grupo}"
done
```

5. Escribe un shell script que analice el archivo `/etc/group` y que diga si una serie de GIDs que se pasan como argumentos corresponden a grupos válidos del sistema. Debe escribir por pantalla cuántos GIDs pasados son grupos válidos y cuántos no.

```bash
#!/bin/bash

# Autor: Valentin Villa

ROJO='\e[0;31m'
MAGENTA='\e[0;35m'
BLANCO='\e[0;37m'

if [ $# -lt 1 ]; then
    echo -e "${ROJO} Error: Debes pasar al menos un parámetro."
    echo -e "${BLANCO} Sintaxis: $0 <GID1> <GID2>..."
    exit 1
fi

archivo="/etc/group"

idsValidos=()
idsNoValidos=()

for param in "$@"; do
    encontrado=0

    while IFS= read -r linea; do
        idGrupoLinea=$(echo "${linea}" | cut -d: -f3)
        if [[ "${param}" == "${idGrupoLinea}" ]]; then
            encontrado=1
            break   # Ya lo encontramos, no hace falta seguir leyendo el archivo
        fi
    done < "${archivo}"

    if [ "${encontrado}" -eq 1 ]; then
        idsValidos+=("${param}")
    else
        idsNoValidos+=("${param}")
    fi
done

echo -e "Ids válidos ($(echo ${#idsValidos[@]})): "
for idValido in "${idsValidos[@]}"; do
    echo -e "${idValido}"
done

echo -e "Ids NO válidos ($(echo ${#idsNoValidos[@]})): "
for idNoValido in "${idsNoValidos[@]}"; do
    echo -e "${idNoValido}"
done
```

6. El archivo `/proc/meminfo` contiene información sobre el uso de la memoria del sistema en un instante determinado. Lista su contenido con `cat /proc/meminfo`, estúdialo y escribe un script que diga en un instante determinado, cuánta memoria en megabytes ocupan varios de estos componentes, por ejemplo, los buffers y las tablas de páginas. Debes pasar estos componentes como argumentos.

```bash
#!/bin/bash

# Autor: Valentin Villa

ROJO='\e[0;31m'
VERDE='\e[0;32m'
MAGENTA='\e[0;35m'
RESET='\e[0m'

if [ $# -lt 1 ]; then
    echo -e "${ROJO}Error: Debes pasar al menos un componente de memoria como argumento.${RESET}"
    echo -e "Sintaxis: $0 Buffers PageTables MemFree"
    exit 1
fi

archivo="/proc/meminfo"

for componente in "$@"; do
    # Usamos RegEx para buscar las lineas que empiezan exactamente por "<<componente>>:"
    linea=$(grep -E "^${componente}:" "${archivo}")

    if [ -z "${linea}" ]; then
        echo -e "${MAGENTA}--> El componente '${componente}' no existe en ${archivo}.${RESET}"
    else
        # Extraemos la segunda columna (el valor en kB)
        kb=$(echo "${linea}" | tr -s " " |  cut -d " " -f2)

        # Conversión entera en Bash (1 MB = 1024 kB)
        mb=$(( kb / 1024 ))

        echo -e "${VERDE}--> ${componente}: ${mb} MB (${kb} kB)${RESET}"
    fi
done
```

7. Modifica el script del ejemplo de conversión de segundos para que compruebe que se ha pasado exactamente un argumento y que este corresponde a un número entero no negativo. Si no se cumplen estas condiciones, el script debe mostrar un mensaje de error explicativo por la salida de errores y finalizar con un código de estado distinto de cero.

Script de **conversion de segundos**:

```bash
#!/bin/bash

# Autor: Francisco de Asís Conde Rodríguez
# Descripción: Cambia formato de tiempo.

seg_en_dia=86400
seg_en_hora=3600
min_en_hora=60
seg_en_minuto=60
dias=$(( ${1} / ${seg_en_dia} ))
seg_restantes=$(( ${1} % ${seg_en_dia} ))
horas=$(( ${seg_restantes} / ${seg_en_hora} ))
seg_restantes=$(( ${seg_restantes} % ${seg_en_hora} ))
minutos=$(( ${seg_restantes} / ${seg_en_minuto} ))
seg_restantes=$(( ${seg_restantes} % ${seg_en_minuto} ))

echo ${dias} ${horas} ${minutos} ${seg_restantes}
```

Solución:

```bash
#!/bin/bash

# Autor: Valentín Villa
# Descripción: Cambia formato de tiempo.

ROJO='\e[0;31m'
BLANCO='\e[0;37m'

if [ $# -ne 1 ]; then
    echo -e "${ROJO}Error: Debes pasar un argumento" >&2
    echo -e "${BLANCO}Sintaxis: $0 <<numSegundos>>" >&2
    exit 1
fi

if [[ ! "$1" =~ ^[0-9]+$ ]]; then
    echo -e "${ROJO}Error: El numero de segundos debe ser mayor o igual a 0" >&2
    echo -e "${BLANCO}Sintaxis: $0 <<numSegundos>>" >&2
    exit 1
fi

seg_en_dia=86400
seg_en_hora=3600
min_en_hora=60
seg_en_minuto=60
dias=$(( ${1} / ${seg_en_dia} ))
seg_restantes=$(( ${1} % ${seg_en_dia} ))
horas=$(( ${seg_restantes} / ${seg_en_hora} ))
seg_restantes=$(( ${seg_restantes} % ${seg_en_hora} ))
minutos=$(( ${seg_restantes} / ${seg_en_minuto} ))
seg_restantes=$(( ${seg_restantes} % ${seg_en_minuto} ))

echo -e "Dias: ${dias} Horas: ${horas} Minutos: ${minutos} Segundos: ${seg_restantes}"

```
