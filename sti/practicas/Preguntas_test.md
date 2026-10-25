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
