# **3\. Criptografía básica**

## 1. **Definición y Objetivos de la criptografía**

La criptografía dejó de ser un arte empírico para convertirse en una **disciplina científica rigurosa, fundamentada en la teoría de la información, la aritmética modular**, la complejidad algorítmica y el álgebra abstracta

* **Definición de Criptografía:** Conjunto de técnicas que tratan sobre la protección de la confidencialidad e integridad de la información, transformándola en una forma ininteligible para cualquier agente no autorizado


**Objetivos Principales**

* **Protección de la confidencialidad**: Alterar la información para que recuperarla sin la clave adecuada suponga un problema de computación intratable  
* **Preservación de la integridad:** Proporcionar mecanismos (como la firma digital) para detectar alteraciones y certificar el origen del mensaje

## 2. **El principio de Kerckhoffs y la “Seguridad por Oscuridad”**

Confiar en la seguridad a traǘes de la oscuridad (`security through obscurity`) –** creer que un sistema es seguro porque se mantiene en secreto en su algoritmo** – es una premisa falsa y peligrosa. Cualquier persona puede diseñar un algoritmo que no sea capaz de romper ella misma, pero por eso solo demuestra ignorancia sobre sus propias debilidades

>  Principio de Kerckhoffs (1883): La seguridad de un criptosistema no debe depender del secreto del algoritmo, sino únicamente del secreto de la clave. Se debe asumir que el atacante conoce completamente el funcionamiento del sistema; lo único que desconoce es la clave concreta utilizada. 

## 3. **La escalada de los Números en Criptografía**

 La seguridad de los algoritmos modernos se basa en la inmersión de sus espacios de claves:

* **Probabilidad de rayo en un día:** \=1 / 2^33  
* **Probabilidad de acertar la lotería:** \= 1 / 2^24  
* **Edad del Universo:** \= 2^34 años.  
* **Átomos en la Tierra:** \= 2^17  
* **Átomos en el Universo observable:** \= 2^255

Un criptosistema con una clave de **256 bits** `2^256` combinaciones ofrece un espacio de claves mayor que el número de átomos del Universo observable. Esto convierte un ataque por **fuerza bruta** en algo **físicamente imposible** bajo la física clásica.

## **4\. Definición Formal de Criptosistema**

Un criptosistema es una quíntupla **$(M, C, K, E, D)$**:

* **M:** Conjunto de todos los posibles textos claros (mensajes sin cifrar).  
* **C:** Conjunto de todos los criptogramas (mensajes cifrados).  
* **K:** Conjunto de todas las claves posibles.  
* **E:** Conjunto de transformaciones de cifrado (E\_k : M \-\> C).  
* **D:** Conjunto de transformaciones de descifrado (D\_k).

### **Propiedad Fundamental**

Para cualquier mensaje \$m \\in M\$ y clave \$k \\in K\$:

D\_k(E\_k(m)) \= m
> REVISAR FORMULA 


Descifrar un criptograma con la misma clave usada para cifrarlo debe devolver siempre el texto claro original.

## **5\. Tipos de Sistemas Criptográficos**  
**Sistemas Simétricos (Clave Privada):**

* Emplean la **misma clave** para cifrar y descifrar  
* **Ventaja:** Muy rápidos  
* **Inconveniente:** Complejidad en la distribución segura de la clave.  
* **Subtipos:** Cifrados de **bloque** (operan en bloques de tamaño fijo) y cifrados de **flujo** (operan bit a bit o byte a byte)

**Sistemas Asimétricos (Clave Pública):**

* Usan un par de claves: una **clave pública** (k\_P) y una **clave privada** (k\_p). Lo cifrado con una solo se descifra con la otra  
* Resuelven la distribución de claves y permiten la **firma digital**.

**Funciones Resumen (Hash):**

* No son criptosistemas en sentido estricto (no tienen función de descifrado).  
* Generan un resumen de **longitud fija** a partir de un mensaje de cualquier tamaño para verificar la integridad.

## **6\. Criptoanálisis y Compromiso Económico**

* **Criptoanálisis:** Disciplina orientada a descifrar mensajes o recuperar la clave sin conocerla previamente.  
* **Ataque criptográfico:** Técnica que aprovecha las propiedades internas del criptosistema para romperlo de forma más rápida que la fuerza bruta

### **Viabilidad Económica de la Seguridad**

Prácticamente ningún algoritmo es matemáticamente irrompible (a excepción del cifrado de Vernam). Por tanto, la seguridad es un problema **económico y de gestión del riesgo**:

1. **Coste de implantación:** Complejidad computacional (CPU, consumo), almacenamiento y coste económico.  
2. **Vida útil de la información:** Un algoritmo debe mantener la protección durante el tiempo que la información siga siendo valiosa (segundos en una llamada vs. décadas en un historial médico).  
3. **Punto de compromiso:** Un sistema es seguro si romperlo **cuesta más que el valor de la información protegida**.

> *Dado que romper algoritmos modernos es computacionalmente inviable, los atacantes suelen buscar los eslabones débiles: fallos de implementación, claves mal generadas, canales laterales o **fallos humanos**.*

## **7\. Confusión y Difusión (Claude Shannon, 1949\)**

Son las dos propiedades operacionales clave que combina todo criptosistema seguro:

* **Confusión:** Oculta la relación entre el texto claro y el criptograma. Su operación básica es la **sustitución** (reemplazar símbolos).  
* **Difusión:** Diluye la redundancia del texto claro repartiéndola a lo largo de todo el criptograma. Su operación básica es la **transposición** (cambiar de posición los símbolos).

## **8\. Cifrados de Sustitución**

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

## **10\. Máquinas Criptomecánicas**

**Máquina Enigma (Arthur Scherbius, 1923\)**

* **Mecanismo:** Empleaba rotores móviles que giraban tras cada pulsación de tecla, generando una sustitución polialfabética dinámica. Un **reflector** devolvía la señal a través del circuito, permitiendo que la misma configuración sirviera para cifrar y descifrar.  
* **Clavijero (*stecker*):** Intercambiaba pares de letras a la entrada y salida de los rotores, elevando el espacio de claves a \$\\approx 10^17  
* **Ruptura:** La **Bomba de Turing** (basada en desarrollos polacos previos) permitió probar configuraciones en paralelo explotando una debilidad estructural de Enigma: **ninguna letra podía cifrarse en sí misma**.

## **11\. Cifrado de Lorenz y Colossus**

* **Lorenz SZ40:** Sistema electromecánico de 12 ruedas dentadas utilizado por el alto mando alemán para comunicaciones de teletipo de alta seguridad.  
* **Colossus:** Diseñado por Tommy Flowers sobre el método de Bill Tutte para descifrar el tráfico de Lorenz. Es reconocido como el **primer ordenador electrónico programable** de la historia.

### **3.3. Cifrados por Bloques**

Los cifrados simétricos modernos operan sobre **bits** en lugar de caracteres. En lugar de procesar el texto símbolo a símbolo de forma secuencial, dividen la información en **bloques de tamaño fijo** y aplican transformaciones iterativas basadas en las propiedades de **confusión** (sustitución) y **difusión** (permutación) definidas por Claude Shannon

### **1\. Concepto y Estructura**

Construir una tabla de sustitución explícita para un bloque de datos (por ejemplo, de 128 bits) es computacionalmente inviable (2^128) entradas requerirían más soporte físico del que existe en la Tierra). La solución radica en la utilización de **cifrados de producto**.  