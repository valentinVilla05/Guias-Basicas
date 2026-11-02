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

| Operador | Descripción | Ejemplo | Resultado |
|:---:|---|:---:|:---:|
| `+` | Suma | `$(( 5 + 2 ))` | `7` |
| `-` | Resta / Negación | `$(( 5 - 2 ))` | `3` |
| `*` | Multiplicación | `$(( 5 * 2 ))` | `10` |
| `/` | División entera (sin decimales) | `$(( 1 / 3 ))` | `0` |
| `%` | Módulo (resto de la división) | `$(( 7 % 3 ))` | `1` |
| `**` | Exponenciación | `$(( 2 ** 4 ))` | `16` |
| `&` | AND a nivel de bits | `$(( 6 & 3 ))` | `2` |
| `\|` | OR a nivel de bits | `$(( 6 \| 3 ))` | `7` |
| `^` | XOR a nivel de bits | `$(( 6 ^ 3 ))` | `5` |
| `~` | Complementario a nivel de bits | `$(( ~2 ))` | `-3` |
| `<<` | Desplazamiento a izquierda (× 2ⁿ) | `$(( 2 << 2 ))` | `8` |
| `>>` | Desplazamiento a derecha (÷ 2ⁿ) | `$(( 8 >> 1 ))` | `4` |

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
* `IFS=` (Internal Field Separator nulo): Evita que `read` elimine los espacios o tabuladores iniciales/finales de cada línea

* `read -r`: Desactiva la interpretación de la barra invertida (`\`), permitiendo leer caracteres de escape literalmente

* `< "${archivo}"`: Redirección de entrada que alimenta el bucle con el contenido del archivo

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

* `-d` **(delimiter)**: Especifica el carácter delimitador (ej. `-d`:, `-d','`). Si se omite, usa tabulador por defecto

* `-f` **(fields)**: Indica el número de campo o rango de campos a extraer

### Ejemplos Prácticos
Dada la cadena: `"aa:bb:cc:dd"`

| Comando | Resultado | Explicación |
|---|:---:|---|
| `echo "aa:bb:cc:dd" \| cut -d: -f3` | `cc` | Extrae únicamente el 3. er campo. |
| `echo "aa:bb:cc:dd" \| cut -d: -f1,3` | `aa:cc` | Extrae el 1. er y 3. er campo. |
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
