## Práctica 4: Criptografía Simétrica de Bloque (AES), Máquina Enigma y Funciones Hash

---

### 1. La Máquina Enigma y su Mecanismo

- **Definición e Historia**:
  - Máquina electromecánica de sustitución polialfabética basada en rotores, ideada por Arthur Scherbius (1918).
  - Adoptada por el ejército alemán para cifrar y descifrar comunicaciones militares durante la Segunda Guerra Mundial.

- **Componentes Principales**:
  - **Rotores (Walzen)**: Discos giratorios con conexiones internas que varían el alfabeto de sustitución en cada pulsación.
    - Su orden en la máquina y su **posición inicial de letras cambiaban diariamente**.
    - Los rotores **NO tienen una posición fija**; la rotación dinámica en cada carácter e intercambio de posición son la base de su complejidad.
  - **Reflector (Umkehrwalze / UKW)**: Reenvía la corriente eléctrica de vuelta a través de los rotores, permitiendo que la máquina sea simétrica (la misma configuración sirve tanto para cifrar como para descifrar).
  - **Panel de Conexiones (*Plugboard* / Steckerbrett)**:
    - Panel frontal de intercambio de letras situadas antes y después del paso por los rotores.
    - Utilizaba hasta **10 cables**, donde **cada cable conectaba un par de letras distinto** (intercambiando 20 letras en total). Un solo cable no puede conectar más de dos letras a la vez.

---

### 2. Criptoanálisis de Enigma y la Máquina "Bombe"

- **Máquina Bombe**:
  - Dispositivo electromecánico desarrollado por criptólogos británicos en Bletchley Park para romper las claves diarias de Enigma.
  - **Método de Operación**: Explotaba fragmentos de texto claro conocido o probable (*cribs*) mediante una **cadena de deducciones lógicas** y eliminación de contradicciones para descubrir la posición inicial de los rotores.
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
  - **Etapa Inicial (No cíclica)**: Aplicación exclusiva de **AddRoundKey** con la clave inicial.
  - **Etapa Central (Cíclica)**: Repetida durante $N_r - 1$ rondas en este orden:
    1. **SubBytes**: Sustitución no lineal mediante la S-Box.
    2. **ShiftRows**: Permutación o desplazamiento de filas.
    3. **MixColumns**: Mezcla o transformación lineal por columnas.
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
  - Algoritmos deterministas unidireccionales que transforman cualquier volumen de datos en una cadena de salida de longitud fija.
  - **No son algoritmos de cifrado**: No utilizan claves públicas/privadas ni claves simétricas; por lo tanto, **NO son ni simétricos ni asimétricos**.

- **Ejemplos Estándar**:
  - **MD5**: Función resumen que genera resúmenes de 128 bits.
  - **SHA-1**: Función resumen que genera resúmenes de 160 bits.
  - Ambos son clasificables única y estrictamente como **algoritmos de hashing (funciones resumen)**.