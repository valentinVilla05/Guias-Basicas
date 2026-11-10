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
