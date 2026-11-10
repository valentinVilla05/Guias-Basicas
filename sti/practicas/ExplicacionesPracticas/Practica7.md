## Práctica 7: Aleatoriedad, Entropía, Hashes de Contraseñas

### 1. Aleatoriedad y Generadores de Números (PRNG vs. CSPRNG)

- **Naturaleza de la Aleatoriedad**:
  - En computación no existe la aleatoriedad física pura de forma nativa, ya que los programas son deterministas.
  - La aleatoriedad se evalúa como una **propiedad estadística sobre una secuencia o serie de números**, nunca sobre un número aislado.
  - La distribución ideal esperada de un generador de números aleatorios es **uniforme** (todos los valores del rango tienen la misma probabilidad de ser elegidos). No debe seguir una distribución normal a menos que se aplique una transformación matemática posterior.

- **Generadores Pseudoaleatorios Estándar (PRNG)**:
  - **Funcionamiento**: Algoritmos deterministas que generan una secuencia de números $x_n$ a partir de un valor inicial denominado **semilla** ($x_0$) mediante relaciones de recurrencia (como el Generador Congruencial Lineal: $x_{n+1} = (a x_n + c) \pmod m$).
  - **Determinismo y Reproducibilidad**: Conocer la semilla permite reproducir exactamente toda la secuencia numérica. Esta propiedad es deseable para depurar simulaciones, juegos o pruebas académicas.
  - **Aplicaciones**: Válidos para videojuegos, simulaciones de Montecarlo, gráficos o teoría de decisiones donde prima la velocidad computacional.
  - **Inseguridad Criptográfica**: **NO deben usarse en ciberseguridad ni criptografía**. Si un atacante descubre la semilla o parte de la secuencia de salida, puede predecir con total exactitud todos los números futuros.
  - **Ciclo de un PRNG**: Al ser un algoritmo determinista con un espacio de memoria finito, tarde o temprano vuelve a un estado por el que ya pasó. En ese momento la secuencia se **repite periódicamente (entra en ciclo)**. Es deseable que los parámetros ($a, c, m$) no sean degenerados para que el ciclo sea lo más largo posible.
  - **Gestión de la Semilla**: La semilla se fija una sola vez al inicializar el generador (con funciones como `srand(semilla)`). No debe modificarse en cada llamada individual en tiempo de ejecución, pues destruye la distribución estadística de la secuencia.

- **Generadores Criptográficamente Seguros (CSPRNG)**:
  - Diseñados con propiedades estrictas de impredecibilidad para que sea computacionalmente inviable predecir el siguiente bit o deducir el estado interno a partir de las salidas observadas.
  - En sistemas Linux se alimentan del *pool* de entropía del sistema operativo (ruido térmico del hardware, temporización de interrupciones del teclado, disco o red) y se acceden mediante `/dev/urandom`, la llamada al sistema `getrandom()` o mediante herramientas como `openssl rand`.

---

### 2. Almacenamiento Seguro de Contraseñas, Sales y Entropía

- **Almacenamiento mediante Resumen (Hash)**:
  - Las contraseñas nunca se guardan en texto plano. En su lugar se almacena el resumen generado por una **función hash unidireccional**.
  - Las funciones hash convierten entradas de longitud variable en resúmenes de **longitud fija**.

- **El Concepto de Sal (*Salt*)**:
  - Cadena aleatoria única generada para cada usuario (usando un CSPRNG como `openssl rand -hex 16`) que se concatena a la contraseña antes de calcular el hash (`hash(sal + contraseña)`).
  - **Propósito**: Evita que dos usuarios con la misma contraseña compartan el mismo hash y **neutraliza completamente los ataques con tablas arcoíris** (tablas precalculadas). Obliga al atacante a recalcular la secuencia de hashes individualmente para cada sal/usuario. La sal no es secreta y se almacena en claro junto al hash.
  - **Vulnerabilidad de Sales Predecibles**: Si la sal se genera mediante un PRNG débil (ej. `srand(time(NULL))` tomando la hora del sistema), un atacante que conozca la ventana temporal de creación de la cuenta puede reproducir la semilla, calcular las sales probables y anular la protección de la sal.

- **Entropía de Contraseñas y Método Diceware**:
  - **Fórmula**: La entropía en bits se calcula como $H = L \cdot \log_2(N)$, donde $L$ es la longitud (o número de elementos) y $N$ es el tamaño de la población o diccionario de caracteres.
  - **Significado**: Mide la incertidumbre o complejidad del espacio de búsqueda. El número total de combinaciones posibles a probar en el peor de los casos mediante fuerza bruta es $2^H$.
  - **Método Diceware**: Técnica para generar contraseñas seguras y fáciles de recordar compuestas por palabras aleatorias elegidas mediante tiradas de dados sobre una lista prefijada. La lista estándar tiene $N = 7776$ palabras ($6^5$ combinaciones por palabra). Cada palabra aporta aproximadamente $\log_2(7776) \approx 12.92$ bits de entropía.

- **Algoritmos Rápidos vs. Algoritmos Lentos (KDF)**:
  - **Inadecuación de MD5 y SHA-256**: Aunque SHA-256 es seguro frente a colisiones, es un algoritmo diseñado para ser extremadamente rápido en hardware (capaz de realizar miles de millones de operaciones por segundo en GPUs o ASICs), lo que facilita enormemente los ataques de diccionario masivos.
  - **Funciones de Derivación de Contraseñas (KDF Lentas)**: Diseñadas intencionadamente para consumir tiempo de procesador y memoria RAM con el fin de ralentizar los ataques por fuerza bruta.
    - **bcrypt**: Permite configurar un factor de coste/rondas (OWASP recomienda un mínimo de 10 a 12 rondas, `mkpasswd -m bcrypt --rounds=12`).
    - **Argon2id**: Estándar moderno que parametriza iteraciones de tiempo ($t$), memoria RAM ($m$) y hilos de paralelismo ($p$).
    - **yescrypt**: Algoritmo lento utilizado por defecto en las distribuciones Linux modernas para cifrar las claves en `/etc/shadow`.

---

### 3. Respuestas y Razonamientos de los Cuestionarios

#### Cuestionario de Contraseñas

1. **Cálculo de Entropía en Diceware**:
   - Cada palabra de la lista Diceware ($7776$ palabras) aporta $\log_2(7776) \approx 12.92$ bits de entropía.
   - Para superar el umbral de **70 bits de entropía**, se divide el objetivo entre la entropía por palabra ($70 / 12.92 = 5.41$).
   - **Resultado**: Se necesitan como mínimo **6 palabras aleatorias** para alcanzar $77.55$ bits de entropía.

2. **Criterios Actuales del NIST (SP 800-63B)**:
   - **Longitud mínima**: Recomienda un mínimo de **8 caracteres** (permitiendo contraseñas largas de hasta 64 caracteres).
   - **Reglas de composición**: **NO** recomienda exigir reglas de complejidad obligatorias (como combinar mayúsculas, símbolos y números de forma arbitraria), ya que inducen a patrones predecibles por parte del usuario.
   - **Rotación periódica**: **NO** recomienda forzar cambios periódicos de clave salvo en caso de compromiso confirmado, ya que los usuarios suelen hacer variaciones mínimas y débiles de su clave anterior.

3. **Incompatibilidad entre Hash de Integridad y Hash de Contraseñas (KDF)**:
   - **Hash de Integridad (ej. SHA-256)**: Requiere máxima **velocidad y bajo consumo computacional** para poder procesar y verificar archivos gigantescos o streams de red en milisegundos.
   - **Hash de Contraseñas (ej. bcrypt/Argon2id)**: Requiere ser **intencionadamente lento y pesado en memoria** para encarecer el hardware y frenar las pruebas por fuerza bruta del atacante.
   - *Incompatibilidad*: Un diseño rápido para comprobar integridad hace vulnerable el almacenamiento de contraseñas; un diseño lento para contraseñas inutilizaría la verificación de integridad en archivos grandes.

4. **Metodología de Ataque a una Sal Predecible Generada por Tiempo**:
   - Se toma el rango temporal comprendido en la última hora (un intervalo de 3600 segundos).
   - Para cada segundo de ese intervalo, se inicializa el generador pseudoaleatorio utilizando ese timestamp como semilla.
   - Se genera la sal candidata y se calcula el hash concatenándola con la palabra del diccionario.
   - Se compara el hash resultante con el hash robado hasta dar con la coincidencia que revela la clave y la sal original.

5. **Modos de Ataque Principales en Hashcat**:
   - **Modo Diccionario (Modo 0 - `-a 0`)**: Comprueba secuencialmente las palabras contenidas en una lista de texto (*wordlist* como `rockyou.txt`).
   - **Modo Máscara / Fuerza Bruta (Modo 3 - `-a 3`)**: Genera combinaciones basadas en un patrón o conjunto de caracteres especificado (por ejemplo, definir longitud y tipos de caracteres como dígitos o mayúsculas).
   - **Modo Combinador (Modo 1 - `-a 1`)**: Toma palabras de dos diccionarios diferentes y las combina entre sí formando parejas.

#### Cuestionario de Pseudoaleatoriedad

1. **Diferencias entre PRNG y CSPRNG**:
   - **PRNG**: Es un algoritmo determinista rápido enfocado en rendimiento estadístico, pero predecible si se conoce la semilla o parte de la serie. Ejemplo: El algoritmo `Mersenne Twister` (usado en lenguajes como Python o C++ para simulaciones) o `Xorshift`.
   - **CSPRNG**: Es un algoritmo diseñado para ser indistinguible del ruido blanco, impidiendo calcular valores pasados o futuros del sistema. Ejemplo: El algoritmo `Fortuna` o el uso de `AES-CTR` (AES en modo contador) alimentado por entropía del núcleo del sistema operativo.

2. **Relación entre Sal Predecible, Ciclo y Reproducibilidad**:
   - La *reproducibilidad* (capacidad de repetir una secuencia si se conoce la semilla) es una virtud en simulaciones, pero se convierte en una **vulnerabilidad crítica** en seguridad si la semilla se basa en un valor adivinable como el tiempo (`time()`).
   - **Impacto de ampliar la ventana temporal**: Si la cuenta se hubiese creado en un intervalo de varios meses en lugar de una hora, el número de semillas a probar aumentaría a unos pocos millones (los segundos equivalentes a esos meses). Sin embargo, para la capacidad de cálculo actual, probar unos pocos millones de semillas sigue siendo una tarea trivial que se resuelve en cuestión de segundos.

---

### 4. Resumen de Conceptos de Ingeniería Inversa (Repaso de Auditoría)

| Concepto / Herramienta | Naturaleza Real | Falsas Creencias / Erratas Comunes |
|---|---|---|
| **Objetivo de la Ingeniería Inversa** | Analizar un ejecutable sin código fuente para obtener su diseño, estructura, auditar fallos o replicar funcionalidades. | **No** se limita a "obtener un esquema", ni se aplica únicamente al ámbito informático (se aplica en mecánica, electrónica, etc.). |
| **Beneficios del Análisis** | Permite detectar errores ocultos, comportamientos/efectos laterales y vulnerabilidades de seguridad. | **No** garantiza directamente reducir el tamaño o la complejidad del código del sistema original. |
| **Desensambladores** | Traducen código máquina ejecutable a **lenguaje ensamblador (assembly)**. | **No** traducen código máquina a "lenguaje normal" ni a lenguajes de alto nivel (eso lo hacen los decompiladores). |
| **OllyDbg** | Depurador/desensamblador a nivel de ensamblador x86 **exclusivamente para Windows**. | **No** existe versión nativa para Linux. Permite inspeccionar la **memoria** y los **registros de la CPU** (no existen "registros de la memoria"). |