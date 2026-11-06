## Preguntas Obtenidas de la práctica 4


> La máquina Bombe fue utilizada por los criptólogos británicos para descifrar los mensajes enviados con la máquina Enigma a través de una cadena de deducciones lógicas para obtener la configuración de los rotores de la máquina.

- **Verdadero**
- _Motivo: la Bombe explotaba un texto claro conocido mediante una cadena de deducciones lógicas (y el "ban" de ventanas) para descartar configuraciones de rotores imposibles y determinar la configuración inicial de la Enigma._

----------------------------

> El plugboard de la máquina Enigma es el sistema frontal de intercambio de letras que permitía añadir gran complejidad al cifrado de mensajes y permite conectar dos letras con el mismo cable.

- **Verdadero**
- _Motivo: el plugboard (Steckerbrett) era el panel frontal de intercambio de letras donde cada cable conectaba un par de letras (una en cada extremo), intercambiándolas antes y después de los rotores y añadiendo gran complejidad al cifrado._

----------------------------

> La máquina Bombe fue utilizada por los criptólogos británicos para descifrar los mensajes enviados con la máquina Enigma mediante la búsqueda de patrones en el mensaje cifrado para poder obtener la configuración de los rotores a través del cálculo del MCM.

- **Falso**
- _Motivo: la Bombe no busca patrones ni emplea el MCM: funciona por deducción lógica a partir de un texto conocido; el MCM se usa, por ejemplo, en el ataque de Kasiski para calcular la longitud de la clave._

----------------------------

> La combinación de rotores era un aspecto fundamental en la configuración de la máquina para el cifrado/descifrado de los mensajes donde cada rotor tenía un identificador, y a cada uno de ellos se le asignaba una letra de inicio para cifrar y descifrar mensajes al comienzo de cada día.

- **Verdadero**
- _Motivo: cada rotor llevaba un identificador y, además de elegir el orden de los rotores, se les asignaba una letra de posición inicial que se configuraba cada día junto con el plugboard; era un aspecto fundamental para cifrar y descifrar los mensajes._

----------------------------

> El británico Alan Turing y el alemán Gordon Welchman fueron los principales artífices de la máquina "Bombe".

- **Falso**
- _Motivo: Alan Turing y Gordon Welchman fueron los principales artífices de la Bombe, pero Gordon Welchman era **británico**, no alemán (el enunciado erra su nacionalidad)._

----------------------------

> La combinación de rotores era un aspecto fundamental en la configuración de la máquina para el cifrado/descifrado de los mensajes donde los rotores contaban con una posición fija en cualquier cifrado.

- **Falso**
- _Motivo: los rotores no tenían posición fija: su orden y su posición inicial cambiaban en cada configuración (y se reiniciaban a diario); de ello dependía precisamente la seguridad del cifrado._

----------------------------

> El plugboard de la máquina Enigma es el sistema frontal de intercambio de letras que permitía añadir gran complejidad al cifrado de mensajes y permite conectar 10 cables a un par de letras, una de ellas en cada extremo.

- **Falso**
- _Motivo: el plugboard disponía de 10 cables, pero **cada cable conectaba un par de letras distinto** (una en cada extremo, hasta un máximo de 20 letras); no podían conectarse 10 cables a un solo par de letras._

----------------------------


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

> Los algoritmos MD5 y SHA1 son algoritmos asimétricos

- **Falso**
- _Motivo: MD5 y SHA-1 son **funciones hash** (de resumen unidireccional), no algoritmos de cifrado; por tanto no son simétricos ni asimétricos._

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
- _Motivo: SubBytes **no combina** nada con una transformación lineal: sustituye cada byte por otro mediante la **S-box**, una transformación **no lineal** (propiedad de confusión de la que depende la seguridad de AES)._

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

> Los algoritmos MDS y SHAI son algoritmos de hashing

- **Verdadero**
- _Motivo: con las erratas corregidas son **MD5 y SHA-1**, que efectivamente son algoritmos de hashing (funciones de resumen)._

----------------------------

> La etapa final del algoritmo AES está compuesta por 3 operaciones: AddRoundKey, ShiftRows y MaxColumns.

- **Falso**
- _Motivo: omite SubBytes e incluye erróneamente MixColumns (escrito como MaxColumns), la cual se excluye en la ronda final. Las operaciones correctas son SubBytes, ShiftRows y AddRoundKey._

----------------------------

> El módulo SubBytes se encarga de dividir la entrada en bytes y pasar cada uno a través de una caja de sustitución.

- **Verdadero**
- _Motivo: toma los 16 bytes de la matriz de estado y los sustituye de forma independiente mediante una tabla fija no lineal (S-Box)._

----------------------------

> El esquema general del algoritmo AES está formado por una etapa inicial cíclica, una central y una final no cíclicas.

- **Falso**
- _Motivo: invierte los conceptos: la etapa inicial es no cíclica, la etapa central (rondas intermedias) es cíclica (se repite en bucle) y la final es no cíclica._

----------------------------

> Los algoritmos MD5 y SHA1 son algoritmos de hashing.

- **Verdadero**
- _Motivo: ambos son funciones resumen (hash) unidireccionales que generan salidas de longitud fija._

----------------------------

> El número de rondas del algoritmo AES es 12 para claves de 128-bit, 13 para claves de 192-bit, y 14 para 256-bit.

- **Falso**
- _Motivo: las rondas correctas son: **10** para claves de 128 bits, **12** para claves de 192 bits y **14** para claves de 256 bits._

----------------------------