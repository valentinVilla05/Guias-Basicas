## Preguntas de los test de STI

> El número de rondas del algoritmo AES es 14 para claves de 128-bit, 16 para claves de 192-bit, y 18 para 256-bit

- **Falso**
- _Motivo: las rondas son 10, 12 y 14 para claves de 128, 192 y 256 bits respectivamente._

> El esquema general del algoritmo AES está formado por una etapa inicial, una central y una final, donde la central es cíclica

- **Verdadero**
- _Motivo: la etapa central (SubBytes, ShiftRows, MixColumns, AddRoundKey) se repite Nr - 1 veces; la inicial y la final no son cíclicas._

> En el proceso de la operación AddRoundKey una entrada con todo a "00" salvo la diagonal con todos sus valores a "0F" y una clave completa a valores de "FF" nos devuelve la inversa de la entrada.

- **Verdadero**
- _Motivo: AddRoundKey es una XOR, y X ⊕ FF equivale a invertir todos los bits (00 → FF, 0F → F0), es decir, el complemento de la entrada._

> El esquema general del algoritmo AES está formado por una etapa inicial y una final

- **Falso**
- _Motivo: falta la etapa central, que es la cíclica y la que contiene casi todas las operaciones._

> En la etapa inicial del algoritmo AES se emplea únicamente la operación AddRoundKey

- **Verdadero**
- _Motivo: antes de las rondas solo se hace una XOR del bloque con la primera subclave (la clave original)._

> Las operaciones de la ronda estándar para el algoritmo AES son SubBytes, ShiftRows, AddRoundKey y MaxColumns

- **Falso**
- _Motivo: la operación se llama MixColumns; "MaxColumns" no existe en AES._

> Los algoritmos MD5 y SHA1 son algoritmos asimétricos

- **Falso**
- _Motivo: son funciones hash, que no usan clave y no son reversibles; no son ni simétricas ni asimétricas._

> Las operaciones de la ronda estándar para el algoritmo AES son SubBytes, AddRoundKey y MaxColumns

- **Falso**
- _Motivo: faltan ShiftRows y MixColumns (y además "MaxColumns" no existe)._

> El esquema general del algoritmo AES está formado por una etapa inicial, una central y una final, todas ellas no cíclicas

- **Falso**
- _Motivo: la etapa central sí es cíclica, se repite en bucle durante Nr - 1 rondas._

> El número de rondas del algoritmo AES es 10 para claves de 128-bit, 11 para claves de 192-bit, y 12 para 256-bit

- **Falso**
- _Motivo: lo correcto es 10, 12 y 14. El 11 y el 12 de esta opción son valores equivocados._

> El número de rondas del algoritmo AES es 14 para claves de 128-bit, 16 para claves de 192-bit, y 18 para 256-bit

- **Falso**
- _Motivo: El número real de rondas del algoritmo AES es **10 rondas** para claves de 128 bits, **12 rondas** para claves de 192 bits y **14 rondas** para claves de 256 bits

> El esquema general del algoritmo AES está formado por una etapa inicial, una central y una final, donde la central es cíclica

- **Verdadero**
- _Motivo: AES se compone de una etapa inicial ( AddRoundKey ), una etapa central repetitiva/cíclica ( SubBytes, ShiftRows, MixColumns, AddRoundKey ) y una etapa final (igual a la central pero sin MixColumns )

> En el proceso de la operación AddRoundKey una entrada con todo a "00" salvo la diagonal con todos sus valores a "0F" y una clave completa a valores de "FF" nos devuelve la inversa de la entrada

- **Falso**
- _Motivo:  La operación `AddRoundKey` realiza una suma a nivel de bits utilizando el operador XOR ($\oplus$). Hacer XOR con un valor fijo como "FF" invierte los bits de esos bytes específicos (complemento a 1), pero no genera la inversa del estado ni la inversa matemática en el cuerpo de Galois GF($2^8$)

> El esquema general del algoritmo AES está formado por una etapa inicial y una final.

- **Falso**
- _Motivo: Carece de la etapa central/cíclica, la cual ejecuta el bucle principal de rondas de cifrado del algoritmo.

> En la etapa inicial del algoritmo AES se emplea únicamente la operación AddRoundKey

- **Verdadero**
- _Motivo: En la etapa inicial (fase de blanqueamiento de clave) se realiza exclusivamente una suma XOR del estado inicial con la clave inicial mediante `AddRoundKey`

> Las operaciones de la ronda estándar para el algoritmo AES son SubBytes, ShiftRows, AddRoundKey y MaxColumns

- **Falso**
- _Motivo: La operación correcta se denomina MixColumns, no "MaxColumns"

> Los algoritmos MD5 y SHA1 son algoritmos asimétricos
- **Falso**
- _Motivo: MD5 y SHA-1 son funciones hash criptográficas (funciones de resumen unidireccionales), no algoritmos de cifrado ni simétricos ni asimétricos

> Las operaciones de la ronda estándar para el algoritmo AES son SubBytes, AddRoundKey y MaxColumns
- **Falso**
- _Motivo: Es incorrecta tanto por incluir "MaxColumns" (en vez de MixColumns) como por omitir la transformación ShiftRows. La ronda estándar completa consta de `SubBytes`, `ShiftRows`, `MixColumns` y `AddRoundKey`

> El esquema general del algoritmo AES está formado por una etapa inicial, una central y una final, todas ellas no cíclicas

- **Falso**
- _Motivo: La etapa central es cíclica, ya que repite el conjunto de operaciones (SubBytes, ShiftRows, MixColumns y AddRoundKey) en un bucle de varias rondas según el tamaño de la clave

> El número de rondas del algoritmo AES es 10 para claves de 128-bit, 11 para claves de 192-bit, y 12 para 256-bit

- **Falso**
- _Motivo: El número correcto de rondas en AES es:
* 10 rondas para 128 bits.
* 12 rondas para 192 bits (no 11).
* 14 rondas para 256 bits (no 12).

> Las operaciones de la ronda estándar para el algoritmo AES son SubBytes, ShitRows y MixComuns

- **Falso**

> La etapa final del algirtmo AES está compuesta por 3 operaciones: AddRoundKey, ShitRosws y ShitBytes

- **Verdadero**

> El módulo SubBytes se encarga de dividir la entrada en bytes y combinarlos usando una transformación lineal

- **Falso**

> La matriz estado del algoritmo AES es un bloque formado por segmentos que se agrupan en tamaños de matrices cada casilla tiene una parte del mensaje igual a 1024 bits

- **Falso**

> El esquema general del algoritmo AES está formado por una etapa inicial, una central y una final , todas ellas no

- **Falso**

> La matriz estado del algoritmo AES es un vector de tamaño 1024 bits

- **False**

> Los algoritmos MDS y SHAI son algoritmos de hashing

- **Verdadero**


> En el proceso de la opración AddRoundKey una entrada con todo a "00" salvo la diagonal con todos sus valores y clave completa a valores de "FF" nos devuelve la inversa de la entrada

> La ingeniería inversa facilita la realización de prototipos y disminuye el costo al desarrollar nuevos productos

- **Verdadero**
- _Motivo: La ingeniería inversa facilita la creación de prototipos y puede reducir los costes y el tiempo necesarios para desarrollar nuevos productos , al analiazr diseños o productos existentes

> OllyDbg permite la integración del codigo fuente de una aplicación

- **Falso** 

- _Motivo: OllyDbg es un depurador que permite analizar y ejecutar paso a paso el código máquina de una aplicación pero no recupera automáticamente todo el código fuente original

> Los productos más comunes sometidos a la ingeniería inversa son microsoft y dell

- **Falso**

- _Motivo: Los productos sometidos a ingeiería inversa pueden ser software , dispositivos electrónicos, hardware y productos mecánicos. Como MIcrosoft y Dell son empreas, no categorías de productos

> Los conceptos de vulnerabilidades de la práctica 1 y la ingeniería inversa son conceptos sin relación

- **Falso**

- _Motivo: Las vulnerabilidades y la ingeniería inversa si están relacionadas ya que la ingeniería inversa permite analizar software y sistemas para identificar posibles vulnerabilidades de seguridad

> Entre los beneficios que se generan al hacer ingeniería inversa está el de reducir los fallos y calidad de los sistemas

- **Verdadero**

- _Motivo: La ingeniería inversa puede ayudar a reducir los fallos y mejorar la caliidad de los sitemas mediante el análisis , la detección de errores y la identifcación de problemas de diseño

> La función `lstrcmp()` sirve para comparar cadenas

- **Verdadero**

> La ingeniería inversa permite mejorar el diseño de lso produtos ya xistentes haciendolos más eficientes y efectivos

- **Verdadero**
- _Motivo: La ingeniería inversa permite analizar productos existentes para identificar mejoras en su diseño, aumentar su eficiencia y efectividad, reducir costes

> Entre los beneficios que se generan al hacer una ingeniería inversa está recuperar y actualizar la información

- **Verdadero**

- _Motivo: La ingenieŕia inversa permite recuperar, analizar y actualizar la información de sistemas existentes, facilitando su mantenimiento y modernización

> El objetivo de la ingeniería inversa es obtener el diseño y esquema de un producto softwar

- **Verdadero**

- _Motivo: La ingeniería inversa busca analizar un producto software existente para extraer e identificar sus componentes, estructura y principios de diseño.   

> Entre los beneficios que se generan al hacer una ingeniería inversa se encuentra la de detectar efectos/errores laterales   

- **Verdadero**

- _Motivo: Al analizar en profundidad la estructura interna y el comportamiento del sistema, es posible identificar fallos ocultos, inconsistencias y efectos secundarios no deseados.   

> El objetivo de la ingeniería inversa es obtener información o un diseño a partir de un producto accesible al público para rehacer el propio programa   

- **Verdadero**

- _Motivo: Permite entender el funcionamiento interno de un sistema comercial o público para rediseñarlo, replicarlo o mejorarlo sin contar con la documentación original.   

> Los desensambladores son herramientas que convierte código máquina en lenguaje normal.   


- **Falso**

- _Motivo: Los desensambladores traducen el código máquina (binario) a lenguaje ensamblador (assembly), no a "lenguaje normal" o de alto nivel.   

> El concepto de ingeniería inversa sólo se aplica en el ámbito informático   

* **Falso**

- _Motivo: La ingeniería inversa se utiliza en multitud de campos como la mecánica, la electrónica, la arquitectura, la industria química y la manufactura, no solo en informática.   

> La herramienta OllyDBG para Windows y Linux es un depurador de código ensamblador muy empleado en auditoría informática para detectar los agujeros de seguridad de una herramienta   

* **Falso**

- _Motivo: OllyDbg es un depurador diseñado exclusivamente para arquitecturas x86 en sistemas Windows, no está disponible de forma nativa para Linux.   

> Entre los beneficios que se generan al hacer una ingeniería inversa se encuentran los de reducir los tamaños y complejidad de los sistemas   

* **Verdadero**

- _Motivo: El análisis detallado de la arquitectura facilita la reestructuración y optimización del código, ayudando a simplificar la complejidad y eliminar partes redundantes.   

> El objetivo de la ingeniería inversa es obtener información o un diseño a partir de un producto que nos permite auditar y buscar agujeros de seguridad   

* **Verdadero**

- _Motivo: La ingeniería inversa es fundamental en ciberseguridad para descubrir vulnerabilidades, fallos de diseño y puertas traseras dentro de las aplicaciones.   

> Se conoce por ingeniería inversa a la actividad que se ocupa de descubrir cómo funciona un programa, función o característica de cuyo código fuente no se dispone, hasta el punto de poder modificar ese código o generar código propio que cumpla las mismas funciones   

* **Verdadero**

- _Motivo: Define con precisión el concepto básico de ingeniería inversa aplicada al software cuando no se cuenta con el código fuente de origen.   

> El software de ollydbg nos permite analizar los valores de los registros de la memoria   

* **Verdadero**
- _Motivo: Como depurador a nivel de ensamblador, OllyDbg permite visualizar e inspeccionar en tiempo de ejecución tanto la memoria como los registros del procesador.   

> El objetivo de la ingeniería inversa es obtener información o un diseño a partir de un producto que nos permite auditar y buscar agujeros de seguridad   

* **Verdadero**

- _Motivo: Permite analizar un software o sistema existente para descubrir fallos de diseño, brechas de seguridad y vulnerabilidades no documentadas.   

> Los desensambladores son herramientas que convierte código máquina en lenguaje normal.   

* **Falso**

- _Motivo: Los desensambladores convierten el código máquina (binario) en lenguaje ensamblador (assembly), no en lenguaje comprensible en texto plano ni en lenguajes de alto nivel.   

> La herramienta OllyDBG para Windows y Linux es un depurador de código ensamblador muy empleado en auditoría informática para detectar los agujeros de seguridad de una herramienta   

* **Falso**

- _Motivo: OllyDbg es una herramienta orientada en exclusiva a sistemas operativos Windows (x86), por lo que no funciona de forma nativa en Linux.   

> Los productos más comunes sometidos a la ingeniería inversa son los software de Microsoft y Dell   

* **Falso**

- _Motivo: La ingeniería inversa se aplica ampliamente a todo tipo de software, firmware, malware, protocolos y hardware de cualquier fabricante, no estando limitada ni centrada de forma particular en Dell o Microsoft.   

> Entre los beneficios que se generan al hacer una ingeniería inversa se encuentra el recuperar y/o actualizar la información (cambios que no se documentaron en su momento)   

* **Verdadero**
- _Motivo: Facilita la recuperación de especificaciones perdedoras o cambios no registrados en la documentación original del sistema


> Entre los beneficios que se generan al hacer una ingeniería inversa se encuentran los de reducir los tamaños y complejidad de los sistemas   

* **Verdadero**

- _Motivo: Al comprender la arquitectura interna, es posible rediseñar el código para eliminar redundancias, simplificar su estructura y optimizar el sistema.   

> El concepto de ingeniería inversa sólo se aplica en el ámbito informático   

* **Falso**

- _Motivo: Es una metodología empleada en múltiples industrias como la ingeniería mecánica, electrónica, automotriz, aeroespacial y de diseño de productos
