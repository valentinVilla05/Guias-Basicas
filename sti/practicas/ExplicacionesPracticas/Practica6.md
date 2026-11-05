## Práctica 6: Ingeniería Inversa, Análisis Binario y Depuración con OllyDbg

### 1. Fundamentos de la Ingeniería Inversa de Software

- **Definición**: Es la actividad centrada en descubrir cómo funciona un programa, binario, función o característica **cuando no se dispone del código fuente original**, permitiendo auditarlo, modificarlo o generar código propio que cumpla las mismas funciones.

- **Objetivo Real**: Obtener información, lógica o un diseño a partir de un producto público o accesible para rediseñarlo, replicarlo, mejorarlo o auditarlo en busca de fallos de seguridad. No se limita simplemente a "obtener un esquema".

- **Ámbitos de Aplicación**:
  - **NO es exclusiva de la informática**: Se aplica en mecánica, electrónica, arquitectura, industria química, automoción y sector aeroespacial.
  - **Productos sometidos a análisis**: Se aplica sobre software general, *firmware*, *hardware*, *malware*, protocolos y electrónica; no está restringida a productos de marcas específicas como Microsoft o Dell.

- **Relación con la Ciberseguridad (Práctica 1)**:
  - Existe una relación directa: la ingeniería inversa es la metodología principal para auditar ejecutables binarios y descubrir **vulnerabilidades, fallos de código y puertas traseras**.

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
  - Traducen el código máquina binario exclusivamente a **lenguaje ensamblador (assembly)**.
  - **NO** traducen a "lenguaje normal" ni a lenguajes de alto nivel legible.

- **Decompiladores**:
  - Herramientas que intentan reconstruir código fuente de alto nivel (como C/C++) a partir del binario compilado.

- **Depuradores (*Debuggers*)**:
  - Permiten ejecutar el programa paso a paso, pausar la ejecución en puntos de interrupción (*breakpoints*) y analizar en tiempo real los registros de la CPU y la memoria RAM.

---

### 3. Depuración y Análisis Práctico con OllyDbg

- **Arquitectura y Plataforma**:
  - Es un depurador/desensamblador a nivel de ensamblador x86 **exclusivamente para Windows** (no existen versiones nativas para Linux; en Linux se emplean herramientas como GDB o Radare2).

- **Casos de Uso**:
  - Es de interés precisamente cuando **NO se dispone del código fuente**. Si se dispone del código fuente, se utilizan depuradores tradicionales integrados en los entornos de desarrollo.
  - Se emplea extensamente en auditorías informáticas y análisis de *malware* para detectar agujeros de seguridad.

- **Inspección de Registros y Memoria**:
  - Permite analizar en tiempo real los valores almacenados en los **registros del procesador** (`EAX`, `EBX`, `ESP`, etc.) y rangos de memoria.

- **Limitación Fundamental**:
  - Trabaja sobre el código binario compilado: desensambla y depura, pero **NO recupera ni integra todo el código fuente original** de la aplicación.

---

### 4. Técnicas Prácticas de Ingeniería Inversa en Windows

- **Comparación de Cadenas (`lstrcmp`)**:
  - `KERNEL32.lstrcmp` es una función de la API de Windows que compara dos cadenas de caracteres.
  - En auditorías y *crackmes*, se rastrean las llamadas a `lstrcmp` para identificar la comparación entre la clave/usuario introducido y los valores correctos esperados en memoria.

- **Búsqueda de Cadenas Referenciadas (*Referenced Strings*)**:
  - Permite localizar textos clave en el binario (como mensajes de error, nombres de usuario por defecto o avisos de licencia/*nag-screens*).

- **Modificación de Código en Tiempo de Ejecución (*Patching*)**:
  - **Modificación de Saltos Condicionales**: Las comprobaciones de seguridad suelen ir seguidas de instrucciones de salto condicional (ej. `JNE` - *Jump if Not Equal*).
  - **Uso de `NOP` (*No Operation*)**: Reemplazar las instrucciones de salto condicional por instrucciones `NOP` (código de máquina `0x90`) inhabilita la comprobación, permitiendo bypasses de autenticación o la eliminación de restricciones (como activar menús inhabilitados o quitar *nag-screens*).