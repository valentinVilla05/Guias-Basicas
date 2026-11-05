## Práctica 5: Cifrado por Bloques (AES), Funciones Hash e Ingeniería Inversa


### 1. El Algoritmo AES: Modos de Operación y Estructura

- **Modos de Operación (Modo ECB)**:
  - **ECB (Electronic Codebook)**: Es el modo de cifrado más simple. Divide el texto en bloques independientes de 128 bits y cifra cada uno con la misma clave.
  - **Inconveniente de ECB**: Bloques idénticos de texto claro producen bloques idénticos de texto cifrado, lo que no oculta patrones en los datos.

- **Comportamiento de la Clave**:
  - Si la clave introducida no alcanza la longitud requerida (128, 192 o 256 bits), los sistemas de cifrado o bibliotecas aplican un relleno (*padding*) o un proceso de derivación para ajustar su tamaño.

- **Operaciones Internas de la Ronda**:
  - **SubBytes**: Sustituye cada byte de la matriz de estado por otro utilizando la caja de sustitución **S-Box** de Rijndael (basada en el cuerpo de Galois $GF(2^8)$). Es la única operación **no lineal** del algoritmo y aporta la propiedad de **confusión**.
  - **ShiftRows**: Desplaza de forma circular y cíclica los bytes de las filas de la matriz de estado. Aporta difusión a nivel de fila.
  - **AddRoundKey**: Combina la matriz de estado con la subclave de la ronda mediante una operación **XOR ($\oplus$) byte a byte**.
    - *Matemática del operador*: Al realizar XOR con `FF`, se obtiene el complemento a 1 (inversión bit a bit). Para obtener una salida determinada a partir de la entrada, la clave se calcula mediante la operación XOR entre la entrada y la salida deseada ($\text{Clave} = \text{Entrada} \oplus \text{Salida}$).
  - **MixColumns**: Multiplica cada columna por una matriz fija en $GF(2^8)$. Es la operación de mayor complejidad y proporciona la **difusión** entre los bytes de una misma columna.

---

### 2. Funciones Hash: Obsolescencia, Colisiones y Algoritmos Actuales

- **Naturaleza de las Funciones Hash**:
  - Son funciones resumen unidireccionales deterministas.
  - **NO son algoritmos de cifrado**: No utilizan claves públicas, privadas ni simétricas; por tanto, **NO son algoritmos simétricos ni asimétricos**.
  - **MD5 y SHA-1**: Se consideran obsoletos e inseguros debido a la demostración práctica de **colisiones** (dos entradas distintas que producen el mismo resumen).

- **Funciones Hash Actuales**:
  - **SHA-2 (ej. SHA-256)**: Basado en la construcción Merkle-Damgård. Genera resúmenes de 256 bits procesando bloques de datos mediante rondas de expansión.
  - **SHA-3 (ej. SHA-3-256)**: Basado en la **construcción de esponja** (fases de absorción y exprime), utilizando estados internos de $5 \times 5$ palabras.

- **Propiedades Clave**:
  - **Efecto Avalancha**: Propiedad deseable en la que la modificación de un único bit en el mensaje de entrada cambia aproximadamente el **50% de los bits** del resumen resultante.
  - **Sensibilidad a la Codificación**: El resumen hash opera sobre bytes en bruto. Si un texto con caracteres especiales (ej. "ó") se codifica en **UTF-8** frente a **Latin-1**, los bytes de entrada varían y el resumen resultante será completamente diferente.

---

### 3. Fundamentos de la Ingeniería Inversa de Software

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

### 4. Herramientas y Análisis Binario: OllyDbg

- **Tipos de Herramientas**:
  - **Desensambladores**: Traducen el código máquina binario a **lenguaje ensamblador (assembly)**. **NO** traducen a "lenguaje normal" ni a lenguajes de alto nivel.
  - **Decompiladores**: Intentan reconstruir código fuente de alto nivel (como C/C++) a partir del binario.
  - **Depuradores (*Debuggers*)**: Permiten ejecutar el programa paso a paso analizando la memoria y los registros.

- **OllyDbg**:
  - Es un depurador/desensamblador de código ensamblador x86 **exclusivamente para Windows** (no existen versiones nativas para Linux).
  - **Caso de uso principal**: Es de utilidad cuando **NO se dispone del código fuente**. Si el código fuente está disponible, se utilizan depuradores integrados tradicionales.
  - **Inspección**: Permite analizar en tiempo real los **registros de la CPU** y el estado de la **memoria RAM**.
  - **Limitación**: Trabaja directamente sobre el binario compilado; **NO recupera ni integra el código fuente original** de la aplicación.

- **Llamadas a la API en Auditoría (`lstrcmp`)**:
  - La función `lstrcmp()` / `lstrcmpA()` es una rutina de la API de Windows utilizada para **comparar cadenas de caracteres**. En análisis de binarios se rastrea para localizar puntos de validación de contraseñas, licencias o claves de acceso.