# **3\. Criptografía básica**

## 1. **Definición y Objetivos de la criptografía**

La criptografía dejó de ser un arte empírico para convertirse en una **disciplina científica rigurosa, fundamentada en la teoría de la información, la aritmética modular**, la complejidad algorítmica y el álgebra abstracta

* **Definición de Criptografía:** Conjunto de técnicas que tratan sobre la protección de la confidencialidad e integridad de la información, transformándola en una forma ininteligible para cualquier agente no autorizado


**Objetivos Principales**

* **Protección de la confidencialidad**: Alterar la información para que recuperarla sin la clave adecuada suponga un problema de computación intratable  
* **Preservación de la integridad:** Proporcionar mecanismos (como la firma digital) para detectar alteraciones y certificar el origen del mensaje

## 2. **El principio de Kerckhoffs y la “Seguridad por Oscuridad”**

Confiar en la seguridad a traǘes de la oscuridad (`security through obscurity`) –**creer que un sistema es seguro porque se mantiene en secreto en su algoritmo – es una premisa falsa y peligrosa**. Cualquier persona puede diseñar un algoritmo que no sea capaz de romper ella misma, pero por eso solo demuestra ignorancia sobre sus propias debilidades

>  Principio de Kerckhoffs (1883): La seguridad de un criptosistema no debe depender del secreto del algoritmo, sino únicamente del secreto de la clave. Se debe asumir que el atacante conoce completamente el funcionamiento del sistema; lo único que desconoce es la clave concreta utilizada. 

## 3. **La escalada de los Números en Criptografía**

 La seguridad de los algoritmos modernos se basa en la inmersión de sus espacios de claves:

* **Probabilidad de rayo en un día:** \=1 / 2^33  
* **Probabilidad de acertar la lotería:** \= 1 / 2^24  
* **Edad del Universo:** \= 2^34 años.  
* **Átomos en la Tierra:** \= 2^17  
* **Átomos en el Universo observable:** \= 2^255

Un criptosistema con una clave de **256 bits** `2^256` combinaciones ofrece un espacio de claves mayor que el número de átomos del Universo observable. Esto convierte un ataque por **fuerza bruta** en algo **físicamente imposible** bajo la física clásica.

## **4. Definición Formal de Criptosistema**

Un criptosistema es una quíntupla **$(M, C, K, E, D)$**:

* **M:** Conjunto de todos los posibles textos claros (mensajes sin cifrar).  
* **C:** Conjunto de todos los criptogramas (mensajes cifrados).  
* **K:** Conjunto de todas las claves posibles.  
* **E:** Conjunto de transformaciones de cifrado ($E_k$ : $M -> C$).  
* **D:** Conjunto de transformaciones de descifrado .

### **Propiedad Fundamental**

Para cualquier mensaje:

> $D_k$($E_k$(m)) = m , ∀m ∈ $M$ , ∀k ∈ $K$ 


Descifrar un criptograma con la misma clave usada para cifrarlo debe devolver siempre el texto claro original.

## **5. Tipos de Sistemas Criptográficos**  
**Sistemas Simétricos (Clave Privada):**

* Emplean la **misma clave** para cifrar y descifrar  
* **Ventaja:** Muy rápidos  
* **Inconveniente:** Complejidad en la distribución segura de la clave.  
* **Subtipos:** Cifrados de **bloque** (operan en bloques de tamaño fijo) y cifrados de **flujo** (operan bit a bit o byte a byte)

**Sistemas Asimétricos (Clave Pública):**

* Usan un par de claves: una **clave pública** ($k_P$) y una **clave privada** ($k_p$). Lo cifrado con una solo se descifra con la otra  
* Resuelven la distribución de claves y permiten la **firma digital**.

**Funciones Resumen (Hash):**

* No son criptosistemas en sentido estricto (no tienen función de descifrado).  
* Generan un resumen de **longitud fija** a partir de un mensaje de cualquier tamaño para verificar la integridad.

## **6. Criptoanálisis y Compromiso Económico**

* **Criptoanálisis:** Disciplina orientada a descifrar mensajes o recuperar la clave sin conocerla previamente.  
* **Ataque criptográfico:** Técnica que aprovecha las propiedades internas del criptosistema para romperlo de forma más rápida que la fuerza bruta

### **Viabilidad Económica de la Seguridad**

Prácticamente ningún algoritmo es matemáticamente irrompible (a excepción del cifrado de Vernam). Por tanto, la seguridad es un problema **económico y de gestión del riesgo**:

1. **Coste de implantación:** Complejidad computacional (CPU, consumo), almacenamiento y coste económico.  
2. **Vida útil de la información:** Un algoritmo debe mantener la protección durante el tiempo que la información siga siendo valiosa (segundos en una llamada vs. décadas en un historial médico)  
3. **Punto de compromiso:** Un sistema es seguro si romperlo **cuesta más que el valor de la información protegida**

> *Dado que romper algoritmos modernos es computacionalmente inviable, los atacantes suelen buscar los eslabones débiles: fallos de implementación, claves mal generadas, canales laterales o **fallos humanos**.*

## **7. Confusión y Difusión (Claude Shannon, 1949)**

Son las dos propiedades operacionales clave que combina todo criptosistema seguro:

* **Confusión:** Oculta la relación entre el texto claro y el criptograma. Su operación básica es la **sustitución** (reemplazar símbolos) 
* **Difusión:** Diluye la redundancia del texto claro repartiéndola a lo largo de todo el criptograma. Su operación básica es la **transposición** (cambiar de posición los símbolos).

## **8. Cifrados de Sustitución**

Sustituyen los caracteres del texto claro por otros símbolos para ocultar su significado.

**Cifrados Monoalfabéticos**

Usan un único alfabeto de sustitución durante todo el mensaje.

* **Tipos:** Cifrado César (desplazamiento fijo), Sustitución Afín (c\_i \= a \* m\_i \+ b(mod n) y Sustitución General (mapeo arbitrario).  
* **Vulnerabilidad:** Mantienen intacta la estructura estadística del idioma (frecuencia de letras, n-gramas y palabras cortas). Un análisis de frecuencias directo permite romperlos rápidamente, demostrando que un espacio de claves grande (26\! \= 2^88 en sustitución general) no garantiza seguridad si las regularidades del texto claro permanecen.

**Cifrados Polialfabéticos**

Varias reglas de sustitución cambian según la posición del símbolo en el texto.

* **Ejemplo emblemático:** Cifrado de Vigenère, que aplica n alfabetos monoalfabéticos de forma cíclica mediante una palabra clave.  
* **Criptoanálisis:** Aunque aplanan la frecuencia global del criptograma, la redundancia del idioma persiste. Mediante el **examen de Kasiski** o el **índice de coincidencia**, se deduce primero la longitud de la clave y luego se descompone el texto en subtextos monoalfabéticos aislados para resolverlos individualmente.

## **9\. Cifrados de Transposición**

Reorganizan las posiciones de los símbolos del texto claro sin alterar los caracteres originales, aplicando así la propiedad de **difusión**.

* **Ejemplo histórico:** La escítala espartana.  
* **Permutación por columnas:** El mensaje se escribe por filas en una rejilla de \$N\$ columnas y se lee en el orden dictado por una clave de permutación.  
* **Propiedad estadística:** Conservan la frecuencia exacta de las letras del texto claro (fácilmente identificable mediante análisis estadístico), por lo que su seguridad depende del tamaño de bloque y de la complejidad de la regla de permutación.

## **10. Máquinas Criptomecánicas**

**Máquina Enigma (Arthur Scherbius, 1923)**

* **Mecanismo:** Empleaba rotores móviles que giraban tras cada pulsación de tecla, generando una sustitución polialfabética dinámica. Un **reflector** devolvía la señal a través del circuito, permitiendo que la misma configuración sirviera para cifrar y descifrar.  
* **Clavijero (*stecker*):** Intercambiaba pares de letras a la entrada y salida de los rotores, elevando el espacio de claves a $=$ 10^17  
* **Ruptura:** La **Bomba de Turing** (basada en desarrollos polacos previos) permitió probar configuraciones en paralelo explotando una debilidad estructural de Enigma: **ninguna letra podía cifrarse en sí misma**.

## **11. Cifrado de Lorenz y Colossus**

* **Lorenz SZ40:** Sistema electromecánico de 12 ruedas dentadas utilizado por el alto mando alemán para comunicaciones de teletipo de alta seguridad.  
* **Colossus:** Diseñado por Tommy Flowers sobre el método de Bill Tutte para descifrar el tráfico de Lorenz. Es reconocido como el **primer ordenador electrónico programable** de la historia.

### **3.3. Cifrados por Bloques**

Los cifrados simétricos modernos operan sobre **bits** en lugar de caracteres. En lugar de procesar el texto símbolo a símbolo de forma secuencial, dividen la información en **bloques de tamaño fijo** y aplican transformaciones iterativas basadas en las propiedades de **confusión** (sustitución) y **difusión** (permutación) definidas por Claude Shannon

### **1. Concepto y Estructura**

Los **algoritmos de cifrado por bloques** dividen el mensaje en fragmentos de tamaño fijo y los cifran uno a uno

* **El problema de la sustitución pura**: Una tabla de sustitución explícita para un bloque de 128 bits requerirá de 2^218 entradas. Guardar una tabla de este tañano es imposible

* **La solución (Cifrado de Producto)**: Construir una sustitución de forma **implícita** aplicando iterativamente operaciones sencillas mediante la combinación de **Sustitución y Permutación**

**Conceptos clave de Claude Shannon**
* **Confusión**: Oculta la relación entre la clave y el criptograma (por sustituciones)
* **Difusión**: Reparte la influencia de cada bit de entrada por todo el bloque (por permutaciones)

## Estructuras Principales:
**1. Red de Sustitución-Permutación (SPN)**: Aplica en cada ronda capas de sustitución (S-Cajas),mezcla lineal (permutación) y adición de subclave : EJ `AES`

**2. Red Feistel**: Divide el bloque en dos mitades y las procesa alternativamente. Su gran ventaja es que **el cifrado y el descifrado son idénticos** (solo cambia el orden de las subclaves): EJ: `DES`

> Ninguna ronda individual es seguroa por sí sola. La seguridad emerge de la acumulación de Rondas

**Compontentes Internos**:
* **Rondas y Subclaves**: Los algoritmos operan de forma iterativa. En cada ronda se utiliza una subclave distinta -> *Key Schedule*

* **S-Cajas (Substitution Boxes)**: Es la unidad básica de sustitución para aportar confusión no linea

* **No biyectivas (m $>$ n o m $!=$ n). Reducen bits y no son invertibles por sí solas. Son válidas en estructuras como las redes de Feistel (ej. DES)

* **Biyectivas ($m = n$)**: Deben ser obligatoriamente invertibles para poder descifrar. Son necesarias en redes SPN (ej. AES utiliza S-Cajas de $8 \times 8$ bits

### Algoritmos Principales: DES y AES
| Caracteristica | DES (Data Encryption Standard) | AES (Advanced Encryption Standard) | 
| -- | -- | -- |
| **Año / Adopción** | 1976 | 2001 | 
| **tamaño de bloque** | 64 bits | 128 bits | 
| **Tamaño de clave** | 56 bits efectivos ( 64 bits nominales y 8 de prioridad ) | Variable : 128,192 o 256 bits | 
| **Estructura** | Red de Feistel (16 rondas)| Red SPN (10,12 o 14 rondas según la clave) | 
| **Estado Actual** | **Obsoleto/Inseguro** (vulnerable a fuerza bruta por clave corta). Su parche fue **3DES** | Estandar actual y completamente seguro | 


## 3. Modos de Operación
Estrategias para cifrar mensajes que ocupan más de un bloque (aplicando *padding* si el último no esá completo)

> ¿Qué es Padding? : 

### A. Modo ECB (Electronic Code Book)
* **Funcionamiento:** Cada bloque se cifra de forma totalmente independiente ($C_i = E_K(M_i)$).

* **Problema:** Dos bloques con el mismo texto plano producen criptogramas idénticos. Esto revela patrones de datos 

* **Uso:** Desaconsejado e inseguro para casi cualquier propósito

### B. Modo CBC (Cipher Block Chaining)
* **Funcionamiento:** Cada bloque de texto claro se combina mediante una operación XOR con el criptograma del bloque anterior antes de cifrarse. El primer bloque usa un Vector de Inicialización (VI)

**Propiedades:**

* Impide la reordenación o sustitución de bloques

    * Un error en el descifrado solo afecta al bloque actual y al siguiente

    * Cifrado secuencial (no paralelizable), descifrado paralelizable

* **Atención:** El VI no necesita ser secreto, pero debe ser impredecible y único para cada mensaje

### C. Modo CFB (Cipher Feedback)
* **Funcionamiento:** Se cifra el criptograma anterior y el resultado se combina (`XOR`) con el texto claro actual

* **Propiedades:** 
    * Convierte el cifrado por bloques en un cifrado de flujo.
    * No necesita *padding*, permitiendo cifrar datos en unidades pequeñas (bytes o bits) a medida que llegan
    * Ideal para comunicaciones interactivas de baja latencia (ej. terminales remotos)
* **Solo utiliza la función de cifrado** $E_K$ (nunca se aplica la función de descifrado $D_K$)

## 4. Cifrados de Flujo
En lugar de procesar el mensaje por bloques, se genera una secuencia pseudoaleatoria (*keystream*) tan larga como el mensaje y se combina bit a bit mediante la operación `XOR`: $c = m \oplus o$

**El caso ideal: Criptosistema Seguro de Shannon (One-Time Pad/Vernam)**

* Es el único sistema **matemáticamente irrompible** demostrado

* **Requisitos (imprácticos en el mundo real)**: La clave debe ser tan larga como el mensaje, totalmente aleatoria y **usarse una sola vez**

### **Cifrados de Flujo Prácticos**
* Utilizan una **semilla** (clave corta) para generar una secuencia pseudoaleatoria criptográficamente segura

* Toda la seguridad depende de la caliidad matemática del generador

### **Algortimos Destacados**
* **RC4 (1987)**: Diseñado por Ron Rivers, usa una S-Caja dinamica de 8x8. Se usó históricamente pero **hoy está obsoleto** por segos estadísticos en su secuencia

* **ChaCha20**: Diseñado por Daniel Bernstein en 2008, es un generador de secuencia pseudoaleatoria moderno muy eficiente

    * **Características**: Utiliza una clave de 256 bits y un **nonce de 64 bits** (núm de un solo uso) para cifrar de forma segura múltiples mensajes con la misma clave

    * **Paralelismo y Acceso Aleatorio**: Genera bloques de secuencia independientes mediante un índice de 64 bits

    * **Uso**: es una alternativa de referencia a AES-CTR especialmente en dispositivos o procesadores que carecen de aceleración por hardware para AES

**Generación de Secuencias mediante Cifrados por Bloques**
Los cifrados por bloques se pueden transofmrar en cifrados de flujo aplicando modos de especificación

**A. Modo OFB (Output Feedback)**

* **Mecanismo:** La secuencia cifrante **($o_i$)** se obtiene reincorporando iterativamente la salida del cifrado del bloque anterior: **$o_i = E_K(o_{i-1})$**, partiendo de un Vector de Inicialización **($o_0 = VI$)**. El criptograma final se genera mediante **$C_i = M_i \oplus o_i$**

* **Diferencia con CFB:** La secuencia depende únicamente de la clave y del VI, no del mensaje

* **Ventajas:** Permite precalcular la secuencia cifrante antes de recibir el mensaje y evita la propagación de errores en la transmisió

**B. Modo CTR (Counter Mode)**
* **Mecanismo:** Cada bloque de la secuencia se calcula cifrando la concatenación de un nonce y un contador que se incrementa en cada bloque: **$o_i = E_K(\text{nonce} \parallel i)$**

* **Ventajas principales:**

    * **Paralelizable:** Los bloques no dependen entre sí, permitiendo procesar múltiples bloques en paralelo

    * **Acceso Aleatorio:** Permite descifrar un bloque específico directamente (ideal para discos y bases de datos)
    
    * **Precálculo:** La secuencia cifrante puede calcularse con antelación
    
* **AES-GCM:** La combinación del modo `CTR` con `GMAC` (Galois Message Authentication Code) ofrece cifrado y autenticación simultáneos (Cifrado Autenticado / AEAD), siendo el estándar más recomendado en la actualidad

## 5. Funciones Resumen (Hash)
Las funciones resumen garantizan la **integridad** de los datos (detectan modificaciones no autorizadas). Transforman mensajes de longitud arbitraria en una huella digital (hash) de **longitud fija**. Son irreversibles


* **Clasificación**
* **MDC (Modification Detection Code)**: Sin clave Secreta ($K =0$). Verificacn únicamente la integridad del mensaje

* **MAC (Message Authentication Code)**: Emplean una clave dsecreta para verificar tanto la **integridad** como el **origen/autenticidad** del mensaje

**Propiedades de una Función Resumen Segura**
**1. Longitud Fija**: Mismo tamaño de salida independientemente del tamaño de entrada

**2. Eficiencia**: Cálculo computacional rápido

**3. Resistencia a Preimagen**: Dadho $h$, debe ser inviable hallar $m$ tal que $r(m) = h$ (no se puede invertir)

**4. Resistencia a Segunda preimagen**: Dado $m$, debe ser inviable hallar otro $m' != m$ con el mismo hash $(r(m')=r(m))

**5. Resistencia a Colisiones**: Debe ser inviable encontrar **cualquier par arbitrario** (m,m') tal que $r(m)=r(m')$

**Estructura de las Funciones MDC**

**Construcción Merkle-Damgard**
Aplicar iterativamente una función de compresión $R$
> $$r_{i+1} = R(m_i, r_i)$$

El mensaje se divide en bloques $m_i$ y se combina iterativamente con el estado anterior $r_i$ (partiendo de un Vector de Inicialización $r_0$)
* **Pérdida de información:** Es intrínseca al reducir datos arbitrarios a un tamaño fijo

* **Limitación:** Es estrictamente secuencial y vulnerable a *ataques de extensión de longitud* si se intenta usar como MAC simple

#### Algoritmos Hash Principales

| Algoritmo | Tamaño de Hash | Estado / Seguridad | 
| -- | -- | -- | 
| **MD5** | 128 bits | **Roto/Obsoleto**: Vulnerable a ataques de colisión eficientes | 
| **SHA-1** | 160 bits | **Roto/Obsoleto**: Colisiones demostradas en la práctica | 
| **Familia SHA-2** | 256 o 512 bits | **Seguro y ampliamente utilizado**: Basado en Merkle-Damgard | 
| **SHA-3(Keccak)** | Variable | **Seguro**. Basado en **Estructura de Esponja** (fase de absorción de datos y fase de exprimido del hash) | 

**Seguridad y Colisiones**
Requiere una clave secreta para impedir que un atacante genere resúmenes válidos

**1.CBC-MAC:** Utiliza un cifrado por bloques en modo CBC y toma como MAC únicamente el último bloque de criptograma

**2.HMAC (Hash-based MAC):** Combina una función MDC con una clave secreta mediante constantes de relleno (ipad y opad):

> $$\text{HMAC}(k, m) = \text{MDC}(k \oplus \text{opad}, \text{MDC}(k \oplus \text{ipad}, m))$$

Es el estándar más extendido 

**3. MAC de cifrados de flujo**: Basados en generadores pseudoaleatorios combinados con clave

## 6. Criptografía Asimétrica (Clave Pública)

Introducida por Whitfield Diffie y Martin Hellman en 1976. Resuelve los dos grandes problemas de la criptografía simétrica:

**1. Distribución de claves:** Elimina la necesidad de intercambiar claves secretas por un canal seguro previo

**2. Escalabilidad:** Evita el crecimiento exponencial de claves en la red ($n(n-1)/2$)

### **Funcionamiento**
Utiliza un **par de claves matemáticamente vinculadas**:
* **Clave Pública ($k_P$)**: Se comparte abiertamente con todo el mundo
* **Clave Privada ($k_p$)**: La conserva únicamente su propietario en secreto

> Regra fundamental: Lo que se cifra con una clave del par **solo se puede descifrar con la otra**

### Inconvenientes respecto a la Criptografía Simétrica:
* **Claves mucho más largas:** Necesita claves mayores (ej. RSA de 2048/4096 bits frente a AES de 128/256 bits)

* **Rendimiento más lento:** Requiere operaciones matemáticas complejas

> **Solución (Cifrado Híbrido)**: Se usa criptografía asimétrica para intercambiar de forma segura una clave simétrica efímera, y luego esta clave simétrica rápida se utiliza para cifrar el volumen real del mensaje

### Aplicaciones Según el Uso de las Claves
**1. Cifrado Tradicional (Confidencialidad):** 
* El emisor cifra con la clave pública del destinatario ($c = E_{k_P}(m)$)
* Solo el destinatario puede descifrar con su clave privada ($m = D_{k_p}(c)$)

**2. Firma Digital (Autenticación y No Repudio):**
* El emisor cifra (o firma) con su propia clave privada

* Cualquier receptor puede verificar el mensaje usando la clave pública del emisor, demostrando la identidad del autor

Para firmar un mensaje $m$, el emisor calcula un resumen $r(m)$ y lo cifra utilizando su **clave privada** ($k_p$). Cualquier receptor puede verificar la firma empleando la **clave pública** del emisor ($k_P$)

> $$s = E_{k_p}(r(m)), \quad \text{válida} \iff D_{k_P}(s) = r(m')$$

* **Puntos clave de la firma digital:**
**1. El mensaje viaja en claro:** La firma digital no proporciona confidencialidad (para ello hay que combinar firma y cifrado)

**2. Se firma el resumen, no el mensaje:** Cifrar un documento extenso con algoritmos asimétricos es muy lento. Al firmar el hash (de tamaño fijo), el coste es constante

**3. Uso invertido de claves:** Cifrar para confidencialidad usa la clave pública del destino; firmar usa la clave privada del emisor

**4. No repudio:** Dado que solo el poseedor de $k_p$ pudo haber generado $s$, el emisor no puede negar haber firmado el mensaje

### Ataques de Intermediario (*Man-in-the-Middle / MitM*)
Ocurren cuando un atacante $C$ intercepta el intercambio de claves públicas entre $A$ y $B$, entregando su propia clave pública $K_C$ en lugar de la legítima

* **El verdadero fallo:** No rompe la matemática de los algoritmos (como RSA), sino el supuesto implícito de que la clave pública pertenece a quien dice ser

* **Solución (Certificados Digitales y PKI):** Para garantizar la autenticidad de las claves públicas se emplean Certificados Digitales, respaldados por una Autoridad de Certificación (CA) dentro de una Infraestructura de Clave Pública (PKI)

### Problemas Matemáticos Difíciles
La seguridad asimétrica se basa en operaciones complejas de resolver en sentido inverso:

**1. Logaritmo Discreto:** Dados $a, b, n$, es computacionalmente intratable hallar $c$ tal que $a \equiv b^c \pmod n$

**2. Factorización de Enteros:** Es trivial multiplicar dos primos grandes $p \cdot q = n$, pero extremadamente difícil hallar $p$ y $q$ a partir de $n$

### Algoritmos Asimétricos Clásicos
* **Diffie-Hellman (DH):** Permite acordar un secreto compartido $K = \alpha^{xy} \pmod p$ sobre un canal inseguro mediante el problema del logaritmo discreto.
> Atención: En su versión básica no autentica a los participantes, siendo vulnerable a ataques MitM si no se combina con certificados o firmas

* **RSA:** Basado en la dificultad de factorizar $n = p \cdot q$ y en el problema del logaritmo discreto
    * Clave pública: $(e, n)$ | Clave privada: $(d, n)$
    * Cifrado: $c = m^e \pmod n$
    * Descifrado: $m = c^d \pmod n$
    
* **Criptografía de Curva Elíptica (ECC):**  Reformula la criptografía asimétrica sobre grupos de puntos de curvas elípticas (ECDLP)
    * **Ventaja:** Permite claves mucho más pequeñas con la misma seguridad (ej. una clave ECC de 256 bits equivale a una RSA de 3072 bits). Usado en TLS 1.3, SSH y criptomonedas (ECDH, ECDSA)

## 7. Criptografía Poscuántica
**La Amenaza Cuántica y el Algoritmo de Shor**

Los algoritmos asimétricos clásicos (RSA, DH, ECC) colapsarán cuando existan ordenadores cuánticos lo suficientemente potentes:

* **Algoritmo de Shor (1994):** Resuelve la factorización de enteros y el logaritmo discreto en tiempo polinómico, rompiendo completamente la criptografía asimétrica sin importar la longitud de la clave

* **Algoritmo de Grover (1996):** Afecta a la criptografía simétrica reduciendo a la mitad la seguridad efectiva por fuerza bruta. Solución simple: Duplicar el tamaño de la clave simétrica (ej. usar AES-256 da 128 bits de seguridad cuántica efectiva, lo cual es totalmente seguro)

>  **Ataque "Cosechar ahora, descifrar después" (Harvest Now, Decrypt Later - HNDL):** Un adversario puede guardar tráfico cifrado hoy para descifrarlo en 10 o 20 años cuando disponga de un ordenador cuántico. Por ello, la migración es urgente para datos de larga vida útil

**Familias de Problemas Poscuánticos**

A diferencia de la *criptografía cuántica* (que requiere hardware especial como QKD), **la criptografía poscuántica** se ejecuta en ordenadores convencionales usando problemas matemáticos no vulnerables a Shor:

**1. Retículas (Lattices):** Problemas como MLWE y MSIS (vectores cortos en estructuras algebraicas). Es la base de la mayoría de los estándares actuales

**2. Basada en Funciones Hash:** Se apoya únicamente en las propiedades de resistencia de las funciones hash

**3. Códigos Correctores de Errores:** Basada en decodificación de códigos lineales aleatorios (ej. McEliece)

### Estándares del NIST
| Estándar | Nombre / Algoritmo Base | Función | Problema Matemático | Observaciones | 
| -- | -- | -- | -- | -- |
| **FIPS 203** | **ML-KEM** (Crystals-kyber) | Intercambio de claves | Retículas (MLWE) | Sustituye a RSA / ECDH. Rápido y de claves compactas | 
| **FIPS 204** | **ML-DSA** (Crystals-Dilithium)  | Firma Digital | Retículas (MLWE/MSIS) | Estándar principal para sustituir RSA, ECDSA y EdDSA | 
| **FIPS 205** | **SLH-DSA** | Firma Digital | Funciones Hash | ALgoritmo de respaldo (firmas más grandes y lentas pero muy seguros) |

### Desafíos de la Transición Organizativa

**1. Inventario Criptográfico:** Identificar todos los sistemas y protocolos que usan criptografía asimétrica

**2. Compatibilidad:** Los nuevos algoritmos manejan claves y firmas significativamente más grandes (ej. firma ML-DSA-65 de 3309 bytes frente a 256 bytes en ECDSA)

**3. Enfoque Híbrido:** Durante la transición se combinan algoritmos clásicos y poscuánticos simultáneamente (ej. `X25519 + ML-KEM-768` en TLS 1.3) para evitar vulnerabilidades si uno falla

**4. Agilidad Criptográfica:** Diseñar sistemas modulares capaces de cambiar de algoritmo sin necesidad de rediseñar la infraestructura completa