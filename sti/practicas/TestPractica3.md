## Preguntas Obtenidas de la práctica 3

> El número de rondas del algoritmo AES es 14 para claves de 128-bit, 16 para claves de 192-bit, y 18 para 256-bit

- **Falso**
- _Motivo: AES usa **10 rondas** para claves de 128 bits, **12 rondas** para 192 bits y **14 rondas** para 256 bits._

----------------------------

> El esquema general del algoritmo AES está formado por una etapa inicial, una central y una final, donde la central es cíclica

- **Verdadero**
- _Motivo: consta de una etapa inicial (solo AddRoundKey), una etapa central repetida Nr − 1 veces (SubBytes, ShiftRows, MixColumns, AddRoundKey) y una etapa final (igual a la central pero sin MixColumns)._

----------------------------

> En el proceso de la operación AddRoundKey una entrada con todo a "00" salvo la diagonal con todos sus valores a "0F" y una clave completa a valores de "FF" nos devuelve la inversa de la entrada.

- **Falso**
- _Motivo: AddRoundKey es una XOR. Hacer XOR con "FF" devuelve el **complemento a 1** (NOT bit a bit) de cada byte (00 → FF, 0F → F0), no la inversa multiplicativa en GF(2⁸); además el byte 00 no tiene inversa multiplicativa._

----------------------------

> El esquema general del algoritmo AES está formado por una etapa inicial y una final

- **Falso**
- _Motivo: falta la etapa central, que es la cíclica y donde se ejecutan la mayoría de las rondas._

----------------------------

> En la etapa inicial del algoritmo AES se emplea únicamente la operación AddRoundKey

- **Verdadero**
- _Motivo: antes de las rondas solo se realiza una XOR del bloque de estado con la primera subclave (AddRoundKey inicial)._

----------------------------

> Las operaciones de la ronda estándar para el algoritmo AES son SubBytes, ShiftRows, AddRoundKey y MaxColumns

- **Falso**
- _Motivo: la operación se llama **MixColumns**; "MaxColumns" no existe en AES._

----------------------------

> Las operaciones de la ronda estándar para el algoritmo AES son SubBytes, AddRoundKey y MaxColumns

- **Falso**
- _Motivo: además del nombre incorrecto "MaxColumns" (es **MixColumns**), falta **ShiftRows**. La ronda completa es: SubBytes, ShiftRows, MixColumns y AddRoundKey._

----------------------------

> El esquema general del algoritmo AES está formado por una etapa inicial, una central y una final, todas ellas no cíclicas

- **Falso**
- _Motivo: la etapa **central sí es cíclica**: se repite en bucle durante Nr − 1 rondas._

----------------------------

> El número de rondas del algoritmo AES es 10 para claves de 128-bit, 11 para claves de 192-bit, y 12 para claves de 256-bit

- **Falso**
- _Motivo: lo correcto es **10, 12 y 14**; los valores 11 y 12 son incorrectos._

----------------------------

> Las operaciones de la ronda estándar para el algoritmo AES son SubBytes, ShitRows y MixComuns

- **Falso**
- _Motivo: con las erratas corregidas serían SubBytes, ShiftRows y MixColumns, pero **falta AddRoundKey**, operación presente en todas las rondas._

----------------------------

> La etapa final del algirtmo AES está compuesta por 3 operaciones: AddRoundKey, ShitRosws y ShitBytes

- **Verdadero**
- _Motivo: la ronda final realiza exactamente 3 operaciones: **SubBytes, ShiftRows y AddRoundKey** (sin MixColumns). Las erratas "ShitBytes" y "ShitRosws" son SubBytes y ShiftRows._

----------------------------

> El módulo SubBytes se encarga de dividir la entrada en bytes y combinarlos usando una transformación lineal

- **Falso**
- _Motivo: SubBytes **no divide** nada: sustituye cada byte por otro mediante la **S-box**, una transformación **no lineal** (propiedad de confusión de la que depende la seguridad de AES)._

----------------------------

> La matriz estado del algoritmo AES es un bloque formado por segmentos que se agrupan en tamaños de matrices cada casilla tiene una parte del mensaje igual a 1024 bits

- **Falso**
- _Motivo: el estado es una matriz de **4×4 = 16 bytes = 128 bits**, y cada casilla contiene **1 byte (8 bits)**, no 1024 bits._

----------------------------

> El esquema general del algoritmo AES está formado por una etapa inicial, una central y una final , todas ellas no

- **Falso**
- _Motivo: la pregunta está incompleta, pero al referirse a que todas las etapas no son cíclicas es falsa: **la etapa central es cíclica**._

----------------------------

> La matriz estado del algoritmo AES es un vector de tamaño 1024 bits

- **Falso**
- _Motivo: el estado tiene **128 bits** (16 bytes), igual que el bloque de cifrado de AES._

----------------------------

> ¿Y esto es cifrado por permutación?

- **Falso**
- _Motivo: el cifrado de Vigenère es un algoritmo de sustitución polialfabética (sustituye unas letras por otras mediante suma modular). La permutación (o transposición) no cambia las letras, sino que únicamente altera su orden._

----------------------------

> Si cambiamos el lenguaje de Z27 a Z37 en español e intentamos resolver el último ejercicio del cuestionario, el algoritmo de Vigenère funciona sin problemas.

- **Falso**
- _Motivo: cambiar a Z37 no resuelve el problema principal de ese ejercicio, que es la falta de longitud del texto cifrado. Al ser un mensaje muy corto, el método de Kasiski sigue sin encontrar repeticiones suficientes para determinar la clave. Además, un espacio de búsqueda mayor (MOD 37) reduce aún más la probabilidad de repeticiones casuales._

----------------------------

> CrypTool implementa múltiples operadores matemáticos como primalidad, módulos, MCD, mcm, etc.

- **Verdadero**
- _Motivo: tanto CrypTool como la herramienta criptoclásicos incluyen un módulo con utilidades de aritmética modular, comprobación de números primos, cálculo de MCD/mcm, inversos modulares y operaciones con matrices._

----------------------------

> La principal diferencia entre Z27 y Z37 en español es que el segundo incorpora signos de puntuación.

- **Falso**
- _Motivo: la diferencia real radica en que Z37 incorpora los 10 dígitos numéricos (del 0 al 9) junto a las 27 letras del abecedario (27+10=37). Ninguno de los dos alfabetos incluye signos de puntuación ni espacios (eso corresponde a ASCII 191)._

----------------------------

> El alfabeto ASCII de 191 contiene la mayoría de caracteres imprimibles como mayúsculas, minúsculas, caracteres con puntuación, etc.

- **Verdadero**
- _Motivo: el subconjunto ASCII 191 abarca desde el código ASCII 32 al 222, e incluye mayúsculas, minúsculas, números, espacios y signos de puntuación._

----------------------------

> El operador de MCD y mcm se emplean en el ataque de Kasiski.

- **Falso**
- _Motivo: el ataque de Kasiski emplea únicamente el MCD (Máximo Común Divisor) para calcular la longitud de la clave a partir de las distancias entre patrones repetidos. El mcm (Mínimo Común Múltiplo) no se utiliza en este proceso._

----------------------------

> La herramienta de criptoanálisis permite trabajar con distintos alfabetos como el Español Z37, Inglés Z36 y ASCII 191, exclusivamente.

- **Falso**
- _Motivo: la herramienta soporta 5 alfabetos distintos, no solo esos 3. Omite los alfabetos básicos de solo letras: Inglés mayúsculas (MOD 26) y Castellano mayúsculas (MOD 27)._

----------------------------

> CrypTool es una herramienta de aprendizaje interactivo sobre criptografía avanzada.

- **Falso**
- _Motivo: aunque incluye criptografía avanzada, no es una herramienta orientada exclusivamente a ella. Es una plataforma didáctica para el estudio integral de la Criptografía en general, abarcando ampliamente los algoritmos clásicos y tradicionales._

----------------------------

> Si ciframos el mensaje "esto es una prueba" con la clave "hola" nos aparece el mensaje LHEOLHFNHECULPL usando el lenguaje en inglés Z36.

- **Falso**
- _Motivo: realizando la suma modular en MOD 36 (A-Z0-25 y 0-9 26-35), el cifrado de ESTOESUNAPRUEBA con la clave HOLA genera el criptograma L64OL65NH32ULPL._

----------------------------

> Aunque hemos empleado cifrado simétrico con el criptosistema Vigenère, también permite el asimétrico con claves dinámicas.

- **Falso**
- _Motivo: el algoritmo de Vigenère es un cifrado estrictamente simétrico y clásico. Utiliza una única clave estática compartida tanto para cifrar como para descifrar._

----------------------------

> El mensaje AMT8RKLEUBEYY91DPUWK07AIHSWSVGC92VPH5WU con Vigenère en inglés Z36 y clave seguridad devuelve el mensaje "siaciertasestapreguntaaprobarás".

- **Falso**
- _Motivo: al descifrar el criptograma de 39 caracteres en MOD 36 con la clave SEGURIDAD, el texto en claro real resultante es SINOACIERTASESTAPREGUNTAAPROBARASELEXAMEN ("Si no aciertas esta pregunta aprobarás el examen")._

----------------------------