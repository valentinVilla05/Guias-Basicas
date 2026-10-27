## Preguntas del test de STI

> El número de rondas del algoritmo AES es 14 para claves de 128-bit, 16 para claves de 192-bit, y 18 para 256-bit

- **Falso**
- _Motivo: AES usa **10 rondas** para claves de 128 bits, **12 rondas** para 192 bits y **14 rondas** para 256 bits._

> El esquema general del algoritmo AES está formado por una etapa inicial, una central y una final, donde la central es cíclica

- **Verdadero**
- _Motivo: consta de una etapa inicial (solo AddRoundKey), una etapa central repetida Nr − 1 veces (SubBytes, ShiftRows, MixColumns, AddRoundKey) y una etapa final (igual a la central pero sin MixColumns)._

> En el proceso de la operación AddRoundKey una entrada con todo a "00" salvo la diagonal con todos sus valores a "0F" y una clave completa a valores de "FF" nos devuelve la inversa de la entrada.

- **Falso**
- _Motivo: AddRoundKey es una XOR. Hacer XOR con "FF" devuelve el **complemento a 1** (NOT bit a bit) de cada byte (00 → FF, 0F → F0), no la inversa multiplicativa en GF(2⁸); además el byte 00 no tiene inversa multiplicativa._

> El esquema general del algoritmo AES está formado por una etapa inicial y una final

- **Falso**
- _Motivo: falta la etapa central, que es la cíclica y donde se ejecutan la mayoría de las rondas._

> En la etapa inicial del algoritmo AES se emplea únicamente la operación AddRoundKey

- **Verdadero**
- _Motivo: antes de las rondas solo se realiza una XOR del bloque de estado con la primera subclave (AddRoundKey inicial)._

> Las operaciones de la ronda estándar para el algoritmo AES son SubBytes, ShiftRows, AddRoundKey y MaxColumns

- **Falso**
- _Motivo: la operación se llama **MixColumns**; "MaxColumns" no existe en AES._

> Los algoritmos MD5 y SHA1 son algoritmos asimétricos

- **Falso**
- _Motivo: MD5 y SHA-1 son **funciones hash** (de resumen unidireccional), no algoritmos de cifrado; por tanto no son simétricos ni asimétricos._

> Las operaciones de la ronda estándar para el algoritmo AES son SubBytes, AddRoundKey y MaxColumns

- **Falso**
- _Motivo: además del nombre incorrecto "MaxColumns" (es **MixColumns**), falta **ShiftRows**. La ronda completa es: SubBytes, ShiftRows, MixColumns y AddRoundKey._

> El esquema general del algoritmo AES está formado por una etapa inicial, una central y una final, todas ellas no cíclicas

- **Falso**
- _Motivo: la etapa **central sí es cíclica**: se repite en bucle durante Nr − 1 rondas._

> El número de rondas del algoritmo AES es 10 para claves de 128-bit, 11 para claves de 192-bit, y 12 para claves de 256-bit

- **Falso**
- _Motivo: lo correcto es **10, 12 y 14**; los valores 11 y 12 son incorrectos._

> Las operaciones de la ronda estándar para el algoritmo AES son SubBytes, ShitRows y MixComuns

- **Falso**
- _Motivo: con las erratas corregidas serían SubBytes, ShiftRows y MixColumns, pero **falta AddRoundKey**, operación presente en todas las rondas._

> La etapa final del algirtmo AES está compuesta por 3 operaciones: AddRoundKey, ShitRosws y ShitBytes

- **Verdadero**
- _Motivo: la ronda final realiza exactamente 3 operaciones: **SubBytes, ShiftRows y AddRoundKey** (sin MixColumns). Las erratas "ShitBytes" y "ShitRosws" son SubBytes y ShiftRows._

> El módulo SubBytes se encarga de dividir la entrada en bytes y combinarlos usando una transformación lineal

- **Falso**
- _Motivo: SubBytes **no divide** nada: sustituye cada byte por otro mediante la **S-box**, una transformación **no lineal** (propiedad de confusión de la que depende la seguridad de AES)._

> La matriz estado del algoritmo AES es un bloque formado por segmentos que se agrupan en tamaños de matrices cada casilla tiene una parte del mensaje igual a 1024 bits

- **Falso**
- _Motivo: el estado es una matriz de **4×4 = 16 bytes = 128 bits**, y cada casilla contiene **1 byte (8 bits)**, no 1024 bits._

> El esquema general del algoritmo AES está formado por una etapa inicial, una central y una final , todas ellas no

- **Falso**
- _Motivo: la pregunta está incompleta, pero al referirse a que todas las etapas no son cíclicas es falsa: **la etapa central es cíclica**._

> La matriz estado del algoritmo AES es un vector de tamaño 1024 bits

- **Falso**
- _Motivo: el estado tiene **128 bits** (16 bytes), igual que el bloque de cifrado de AES._

> Los algoritmos MDS y SHAI son algoritmos de hashing

- **Verdadero**
- _Motivo: con las erratas corregidas son **MD5 y SHA-1**, que efectivamente son algoritmos de hashing (funciones de resumen)._

> La ingeniería inversa facilita la realización de prototipos y disminuye el costo al desarrollar nuevos productos

- **Verdadero**
- _Motivo: al analizar productos o diseños existentes se reutilizan ideas y conocimientos, lo que reduce el tiempo y el coste de desarrollar prototipos y nuevos productos._

> OllyDbg permite la integracion del codigo fuente de una aplicacion

- **Falso**
- _Motivo: OllyDbg es un depurador de código **máquina/ensamblador**; no recupera ni integra el código fuente original de la aplicación._

> Los productos más comunes sometidos a la ingeniería inversa son microsoft y dell

- **Falso**
- _Motivo: la ingeniería inversa se aplica a **software, firmware, hardware, malware, protocolos y productos electrónicos** en general; Microsoft y Dell son empresas, no categorías de productos._

> Los conceptos de vulnerabilidades de la práctica 1 y la ingeniería inversa son conceptos sin relación

- **Falso**
- _Motivo: están directamente relacionados: la ingeniería inversa es una de las técnicas principales para **analizar software y descubrir vulnerabilidades**._

> Entre los beneficios que se generan al hacer ingeniería inversa está el de reducir los fallos y calidad de los sistemas

- **Verdadero**
- _Motivo: su análisis interno permite detectar errores, fallos de diseño y problemas ocultos, lo que se traduce en **menos fallos y mejor calidad** en los sistemas._

> La función `lstrcmp()` sirve para comparar cadenas

- **Verdadero**
- _Motivo: es una función de la API de Windows que compara dos cadenas de caracteres y devuelve su relación de orden (menor, igual, mayor)._

> La ingeniería inversa permite mejorar el diseño de lso produtos ya xistentes haciendolos más eficientes y efectivos

- **Verdadero**
- _Motivo: al entender el diseño de los productos existentes se pueden identificar mejoras que aumentan su eficiencia y efectividad y reducen costes._

> Entre los beneficios que se generan al hacer una ingeniería inversa está recuperar y actualizar la información

- **Verdadero**
- _Motivo: permite recuperar especificaciones o cambios que no se documentaron y actualizarlos, facilitando el mantenimiento y la modernización del sistema._

> El objetivo de la ingeniería inversa es obtener el diseño y esquema de un producto softwar

- **Verdadero**
- _Motivo: busca extraer e identificar los componentes, la estructura y los principios de diseño de un producto software existente._

> Entre los beneficios que se generan al hacer una ingeniería inversa se encuentra la de detectar efectos/errores laterales

- **Verdadero**
- _Motivo: al analizar en profundidad la estructura y el comportamiento del sistema se pueden identificar fallos ocultos, inconsistencias y efectos secundarios no deseados._

> El objetivo de la ingeniería inversa es obtener información o un diseño a partir de un producto accesible al público para rehacer el propio programa

- **Verdadero**
- _Motivo: permite entender el funcionamiento interno de un sistema comercial o público para rediseñarlo, replicarlo o mejorarlo sin disponer de la documentación original._

> Los desensambladores son herramientas que convierte código máquina en lenguaje normal.

- **Falso**
- _Motivo: convierten código máquina en **lenguaje ensamblador (assembly)**, no en "lenguaje normal" ni en lenguaje de alto nivel; para eso existen los decompiladores._

> El concepto de ingeniería inversa sólo se aplica en el ámbito informático

- **Falso**
- _Motivo: se aplica también a mecánica, electrónica, arquitectura, industria química, automoción, aeroespacial, etc._

> La herramienta OllyDBG para Windows y Linux es un depurador de código ensamblador muy empleado en auditoría informática para detectar los agujeros de seguridad de una herramienta

- **Falso**
- _Motivo: OllyDbg es un depurador de arquitectura x86 **exclusivamente para Windows**; no existe una versión nativa para Linux (en Linux se usan GDB, radare2, etc.)._

> Entre los beneficios que se generan al hacer una ingeniería inversa se encuentran los de reducir los tamaños y complejidad de los sistemas

- **Verdadero**
- _Motivo: al comprender la arquitectura interna se puede reestructurar y optimizar el código, eliminando redundancias y simplificando el sistema._

> El objetivo de la ingeniería inversa es obtener información o un diseño a partir de un producto que nos permite auditar y buscar agujeros de seguridad

- **Verdadero**
- _Motivo: en ciberseguridad se usa precisamente para descubrir vulnerabilidades, fallos de diseño y puertas traseras no documentadas._

> Se conoce por ingeniería inversa a la actividad que se ocupa de descubrir cómo funciona un programa, función o característica de cuyo código fuente no se dispone, hasta el punto de poder modificar ese código o generar código propio que cumpla las mismas funciones

- **Verdadero**
- _Motivo: es la definición clásica de ingeniería inversa aplicada al software cuando no se cuenta con el código fuente original._

> El software de ollydbg nos permite analizar los valores de los registros de la memoria

- **Verdadero**
- _Motivo: como depurador a nivel de ensamblador, OllyDbg permite inspeccionar en tiempo de ejecución tanto la **memoria** como los **registros** del procesador._