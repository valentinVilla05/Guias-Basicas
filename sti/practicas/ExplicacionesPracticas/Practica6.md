## Práctica 6: Ingeniería Inversa, Análisis Binario y Depuración con OllyDbg


### 1. Fundamentos de la Ingeniería Inversa de Software

- **Definición**: Es la actividad centrada en descubrir cómo funciona un programa, binario, función o característica **cuando no se dispone del código fuente original**, permitiendo auditarlo, modificarlo o generar código propio que cumpla las mismas funciones.

- **Objetivo Real**: Obtener información, lógica o un diseño a partir de un producto público o accesible para rediseñarlo, replicarlo, mejorarlo o auditarlo en busca de fallos de seguridad. No se limita simplemente a "obtener un esquema".

- **Ámbitos de Aplicación**:
  - **NO es exclusiva de la informática**: Se aplica en mecánica, electrónica, arquitectura, industria química, automoción y sector aeroespacial.
  - **Productos sometidos a análisis**: Se aplica sobre software general, *firmware*, *hardware*, *malware*, protocolos y electrónica; no está restringida a productos de marcas específicas como Microsoft o Dell.

- **Relación con la Ciberseguridad (Práctica 1)**:
  - Existe una relación directa: la ingeniería inversa es la metodología principal para auditar ejecutables binarios y descubrir **vulnerabilidades, fallos de código y puertas traseras** en aplicaciones compiladas.

- **Beneficios del Análisis**:
  - **Reducción de fallos y aumento de calidad**: Permite detectar errores de diseño y problemas ocultos.
  - **Detección de efectos laterales**: Identifica errores secundarios o inconsistencias no deseadas.
  - **Recuperación de información**: Facilita rescatar especificaciones y cambios no documentados en sistemas antiguos.
  - **Optimización**: Ayuda a reestructurar el código para reducir el tamaño y la complejidad de los sistemas.
  - **Prototipado rápido**: Facilita la creación de nuevos productos al reutilizar conceptos y estructuras existentes.

---

### 2. Clasificación de Herramientas de Análisis

Es crucial distinguir las capacidades y los niveles de abstracción de cada tipo de herramienta:

- **Desensambladores**:
  - Traducen el código máquina binario (hexadecimal / opcodes) exclusivamente a **lenguaje ensamblador (assembly)**.
  - **NO** traducen a "lenguaje normal" ni a lenguajes de alto nivel legible.

- **Decompiladores**:
  - Herramientas que intentan reconstruir código fuente de alto nivel (como C/C++) a partir del binario compilado (ej. Ghidra, IDA Pro Hex-Rays).

- **Depuradores (*Debuggers*)**:
  - Permiten ejecutar el programa paso a paso (instrucción a instrucción), pausar la ejecución en puntos de interrupción (*breakpoints*) y analizar en tiempo real los registros de la CPU y la memoria RAM.

---

### 3. Depuración y Análisis Práctico con OllyDbg

- **Arquitectura y Plataforma**:
  - Es un depurador/desensamblador a nivel de ensamblador x86 de 32 bits **exclusivamente para Windows** (no existen versiones nativas para Linux; en Linux se emplean herramientas como GDB, Radare2 o Cutter).

- **Casos de Uso**:
  - Es de interés precisamente cuando **NO se dispone del código fuente**. Si se dispone del código fuente, se utilizan depuradores tradicionales integrados en los entornos de desarrollo (IDEs).
  - Se emplea extensamente en auditorías informáticas, análisis de *malware* y resolución de *crackmes* para detectar agujeros de seguridad o alterar el comportamiento de ejecutables.

- **Inspección de Registros y Memoria**:
  - Permite analizar en tiempo real los valores almacenados en los **registros del procesador** (`EAX`, `EBX`, `ECX`, `EDX`, `ESP`, `EBP`, `EIP`), los *flags* de estado (`ZF`, `CF`) y rangos de memoria RAM (panel *Hex Dump*).

- **Limitación Fundamental**:
  - Trabaja sobre el código binario compilado: desensambla y depura en tiempo de ejecución, pero **NO recupera ni integra el código fuente original** de la aplicación.

---

### 4. Técnicas Prácticas de Ingeniería Inversa en Windows

- **Comparación de Cadenas (`lstrcmp`) (Actividad 1)**:
  - `KERNEL32.lstrcmp` / `lstrcmpA` es una función de la API de Windows que compara dos cadenas de caracteres terminadas en nulo. Devuelve `0` en el registro `EAX` si las cadenas son idénticas.
  - En auditorías y *crackmes* (ej. `vault.exe`), se rastrean las llamadas a `lstrcmp` para identificar la comparación entre el usuario/contraseña introducido y las credenciales válidas almacenadas en memoria (ej. usuario "Robin Banks").

- **Búsqueda de Cadenas Referenciadas (*Referenced Strings*)**:
  - A través del menú contextual (*Search for -> All referenced text strings*), permite localizar textos clave hardcodeados en el binario (como mensajes de error, credenciales por defecto, textos de diálogos o avisos de licencia/*nag-screens*).

- **Modificación de Código en Tiempo de Ejecución y Parcheo (*Patching*)**:
  - **Mecanismo del Flag de Zero**: La instrucción `OR EAX, EAX` tras la llamada a `lstrcmp` evalúa si el resultado devuelto fue cero, ajustando el marcador *Zero Flag* (`ZF`).
  - **Modificación de Saltos Condicionales**: La instrucción de salto condicional `JNE` (*Jump if Not Equal* / `0x75`) salta a la rutina de "contraseña/licencia incorrecta" si las cadenas no coinciden (`ZF = 0`).
  - **Uso de `NOP` (*No Operation*)**: Reemplazar la instrucción `JNE` por instrucciones `NOP` (código máquina `0x90` en hexadecimal) inactiva el salto condicional, haciendo que la CPU ignore la comprobación de seguridad y ejecute directamente el bloque de código de acceso concedido (*bypass* de autenticación).

---

### 5. Guía de Resolución del Cuestionario y Prácticas (`vault.exe`, `crackme.exe` y WinRAR)

- **Caso 1: Autenticación en `vault.exe` (Actividad 1)**:
  - *Identificación de credenciales*: Al buscar *referenced strings*, se hallan los valores hardcodeados en claro para el nombre de usuario ("Robin Banks") y contraseña.
  - *Bypass*: Si se inhabilitan los saltos condicionales `JNE` sustituyéndolos por `NOP` (`0x90`), el programa acepta cualquier usuario y clave arbitrarios introducidos en la interfaz.

- **Caso 2: Inhabilitación de Ventana Inicial (*Nag-Screen*) en `crackme.exe` (Cuestionario)**:
  - *Eliminación de la Nag-Screen*: Al iniciar el depurador, se busca la llamada a la función de la API de Windows que crea la ventana inicial (ej. `DialogBoxParamA` o `MessageBoxA`). Se modifica la instrucción de salto inicial (`JMP` / `CALL`) o se sustituye el salto que dibuja la ventana emergente por instrucciones `NOP` para que el flujo de ejecución pase directamente a la ventana principal.

- **Caso 3: Habilitación de Menú Inhabilitado y Edición de Texto (Cuestionario)**:
  - *Menú Secret*: En el código de inicialización del menú (`WM_INITMENU` o llamadas a `EnableMenuItem`), la opción *Secret* aparece con el flag deshabilitado (`MF_DISABLED` / `MF_GRAYED` = `0x01`). Para hacerla seleccionable se modifica el valor del parámetro a `MF_ENABLED` (`0x00`) o se parchean/eliminan con `NOP` las instrucciones que desactivan la entrada del menú.
  - *Modificación del mensaje por DNI*: Se busca la cadena de texto original del cuadro de diálogo del menú *Secret* en el panel *Hex Dump* o cadenas de texto referenciadas, y se reemplaza en hexadecimal el texto por el número de DNI del alumno. A continuación se guardan las modificaciones en un ejecutable Parcheado (*Copy to executable -> Save file*).

- **Caso 4: Ejercicio Voluntario (Análisis y Eliminación de Nag-Screen en WinRAR)**:
  - *Ingeniería Inversa sobre WinRAR*: La versión de prueba de WinRAR lanza un aviso emergente (*nag-screen*) tras vencer el periodo de evaluación de 40 días, invocando internamente rutinas de ventana y comprobación del registro de licencia.
  - *Metodología de eliminación*: Mediante OllyDbg/x64dbg, se establece un *breakpoint* en las funciones de creación de ventanas de diálogo (`CreateWindowExW` o `DialogBoxParamW`) o sobre la búsqueda de cadenas de texto asociadas al aviso de compra. Localizado el salto condicional que evalúa si la copia está registrada (`JE` / `JNE`), se parchea dicho salto sustituyéndolo por un salto incondicional (`JMP`) o rellenando el bloque del aviso con instrucciones `NOP`, eliminando la ventana emergente al arrancar la aplicación.