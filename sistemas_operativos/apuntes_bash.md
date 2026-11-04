# APUNTES COMPLETOS DE BASH — De cero a dominio

> **Asignatura:** Sistemas Operativos
> **Basado en:** prácticas 7, 8, 9, 10 y 11 de programación en Shell, `EjerciciosBash.md`, `RegEx.md` y `manual_linux/basico_scripting.md` (directorio `Guias-Basicas/sistemas_operativos/`).
> **Teoría del resto de la asignatura:** ver `README.md` (4 bloques: fundamentos, procesos, memoria, E/S y almacenamiento) y las carpetas `Bloque_1` … `Bloque_4`.

---

## Índice

| § | Sección |
|---|---------|
| 1 | Qué es Bash, la terminal y la shell |
| 2 | Primer script: creación, permisos y ejecución |
| 3 | `echo`, `read` y sustitución de comandos `$()` |
| 4 | Variables |
| 5 | Parámetros del script (argumentos) |
| 6 | Comillas y escapes |
| 7 | Redirecciones, tuberías y códigos de salida |
| 8 | Filtros de texto: `cat`, `head`, `tail`, `wc`, `grep` |
| 9 | `cut` (extraer columnas) |
| 10 | **`sort` (ordenar)** ★ |
| 11 | **`uniq` (duplicados)** ★ |
| 12 | **`awk` y `-F` (procesar línea a línea)** ★ |
| 13 | Tuberías de examen: encadenar filtros |
| 14 | Condicionales `if` |
| 15 | `case` (múltiples opciones) |
| 16 | Bucles `for`, `while`, `until` |
| 17 | Aritmética e indirección |
| 18 | Listas, arrays e `IFS` |
| 19 | Expansión de parámetros (manipular cadenas) |
| 20 | `printf` (salida formateada) |
| 21 | Funciones |
| 22 | Expresiones regulares |
| 23 | Depuración, colores y buenas prácticas |
| 24 | Ejercicios resueltos de las prácticas 7–11 |
| 25 | Chuleta rápida (cheat sheet) |

★ = secciones con hincapié especial.

---

# 1. Qué es Bash, la terminal y la shell

- **Terminal / consola:** ventana donde escribes comandos.
- **Shell (intérprete de comandos):** programa que lee lo que escribes y lo ejecuta. **Bash** (*Bourne Again SHell*) es la shell más común en Linux.
- **Script (shell script):** archivo de texto con una lista de comandos que la shell ejecuta secuencialmente. No necesita compilación: solo permisos de ejecución.
- **Distribución de trabajo:** la shell parsea la línea (expande variables, aplica redirecciones) y **después** lanza los programas.

### Órdenes internas vs. externas

| Tipo | Qué son | Ejemplos | ¿Crean proceso? |
|---|---|---|---|
| **Internas** (builtins) | Las ejecuta la propia shell | `cd`, `pwd`, `echo`, `test`, `export`, `unset`, `source` | No |
| **Externas** | Programas del disco | `ls`, `grep`, `sort`, `awk`, `cat`, `kill` | Sí (proceso hijo) |

```bash
type cd          # es orden interna
type ls          # es /usr/bin/ls (externa)
type -a echo     # muestra TODAS las coincidencias (interna y externa)
```

> **¿Por qué `cd` no puede ser un programa externo?** Porque cada proceso tiene su propio directorio de trabajo: si `cd` fuera externo, cambiaría el directorio de un proceso hijo que moriría al terminar, y la shell seguiría donde estaba. Por eso debe ser interna.

### Ayuda: nunca te sepas de memoria todo

```bash
man sort          # manual de la orden (sección 1 por defecto)
man 5 passwd      # formato del fichero passwd (sección 5)
man -k sort       # = apropos sort: busca en todas las secciones
whatis sort       # descripción de una línea
apropos awk       # busca páginas cuya descripción contenga "awk"
help echo         # ayuda de la orden INTERNA de bash
```

Secciones del manual: **1** órdenes de usuario · **2** llamadas al sistema · **3** funciones de biblioteca · **5** formatos de fichero · **7** temas/convenios · **8** administración.

Dentro de `man` (paginador `less`): `Espacio`/`b` avanzar/retroceder · `/patrón` buscar · `n`/`N` siguiente/anterior · `g`/`G` inicio/final · `q` salir.

### Entorno (de la práctica 2)

```bash
cat /etc/os-release   # distribución instalada
uname -a              # kernel y hardware
echo "$BASH_VERSION"  # versión de bash
```

---

### ✏️ Ejercicios de la sección 1

1. Clasifica como internas o externas: `cd`, `pwd`, `echo`, `ls`, `test`, `kill`, `time`. Usa `type -a` para comprobar las que existen de las dos formas.
2. ¿Qué comando te dice qué hace otro comando sin abrir el manual completo? (`whatis`) ¿Y cuál busca en todas las secciones? (`apropos` / `man -k`)
3. Ejecuta `help echo` y `man 1 echo`: nombra una diferencia observable entre ambas.

<details><summary>Respuestas</summary>

1. Internas: `cd`, `pwd`, `echo`, `test`, `kill` (y `time` es palabra reservada **y** programa). Externas: `ls`. Con `type -a echo` ves que existen de las dos formas.
2. `whatis` / `apropos` (o `man -k`).
3. `man 1 echo` documenta `--help` y `--version` (que el echo interno no tiene); `help echo` detalla las secuencias de escape de `-e`.

</details>

---

# 2. Primer script: creación, permisos y ejecución

### Anatomía de un script estructurado

```bash
#!/bin/bash
# Autor: Tu Nombre
# Descripción: Qué hace este script
# Versión: 1.0

echo "Ejecutando script..."
```

1. **Shebang (`#!`)**: **primera línea** del archivo. Indica la ruta absoluta del intérprete: `#!/bin/bash`. Los dos primeros bytes del archivo deben ser `#!`.
   - Para saber la ruta: `which bash`
2. **Comentarios (`#`)**: todo lo que va detrás de `#` (al inicio de la palabra) lo ignora la shell. Sirven para documentar autor, fecha y propósito.
3. **Órdenes**: los comandos, que se ejecutan **de arriba abajo, en orden**.

### Creación, permisos y ejecución

```bash
touch mi_script.sh        # crear (o directamente con nano/vim)
nano mi_script.sh         # escribirlo
chmod +x mi_script.sh     # dar permiso de ejecución
./mi_script.sh            # ejecutarlo
```

- **Convención:** extensión `.sh` (opcional, pero recomendada).
- **`./` es obligatorio** porque el directorio actual normalmente **no** está en `$PATH` (por seguridad).
- **Conflictos de nombre:** comprueba que no pises una orden existente: `type -a mi_script`
- **Ejecutar desde cualquier sitio:** guarda tus scripts en `~/bin` (que en muchas distros ya está en el `$PATH`):

```bash
mkdir -p ~/bin
mv mi_script.sh ~/bin/
mi_script.sh              # ya funciona sin ./ desde cualquier directorio
```

- **Ejecutar con otra shell/interpretación:** `bash mi_script.sh` (no hace falta `chmod`).

### Depuración

| Comando | Efecto |
|---|---|
| `bash -n mi_script.sh` | Comprueba **solo la sintaxis**, sin ejecutar |
| `bash -v mi_script.sh` | Muestra cada línea **mientras se lee** (verbose) |
| `bash -x mi_script.sh` | Muestra cada orden **tras la expansión** de variables (trace) |
| `shellcheck mi_script.sh` | Analizador estático: `sudo apt install shellcheck` |

### Orden correcto al crear un script

```text
1. Escribir la cabecera (shebang + comentarios)
2. Validar argumentos (¡siempre al principio!)
3. Hacer el trabajo
4. Devolver un código de salida coherente (exit 0 = bien, ≠0 = error)
```

---

### ✏️ Ejercicios de la sección 2

1. Crea `hola.sh` que salude con `echo`, dale permisos y ejecútalo de las dos formas (`./hola.sh` y `bash hola.sh`).
2. Comprueba con `bash -n` que no tiene errores de sintaxis un script con un `fi` sin cerrar.
3. Guarda el script en `~/bin` y ejecútalo desde `/tmp` sin poner ruta.

<details><summary>Respuestas</summary>

```bash
#!/bin/bash
echo "Hola Mundo"
```
```bash
chmod +x hola.sh && ./hola.sh
bash -n hola.sh   # dirá algo como "syntax error: unexpected end of file"
mkdir -p ~/bin && mv hola.sh ~/bin/ && cd /tmp && hola.sh
```
</details>

---

# 3. `echo`, `read` y sustitución de comandos `$()`

## 3.1 `echo` (salida)

```bash
echo "Hola Mundo"     # imprime Hola Mundo + salto de línea
echo -n "Sin salto"    # -n: NO añade salto de línea al final
echo -e "Fila1\nFila2" # -e: interpreta \n (salto), \t (tabulador), \c (sin salto)...
echo -e "Aviso:\turgente"
```

## 3.2 Sustitución de comandos `$(...)`

Ejecuta lo de dentro y **sustituye por su salida**.

```bash
echo "Hoy es $(date)"
ficheros=$(ls)              # guarda la LISTA de ficheros como una cadena
n=$(wc -l < /etc/passwd)    # guarda el número de líneas
fecha=$(date +%Y-%m-%d)     # fecha en formato 2026-11-03
usuario=$(whoami)
```

> ⚠️ `resultado='ls'` guarda la **cadena literal** "ls". `resultado=$(ls)` guarda lo que **imprime** `ls`.

## 3.3 `read` (entrada)

Lee de la entrada estándar y lo guarda en una variable.

```bash
#!/bin/bash
echo -n "Escribe tu nombre: "
read nombre            # simple
echo "Hola, $nombre"

read -p "Edad: " edad   # -p: muestra el prompt directamente
read -s clave           # -s: sin eco (contraseña)
read -r linea           # -r: no interpreta barras invertidas
```

Si `read` no recibe nada (Ctrl+D), la variable queda vacía: compruébalo con `[ -n "$variable" ]`.

---

### ✏️ Ejercicios de la sección 3

1. Escribe un script que pida el nombre con `read -p` y salude.
2. Guarda en una variable el número de usuarios del sistema (`/etc/passwd`) y muéstralo con un mensaje.
3. ¿Qué imprime `echo "Son $(echo 2 + 2)"`? ¿Y por qué no es 4?

<details><summary>Respuestas</summary>

```bash
#!/bin/bash
read -p "¿Cómo te llamas? " nombre
echo "Hola, $nombre!"
```
```bash
n=$(grep -c ':' /etc/passwd)   # o: n=$(wc -l < /etc/passwd)
echo "Hay $n entradas en /etc/passwd"
```
3. Imprime `Son 2 + 2`: `$(...)` ejecuta el comando `echo`, no hace aritmética (eso es `$(( ))`).
</details>

---

# 4. Variables

### Reglas de oro

1. **Nombres:** solo letras, números y `_`; **no pueden empezar por número**. Ejemplos válidos: `mi_var`, `_temp`, `var2`.
2. **NUNCA mayúsculas** para variables tuyas: `$PATH`, `$HOME`, `$USER`, `$LANG`… están reservadas para el sistema.
3. **Sin espacios alrededor del `=`:**
   ```bash
   var=hola          # ✅
   var2="hola mundo" # ✅ (con espacios dentro, hace falta comillas)
   var3=hola mundo   # ❌ error: "mundo: orden no encontrada"
   ```
4. **Acceso:** `$var` o, mejor, `${var}` (delimita el nombre).
5. **Borrar:** `unset var`
6. **Tipado:** **todo es cadena de texto**. Bash no hace sumas mágicas:
   ```bash
   resultado=1+2
   echo $resultado   # imprime 1+2  (¡la cadena!)
   ```

### Entorno vs. del script

```bash
export MIVAR=valor   # visible también en los procesos hijos
echo $MIVAR
env | grep MIVAR     # ver variables de entorno
```

| Variable | Significado |
|---|---|
| `$HOME` | Directorio personal `/home/usuario` |
| `$USER` | Usuario actual |
| `$PATH` | Lista de directorios donde se buscan los comandos (separados por `:`) |
| `$PWD` | Directorio actual |
| `$SHELL` | Shell por defecto |
| `$BASH_VERSION` | Versión de bash |
| `$RANDOM` | Número aleatorio 0–32767 |
| `$LINUM` / `$0` | (ver sección 5) |

### Truco: variables dentro de variables

```bash
var1=3
var2=${var1}hola   # -> 3hola  ✅ (llaves delimitan)
var3=$var1hola     # -> busca la variable "var1hola" (no existe) -> vacío
```

---

### ✏️ Ejercicios de la sección 4

1. ¿Qué pasa con `var1=3` + `unset var1` + `echo $var1`? (prueba `pruebavariables03.sh`)
2. Corrige: `mi edad=18`
3. Guarda tu ruta de trabajo en una variable e imprímela con `echo "Estás en ${PWD}"`.

<details><summary>Respuestas</summary>

1. No hay error: bash trata las variables inexistentes como cadena vacía.
2. `mi_edad=18` (los nombres no admiten espacios).
3. `mi_ruta=$PWD`
</details>

---

# 5. Parámetros del script (argumentos)

Cuando ejecutas `./script.sh arg1 arg2 "arg 3"`:

| Parámetro | Significado |
|---|---|
| `$0` | Nombre/ruta con la que se invocó el script |
| `$1`, `$2`, `$3`… | Argumento 1º, 2º, 3º… |
| `${10}` | **Obligatorio usar llaves** a partir de la posición 10 |
| `$#` | **Número total** de argumentos |
| `$*` | Todos los argumentos (sin comillas: se parte por espacios) |
| `$@` | Todos los argumentos (como lista de palabras) |
| `"$*"` | Todos los argumentos **concatenados en una sola cadena** |
| `"$@"` | Todos los argumentos **respetando cada uno como elemento** ← el correcto para bucles |
| `$$` | PID de la shell que ejecuta el script |
| `${!#}` | **Valor del último argumento** (indirección sobre `$#`) |
| `$?` | Código de salida del **último comando** (0 = éxito) |

### Ejemplo: comprobar argumentos (patrón de examen)

```bash
#!/bin/bash
# uso: ./saluda.sh <nombre>

if [ $# -ne 1 ]; then        # ¿exactamente 1 argumento?
    echo "Uso: $0 <nombre>"
    exit 1                    # código de error
fi

echo "Hola, $1"
exit 0                        # código de éxito
```

```bash
./saluda.sh Ana     # Hola, Ana
./saluda.sh         # Uso: ./saluda.sh <nombre>  (y sale con error)
```

### Diferencia crucial `"$*"` vs `"$@"`

```bash
./script.sh 1 2 "3 4" 5

"$*"  ->  "1 2 3 4 5"      (una sola palabra)
"$@"  ->  "1"  "2"  "3 4"  "5"   (4 elementos: los espacios internos se respetan)
```

**Regla:** en bucles usa **siempre `"$@"`**.

---

### ✏️ Ejercicios de la sección 5

1. Escribe `info.sh` que imprima: número de argumentos, todos ellos, y el primero y el último.
2. ¿Qué imprime `echo ${!#}` en `./t.sh a b c`?
3. Valida que se pasen exactamente 2 argumentos y muestra mensaje de uso si falla.

<details><summary>Respuestas</summary>

```bash
#!/bin/bash
echo "Nº argumentos: $#"
echo "Todos: $@"
echo "Primero: $1"
echo "Último: ${!#}"
```
2. `c`
3. `if [ $# -ne 2 ]; then echo "Uso: $0 <a> <b>"; exit 1; fi`
</details>

---

# 6. Comillas y escapes

| Tipo | Sintaxis | Comportamiento |
|---|---|---|
| **Comillas dobles** | `"texto"` | **Sí** expande `$var`, `$(comando)`, `` `comando` `` e interpretan algunos escapes |
| **Comillas simples** | `'texto'` | **No** expande nada: todo literal (ideal para regex y `$` literales) |
| **Barra invertida** | `\$` | Neutraliza el significado del carácter siguiente |

```bash
nombre=Ana
echo "Hola $nombre"      # Hola Ana
echo 'Hola $nombre'      # Hola $nombre
echo "El precio es 5\€"  # El precio es 5€
echo "Usa \$HOME para..."# Usa $HOME para...
```

**Siempre entrecomilla variables y rutas:** `rm "$fichero"` evita desastres con nombres con espacios o glob (`*`).

---

### ✏️ Ejercicios de la sección 6

1. Imprime literalmente: `La ruta es $HOME` (sin que se expanda).
2. ¿Por qué falla `rm $fichero` si el archivo se llama `mi foto.txt`?

<details><summary>Respuestas</summary>

1. `echo 'La ruta es $HOME'`
2. Sin comillas, bash parte por espacios: intenta borrar `mi` y `foto.txt`.
</details>

---

# 7. Redirecciones, tuberías y códigos de salida

### Flujos estándar

| Descriptor | Nombre | Abreviatura |
|---|---|---|
| 0 | stdin (entrada) | `<` |
| 1 | stdout (salida normal) | `>` |
| 2 | stderr (errores) | `2>` |

### Operadores de redirección

| Operador | Qué hace | Ejemplo |
|---|---|---|
| `>` | **Sobrescribe** stdout en el archivo | `ls -l > lista.txt` |
| `>>` | **Añade** al final del archivo | `ps -ef >> procesos.txt` |
| `2>` | Sobrescribe solo errores | `g++ main.cpp 2> errores.log` |
| `2>>` | Añade errores | `g++ main.cpp 2>> errores.log` |
| `&>` | Sobrescribe **todo** (stdout+stderr) | `g++ main.cpp &> todo.log` |
| `<` | Usa un archivo como entrada | `sort < lista.txt` |
| `<<` | Entrada desde la propia línea (heredoc) | `cat << FIN` |
| `2>/dev/null` | **Descarta** los errores (silenciar) | `comando_ruidoso 2>/dev/null` |
| `> /dev/null` | Descarta la salida normal | `chmod +x f 2>/dev/null` |
| `<>` | Archivo como entrada y salida | `cmd <> fichero.txt` |

> ⚠️ `>` sobre un archivo existente **lo vacía**. Si solo quieres comprobar si existe sin borrar nada, no redirijas encima.

### Tuberías (pipes) `|`

La **salida** de un comando pasa a ser la **entrada** del siguiente:

```bash
cat /etc/passwd | grep usuario | cut -d: -f1 | sort | uniq
```

```
Comando1  ==[ | ]==>  Comando2  ==[ | ]==>  Comando3     (en memoria, sin ficheros intermedios)
```

### Operadores de encadenamiento

| Operador | Significado |
|---|---|
| `cmd1 && cmd2` | Ejecuta `cmd2` **solo si** `cmd1` tuvo éxito (código 0) |
| `cmd1 \|\| cmd2` | Ejecuta `cmd2` **solo si** `cmd1` **falló** |
| `cmd1 ; cmd2` | Ejecuta `cmd2` **siempre**, haya tenido éxito o no |
| `$( )` o `` ` ` `` | Sustitución de comandos |
| `<(cmd)` | *Process substitution*: da a `cmd` la forma de un fichero |

### Códigos de salida `$?`

```bash
ls /no_existe
echo $?      # 2  (≠ 0 significa error)

if [ $? -eq 0 ]; then
    echo "Todo bien"
else
    echo "Algo falló"
fi
```

**Convención:** `0` = éxito, cualquier otro valor = tipo de error. `exit 0` / `exit 1` al final de tus scripts.

---

### ✏️ Ejercicios de la sección 7

1. Redirige los errores de `ls /ruta_mala` a un fichero `err.log` y la salida normal a `out.log`.
2. Explica la diferencia entre `a ; b` y `a && b`.
3. ¿Qué hace `command 2>/dev/null`?
4. Muestra solo la tercera línea de `/etc/passwd` usando `head` y `tail`.

<details><summary>Respuestas</summary>

1. `ls /ruta_mala > out.log 2> err.log`
2. `;` ejecuta `b` siempre; `&&` solo si `a` devolvió 0.
3. Oculta los mensajes de error.
4. `head -n 3 /etc/passwd | tail -n 1`
</details>

---

# 8. Filtros de texto: `cat`, `head`, `tail`, `wc`, `grep`

Estos comandos son la base de casi **toda** tubería de examen.

### `cat` — mostrar/unir

```bash
cat fichero.txt            # muestra todo
cat a.txt b.txt > c.txt    # concatena
cat -n fichero.txt         # numera líneas
```

### `head` / `tail` — principio y final

```bash
head fichero.txt           # 10 primeras líneas (por defecto)
head -n 3 fichero.txt      # 3 primeras
head -c 100 fichero.txt    # 100 primeros bytes
tail fichero.txt           # 10 últimas
tail -n 5 fichero.txt      # 5 últimas
tail -f log.txt            # sigue el fichero en vivo (logs)
tail -n +2 fichero.txt     # todas las líneas DESDE la 2ª (omite la 1ª) ← muy usado con `ls -l`
```

### `wc` — contar

```bash
wc -l fichero.txt   # líneas
wc -w fichero.txt   # palabras
wc -c fichero.txt   # bytes
wc -m fichero.txt   # caracteres
wc < fichero.txt    # sin nombre de fichero en la salida
```

### `grep` — buscar patrones

```bash
grep "universidad" apuntes.txt         # líneas que contienen "universidad"
grep -i "error" log.txt                # ignora mayúsculas/minúsculas
grep -v "comentario" fichero.txt       # líneas que NO coinciden (invertir)
grep -c "ERROR" log.txt                # cuenta las coincidencias (nº de líneas)
grep -o "ERROR" log.txt                # imprime SOLO la coincidencia, una por línea
grep -n "ERROR" log.txt                # numera las líneas
grep -r "TODO" src/                    # busca recursivamente en directorios
grep -E "^(URIs|Suites)" fichero       # regex extendidas (alternancia |, +, ?...)
grep "^$USER:" /etc/passwd             # ancla ^ = inicio de línea
grep '/bin/false$' /etc/passwd         # ancla $ = final de línea
grep -E '^(UID|GID)_(MIN|MAX)' /etc/login.defs | grep -v '#'
```

**Truco clásico (práctica 7, ejercicio 1):** contar las veces que aparece una palabra:

```bash
numero=$(grep -io "$palabra" "$fichero" | wc -l)
```
- `-i` también cuenta `HOLA`, `Hola`…
- `-o` saca cada coincidencia en su propia línea → `wc -l` las cuenta.

---

### ✏️ Ejercicios de la sección 8

1. Cuenta cuántas líneas de `/etc/passwd` terminan en `/bin/bash`.
2. Muestra las 5 últimas líneas de un log sin mostrar las 5 primeras ni las 3 últimas (`tail` + `head`).
3. Lista los ficheros de `src/` que contengan `TODO` sin mostrar el contenido, solo nombres.

<details><summary>Respuestas</summary>

1. `grep -c '/bin/bash$' /etc/passwd`
2. `tail -n 8 log.txt | head -n 5`
3. `grep -rl "TODO" src/`
</details>

---

# 9. `cut` (extraer columnas)

`cut` trocea cada línea por un **delimitador** y se queda con los campos indicados. Es el "hermano simple" de `awk`.

```bash
cut -d':' -f1 /etc/passwd        # primer campo separado por :
cut -d':' -f1,3 /etc/passwd      # campos 1 y 3
cut -d':' -f2-4 fichero.txt      # del 2º al 4º
cut -d',' -f3 datos.csv          # CSV
cut -c1-10 fichero.txt           # caracteres 1 a 10 (con -c, no con -d/-f)
cut -s -d':' -f1 fichero.txt     # -s: SOLO líneas que contienen el delimitador
```

| Opción | Significado |
|---|---|
| `-d X` | **delimiter**: carácter separador (por defecto **tabulador**) |
| `-f n` | **fields**: campo(s) a extraer (1-based) |
| `-c n` | **characters**: por posición de caracteres |
| `-s` | Salta las líneas **sin** delimitador |

```bash
echo "aa:bb:cc:dd" | cut -d: -f3     # cc
echo "aa:bb:cc:dd" | cut -d: -f1,3   # aa:cc
echo "aa:bb:cc:dd" | cut -d: -f2-4   # bb:cc:dd
```

> En los ficheros de configuración del sistema (`/etc/passwd`, `/etc/group`) el separador es `:` → `cut -d: -f1`.

---

### ✏️ Ejercicios de la sección 9

1. Extrae el nombre de usuario (campo 1) y el shell (campo 7) de `/etc/passwd`.
2. Con `cut`, ¿cómo sacas el dominio de `usuario@ejemplo.com` (separador `@`, campo 2)?

<details><summary>Respuestas</summary>

1. `cut -d: -f1 /etc/passwd` y `cut -d: -f7 /etc/passwd`
2. `echo "usuario@ejemplo.com" | cut -d@ -f2`
</details>

---

# 10. ★ `sort` — ORDENAR

> **`sort` es para ORDENAR.** Recibe líneas de texto y las reordena. Es el filtro que casi siempre va **antes** de `uniq` (para que los iguales queden juntos).

```bash
sort fichero.txt          # orden alfabético (según LC_COLLATE)
sort -o salida.txt f.txt  # -o: guarda el resultado en un fichero
```

### Opciones principales

| Opción | Significado | Ejemplo típico |
|---|---|---|
| **`-n`** | Ordena de forma **numérica** (no alfabética: "10" > "9") | `sort -n` |
| **`-r`** | **Invierte** el orden (de mayor a menor) | `sort -nr` |
| **`-h`** | Ordena números **con sufijos legibles** (`1K`, `2M`, `3G`…) como los escribe `du -h` | `du -ah \| sort -hr` |
| **`-k2,2`** | Ordena usando **la columna 2** (de la 2 a la 2) | `ls -l \| sort -k2,2 -nr` |
| **`-t X`** | Define el **carácter separador** de columnas (por defecto espacios) | `sort -t: -k3,3` |
| **`-u`** | **Elimina duplicados** (deja una copia de cada línea) | `sort -u` = `sort \| uniq` |
| **`-f`** | Ignora mayúsculas/minúsculas (*fold*) | `sort -f` |
| **`-b`** | Ignora los espacios iniciales al comparar | `sort -b` |
| **`-V`** | Ordena por **versión** (`file2` < `file10`) | `sort -V` |
| **`-R`** | Orden **aleatorio** | `sort -R` |

### Trampas frecuentes

1. **`sort` sin `-n` ordena alfabéticamente**: `10` va **antes** que `2`. Para números usa **siempre `-n`**.
2. **`-n` + `-h` no se mezclan a la ligera**: si `du` te da `67K`, necesitas **`sort -h`** (no `-n`, que leería "67K" como 67 y luego fallaría con "1M").
3. **`-r` es lo opuesto a -n**: `-nr` = numérico descendente.
4. **Orden según el locale**: el orden alfabético lo define `LC_COLLATE` (prioridad: `LC_ALL` > `LC_COLLATE` > `LANG`). Para un orden **por bytes** (determinista en cualquier equipo): `LC_ALL=C sort`.

### Ejemplos reales (de las prácticas)

```bash
# Práctica 7, ej.3 — los N ficheros que MÁS ocupan (con sufijos K/M/G)
du -ah "$dir" | sort -hr | grep "$extension" | head -n "$num"

# Práctica 7, ej.4 — los N ficheros con MÁS enlaces duros (2ª columna de ls -l)
ls -l "$dir" | tail -n +2 | sort -k2,2 -nr | head -n "$num"
#         (tail -n +2 quita la línea "total XX")
```

### `sort` + `uniq`: la combinación estrella

```bash
sort fichero | uniq        # ORDENA y quita duplicados (aunque no estén juntos)
sort -u fichero            # idéntico, en un solo paso
sort -n fichero | uniq -c  # cuenta cuántas veces aparece cada número
```

---

### ✏️ Ejercicios de la sección 10

1. Ordena numéricamente de mayor a menor una lista de tamaños: `10K 2M 9K 1G 512B`.
2. ¿Qué imprime `printf "2\n10\n1\n" | sort`? ¿Y con `sort -n`?
3. Ordena `/etc/passwd` por el campo 3 (UID) numéricamente usando `-t:` y `-k`.
4. Muestra los 3 procesos que más memoria ocupan (`ps` o `top -bn1`).

<details><summary>Respuestas</summary>

1. `printf "10K\n2M\n9K\n1G\n512B\n" | sort -hr`
2. `sort` → `1`, `10`, `2` (alfabético) · `sort -n` → `1`, `2`, `10`
3. `sort -t: -k3,3n /etc/passwd`
4. `ps aux --sort=-%mem | head -n 4`
</details>

---

# 11. ★ `uniq` — DUPLICADOS (ojo con `-d`)

> **`uniq` trabaja sobre líneas ADYACENTES.** Por eso **casi siempre va después de `sort`**: al ordenar, los iguales quedan pegados y `uniq` puede verlos.

### Las cuatro formas de `uniq` (memoriza esto)

| Comando | Qué hace exactamente |
|---|---|
| `uniq fichero` | **Elimina** las líneas duplicadas **adyacentes** dejando **una** copia de cada una |
| **`uniq -d`** | **NO elimina nada**: muestra **solo las líneas que están repetidas** (cada una **una sola vez**) |
| `uniq -u` | Muestra **solo las líneas NO repetidas** (las que aparecen exactamente una vez) |
| `uniq -c` | Muestra **todas** las líneas con un **contador** delante de cada una |

```bash
# Fichero de ejemplo (desordenado):
# b
# a
# b
# b
# c

sort fichero | uniq        # a, b, c        <- ELIMINA duplicados (lo que busca la gente)
sort fichero | uniq -d     # b              <- solo los que se repiten (b salía 3 veces)
sort fichero | uniq -u     # a, c           <- solo los que NO se repiten
sort fichero | uniq -c     # 1 a / 3 b / 1 c
```

### Otras opciones útiles

| Opción | Significado |
|---|---|
| `uniq -i` | Ignora mayúsculas/minúsculas al comparar |
| `uniq -f N` | Ignora los **primeros N campos** al comparar (usar con `-t`) |
| `uniq -s N` | Ignora los primeros **N caracteres** |
| `uniq -d -c` | Combina: contador solo de los repetidos |

### ¿Cuándo uso cada cosa? (árbol de decisión)

```text
¿Quieres ELIMINAR duplicados?
        │
        ├─ Los duplicados están JUNTOS (o ya lo ordenas)
        │        →  uniq                  (o directamente  sort -u)
        │
        └─ Están DISPERSOS por el fichero
                 →  sort | uniq           (equivalente: sort -u)

¿Quieres SABER cuáles se repiten?
        │
        └─  sort | uniq -d                (cada duplicado, una sola vez)

¿Quieres CONTAR cuántas veces sale cada línea?
        │
        └─  sort | uniq -c
```

### Errores clásicos

- ❌ `uniq fichero` **solo** quita repetidos **consecutivos**: si el fichero es `a b a`, `uniq` **no** toca nada (las `a` no son adyacentes). Hay que ordenar primero.
- ❌ `uniq -d` **no sirve para eliminar** repetidos: **muestra** los repetidos. (En el ejercicio 5 de la práctica 7 se usa exactamente para eso: listar los UID duplicados de `/etc/passwd`.)
- ❌ `sort | uniq -d` **no** te deja el fichero sin duplicados: te deja **solo** los duplicados.

### Ejemplo real (práctica 7, ejercicio 2 → `uniq_all.sh`)

```bash
# Quitar líneas repetidas estén o no consecutivas:
sort "$1" | uniq > "$2"
```

### Ejemplo real (práctica 7, ejercicio 5 → `num_duplicados.sh`)

```bash
# ¿Hay números repetidos en el campo N de un fichero con ':'?
duplicados=$(cut -s -d: -f"$1" "$2" | sort -n | uniq -d)

if [ -z "$duplicados" ]; then
    echo "No hay números duplicados en el campo $1 de $2"
else
    echo "Números duplicados en el campo $1 de $2:"
    echo "$duplicados"
fi
```

Flujo: `cut` extrae la columna → `sort -n` junta los iguales → **`uniq -d`** se queda con los que se repiten → `-z` comprueba si la variable está vacía.

---

### ✏️ Ejercicios de la sección 11

1. Dado `mi_lista.txt` con líneas repetidas y dispersas, escribe **dos** formas de dejarlo sin duplicados.
2. ¿Qué hace `uniq -d`? ¿Elimina o muestra? Justifícalo con un ejemplo.
3. Cuenta cuántas veces aparece cada usuario en el campo 1 de `/etc/passwd` (spoiler: 1 cada uno) y, más útil, cuenta los UID (campo 3) repetidos.
4. Explica por qué `uniq` solo funciona con adyacentes y qué truco lo arregla.

<details><summary>Respuestas</summary>

1. `sort mi_lista.txt | uniq > limpio.txt` · `sort -u mi_lista.txt > limpio.txt`
2. **Muestra** solo las líneas repetidas, una vez cada una. Ej: con `a b b c`, `uniq -d` → `b`.
3. `cut -d: -f3 /etc/passwd | sort -n | uniq -d` (vacío si no hay UID repetidos)
4. `uniq` compara cada línea **con la anterior**; al ordenar, los iguales quedan juntos y sí son adyacentes.
</details>

---

# 12. ★ `awk` y `-F` — procesar línea a línea

> **`awk` recorre el fichero LÍNEA A LÍNEA** (cada línea es un *registro*), trocea cada línea en **campos** y ejecuta acciones sobre ellos.
> **`-F` no "mira" la línea: `-F` fija el CARÁCTER SEPARADOR de CAMPOS** con el que se trocea cada línea (igual que `cut -d`).

### Sintaxis

```bash
awk  [opciones]  'patrón {acción}'  fichero1 fichero2 ...
```

- **`patrón`** (opcional): *en qué líneas* actuar. Puede ser una regex (`/error/`), una condición (`$3 > 100`), `BEGIN`/`END`, o vacío (todas las líneas).
- **`{acción}`** (opcional): *qué hacer* con esa línea. Por defecto `{print}`.
- **`-F sep`**: separador de campos. **Por defecto**: espacios y/o tabuladores (cualquier racha de blancos).

### Variables de campo (siempre con `$`)

| Elemento | Significado |
|---|---|
| `$0` | **La línea completa** (el registro entero) |
| `$1`, `$2`, `$3`… | 1º, 2º, 3º… **campo** de la línea |
| `$NF` | **Último** campo (N Field) |
| `$1 " " $2` | Concatenar campos (awk pone los espacios que tú le digas) |

| Variable | Significado |
|---|---|
| `NR` | **N**úmero de **R**egistro = contador de **líneas** leídas |
| `NF` | **N**úmero de **F**ields = **cuántos campos** tiene la línea actual |
| `FS` | *Field Separator* (equivalente a `-F`, se puede asignar) |
| `OFS` | *Output* Field Separator (espacios entre campos al imprimir) |
| `ORS` | *Output* Record Separator (`\n` por defecto) |
| `FILENAME` | Nombre del fichero que se está leyendo |

### Las 3 fases de un programa awk

```text
BEGIN  { ... }   →  se ejecuta UNA vez ANTES de leer el fichero (inicializar)
       { ... }   →  se ejecuta para CADA línea
END    { ... }   →  se ejecuta UNA vez DESPUÉS de leer todo (resumen)
```

### Ejemplos de 0 a dominar

```bash
# 1) Imprimir la línea entera
awk '{print}' fichero.txt            # = cat fichero.txt

# 2) Primer campo de cada línea (separador: espacios)
awk '{print $1}' fichero.txt

# 3) CAMBIAR EL SEPARADOR CON -F (¡lo importante!)
awk -F':' '{print $1}' /etc/passwd   # nombres de usuario (separador ':')
awk -F:  '{print $1}' /etc/passwd    # las comillas no hacen falta si no hay caracteres raros
awk -F',' '{print $2}' datos.csv     # CSV
awk -F';' '{print $1, $3}' datos.txt # imprime campo 1 y 3 separados por un espacio

# 4) La línea completa y el número de línea
awk '{print NR": "$0}' fichero.txt

# 5) Cuántos campos tiene cada línea
awk '{print NF}' fichero.txt

# 6) Último campo
awk -F':' '{print $NF}' /etc/group

# 7) Condición: SOLO las líneas donde el campo 3 es > 100
awk -F':' '$3 > 100 {print $1, $3}' /etc/passwd

# 8) Condición con regex: líneas que contienen "error"
awk '/error/' log.txt
awk '/error/ {print NR, $0}' log.txt

# 9) Fase BEGIN: poner cabecera antes de los datos
awk -F':' 'BEGIN{print "USUARIO\tSHELL"} {print $1"\t"$7}' /etc/passwd

# 10) Fase END: resumen final
awk 'END{print "Total de líneas:", NR}' /etc/passwd

# 11) SUMAR la columna 2 de un fichero de números
awk '{s+=$2} END{print s}' numeros.txt

# 12) Contar líneas con awk (equivale a wc -l)
awk 'END{print NR}' fichero.txt

# 13) Imprimir de la 5ª a la 8ª columna
awk '{for(i=5;i<=8;i++) printf "%s ", $i; print ""}' datos.txt

# 14) Unir campos: los 3 primeros con comas
awk -F':' 'BEGIN{OFS=","} {print $1,$2,$3}' /etc/group

# 15) awk sobre la salida de otro comando
apt-cache policy | grep -E '^ +[0-9]+ ' | awk '{print $1}' | sort | uniq -c
```

### `awk` vs `cut` — ¿cuál uso?

| Situación | Herramienta |
|---|---|
| Extraer 1 columna con un separador simple | `cut -d: -f1` (más rápido y simple) |
| Hacer **cálculos**, condiciones, resúmenes, formatos | **`awk`** |
| Varias columnas + lógica (`$3 > 100`) | **`awk`** |
| Separador = varios espacios seguidos | **`awk`** (`cut` con `-d ' '` deja campos vacíos) |

### Nota sobre `-F` (la duda de clase)

```bash
awk -F':' '{print $1}' /etc/passwd
       └─┬─┘
   -F fija el separador de CAMPOS de cada línea
```

- `-F` **no** selecciona ni "fija" la línea: awk **siempre** lee **todas** las líneas una a una (`NR`).
- Lo que `-F` fija es **con qué carácter se parte cada línea en `$1`, `$2`…**.
- Si no pones `-F`, awk usa espacios/tabuladores: `awk '{print $1}'` coge la primera palabra.
- Puedes cambiarlo dentro del programa con `-F` **o** con `BEGIN{FS=":"}` (equivalente).

---

### ✏️ Ejercicios de la sección 12

1. Con `awk`, imprime el campo 1 y el campo 7 de `/etc/passwd` usando `:` como separador.
2. ¿Cuál es la diferencia entre `awk '{print $1}'` y `awk -F':' '{print $1}'` sobre `/etc/passwd`?
3. Cuenta con `awk` cuántas líneas tiene `/etc/group` (sin usar `wc`).
4. Suma la columna 3 de un fichero `notas.txt` separado por espacios.
5. Imprime solo las líneas cuyo campo 2 sea exactamente `x` en `/etc/group` (separador `:`).
6. Escribe la versión `awk` de: `cut -d: -f1 /etc/group | sort | uniq -d`

<details><summary>Respuestas</summary>

1. `awk -F':' '{print $1, $7}' /etc/passwd`
2. Sin `-F` trocea por espacios (toma la primera "palabra" de la línea, que sería `root:x:0:...` entera si no hay espacios → $1 = línea completa en passwd); con `-F':'` trocea por `:` y `$1` es solo el nombre de usuario.
3. `awk 'END{print NR}' /etc/group`
4. `awk '{s+=$3} END{print s}' notas.txt`
5. `awk -F':' '$2 == "x" {print}' /etc/group`
6. `awk -F':' '{print $1}' /etc/group | sort | uniq -d`
</details>

---

# 13. Tuberías de examen: encadenar filtros

Patrón mental: **`origen → filtrar → transformar → ordenar → recortar`**.

```bash
# Los 5 mayores ficheros .png de un directorio (práctica 7, ej.3)
du -ah ~/Descargas | sort -hr | grep '\.png' | head -n 5

# Los 3 ficheros con más enlaces duros (práctica 7, ej.4)
ls -l dir | tail -n +2 | sort -k2,2 -nr | head -n 3

# Usuarios sin shell (campo 7) — doble filtro
grep '/bin/false$' /etc/passwd | cut -d: -f1

# Líneas duplicadas de un fichero
sort fichero | uniq

# Contar cuántas veces aparece cada línea
sort fichero | uniq -c | sort -nr

# Las 3 primeras líneas de /etc/passwd → la última de ellas
head -n 3 /etc/passwd | tail -n 1

# Extraer versiones de paquetes con apt-cache (de la práctica 5)
apt-cache policy | grep -E '^ +[0-9]+ ' | awk '{print $1}' | sort | uniq -c
```

### Anatomía de una tubería larga

```bash
du -ah "$dir" | sort -hr | grep "$ext" | head -n "$num"
 └──┬──┘        └──┬──┘     └───┬───┘    └───┬────┘
 espacio de      ordena      filtra por    se queda
 cada fichero  (legible,   la extensión   con los N
               descendente)               primeros
```

---

### ✏️ Ejercicios de la sección 13

1. Muestra los 10 usuarios con UID más alto de `/etc/passwd` numéricamente.
2. Lista los 5 ficheros más grandes del directorio actual (`du -ah .`).
3. Cuenta cuántas veces aparece cada palabra del primer campo de `palabras.txt`.
4. Muestra las líneas 5 a 10 de un fichero.
5. Encadena: de `/etc/group` saca los nombres de grupo (campo 1) que están **duplicados**.

<details><summary>Respuestas</summary>

1. `cut -d: -f3 /etc/passwd | sort -n | tail -n 10`
2. `du -ah . | sort -hr | head -n 10`
3. `awk '{print $1}' palabras.txt | sort | uniq -c | sort -nr`
4. `tail -n +5 fichero.txt | head -n 6`
5. `awk -F':' '{print $1}' /etc/group | sort | uniq -d`
</details>

---
