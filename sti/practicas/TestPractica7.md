# Tipo Test Práctica 7

## Aleatoriedad, entropía y hashes

---

> Los números pseudo-aleatorios son buenos para aplicaciones como videojuegos

- **Verdadero**
- **Motivo**: Los generadores de números pseudoaleatorios (PRNG) son deterministas y computacionalmente muy rápidos, lo que los hace ideales para simulaciones y videojuegos donde la velocidad es prioritaria y no se requiere seguridad criptográfica

---

> La mayor parte de gestores de contraseñas incorpora herramientas para la actualización automática de nuestras contraseñas almacenadas

- **Falso**
- **Motivo**: Aunque los gestores sugieren o generan contraseñas fuertes, el cambio o actualización en los sitios web suele requerir la intervención e interacción del usuario debido a las distintas formas y flujos de autenticación de cada plataforma

---

> Las características de la aleatoriedad dependen de una serie de números y no de un número en sí

- **Verdadero**
- **Motivo**: La aleatoriedad es una propiedad estadística que se evalúa sobre una secuencia o distribución de números, no sobre un valor individual (un número aislado no puede ser "aleatorio" por sí solo)

---

> La entropía de una contraseña marca el número total de intentos para adivinar nuestra contraseña mediante el algoritmo de fuerza bruta

- **Falso**
- **Motivo**: La entropía mide la incertidumbre o complejidad en bits ($E$). El número total de combinaciones o intentos requeridos en el peor de los casos es $2^E$, no el valor numérico de la entropía directamente

---

> En un generador de números pseudo-aleatorios, si se conoce el valor inicial o semilla se conoce toda la secuencia de números

- **Verdadero**
- **Motivo**: Los generadores pseudoaleatorios son algoritmos deterministas; partiendo del mismo estado o semilla (seed), siempre producirán exactamente la misma secuencia de números

---

> Los números pseudo-aleatorios son requeridos en aplicaciones críticas, como la criptografía

- **Falso**
- **Motivo**: La criptografía requiere generadores criptográficamente seguros (CSPRNG) o números aleatorios verdaderos (TRNG); los pseudoaleatorios estándar son predecibles si se conoce el estado interno

---

> La función $H = L \cdot \log_2(N)$ es la fórmula matemática que nos permite calcular la entropía de contraseñas con una longitud $L$

- **Verdadero**
- **Motivo**: Mide la entropía en bits donde $L$ es la longitud de la contraseña y $N$ es el tamaño del conjunto de caracteres posibles ($N^L$ número de combinaciones, luego $\log_2(N^L) = L \cdot \log_2(N)$)

---

> Una de las características deseables de un generador de números aleatorios es que la secuencia producida no sea repetible

- **Verdadero**
- **Motivo**: En la aleatoriedad ideal o verdadera, las secuencias no deben repetirse de forma periódica o predecible

---

> Una de las características deseables de un generador de números aleatorios es que los números generados deben repetirse con frecuencia

- **Falso**
- **Motivo**: La repetición frecuente o patrones periódicos reducen la calidad de la aleatoriedad y la hacen predecible

---

> El valor de la semilla debe ser modificado en tiempo de ejecución

- **Falso**
- **Motivo**: La semilla se establece al inicializar el generador (seeding); modificarla continuamente en cada llamada altera la secuencia matemática y destruye las propiedades de distribución del generador

---

> La utilización de espacio en un generador de números pseudo-aleatorios no es importante porque el espacio es un conjunto infinito de estados

- **Falso**
- **Motivo**: El espacio de estados de un ordenador es finito y está determinado por la memoria/registros asignados; además, el tamaño del espacio del estado influye directamente en el periodo del generador

---

> Un buen generador de números aleatorios es aquel que genera sucesiones de números que se asemejan a realizaciones de una variable aleatoria que sigue una distribución normal

- **Falso**
- **Motivo**: Por definición, un generador estándar de números aleatorios debe producir una distribución uniforme (donde todos los valores del rango tienen exactamente la misma probabilidad de ser elegidos). Si se necesita una distribución normal u otra específica, se aplican transformaciones estadísticas posteriores

---

> La entropía se calcula realizando el logaritmo en base 2 de la cantidad de elementos de la población por la longitud de la contraseña

- **Falso**
- **Motivo**: La fórmula de la entropía para contraseñas de caracteres equiprobables es $H = L \cdot \log_2(N)$, donde $L$ es la longitud y $N$ el número de caracteres de la población. Se multiplica la longitud por el logaritmo de la población, no el logaritmo del producto ($L \times N$)

---

> Si incluimos en nuestra contraseña mayúsculas, minúsculas y símbolos, la entropía de nuestra contraseña será mayor puesto que la población de caracteres usados es mucho mayor

- **Verdadero**
- **Motivo**: Al ampliar la variedad de caracteres se incrementa el tamaño del alfabeto/población ($N$), lo que eleva el valor del término $\log_2(N)$ y, por ende, aumenta la entropía final ($H$) para la misma cantidad de caracteres

---

> Una función hash es un algoritmo matemático que transforma un bloque arbitrario de datos en una serie de caracteres con una longitud fija

- **Verdadero**
- **Motivo**: Es la propiedad fundamental de las funciones hash (como SHA-256 o MD5): aceptan una entrada de cualquier tamaño y generan una salida o digest de longitud predeterminada e invariable

---

> El valor denominado semilla es el valor inicial con el que inicia la secuencia de números de un generador pseudoaleatorio

- **Verdadero**
- **Motivo**: La semilla (seed) actúa como el estado inicial o punto de partida a partir del cual el algoritmo determinista genera toda la serie numérica

---

> En un generador de números pseudoaleatorios se produce un ciclo cuando un número de la secuencia se repite

- **Verdadero**
- **Motivo**: Al ser un algoritmo determinista con una cantidad finita de estados internos, en cuanto el generador vuelve a pasar por un estado o valor ya visitado, comenzará a repetir íntegramente la misma secuencia de números a partir de ese instante

---

## Ingeniería inversa

---

> El objetivo de la ingeniería inversa es obtener el diseño y esquema de un producto software

- **Verdadero**
- **Motivo**: Recuperar el diseño, la estructura y el esquema de un software a partir de su producto ejecutable es uno de los objetivos clásicos de la ingeniería inversa

---

> Entre los beneficios que se generan al hacer una ingeniería inversa se encuentra la de detectar efectos/errores laterales

- **Verdadero**
- **Motivo**: Al analizar el comportamiento real de un programa, la ingeniería inversa permite identificar efectos no documentados, errores y comportamientos laterales que no se ven a simple vista

---

> El objetivo de la ingeniería inversa es obtener información o un diseño a partir de un producto accesible al público para rehacer el propio programa

- **Verdadero**
- **Motivo**: Consiste en estudiar un producto ya existente (accesible o distribuido) para extraer de él conocimiento, diseño o especificaciones y poder rehacer o replicar un programa propio

---

> Los desensambladores son herramientas que convierten código máquina en lenguaje normal

- **Falso**
- **Motivo**: Los desensambladores convierten código máquina en **lenguaje ensamblador** (código fuente de bajo nivel), no en un lenguaje de alto nivel o "normal". Para obtener código de alto nivel se usarían los **decompiladores**

---

> El concepto de ingeniería inversa solo se aplica en el ámbito informático

- **Falso**
- **Motivo**: La ingeniería inversa se aplica en muchos campos más allá de la informática, como la ingeniería mecánica, electrónica, química, biotecnología o el análisis de protocolos y formatos de datos

---

> La herramienta OllyDBG para Windows y Linux es un depurador de código ensamblador muy empleado en auditoría informática para detectar los agujeros de seguridad de una herramienta

- **Falso**
- **Motivo**: OllyDbg es un depurador de código ensamblador muy usado en auditoría, pero **solo está disponible para Windows** (principalmente 32 bits), no para Linux

---

> Entre los beneficios que se generan al hacer una ingeniería inversa se encuentran los de reducir los tamaños y complejidad de los sistemas

- **Falso**
- **Motivo**: Los beneficios típicos de la ingeniería inversa son recuperar el diseño, entender cómo funciona un producto, detectar errores/efectos laterales, auditar seguridad, lograr interoperabilidad o portar software; **no** reducir directamente el tamaño o la complejidad de los sistemas

---

> El objetivo de la ingeniería inversa es obtener información o un diseño a partir de un producto que nos permite auditir y buscar agujeros de seguridad

- **Verdadero**
- **Motivo**: Una de las aplicaciones más importantes de la ingeniería inversa es la auditoría de seguridad: analizar un producto para entender su funcionamiento y descubrir vulnerabilidades o agujeros de seguridad

---

> Se conoce por ingeniería inversa a la actividad que se ocupa de descubrir cómo funciona un programa, función o característica de cuyo código fuente no se dispone, hasta el punto de poder modificar ese código o generar código propio que cumpla las mismas funciones

- **Verdadero**
- **Motivo**: Es la definición clásica de ingeniería inversa: analizar un software sin disponer de su código fuente para entenderlo, modificarlo o crear una implementación equivalente

---

> El software de OllyDbg nos permite analizar los valores de los registros de la memoria

- **Falso**
- **Motivo**: OllyDbg permite analizar los **registros del procesador** (EAX, EBX, ECX…) y el **contenido de la memoria**, pero no existen "registros de la memoria": los registros forman parte de la CPU, no de la memoria