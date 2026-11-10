## Práctica 4: Criptografía Simétrica de Bloque (AES), Máquina Enigma y Funciones Hash

---

### 1. La Máquina Enigma y su Mecanismo

- **Definición e Historia**:
- Máquina electromecánica de sustitución polialfabética basada en rotores, ideada por Arthur Scherbius (1918).
- Adoptada por el ejército alemán para cifrar y descifrar comunicaciones militares durante la Segunda Guerra Mundial.

- **Componentes Principales**:
- **Rotores (Walzen)**: Discos giratorios con conexiones internas que varían el alfabeto de sustitución en cada pulsación.
- Su orden en la máquina y su **posición inicial de letras cambiaban diariamente** según las hojas de claves diarias (*Schlüsseltafel*).
- Los rotores **NO tienen una posición fija**; la rotación dinámica en cada carácter e intercambio de posición son la base de su complejidad. Contaban con un anillo de configuración (*Ringstellung*) y una posición inicial (*Grundstellung*).
- **Reflector (Umkehrwalze / UKW)**: Reenvía la corriente eléctrica de vuelta a través de los rotores, permitiendo que la máquina sea simétrica (la misma configuración sirve tanto para cifrar como para descifrar). Su principal limitación criptográfica era que **una letra nunca podía cifrarse como ella misma**.
- **Panel de Conexiones (*Plugboard* / Steckerbrett)**:
- Panel frontal de intercambio de letras situadas antes y después del paso por los rotores.
- Utilizaba hasta **10 cables**, donde **cada cable conectaba un par de letras distinto** (intercambiando 20 letras en total). Un solo cable no puede conectar más de dos letras a la vez.

---

### 2. Criptoanálisis de Enigma y la Máquina "Bombe"

- **Máquina Bombe**:
- Dispositivo electromecánico desarrollado por criptólogos británicos en Bletchley Park para romper las claves diarias de Enigma (basado en el trabajo previo de los matemáticos polacos Marian Rejewski, Jerzy Różycki y Henryk Zygalski).
- **Método de Operación**: Explotaba fragmentos de texto claro conocido o probable (*cribs*) mediante una **cadena de deducciones lógicas** (circuitos eléctricos cerrados o *loops*) y eliminación de contradicciones para descubrir la posición inicial de los rotores y la configuración del plugboard.
- **Falsas Creencias de Criptoanálisis**: La máquina Bombe **NO utilizaba análisis de patrones** ni operaciones aritméticas como el **MCM (Mínimo Común Divisor/Múltiplo)** (el MCD/MCM pertenece a métodos clásicos como el ataque de Kasiski).
- **Diseñadores**: Principalmente **Alan Turing** y **Gordon Welchman**. *(Nota: Welchman era británico, no alemán)*.

---

### 3. Profundización en AES (Advanced Encryption Standard)

- **Parámetros Técnicos del Estándar**:
- **Bloque de Entrada/Estado**: Matriz de **4×4 bytes = 16 bytes = 128 bits**. Cada casilla contiene estrictamente **1 byte (8 bits)**.
- **Relación Tamaño de Clave vs. Rondas ($N_r$)**:
- **128 bits**: 10 rondas.
- **192 bits**: 12 rondas.
- **256 bits**: 14 rondas.

- **Estructura Interna de las Fases**:
- **Etapa Inicial (No cíclica)**: Aplicación exclusiva de **AddRoundKey** con la clave inicial (Ronda 0).
- **Etapa Central (Cíclica)**: Repetida durante $N_r - 1$ rondas en este orden:
1. **SubBytes**: Sustitución no lineal mediante la S-Box.
    2. **ShiftRows**: Permutación o desplazamiento de filas.
    3. **MixColumns**: Mezcla o transformación lineal por columnas mediante multiplicación matricial en el cuerpo Galois $GF(2^8)$.
    4. **AddRoundKey**: Operación XOR con la subclave de la ronda.
- **Etapa Final (No cíclica)**: Ejecuta la última ronda eliminando MixColumns. Consta de 3 operaciones: **SubBytes, ShiftRows y AddRoundKey**.

- **Propiedades de la Operación SubBytes**:
- Sustituye cada byte de la matriz de estado de forma independiente usando una tabla de sustitución no lineal (S-Box).
- **Aporta Confusión**: Es la única operación no lineal dentro del algoritmo AES. No divide datos ni aplica transformaciones lineales.

- **Propiedades Matemáticas de AddRoundKey**:
- Consiste en aplicar una operación XOR ($\oplus$) bit a bit.
- Hacer XOR contra un valor `FF` invierte todos los bits (calcula el **complemento a 1** o NOT bit a bit). No calcula la inversa multiplicativa en el cuerpo Galois $GF(2^8)$.

---

### 4. Funciones Hash (Resumen)

- **Definición y Naturaleza**:
- Algoritmos deterministas unidireccionales que transforman cualquier volumen de datos en una cadena de salida de longitud fija (resumen o *digest*).
- **No son algoritmos de cifrado**: No utilizan claves públicas/privadas ni claves simétricas; por lo tanto, **NO son ni simétricos ni asimétricos**. Poseen resistencia a preimagen, segunda preimagen y colisiones.

- **Ejemplos Estándar**:
- **MD5**: Función resumen que genera resúmenes de 128 bits.
- **SHA-1**: Función resumen que genera resúmenes de 160 bits.
- Ambos son clasificables única y estrictamente como **algoritmos de hashing (funciones resumen)**.

---

### 5. Guía Práctica de Resolución del Cuestionario (Simulaciones Enigma)

- **Propiedad Recíproca / Simetría de Enigma (Cuestionario 1 y 2)**:
- Debido al reflector (UKW), el proceso de cifrado y descifrado en Enigma es **exactamente idéntico**.
- Para descifrar un criptograma y recuperar el mensaje original ("BIENVENIDO A LA GLOBALIZACION"), se debe volver a introducir el texto cifrado utilizando la **misma configuración inicial exacta** (mismos rotores, mismo *ring setting*, mismo *plugboard* y la **misma posición inicial de los rotores**).

- **Orden de Rotores en Simuladores**:
- En la máquina Enigma, la corriente pasa desde el panel frontal (*plugboard*), atraviesa los rotores de derecha a izquierda (Entrada $\rightarrow$ Rotor I $\rightarrow$ Rotor II $\rightarrow$ Rotor IV $\rightarrow$ Reflector UKW-B), rebota en el reflector y regresa de izquierda a derecha.
- Al configurar la máquina con el esquema **UKW-B, IV, II, I**, el primer rotor que gira con cada pulsación de tecla es el rotor situado más a la derecha (Rotor I).