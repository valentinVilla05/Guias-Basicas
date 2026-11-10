## Práctica 3: Criptografía Clásica, AES y Herramientas (CrypTool y Criptoclásicos)


### 1. El Algoritmo AES (Advanced Encryption Standard)

- **Definición**: Es el estándar actual de cifrado simétrico por bloques (bloques de tamaño fijo de **128 bits = 16 bytes = 4×4 matriz de estado**, donde cada casilla o elemento contiene **1 byte / 8 bits**).

- **Estructura por Rondas**:
  Dependiendo de la longitud de la clave, AES varía el número de rondas ($N_r$):
  - **128 bits**: 10 rondas.
  - **192 bits**: 12 rondas.
  - **256 bits**: 14 rondas.

- **Fases del Algoritmo**:
  1. **Etapa Inicial (No cíclica)**: Ejecuta únicamente la operación **AddRoundKey** con la subclave inicial (Ronda 0).
  2. **Etapa Central (Cíclica)**: Se repite en bucle $N_r - 1$ veces (rondas 1 a $N_r-1$). Contiene 4 operaciones en este orden exacto:
     - **SubBytes**: Sustitución no lineal de bytes mediante la **S-box** (proporciona la propiedad de confusión). No divide la entrada ni es una transformación lineal.
     - **ShiftRows**: Permutación cíclica de las filas del estado (proporciona difusión a nivel de bytes).
     - **MixColumns**: Mezcla lineal de las columnas del estado mediante multiplicación matricial en el cuerpo de Galois $GF(2^8)$.
     - **AddRoundKey**: Operación XOR bit a bit ($\oplus$) entre el estado y la subclave de la ronda actual.
  3. **Etapa Final (No cíclica)**: Ejecuta la ronda número $N_r$. Es exactamente igual a la ronda central pero **omite MixColumns** (consta solo de **SubBytes, ShiftRows y AddRoundKey**).

- **Comportamiento de AddRoundKey**:
  - Al ser una operación basada en XOR ($\oplus$), hacer una operación con `FF` (todos unos en binario) devuelve el **complemento a 1 (NOT bit a bit)** del byte de entrada (ejemplo: `00` $\oplus$ `FF` = `FF`; `0F` $\oplus$ `FF` = `F0`), nunca la inversa multiplicativa.

---

### 2. Criptosistemas Clásicos: Sustitución vs. Permutación

- **Cifrado de Vigenère**:
  - Es un cifrado **estrictamente simétrico y clásico** basado en **sustitución polialfabética** (aplica desplazamientos por adición modular carácter a carácter mediante una palabra clave que se repite periódicamente).
  - **Diferencia fundamental**: En los cifrados de sustitución los caracteres cambian por otros; en los cifrados de **permutación (o transposición)**, las letras originales no se modifican, únicamente se cambia su posición u orden en el texto.

- **Alfabetos y Cuerpos de Cifra Comunes**:
  - **Castellano Mayúsculas ($Z_{27}$ / MOD 27)**: Contiene solo las 27 letras del abecedario (incluyendo la Ñ). No incluye espacios, números ni signos.
  - **Castellano Mayúsculas y Dígitos ($Z_{37}$ / MOD 37)**: Incorpora las 27 letras más los 10 dígitos numéricos (0-9). **No incluye signos de puntuación ni espacios**.
  - **Inglés Mayúsculas ($Z_{26}$ / MOD 26)** y **Inglés con Dígitos ($Z_{36}$ / MOD 36)**: Versiones sin caracteres extendidos del castellano.
  - **ASCII 191 (MOD 191)**: Subconjunto que abarca desde el código ASCII 32 al 222. Incluye mayúsculas, minúsculas, números, espacios y signos de puntuación imprimibles.

- **Comportamiento con Numéricos y Espacios en Cifrado (Cuestionario 1)**:
  - Al cifrar un poema o texto con números (como "600") o signos en un módulo restringido (como $Z_{27}$), el software elimina o ignora los números y convierte minúsculas a mayúsculas.
  - Al cambiar al modo **ASCII 191**, el algoritmo procesa e incluye en el cifrado los espacios, saltos de línea, mayúsculas/minúsculas y caracteres numéricos, conservando el formato exacto del texto original tras el descifrado.

---

### 3. Criptoanálisis: El Ataque de Kasiski (Cuestionario 2)

- **Fundamento**: Permite averiguar la **longitud de la clave** en un cifrado polialfabético como Vigenère cuando el texto cifrado es lo suficientemente largo.
- **Mecanismo**: Busca patrones o secuencias de n-gramas (cadenas de caracteres) que se repitan en el criptograma y mide las distancias (número de caracteres) entre dichas repeticiones.
- **Uso de Matemáticas**:
  - Se calcula el **MCD (Máximo Común Divisor)** de las distancias entre las repeticiones encontradas. El valor del MCD resultante indica directamente la longitud de la clave (o un múltiplo directo de esta).
  - **El mcm (Mínimo Común Múltiplo) NO se utiliza en el método de Kasiski**.
- **Caso Práctico de la Práctica (El número 600 y el texto recortado)**:
  - **Pérdida del "600"**: Si el texto original contenía "600" y se procesó en alfebeto castellano $Z_{27}$, los dígitos `600` se ignoran o se pierden al descifrar porque los números no forman parte de los 27 caracteres del módulo $Z_{27}$.
  - **Fallo al recortar el texto cifrado**: Al modificar o eliminar parte del texto cifrado (segunda prueba del cuestionario), las repeticiones de patrones se desalinean o desaparecen. Sin suficientes distancias periódicas para calcular el MCD, el análisis de Kasiski **falla y no puede determinar la longitud de la clave**.

---

### 4. Software de Prácticas: CrypTool y Criptoclásicos

- **Criptoclásicos**: Software didáctico desarrollado en Java que permite realizar cifrado, descifrado y criptoanálisis interactivo (desplazamiento, decimación, afín, Gronsfeld, Vigenère, Beaufort, Clave continua, Hill, Playfair, transposición por filas/columnas/vallas/escítala, Vernam binario), soportando **5 alfabetos específicos** (MOD 26, MOD 36, MOD 27, MOD 37 y ASCII 191). Incluye un módulo de herramientas matemáticas para prueba de primalidad, MCD/mcm, inversos modulares y operaciones matriciales.
- **CrypTool**: Plataforma didáctica orientada al estudio interactivo y amplio de la **criptografía en general** (tanto clásica y tradicional como algoritmos modernos y avanzados como AES o RSA, permitiendo analizar frecuencias y estructuras).