# Práctica  7 Programación en Shell. Primeros pasos.

Un **Shell Script** es un archivo de texto ejecutable que contiene una secuecnia de órdenes que el intérprete (shell) procesa e interpreta ordenadamente

* **Utilidad**: Automatiza tareas administrativas repetitivas, evita errores humanos y simplifica comandos complejos

* **Naturaleza**: No requirer compilación, solo necesita permisos de ejecución

## Anatomía de un Shell Script
Un script estructurado consta de tres partes fundamentales:   

```bash
#!/bin/bash
# Autor: Nombre del Autor
# Descripción: Breve explicación de lo que hace el script

echo "Ejecutando script..."
```

**1. Shebang (`#!`)**: Debe ubicarse en la primera línea y ser los dos primeros bites del archivo. Indica la ruta absoluta del intérprete a usar: Ejemplo (`#!/bin/bash`)

> Para averiguar la ruta de Bash: **which bash**

**2. Comentarios (`#`)**: Todo texto tras el carácter # es ignorado por la Shell. Se usan para documentar el autor, fecha, versión y propósito del código.  

**3. Órdenes:** Comandos directos del sistema que se ejecutan secuencialmente

## Creación, Permisos y Ubicación

* **Convención de nombre:** Extensión `.sh` (opcional, pero recomendada)

* **Comprobar conflictos de nombre:** Usar type `-a <nombre>` para evitar sobrescribir comandos del sistema o del intérprete

* **Otorgar permiso de ejecución:**

```bash
chmod +x mi_script.sh
```
* **Ejecución básica (Ruta relativa/absoluta):**

```bash
./mi_script.sh
*(Es necesario indicar `./` porque el directorio actual no suele estar en la variable `$PATH`)
```

* **Ubicación recomendada (`~/bin`):**

Crear la carpeta `~/bin` y guardar allí los scripts para ejecutarlos directamente por su nombre desde cualquier directorio:   

```bash
mkdir -p ~/bin
mv mi_script.sh ~/bin/
```

## Entrada y Salida de Datos
### Comando `echo` (Salida)

* `-n`: Imprime texto sin salto de línea final

* `-e`: Permite la interpretación de caracteres de escape como `\n` (nueva línea) o `\t` (tabulador)

* **Sustitución de comandos: `$()` ejecuta un comando y devuelve su salida.**

```bash
echo "Hoy es $(date)"
```

* **Comando `read` (Entrada)**

Lee el valor introducido por el usuario desde la entrada estándar y lo guarda en una variable

```bash
echo -e "\nEscribe la ruta:"
read la_ruta
ls "$la_ruta"
```

## Tipos de Parámetros

En Bash, los parámetros almacenan valores y se dividen en tres categorías principales:

### A. Variables (Definidas por el usuario)

* **Reglas:** Los nombres solo contienen letras, números y `_` (deben empezar por letra o `_`)
* **Regla de estilo:** **NUNCA usar Mayúsculas** para variables de usuario, ya que están reservadas para las variables de entorno del sistema (`$PATH`, `$HOME`, `$USER`
* **Asignación sin espacios:** `variable=valor` (Si hay espacios en la asignación, falla o se interpreta como comando)
* **Acceso:** `$variable` o `${variable}` (preferible para delimitar)
* **Eliminación:** `unset variable`
* **Tipado:** Todos los valores se almacenan e interpretan como **cadenas de texto** (Ejemplo: `var=1+2` guarda la cadena `"1+2"`, no realiza la suma)

### B. Parámetros Posicionales
Representan los argumentos pasados al script en la línea de comandos:
* `$1`, `$2`, `$3`: Argumento 1, 2, 3, etc
* `${10}`: Obligatorio usar llaves para posiciones mayores a 9

### C. Parámetros Especiales
* `$0`: Nombre o ruta con la que se invocó el script
* `$#`: Número total de parámetros posicionales pasados
* `$*`: Todos los argumentos. Si se usa entre comillas dobles (`"$*"`), se concatenan en **una sola cadena**
* `$@`: Todos los argumentos. Si se usa entre comillas dobles (`"$@"`), se tratan como **elementos o palabras individuales**
* `$$`: PID (ID de proceso) de la shell que ejecuta el script

## Uso de Comillas y Escapes
| Tipo | Sintaxis | Comportamiento |
| :--- | :--- | :--- |
| **Comillas Dobles** | `"texto"` | Permite la expansión de variables (`$var`), ejecución de comandos (`$()`) y escapes|
| **Comillas Simples** | `'texto'` | Inhabilita la expansión. Todo se interpreta de forma **literal** |
| **Barra Invertida** | `\$` | Invalida el significado especial del carácter que le sigue (carácter de escape) |

## Depuración de Scripts
Para solucionar errores sintácticos y lógicos se utilizan las siguientes opciones de ejecución

* `bash -x mi_script.sh`: Muestra cada orden que se ejecuta tras realizar la expansión de variables
* `bash -v mi_script.sh`: Muestra las líneas del guion en pantalla a medida que se van leyendo (modo *verbose*)
* `bash -n mi_script.sh`: Comprueba únicamente la sintaxis del script sin ejecutarlo
* **Herramientas recomendadas:** Uso del analizador estático `shellcheck` (`sudo apt install shellcheck`)


