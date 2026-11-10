## Práctica 5: Cifrado por Bloques (AES), Funciones Hash e Ingeniería Inversa


### 1. El Algoritmo AES: Modos de Operación y Estructura

- **Modos de Operación (Modo ECB - Electronic Codebook)**:
  - **Funcionamiento**: Es el modo de cifrado simétrico más simple. Divide el texto claro en bloques independientes de 128 bits (16 bytes) y cifra cada bloque exactamente con la misma clave.
  - **Inconveniente y Vulnerabilidad de ECB**: Bloques idénticos de texto claro producen bloques idénticos de texto cifrado. Esto hace que no oculte patrones ni estructuras en los datos (por ejemplo, en imágenes o textos repetitivos, la estructura sigue siendo perfectamente visible tras el cifrado).
  - **Diferencia de salida respecto a Prácticas Anteriores**: A diferencia de los algoritmos clásicos de la Práctica 3 (como Vigenère en $Z_{27}$ o ASCII 191), el cifrado AES en modo ECB devuelve una salida binaria no imprimible (o representada en hexadecimal/Base64) de longitud fija múltiplo de 16 bytes, ocultando las frecuencias de caracteres del idioma pero preservando la repetición de bloques completos.

- **Comportamiento de la Clave (Cuestionario 2)**:
  - Si la clave introducida por el usuario no alcanza la longitud exacta requerida (128 bits = 16 bytes, 192 bits = 24 bytes o 256 bits = 32 bytes), los sistemas de cifrado y herramientas como AESphere aplican un mecanismo automático de **relleno (*padding*)** con bytes nulos (`0x00`) o procesan la clave mediante una función de derivación/hash para expandir o truncar la cadena hasta completar los 16/24/32 bytes exactos.

- **Operaciones Internas de la Ronda (Cuestionario 1)**:
  - **SubBytes**: Sustituye cada byte de la matriz de estado por otro utilizando la caja de sustitución **S-Box** de Rijndael (basada en el inverso multiplicativo en el cuerpo de Galois $GF(2^8)$ seguido de una transformación afín). Es la única operación **no lineal** del algoritmo y aporta la propiedad de **confusión**.
    - *Resolución manual del Cuestionario 1a*:
      - Para el byte `c1`: Fila `C`, Columna `1` en la S-Box $\rightarrow$ **`78`**
      - Para el byte `5a`: Fila `5`, Columna `A` en la S-Box $\rightarrow$ **`be`**
      - Para el byte `5b`: Fila `5`, Columna `B` en la S-Box $\rightarrow$ **`39`**
      - Para el byte `9b`: Fila `9`, Columna `B` en la S-Box $\rightarrow$ **`14`**
      - *Resultado manual*: La transformación SubBytes de `c1 5a 5b 9b` devuelve `78 be 39 14`.
      - *Entradas a 00*: Todos los bytes `00` se transforman en `63` (valor fijo de la S-Box para el origen).
      - *Entradas a FF*: Todos los bytes `FF` se transforman en `16`.
  - **ShiftRows (Cuestionario 1b)**: Desplaza de forma circular y cíclica a la izquierda los bytes de cada fila de la matriz de estado de $4 \times 4$:
    - Fila 0: No se desplaza (0 posiciones).
    - Fila 1: Se desplaza 1 posición a la izquierda.
    - Fila 2: Se desplaza 2 posiciones a la izquierda.
    - Fila 3: Se desplaza 3 posiciones a la izquierda.
    - *Función*: Aporta difusión a nivel de fila reordenando la posición espacial de los bytes.
  - **AddRoundKey (Cuestionario 1c)**: Combina la matriz de estado con la subclave de la ronda mediante una operación **XOR ($\oplus$) byte a byte**.
    - *Matemática del operador*: La propiedad de XOR es su propia inversa ($\text{Entrada} \oplus \text{Clave} = \text{Salida} \iff \text{Clave} = \text{Entrada} \oplus \text{Salida}$).
    - *Resolución Cuestionario 1c*: Si la matriz de Entrada son todos bytes `0F` y se busca una Salida con valores `F0` y diagonal a `00`:
      - Para las casillas fuera de la diagonal (Salida `F0`): $\text{Clave} = \text{0F} \oplus \text{F0} =$ **`FF`**.
      - Para las casillas de la diagonal (Salida `00`): $\text{Clave} = \text{0F} \oplus \text{00} =$ **`0F`**.
      - *Matriz Clave resultante*: Una matriz con el valor `0F` en su diagonal principal y `FF` en el resto de posiciones.
  - **MixColumns**: Multiplica cada columna de la matriz de estado por una matriz fija de polinomios en $GF(2^8)$. Es la operación de mayor complejidad matemática y proporciona la **difusión** entre los cuatro bytes de una misma columna.

---

### 2. Funciones Hash: Obsolescencia, Colisiones y Algoritmos Actuales

- **Naturaleza de las Funciones Hash**:
  - Son funciones resumen unidireccionales deterministas.
  - **NO son algoritmos de cifrado**: No utilizan claves públicas, privadas ni simétricas; por tanto, **NO son algoritmos simétricos ni asimétricos**.
  - **Propiedades indispensables**: Resistencia a la primera preimagen (dado $h$, es imposible hallar $m$), resistencia a la segunda preimagen (dado $m_1$, es imposible hallar $m_2$ tal que $h(m_1)=h(m_2)$) y resistencia a colisiones (imposible hallar dos mensajes cualesquiera con el mismo hash).

- **Demostración Práctica de Obsolescencia (Actividad 3)**:
  - **MD5**: Publicado en 1991, genera resúmenes de 128 bits. Inseguro por colisiones prácticas descubiertas en 2004. En el laboratorio, los ficheros `hello` y `erase` tienen tamaños y contenidos en código ejecutable completamente distintos, pero ambos producen exactamente el mismo hash MD5 (`md5sum`).
  - **SHA-1**: Publicado en 1995, genera resúmenes de 160 bits. Inseguro por el ataque **SHAttered (2017)** de CWI/Google. Los ficheros `shattered-1.pdf` y `shattered-2.pdf` son dos documentos PDF con contenidos visuales e internos totalmente distintos que devuelven el mismo hash SHA-1 (`sha1sum`).
  - **Solución actual**: Ambos archivos devuelven hashes radicalmente distintos al aplicar funciones modernas como SHA-256 (`sha256sum`).

- **Funciones Hash Actuales y sus Construcciones (Actividad 4 / Cuestionario 3a)**:
  - **SHA-2 (ej. SHA-256)**: 
    - Basado en la **construcción Merkle-Damgård**.
    - *Procesamiento y Relleno (Padding)*: El mensaje original se rellena añadiendo un bit `1`, seguido de bits `0` y un campo final de 64 bits que indica la longitud exacta del mensaje original. El mensaje resultante se divide en bloques fijos de **512 bits (64 bytes)**.
    - *Rondas y Registros*: Cada bloque de 512 bits se expande en 64 palabras de 32 bits ($W_0$ a $W_{63}$) y procesa los datos iterando sobre 8 registros internos de 32 bits ($a, b, c, d, e, f, g, h$) mediante 64 rondas de operaciones lógicas. Devuelve un resumen final de **256 bits (32 bytes / 64 caracteres hexadecimales)**.
  - **SHA-3 (ej. SHA-3-256)**:
    - Basado en la **construcción de esponja** (fases de *Absorción* de bloques de datos y *Exprime* del resumen).
    - Trabaja con un estado interno masivo de **$5 \times 5$ palabras de 64 bits (1600 bits de estado)** divididos en *Rate* ($r$) y *Capacity* ($c$). Aplica 24 rondas con cinco transformaciones geométricas y lógicas por ronda: $\theta$ (theta - paridad), $\rho$ (rho - rotación), $\pi$ (pi - permutación), $\chi$ (chi - combinación no lineal) e $\iota$ (iota - constante de ronda).

- **Propiedades Clave**:
  - **Efecto Avalancha (Cuestionario 3b)**: 
    - Propiedad por la cual la modificación de un único bit o un solo carácter en el texto de entrada cambia aproximadamente el **50% de los bits** del resumen resultante (tanto en SHA-256 como en SHA-3-256).
    - *Importancia*: Es deseable para garantizar que la salida sea estadísticamente independiente e impredecible respecto a la entrada, impidiendo que un atacante deduzca patrones o realice ingeniería inversa sobre el texto original.
  - **Sensibilidad a la Codificación (Cuestionario 3c)**: 
    - Las funciones hash operan estrictamente sobre la secuencia de bytes en bruto (*raw bytes*) del mensaje.
    - El carácter "ó" (presente en la frase del cuestionario) se representa en **UTF-8** mediante 2 bytes (`0xC3 0xB3`), mientras que en la codificación **Latin-1 (ISO-8859-1)** se representa con 1 solo byte (`0xF3`).
    - *Conclusión*: Al cambiar la codificación de UTF-8 a Latin-1 la secuencia de bytes de entrada cambia por completo, por lo que **NO se obtiene el mismo resumen hash** (el efecto avalancha hace que la salida sea totalmente distinta).

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