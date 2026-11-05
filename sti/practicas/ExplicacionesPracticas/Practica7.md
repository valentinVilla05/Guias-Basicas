## Práctica 7: Aleatoriedad, Entropía, Hashes de Contraseñas e Ingeniería Inversa


### 1. Aleatoriedad y Generadores de Números (PRNG vs. CSPRNG)

- **Naturaleza de la Aleatoriedad**:
  - En computación no existe la aleatoriedad física pura de forma nativa, ya que los programas son deterministas.
  - La aleatoriedad se evalúa como una **propiedad estadística sobre una secuencia o serie de números**, nunca sobre un número aislado.
  - La distribución ideal esperada de un generador de números aleatorios es **uniforme** (todos los valores del rango tienen la misma probabilidad). No debe seguir una distribución normal a menos que se aplique una transformación específica posterior.

- **Generadores Pseudoaleatorios Estándar (PRNG)**:
  - **Funcionamiento**: Algoritmos deterministas que generan una secuencia $x_n$ a partir de un valor inicial denominado **semilla** ($x_0$).
  - **Determinismo**: Conocer la semilla permite reproducir exactamente toda la secuencia numérica. Esta propiedad es muy útil para depurar simulaciones.
  - **Aplicaciones**: Válidos para videojuegos, simulaciones o teoría de decisiones donde prima la velocidad y el bajo coste computacional.
  - **Inseguridad Criptográfica**: **NO deben usarse en seguridad/criptografía**. Si un atacante descubre la semilla o parte de la salida, puede predecir el resto de los números.
  - **Ciclo de un PRNG**: Al ser un algoritmo determinista con un número finito de estados en memoria, tarde o temprano vuelve a un estado previo. En ese momento la secuencia se **repite periódicamente (entra en ciclo)**. Es deseable que el ciclo sea lo más largo posible.
  - **Gestión de la Semilla**: La semilla se fija al inicializar el generador (*seeding*). No debe modificarse en tiempo de ejecución en cada llamada, pues altera la distribución matemática.

- **Generadores Criptográficamente Seguros (CSPRNG)**:
  - Diseñados para que sea computacionalmente inviable predecir el siguiente bit o reconstruir el estado interno a partir de salidas anteriores.
  - En sistemas Linux, se alimentan del *pool* de entropía del sistema (ruido térmico, temporización de interrupciones de teclado o disco) y se acceden mediante `/dev/urandom`, `getrandom()` u `openssl rand`.

---

### 2. Almacenamiento Seguro de Contraseñas, Sales y Entropía

- **Almacenamiento mediante Resumen (Hash)**:
  - Las contraseñas nunca deben guardarse en claro. Se almacena el resumen generado por una **función hash de una sola dirección**.
  - Las funciones hash convierten entradas de longitud variable en salidas de **longitud fija**.

- **El Concepto de Sal (*Salt*)**:
  - Cadena aleatoria única generada para cada usuario (usando un CSPRNG) que se concatena a la contraseña antes de calcular el hash.
  - **Propósito**: Evita que dos usuarios con la misma contraseña tengan el mismo hash y neutraliza los ataques con **tablas arcoíris (tablas precalculadas)**. Obliga al atacante a recalcular el hash individualmente para cada usuario.
  - **Vulnerabilidad de Sales Predecibles**: Si la sal se genera con un PRNG débil (ej. `srand(time(NULL))`), un atacante que conozca la ventana temporal de creación de la cuenta puede reproducir las semillas y reconstruir la sal.

- **Entropía de Contraseñas**:
  - **Fórmula**: La entropía en bits se calcula como $H = L \cdot \log_2(N)$, donde $L$ es la longitud de la contraseña y $N$ es el tamaño de la población/alfabeto de caracteres usados.
  - **Significado**: Mide la incertidumbre o complejidad del espacio de búsqueda. El número total de intentos requeridos para fuerza bruta en el peor de los casos es $2^H$ combinaciones.
  - **Población ($N$)**: Incluir mayúsculas, minúsculas, números y símbolos aumenta $N$, lo que incrementa el valor de $\log_2(N)$ y eleva la entropía final.
  - **Diceware**: Método para generar contraseñas compuestas por palabras aleatorias basadas en una lista prefijada (ej. 7776 palabras).

- **Algoritmos Rápidos vs. Algoritmos Lentos (KDF)**:
  - **Inadecuación de MD5 y SHA-256**: Aunque SHA-256 es resistente a colisiones, es extremadamente rápido de calcular. Permite realizar miles de millones de intentos por segundo en un ataque de diccionario.
  - **Funciones de Derivación de Contraseñas (KDF Lentas)**: Diseñadas intencionadamente para ser computacionalmente intensivas y frenar la fuerza bruta.
    - **bcrypt**: Permite configurar un factor de coste/rondas (OWASP recomienda un mínimo de 10-12).
    - **Argon2id**: Estándar moderno que parametriza iteraciones de tiempo ($t$), uso de memoria ($m$) y paralelismo ($p$).
    - **yescrypt**: Algoritmo lento utilizado por defecto en distribuciones Linux modernas (`/etc/shadow`).

---

### 3. Conceptos de Ingeniería Inversa (Repaso de Auditoría)

| Concepto / Herramienta | Naturaleza Real | Falsas Creencias / Erratas Comunes |
|---|---|---|
| **Objetivo de la Ingeniería Inversa** | Analizar un ejecutable sin código fuente para obtener su diseño, estructura, auditar fallos o replicar funcionalidades. | **No** se limita a "obtener un esquema", ni se aplica únicamente al ámbito informático (se aplica en mecánica, electrónica, etc.). |
| **Beneficios del Análisis** | Permite detectar errores ocultos, comportamientos/efectos laterales y vulnerabilidades de seguridad. | **No** garantiza directamente reducir el tamaño o la complejidad del código del sistema original. |
| **Desensambladores** | Traducen código máquina ejecutable a **lenguaje ensamblador (assembly)**. | **No** traducen código máquina a "lenguaje normal" ni a lenguajes de alto nivel (eso lo hacen los decompiladores). |
| **OllyDbg** | Depurador/desensamblador a nivel de ensamblador x86 **exclusivamente para Windows**. | **No** existe versión nativa para Linux. Permite inspeccionar la **memoria** y los **registros de la CPU** (no existen "registros de la memoria"). |