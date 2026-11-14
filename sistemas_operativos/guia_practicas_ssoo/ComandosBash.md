# Resumen de comandos principales para Bash
> Es recomendable saber que hace cada uno ya que facilitará la resolución de los ejercicios en algunos casos 

### Tabla 1: Búsqueda y Filtrado de Texto (`grep`, `find`, `head`, `tail`)
*La base para localizar archivos o extraer las líneas exactas que te interesan.*

| Comando | Operandos / Flags Imprescindibles | Qué hace exactamente | Ejemplo práctico de alto valor |
| :--- | :--- | :--- | :--- |
| **`grep`** | **`-i`**<br>**`-v`**<br>**`-w`**<br>**`-o`**<br>**`-c`**<br>**`-E`**<br>**`-r`**<br>**`-l`** / **`-L`**<br>**`-C N`** (`-A`/`-B`) | Ignora mayúsculas/minúsculas.<br>**Invierte**: devuelve lo que **NO** coincide.<br>Busca la palabra exacta (no subcadenas).<br>Imprime **solo** el fragmento exacto que coincide.<br>Cuenta el número de líneas que coinciden.<br>Activa expresiones regulares extendidas (`\|`, `+`, `?`, `{n}`).<br>Busca recursivamente en todo un directorio.<br>Muestra solo nombres de archivo que coinciden (`-l`) o no (`-L`).<br>Muestra `N` líneas de contexto alrededor (o después `-A` / antes `-B`). | `grep -roE '[0-9]{1,3}(\.[0-9]{1,3}){3}' /var/log/`<br>*(Extrae todas las IPs de todos los logs, una por línea)* |
| **`find`** | **`-type f`** / **`-type d`**<br>**`-name "patron"`**<br>**`-iname "patron"`**<br>**`-maxdepth N`**<br>**`-size +50M`** / **`-10k`**<br>**`-mtime -7`** / **`+30`**<br>**`-not -path "*/.*"`**<br>**`-exec cmd {} +`**<br>**`-delete`** | Filtra solo ficheros (`f`) o directorios (`d`).<br>Busca por nombre exacto (admite `*` y `?`).<br>Igual que `-name` pero ignorando mayúsculas.<br>Limita la búsqueda a `N` niveles de subcarpetas.<br>Mayores de 50MB (`+`) o menores de 10KB (`-`).<br>Modificados hace menos de 7 días (`-7`) o más de 30 (`+30`).<br>Excluye archivos y carpetas ocultas.<br>Ejecuta un comando sobre todos los resultados.<br>Borra directamente los archivos encontrados. | `find . -type f -name "*.log" -size +100M -exec rm -f {} +`<br>*(Busca logs de más de 100MB y los elimina de golpe)* |
| **`head`** / **`tail`** | **`-n N`**<br>**`tail -n +N`**<br>**`tail -f`** | Muestra las primeras (`head`) o últimas (`tail`) `N` líneas.<br>Muestra **desde la línea N hasta el final** (ideal para saltar cabeceras con `+2`).<br>Monitoriza un archivo en **tiempo real** según crece. | `tail -n +2 datos.csv \| head -n 10`<br>*(Salta la cabecera y coge los 10 primeros registros)* |

---

### Tabla 2: Procesamiento de Columnas y Transformación (`awk`, `sed`, `cut`, `tr`)
*Para cortar, limpiar, reestructurar, reemplazar y hacer cálculos matemáticos sobre texto.*

| Comando | Operandos / Flags Imprescindibles | Qué hace exactamente | Ejemplo práctico de alto valor |
| :--- | :--- | :--- | :--- |
| **`awk`** | **`-F 'C'`**<br>**`$1`, `$2`, `$NF`**<br>**`NR`**<br>**`/patron/ {accion}`**<br>**`BEGIN{}` / `END{}`** | Define el delimitador de columnas (por defecto es cualquier espacio/tabulador).<br>Accede a la columna 1, 2, y a la **última columna** (`$NF`).<br>Variable con el número de línea actual.<br>Ejecuta la acción solo si la línea cumple la condición/patrón.<br>Ejecuta código antes de empezar o al terminar (ideal para totales). | `awk -F':' '$3 >= 1000 {print $1, $NF}' /etc/passwd`<br>*(Usuario y shell de usuarios reales)*<br><br>`ls -l \| awk '{s += $5} END {print s/1024/1024 " MB"}'`<br>*(Suma el peso de todos los archivos y lo pasa a MB)* |
| **`sed`** | **`'s/viejo/nuevo/g'`**<br>**`-i`**<br>**`-E`**<br>**`'/patron/d'`**<br>**`-n '5,15p'`** | Sustituye `viejo` por `nuevo` en toda la línea (`g`).<br>Edita y guarda el archivo directamente (*in-place*).<br>Activa regex extendidas.<br>Elimina todas las líneas que coincidan con el patrón.<br>Imprime únicamente el rango de líneas del 5 al 15. | `sed -i 's/http:/https:/g' enlaces.txt`<br>*(Reemplaza http por https dentro del fichero)*<br><br>`sed '/^#/d; /^$/d' archivo.conf`<br>*(Limpia comentarios y líneas en blanco)* |
| **`cut`** | **`-d 'C'`**<br>**`-f 1,3-5`**<br>**`--complement`**<br>**`-c 1-10`** | Define un delimitador de un solo carácter.<br>Extrae la columna 1 y de la 3 a la 5.<br>Extrae **todas las columnas EXCEPTO** las indicadas.<br>Corta por posición de caracteres (del 1 al 10). | `cut -d',' -f1,4 --complement tabla.csv`<br>*(Muestra el CSV eliminando las columnas 1 y 4)* |
| **`tr`** | **`-d 'set'`**<br>**`-s 'set'`**<br>**`-c`** | Borra todos los caracteres del conjunto.<br>Comprime caracteres repetidos consecutivos en uno solo.<br>Complemento: aplica la acción a todo lo que **NO** esté en el conjunto. | `tr -s ' ' < entrada.txt`<br>*(Reduce múltiples espacios seguidos a uno solo)*<br><br>`tr -cs 'a-zA-Z' '\n' < texto.txt`<br>*(Convierte un texto en una lista de palabras, una por línea)* |

---

### Tabla 3: Ordenación, Agrupación y Conteo (`sort`, `uniq`, `wc`, `du`, `diff`)
*Para sacar estadísticas, rankings, detectar duplicados y medir espacio.*

| Comando | Operandos / Flags Imprescindibles | Qué hace exactamente | Ejemplo práctico de alto valor |
| :--- | :--- | :--- | :--- |
| **`sort`** | **`-t 'C'`**<br>**`-k N,N`**<br>**`-n`**<br>**`-h`**<br>**`-r`**<br>**`-u`** | Define el separador de columnas.<br>Ordena **estrictamente** por la columna `N` (sin arrastrar las siguientes).<br>Ordenación numérica real (`2` antes que `10`).<br>Ordenación de tamaños humanos (`K`, `M`, `G`, `T`).<br>Orden inverso (de mayor a menor / Z-A).<br>Ordena y elimina duplicados. | `sort -t':' -k3,3nr -k1,1 /etc/passwd`<br>*(Ordena por UID de mayor a menor y desempata alfabéticamente)* |
| **`uniq`** | **`-c`**<br>**`-d`**<br>**`-u`**<br>**`-i`** | Cuenta repeticiones de líneas consecutivas (siempre requiere `sort` antes).<br>Muestra **solo** las líneas que estaban duplicadas.<br>Muestra **solo** las líneas únicas (que aparecían una vez).<br>Ignora mayúsculas/minúsculas al comparar. | `sort accesos.log \| uniq -c \| sort -nr \| head -n 5`<br>*(Saca el Top 5 de líneas más repetidas)* |
| **`wc`** | **`-l`**<br>**`-w`**<br>**`-c`** | Cuenta **líneas** (el más usado).<br>Cuenta **palabras**.<br>Cuenta **bytes / caracteres**. | `find . -type f \| wc -l`<br>*(Cuenta cuántos archivos existen en total)* |
| **`du`** | **`-h`**<br>**`-s`**<br>**`-a`**<br>**`-d N`** (`--max-depth=N`) | Muestra tamaños legibles (`B`, `K`, `M`, `G`).<br>Muestra solo el resumen total del elemento.<br>Incluye archivos individuales además de directorios.<br>Muestra el tamaño solo hasta `N` niveles de profundidad. | `du -h -d 1 /var \| sort -hr`<br>*(Muestra qué carpeta de primer nivel ocupa más espacio)* |
| **`diff`** | **`-u`**<br>**`-y`**<br>**`-i`** / **`-w`** | Formato unificado (el estándar de Git, muestra `+` y `-`).<br>Compara dos archivos lado a lado en dos columnas.<br>Ignora mayúsculas (`-i`) o espacios en blanco (`-w`). | `diff -u version1.sh version2.sh`<br>*(Muestra exactamente qué líneas cambiaron entre dos scripts)* |

---

### Tabla 4: Ejecución Masiva, Procesos y Red (`xargs`, `ps`, `kill`, `curl`, `ss`)
*Para automatizar acciones en lote, controlar procesos colgados y diagnosticar red.*

| Comando | Operandos / Flags Imprescindibles | Qué hace exactamente | Ejemplo práctico de alto valor |
| :--- | :--- | :--- | :--- |
| **`xargs`** | **`-n 1`**<br>**`-P N`**<br>**`-I {}`**<br>**`-0`** (junto a `find -print0`) | Ejecuta el comando pasando 1 argumento cada vez.<br>**Paraleliza**: lanza `N` procesos simultáneos.<br>Sustituye `{}` por el argumento recibido en cualquier posición.<br>Maneja de forma segura nombres de archivo con espacios. | `find . -name "*.jpg" -print0 \| xargs -0 -P 4 -I {} cp {} /backup/`<br>*(Copia todas las fotos en paralelo usando 4 hilos sin fallar por espacios)* |
| **`ps`** | **`aux`**<br>**`-ef`** | Lista todos los procesos del sistema con uso de CPU, RAM y usuario.<br>Formato estándar con PID y PPID (proceso padre). | `ps aux --sort=-%mem \| head -n 6`<br>*(Muestra los 5 procesos que más memoria RAM consumen)* |
| **`kill`** / **`pkill`** | **`-9`** (`SIGKILL`)<br>**`-15`** (`SIGTERM`)<br>**`pkill -f "nombre"`** | Mata el proceso inmediatamente sin dejarle cerrar nada.<br>Pide al proceso que termine de forma limpia (por defecto).<br>Mata procesos buscando por su nombre o comando completo (sin buscar el PID). | `pkill -9 -f "python3 script_colgado.py"`<br>*(Mata el script directamente por su nombre)* |
| **`curl`** | **`-s`**<br>**`-I`**<br>**`-o archivo`**<br>**`-L`** | Modo silencioso (oculta la barra de progreso, vital en scripts).<br>Descarga solo las cabeceras HTTP (código 200, 404, etc.).<br>Guarda la descarga con un nombre específico.<br>Sigue redirecciones automáticamente. | `curl -sI https://google.com \| head -n 1`<br>*(Comprueba rápidamente el código de estado HTTP de una web)* |

---

### Tabla 5: Operadores y Variables Especiales de Bash (El pegamento)
*Sin estos símbolos no puedes conectar comandos ni controlar la lógica de un script.*

| Símbolo / Operador | Nombre / Función | Qué hace exactamente | Ejemplo práctico |
| :--- | :--- | :--- | :--- |
| **`\|`** | Tubería (*Pipe*) | Envía la salida estándar (`stdout`) del comando izquierdo como entrada del derecho. | `cat log.txt \| grep "ERROR" \| wc -l` |
| **`>`** y **`>>`** | Redirección de salida | `>` sobrescribe el archivo; `>>` añade el resultado al final sin borrar lo anterior. | `echo "Fin de log" >> registro.txt` |
| **`2>/dev/null`** | Silenciador de errores | Envía los mensajes de error (`stderr`) al agujero negro para limpiar la pantalla. | `find / -name "archivo" 2>/dev/null` |
| **`&&`** y **`\|\|`** | Ejecución condicional | `&&`: ejecuta el 2º **solo si** el 1º tuvo éxito.<br>`\|\|`: ejecuta el 2º **solo si** el 1º falló. | `mkdir backup && cp *.sh backup/` |
| **`$(comando)`** | Sustitución de comando | Ejecuta un comando y guarda su resultado dentro de una variable o texto. | `lineas=$(wc -l < datos.txt)` |
| **`<(comando)`** | Sustitución de proceso | Hace que la salida de un comando actúe como si fuera un archivo físico. | `diff <(sort lista1.txt) <(sort lista2.txt)` |
| **`$#`**, **`$@`**, **`$?`** | Variables especiales | `$#`: número de parámetros recibidos.<br>`"$@"`: lista de todos los parámetros recibidos intactos.<br>`$?`: código de salida del último comando (`0` = éxito, distinto de `0` = error). | `if [ $# -lt 2 ]; then exit 1; fi` |