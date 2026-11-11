## Resumen Shell y programación en bash.

Aquí se añadirá el resumen de los libros para programación bash para complementar la información de los guiones.

Se añadirán los resumenes divididos por el contenido de sus guiones correspondientes.

---

### Resumen - Introducción

**Bash** está basado en el shell **sh** y puede verse como un **superconjunto** de suyo. Muchas órdenes se comportan igual que en **sh**.
¿Qué añade respecto a sh?

- Historial de órdenes, para recuperar las anteriores.
- Edición de la línea de comandos.
- Control de trabajos: conmutar entre procesos y controlar su avance.
- Sustitución de variables más flexible.
- Operadores adicionales, con sintaxis parecida a la de C.
- Alias para órdenes de uso frecuente, sin tener que escribir guiones.

| Característica              | sh  | csh | tcsh | ksh | bash |
| --------------------------- | --- | --- | ---- | --- | ---- |
| Histórico de órdenes        | No  | Sí  | Sí   | Sí  | Sí   |
| Alias                       | No  | Sí  | Sí   | Sí  | Sí   |
| Shell scripts               | Sí  | Sí  | Sí   | Sí  | Sí   |
| Autocompletado de archivos  | No  | Sí  | Sí   | Sí  | Sí   |
| Edición de línea de órdenes | No  | No  | No   | Sí  | Sí   |
| Control de trabajos         | No  | Sí  | Sí   | Sí  | Sí   |

Es importante saber que podemos interrumpir la ejecución de un script. Podemos hacerlo mediante:

- Teclando `exit`
- Pulsando `Ctrl + D`. Este método puede no funcionar si se ha asignado `IGNOREEOF`, la cual es una variable de entorno. Entonces `export IGNOREEOF=42` tendrá que pulsar `Ctrl + D` 42 veces antes de realmente salir a la shell.

---

### Sintaxis de entrada

- Es importante saber que Bash leer las instrucciones separando las palabras mediante espacios o tabuladores. Si queremos seguir escribiendo un comando en la siguiente linea podemos usar `\`

- Bash presenta un simbolo de solicitud cuando está esperando una nueva orden. La solicitud por omisión es: `\u@\h:\w\$`. Se puede personalizar asignando un valor a la variable de entorno `PS1`. (Ej: PS1="paco>"), sin dejar espacios alrededor del `=`.

- **Comillas y metacaracteres**: Simbolos como `;`,`&`, `|`, `<`, `>`, `(` , `)` actúan como separadores y tienen funciones especiales. Para que bash trate una frase como espacios (o separadores) como una sola palabra o texto ordinario, debe encerrarse entre comillas `"` o apóstrofos `'`

- **Comentarios**: Comienzan con `#`. Todo lo que escribamos detrás es ignorado por la shell.

- **Operadores para combinar comandos**:
  Aparte de los vistos en sesiones anteriores de órdenes de linux (`||`, `&&`, `;`...) tenemos otros operadores como:
  - `|&`: Pasa tanto la salída estándar como los errores del primer comando al segundo.
  - `&`: Ejecuta el comando en segundo plano, permitiendo seguir usando el términal de inmediato.
  - `(...)`: Agrupa comandos para tratarlos como una unidad y ejecutarlos en una subshell.

La prioridad de los comandos de mayor a menor precedencia son: `|` > `||` y `&&` > `;` > `&`. El `||` y `&&` se evaluan de izquierda a derechaa.

---

### Ejecución de ordenes

- **Bash** al igual que **sh**, tiene 3 métodos de ejecutar órdenes: ejecución directa, ejecución directa en un _subshell_, y ejecución indirecta en un _subshell_:
  - **Ejecución directa**: El comando se ejecuta en el propio shell actual. Cualquier cambio (como modificar una variable) afecta al entorno de forma permanente hasta que se cierra la sesión. Se usa para comandos internos (intrínsecos) y archivos cargados con `source`.

  - **Ejecución directa en una subshell**: Se crea un entorno hijo que hereda todas las variables del padre. Lo que pasa en el subshell se queda en el subshell (no afecta al shell principal). Se usa para comandos entre paréntesis `(...)` y procesos en segundo plano `&`.

  - **Ejecución indirecta en una subshell**: Crea un entorno hijo pero usando la llamada de sistema `exec`. Solo hereda las variables de entorno (ignora las locales). Tampoco afecta al shell padre. Es el método que se usa para comandos externos, como programas instalados y scripts ordinarios.

- **Busqueda de comandos externos**:
  - Si el comando no es interno, Bash lo busca en los directorios definidos en la variable de entorno `PATH` (rutas separadas por `:`).
  - Se puede incluir el directorio actual de trabajo en la búsqueda utilizando el símbolo del punto (`.`).

- **La tabla hash**:
  - Para no tener que buscar en el `PATH` cada vez, Bash memoriza las ubicaciones de los comandos ejecutados en una tabla de dispersión (hash), acelerando el sistema.

  - Precaución: Si creas o instalas un archivo ejecutable nuevo, Bash podría no encontrarlo inmediatamente porque su caché está desactualizada. Según el texto, esto se soluciona usando el comando `rehash` para reconstruir la tabla (Nota: en versiones estándar de Bash, el comando equivalente actual es `hash -r`).

---

### Redireccionamiento.

- **Decriptores de archivos** UNIX trata los flujos de entrada, salida y errores como si fueran archivos, asignandoles un número (descriptor):
  - **0 (stdin)**: Entrada estándar.
  - **1 (stdout)**: Salida estándar.
  - **2 (stderr)**: Salida de errores.

- Redirección de entrada:
  - `< fichero`: El comando lee los datos desde el archivo especificado en logar de pedirlos por teclado

  - `<< palabra` (Here-Document): El comando toma como entrada todo el texto que se escriba a continuación, hasta encontrar una línea que contenga exactamente la palabra delimitadora. Bash interpretará variables dentro de ese texto, a menos que la palabra contenga comillas o caracteres de escape.

- Redirección de Salida (Sobrescribir):
  - `> fichero`: Envía la salida estándar al archivo. Si el archivo ya existe, su contenido se borra (se trunca a cero); si no existe, se crea.

  - **Protección noclobber**: Si esta variable del shell está activada, Bash lanza un error para evitar que sobrescribas un archivo existente por accidente.

  - `>| fichero`: Fuerza la sobrescritura del archivo, ignorando la protección de noclobber.

- Redirección de Salida (Añadir):
  - `>> fichero`: Envía la salida al archivo, pero añadiendo el contenido al final del mismo, sin borrar lo que ya estaba escrito.

- Redirección por Descriptores Específicos:
  - Se puede elegir qué flujo redirigir colocando su número antes del operador (si no se pone nada, se asume el 1, salida estándar).

  - Uso habitual de errores: 2> fichero captura solo los mensajes de error y los guarda en un archivo.

  - Separar salidas: Una estructura como `(orden > fichero_salida) 2> fichero_errores` permite enviar los resultados correctos a un documento y los mensajes de fallo a otro distinto.

---
### COmpleción de Órdenes y Archivos

Bash permite completar automáticamente nombres de archivos y comandos al presionar cietas teclas:

* **Teclas `[Tab]` o `[Esc]`:**

*  **Coincidencia única**: Si existe un solo archivo que coincida con lo escrito,  Bash completa el nombre automáticamente

  * **Sin coincidencia única**: Completa hasta donde puede. SI hay múltiples opciones, al presionar de neuvo lista de los candidatos. SI el número de opciones es muy alot, Bash pregunta si deseas mostrarlas antes de listarlas

* **Carácter `EOf` (`Ctrl+D`):** Muestra de inmediato la lista de todas las coincidencias posibles y devuelve el control al indicador para termianr de escribir

* **Variable `FIGNORE`:** Contiene una lista de extensiones / sufijos separados por comas (ej: `.tmp`, `.o`) Los archivos con estos sufijos **se ignoran** en las sugerencais de autocompletado a menos que no exista ninguna otra opción posible

---

### Control de Trabajos (Jobs)

Un **trabajo** es un grupo de procesos asociados en el shell. Pueden estar en **primer plano** (máximo uno a la vez, el único que recibe entrada del teclado), en **segundo plano** (se ejecutan sin bloquear el terminal) o **detenidos** (pausados)

#### Estados e Identificación
* **Lanzar en segundo plano**: Se añade `&` al final del comando. Bash devuelve su identificador de trabajo y su PID

  * *Ejemplo* `[2] 470` -> Trabajo num 2, PID 470

* **Avisos de cambio de estado**: Bash notifica cuando un trabajo termina o cambia de estado justo nates de mostrar el siguiente indicador (*promt*). Si la variable `notify` está activa, los avisos se muestran al instante

#### Lista de trabajos (`jobs`)

Al ejecutar el comando `jobs`, los procesos se representan con la siguiente sintaxis:

* `+`: Indica el **trabajo actual** (el último en iniciarse o detenerse)

* `-`: Indica el **trabajo anterior**

* **Estados posibles**:
  * Running (en ejecución)
  * Done (terminado)
  * Stopped (detenido explicitamente o a la espera de entrada por termina `tty input`)
  * Opción `-l`: Muestra además los identificadores de proceso (PID)

#### Sintaxis para Referenciar Trabajos

| Formato | Trabajo al que hace referencia |
|---|---|
| `%n` | Al trabajo número n. |
| `%cadena` | Al trabajo cuyo nombre empieza por cadena. |
| `%?cadena` | Al trabajo cuyo nombre contiene cadena. |
| `%+`, `%%` o `%` | Al trabajo actual (el marcado con +). |
| `%-` | Al trabajo anterior (el marcado con -). |

#### Cambio de Estado y Comandos
* **Detener un trabajo (`Ctrl + Z`)**: Envía la señal `STOP` al trabajo en primer palno, pausándolo y moviendolo al segundo plano (Stopped)

* **Pasar a primer plano (`fg`)**:
  * Uso: `fg %trabajo` (o escribir simplemente `%trabajo`)

  * Concede al trabajo el control de termianl

* **Reanudar en segundo plano (`bg`)**
  * Uso `bg %trabajo`
  * Si el trabajo reanudado requiere entrada del teclado, volverá a quedar detenido

* **Finalizar un trabajo (`kill`):**
  * Uso normal: `kill %trabajo`
  * Forzado: `kill -9 %trabajo` (envía la señal `SIGKILL`, la cual no puede ser bloqueada ni ignorada, matando el proceso de forma incondicional)

---
### Expansión de Nombres de Fichero (Globalización)
Es el mecanismo mediante el cual Bash expande caracteres especiales (comodines) para convertirlos en rutas o nombres de archivo

* **Uso de virgulilla (`~`):**
  * `~` solo: Representa el directorio personal (home) del usuario actual

  * `~usuario`: Representa el directorio personal del usuario especificado (ej. `~maria`)

* **Expansión con llaves (`{ }`):**

  * La estructura `a{x1,x2,...,xn}b` se expande a una lista separada por espacios: `ax1b ax2b ... axnb`

  * *Ejemplo*: `cp ~noe/fauna/{gaviotas,cebras}` se expande a: `cp ~noe/fauna/gaviotas ~noe/fauna/cebras`

  * **Excepción literal**: Si `{`, `}` o `{}` están rodeados por espacios en blanco, Bash los interpreta literalmente como caracteres y no los expande

----
### Sustituciones Históricas
Una **sustitución histórica** permite reutilizar comandos (o partes de comandos) ejecutados previamente. **Bash interpreta estas sustituciones antes de procesar las comillas o ejecutar cualquier orden**

#### Estructura General
* Tiene la forma: `![suceso][:]selector[:modificador]`

* **Escape**: Para usar el carácter `!` de forma literal se antepone una diagonal invertida (`\!`). No hace falta escaparlo si va seguido de un espacio en blanco, `=` o `(`

* **Personalización**: Se puede cambiar el carácter `!` modificando la variable `histchars`

#### Sucesos (`suceso`)
Define a qué orden pasada de la lista de historial hacemos referencia:

| Sintaxis | Descripción |
|---|---|
| `!!` | La orden inmediatamente anterior (equivalente a `!-1`). |
| `!n` | La orden número n del historial. |
| `!-n` | La n-ésima orden anterior a la actual. |
| `!cadena` | La última orden que comience por cadena. |
| `!?cadena?` | La última orden que contenga la cadena. |

#### Selectores (`selector`)
Permiten extraer palabras específicas del suceso seleccionado. Si el selector no empieza por un dígito, se puede omitir el signo `:` inicial

| Selector | Palabra(s) seleccionada(s) |
|---|---|
| `0` | El nombre del comando (palabra 0). |
| `^` / `:^` | El primer argumento (palabra 1). |
| `$` / `:$` | El último argumento. |
| `:n` | El n-ésimo argumento (`$n \ge 1$`). |
| `:n1-n2` | Rango de palabras desde n1 hasta n2. |
| `*` / `:x*` | Desde la palabra 1 (o la palabra x) hasta el final (`$`). |
| `:x*` / `:X*` | Rango desde x hasta el final o el penúltimo argumento. |
| `:-x` | Rango desde el comando (0) hasta el argumento x. |
| `%` / `:%` | La palabra que coincidió con la última búsqueda `!?cadena?`. |

#### Modificadores (`modificador`)
Van precedidos por `:` y alteran las palabras extraídas por los selectores:

#### A. Manipulación de Rutas / Archivos
(Aplican sobre la primera palabra seleccionada):

* `:r` $\rightarrow$ Elimina la extensión del archivo (quita a partir del último .)

* `:h` $\rightarrow$ Elimina el nombre del archivo, dejando solo la ruta (head / directorio)

* `:t` $\rightarrow$ Elimina la ruta, dejando solo el nombre del archivo (tail / archivo)

* **Ejemplo:**
```bash
$ ls -l /usr/elsa/juguetes.texto

$ echo !!^:r  !!^:h  !!^:t  !!^:t:r

Resultado: /usr/elsa/juguetes  /usr/elsa/  juguetes.texto  juguetes
```

#### B. Sustitución y Reemplazo
`:[g]s/l/r` $\rightarrow$ Sustituye la cadena `l` por `r`. Si incluye `g`, se aplica globalmente a todas las palabras del suceso; si no, solo a la primera

`:[g]&` $\rightarrow$ Repite la última sustitución realizada

#### C. Control de Comillas y Ejecución
* `:q` $\rightarrow$ Entrecomilla las palabras seleccionadas para evitar sustituciones posteriores

* `:x` $\rightarrow$ Entrecomilla dividiendo además por espacios en blanco

* `:p` $\rightarrow$ Muestra el comando resultante en pantalla pero no lo ejecuta

#### Convencionalismos Especiales (Abreviaturas)

**Reemplazo rápido con `^`:**

Escribir `^error^correccion` al principio de la línea es una abreviatura de `!:s^error^correccion`. Sirve para corregir rápido una errata de la línea anterior:

```bash
$ cat /etc/lasswd
$ ^l^p
# Se ejecuta: cat /etc/passwd
```

* **Aislamiento con llaves `{}`:**

Permite pegar texto a una sustitución histórica sin que Bash se confunda

* `!{cp}s` expande el comando cp anterior y le concatena la letra `s` al final

----
### Alias
Un **alias** es una abreviatura o atajo de teclado asignado a una orden de uso frecuente. Se gestionan con las órdenes `alias` y `unalias`

#### Funcionamiento de la Sustitución
Cuando escribes una línea de comandos, Bash comprueba si la primera palabra es un alias:

* **Sin sustitución histórica**: Reemplaza el texto del alias directamente

* **Con sustitución histórica**: Procesa las variables/argumentos pasados al alias usando la sintaxis de historial (ej. `\!^`)

* **Prevención de bucles**: Si el alias reemplaza un comando por sí mismo (ej. `alias who='who;date'`), Bash realiza el cambio una sola vez y detiene el procesamiento para no caer en un ciclo infinito

* **Anular un alias en ejecución**: Si antepones una barra invertida `\` al comando (ej. `\ls`), Bash ignorará el alias y ejecutará el comando original del sistema

**Ejemplos**

**1. Alias simples:**

```bash
alias h=history
alias ll='ls -l'
alias ls='ls -CF'
```

**2. Importancia de las comillas:**
```bash
# CORRECTO (las comillas evitan que ';' corte la orden):
$ alias who='who;date'

# INCORRECTO (crea el alias 'who=who' y ejecuta inmediatamente 'date'):
$ alias who=who;date
```

**3. Uso de argumentos en alias:**
```bash
$ alias buscar='who | fgrep \!^'
```

Al ejecutar buscar `igor`, se expande como `who | fgrep igor`, filtrando los terminales conectados por el usuario especificado