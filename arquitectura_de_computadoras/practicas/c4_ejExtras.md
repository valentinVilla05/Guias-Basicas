# Ejercicios similares a los que ha dicho Juan Francisco en clase

> Es muy recomendable hacerlos ya que ha dicho que si o si caerá algún ejercicio similar

---

# Ejercicio 1 – 2/10 puntos - Archivos Eje1.s y P3.pdf
Escribe un programa en ensamblador RISC-V ajustado a las siguientes directivas:

En el segmento de datos se tiene un vector de números enteros de 32 bits con signo:

$$\text{vector} = [12, -7, 45, 18, 9, -2, 3, 14, 21, -5]$$

El programa deberá:

* Recorrer el vector e identificar los números impares.

* Contar cuántos números impares hay en total.

* Calcular la suma total de dichos números impares.

* Almacenar ambos resultados (el conteo y la suma) en espacios reservados en el segmento de datos, como enteros de 32 bits.

Crea un documento y adjunta una captura de pantalla del panel Memory de Ripes tras haber ejecutado el programa completo, en la que se aprecie el código ensamblador y la zona de memoria donde se han guardado el conteo y la suma.

# Ejercicio 2 – 4/10 puntos - Archivo P3.pdf
Ejecuta el programa del Ejercicio 1 sobre las siguientes configuraciones de procesador en Ripes:

* **Configuración 1 (C1):** Single-cycle processor

* **Configuración 2 (C2):** 5-Stage processor w/o Forwarding unit

* **Configuración 3 (C3):** 5-Stage processor

Realiza los siguientes apartados:

1. Anota para cada configuración el número total de ciclos de reloj y el CPI obtenido tras finalizar la ejecución

2. Incluye una tabla comparativa con los ciclos, el CPI y el Speedup de C2 y C3 tomando como base C1

3. Explica brevemente la fórmula empleada para calcular el Speedup

4. Adjunta las capturas de pantalla de Ripes de cada configuración

# Ejercicio 3 – 4/10 puntos - Riesgos de control y reordenación de código
Tomando como base el programa del Ejercicio 1:

1. Analiza los riesgos de datos (load-use) y de control (saltos) que provocan paradas (burbujas) en el procesador de 5 etapas

2. Aplica desenrollamiento de bucle (2 elementos por iteración) y reordena las instrucciones para reducir las paradas

3. Muestra el código ensamblador y explica qué dependencias se han resuelto o intercalado

4. Vuelve a ejecutar el código en C3 y compara el nuevo número de ciclos y CPI con los del Ejercicio 2

# Resolución
## EJ 1
![alt text](../images/cap4ej1.png)

## EJ 2
| Configuración del Procesador | Ciclos Totales | Instrucciones | CPI | Speedup vs. C1 |
|---|---:|---:|---:|---:|
| C1: Single-cycle | 99 | 99 | 1.00 | 1.00× (Base) |
| C2: 5-Stage w/o Forwarding | 167 | 99 | 1.69 | 0.59× ($\frac{99}{167}$) |
| C3: 5-Stage w/ Forwarding | 151 | 99 | 1.53 | 0.66× ($\frac{99}{151}$) |

**Fórmula del Speedup**

$$\text{Speedup}_{Cx} = \frac{\text{Ciclos}_{C1}}{\text{Ciclos}_{Cx}}$$

Se compara el número de ciclos de C1 (base) entre el de cada configuración, ya que el programa es el mismo. Un valor menor que 1 indica que necesita más ciclos que el monociclo. Esto se debe a que los procesadores segmentados añaden ciclos de llenado del cauce y burbujas, aunque su ciclo de reloj es mucho más corto que el del monociclo.

## EJ 3

**1. Análisis de riesgos del bucle original (C3: 5-Stage)**

* **Riesgo de datos (load-use):** `andi t3,t2,1` usa `t2` justo después del `lw t2,0(t0)`. Aunque haya forwarding, el dato no está disponible hasta terminar la etapa MEM, así que se pierde 1 ciclo (burbuja) por elemento: **10 burbujas** en total. Sin forwarding (C2) la espera es mayor.
* **Riesgo de control:** los saltos se resuelven en la etapa EX, por lo que cada salto tomado obliga a descartar las instrucciones ya captadas detrás de él. En el bucle original se toman **17 saltos**: 10 `j bucle`, 6 `bnez t3,impar` (uno por cada impar) y el `beqz t1,fin` final.

**2. Código desenrollado (2 elementos por iteración) y reordenado**

```asm
.data
vector: .word 12, -7, 45, 18, 9, -2, 3, 14, 21, -5
num_impares: .word 0
suma_impares: .word 0

.text
la t0,vector
li t1,10
li a2,0 # contador impares
li a0,0 # suma impares
la a3,num_impares
la a4,suma_impares

bucle:
    beqz t1,fin
    lw t2,0(t0)   # cargamos el primer valor
    lw t4,4(t0)   # cargamos el segundo valor
    addi t0,t0,8  # avanzamos el vector
    addi t1,t1,-2 # disminuimos el núm de elementos restantes

    andi t3,t2,1  # comprobamos primer elemento (t2)
    beqz t3, par  # si t2 es par, pasamos a mirar el segundo

    # Si t2 es impar:
    add a2,a2,t3
    add a0,a0,t2

par:
    andi t5,t4,1  # comprobamos segundo elemento (t4)
    beqz t5,bucle # si t4 es par, volvemos al bucle

    # Si t4 es impar:
    add a2,a2,t5
    add a0,a0,t4

    j bucle

fin:
    li a7,1
    sw a0,0(a4)
    sw a2,0(a3)
    ecall
    mv a0,a2
    ecall
```

**3. Dependencias resueltas e intercaladas**

* **Load-use eliminado:** los dos `lw` van juntos al principio y los dos `addi` se colocan entre las cargas y el primer `andi`. Así, cuando `andi t3,t2,1` necesita `t2`, ya han pasado 3 instrucciones desde su `lw`, y lo mismo ocurre con `t4`. Las **10 burbujas load-use pasan a 0**.
* **Menos sobrecarga de control:** el `beqz t1,fin`, el `j bucle` y los dos `addi` de avance se ejecutan 5 veces en lugar de 10. Los saltos tomados bajan de **17 a 7**.
* **Riesgo que se mantiene:** `andi t3` → `beqz t3` es una dependencia RAW pegada. Con forwarding (C3) no para, pero sin él (C2) sí.

**4. Comparativa en C3**
| Versión del código (C3: 5-Stage) | Ciclos Totales | CPI | Speedup vs. C3 original |
|---|---:|---:|---:|
| Código Ejercicio 1 (sin desenrollar) | 151 | 1.53 | 1.00× (Base) |
| Código Ejercicio 3 (desenrollado 2x y reordenado) | 95 | 1.27 | 1.59× |

$$\text{Speedup} = \frac{\text{Ciclos}_{\text{original}}}{\text{Ciclos}_{\text{desenrollado}}} = \frac{151}{95} \approx 1.59\times$$

---

# Ejercicio 1 – 2/10 puntos - Archivos Eje1.s y P3.pdf
Escribe un programa en ensamblador RISC-V ajustado a las siguientes directivas: En el segmento de datos se define un vector de números enteros de 32 bits con signo:

$$\text{vector} = [15, -42, 8, -100, 55, 0, -7, 33, -12, 90]$$

El programa deberá:

1. Recorrer el vector e invertir todos los bits de cada número (obtener el Complemento a Uno de cada elemento)

2. Contar cuántos números resultantes son negativos (tienen su bit de signo en 1)

3. Calcular la suma total de todos los números tras aplicar la inversión de bits

4. Almacenar ambos resultados en memoria (`num_negativos` y `suma_inversos`) en dos posiciones consecutivas del segmento de datos como enteros de 32 bits

# Ejercicio 2 – 4/10 puntos - Archivo P3.pdf
Ejecuta el programa del Ejercicio 1 sobre las siguientes configuraciones de procesador en Ripes:

* **Configuración 1 (C1):** Single-cycle processor

* **Configuración 2 (C2):** 5-Stage processor w/o Forwarding unit

* **Configuración 3 (C3):** 5-Stage processor

Realiza los siguientes apartados:

1. Anota para cada configuración el número total de ciclos de reloj y el CPI obtenido tras finalizar la ejecución

2. Incluye una tabla comparativa con los ciclos, el CPI y el Speedup de C2 y C3 tomando como base C1

3. Explica brevemente la fórmula empleada para calcular el Speedup

4. Adjunta las capturas de pantalla de Ripes de cada configuración

# Ejercicio 3 – 4/10 puntos - Riesgos de control y reordenación de código
Tomando como base el programa del Ejercicio 1:

1. Analiza las paradas por dependencias de datos Load-Use entre la lectura del vector `lw` y la instrucción de inversión `xori`, además de los saltos condicionales

2. Aplica desenrollamiento de bucle (2 elementos por iteración) y reordena las instrucciones para reducir las paradas

3. Muestra el código ensamblador y explica qué dependencias se han resuelto o intercalado

4. Vuelve a ejecutar el código en C3 y compara el nuevo número de ciclos y CPI con los del Ejercicio 2

# Resolución
## EJ 1
![alt text](../images/ej1ap1cap4.png)

## EJ 2
| Configuración del Procesador | Ciclos Totales | CPI | Speedup vs. C1 |
|---|---:|---:|---:|
| C1: Single-cycle | 103 | 1.00 | 1.00× (Base) |
| C2: 5-Stage w/o Forwarding | 187 | 1.82 | 0.55× ($\frac{103}{187}$) |
| C3: 5-Stage w/ Forwarding | 151 | 1.47 | 0.68× ($\frac{103}{151}$) |

**Fórmula del Speedup**

$$\text{Speedup}_{Cx} = \frac{\text{Ciclos}_{C1}}{\text{Ciclos}_{Cx}}$$

Se compara el número de ciclos de C1 (base) entre el de cada configuración, ya que el programa es el mismo. Un valor menor que 1 indica que necesita más ciclos que el monociclo. Esto se debe a que los procesadores segmentados añaden ciclos de llenado del cauce y burbujas, aunque su ciclo de reloj es mucho más corto que el del monociclo.

## EJ 3


**1. Análisis de riesgos del bucle original (C3: 5-Stage)**

* **Riesgo de datos (load-use):** `xori t3,t2,-1` usa `t2` justo después de `lw t2,0(t0)`, por lo que se pierde 1 ciclo (burbuja) por elemento: **10 burbujas** en total.
* **Riesgo de control:** los saltos se resuelven en la etapa EX, así que cada salto tomado obliga a descartar las instrucciones captadas detrás. Hay **15 saltos tomados**: 10 `j bucle`, 4 `bgez t3,positivo` (uno por cada número cuyo resultado es positivo) y el `beqz t1,fin` final. Además, `bgez` depende de `xori` justo antes, lo que sin forwarding (C2) genera más paradas.

**2. Código desenrollado (2 elementos por iteración) y reordenado**

```asm
.data
vector:         .word 15, -42, 8, -100, 55, 0, -7, 33, -12, 90
num_negativos:  .word 0
suma_inversos:  .word 0

.text
la t0, vector
li t1, 10
li a1, 0              # Conteo negativos
li a0, 0              # Suma invertidos
la a2, num_negativos
la a3, suma_inversos

bucle:
    beqz t1, fin
    lw t2, 0(t0)      # cargamos el primer valor
    lw t4, 4(t0)      # cargamos el segundo valor
    addi t0, t0, 8    # avanzamos el vector
    addi t1, t1, -2   # disminuimos el núm de elementos restantes

    xori t3, t2, -1   # Inversión de bits (NOT) del primero
    xori t5, t4, -1   # Inversión de bits (NOT) del segundo

    add a0, a0, t3    # sumamos el primero invertido
    add a0, a0, t5    # sumamos el segundo invertido

    srli t6, t3, 31   # bit de signo del primero (1 si negativo)
    add a1, a1, t6
    srli t6, t5, 31   # bit de signo del segundo (1 si negativo)
    add a1, a1, t6

    j bucle

fin:
    sw a0, 0(a3)
    sw a1, 0(a2)

    li a7, 1
    ecall
```

**3. Dependencias resueltas e intercaladas**

* **Load-use eliminado:** los dos `lw` van seguidos y los dos `addi` se colocan antes de los `xori`. Así, cada `xori` queda a 2 o más instrucciones de su `lw` y no hay burbuja. Las **10 burbujas load-use pasan a 0**.
* **Saltos condicionales eliminados:** el `bgez` se sustituye por `srli t6, t3, 31`, que extrae el bit de signo (1 si es negativo) y se suma a `a1`. Desaparecen los 4 saltos tomados del `bgez`, y con ellos su penalización por riesgo de control.
* **Menos sobrecarga de bucle:** el `beqz t1,fin`, el `j bucle` y los `addi` de avance se ejecutan 5 veces en lugar de 10. Los saltos tomados bajan de **15 a 6**.

**4. Comparativa en C3**

| Versión del código (C3: 5-Stage) | Ciclos Totales | CPI | Speedup vs. C3 original |
|---|---:|---:|---:|
| Código Ejercicio 1 (sin desenrollar) | 151 | 1.47 | 1.00× (Base) |
| Código Ejercicio 3 (desenrollado 2x y reordenado) | 102 | 1.21 | 1.48× |

$$\text{Speedup} = \frac{\text{Ciclos}_{\text{original}}}{\text{Ciclos}_{\text{desenrollado}}} = \frac{151}{102} \approx 1.48\times$$

---

# Ejercicio 1 – 2/10 puntos - Archivos Eje1.s y P3.pdf

Escribe un programa en ensamblador RISC-V ajustado a las siguientes directivas: En el segmento de datos se define un vector de números enteros de 32 bits en formato binario:

$$\text{vector} = [0\text{b1111}, 0\text{b0011}, 0\text{b0101}, 0\text{b0001}, 0\text{b0000}]$$

El programa deberá:

1. Recorrer el vector analizando sus elementos bit a bit mediante desplazamientos lógicos a la derecha (`srli`) y la extracción del bit menos significativo mediante una máscara lógica (`andi`)

2. Para cada elemento, **contar cuántos bits están a '1' (Popcount)** sumando directamente el bit extraído al contador sin utilizar saltos condicionales para el conteo (branchless)

3. Calcular el **recuento total de bits a '1'** de todo el vector

4. Almacenar el resultado en memoria en la variable `total_unos` como un entero de 32 bits

# Ejercicio 2 – 4/10 puntos - Archivo P3.pdf
Ejecuta el programa del Ejercicio 1 sobre las siguientes configuraciones de procesador en Ripes:

* **Configuración 1 (C1):** Single-cycle processor

* **Configuración 2 (C2):** 5-Stage processor w/o Forwarding unit

* **Configuración 3 (C3):** 5-Stage processor

Realiza los siguientes apartados:

1. Anota para cada configuración el número total de ciclos de reloj y el CPI obtenido tras finalizar la ejecución

2. Incluye una tabla comparativa con los ciclos, el CPI y el Speedup de C2 y C3 tomando como base C1

3. Explica brevemente la fórmula empleada para calcular el Speedup

4. Adjunta las capturas de pantalla de Ripes de cada configuración

# Ejercicio 3 – 4/10 puntos - Riesgos de control y reordenación de código
Tomando como base el programa del Ejercicio 1:

1. Analiza los riesgos de datos (`srli` / `andi` / `add`) y de control (salto del bucle) que provocan paradas en el procesador de 5 etapas

2. Aplica desenrollamiento de bucle (2 bits por iteración) y reordena las instrucciones para reducir las paradas

3. Muestra el código ensamblador y explica qué dependencias se han resuelto o intercalado

4. Vuelve a ejecutar el código en C3 y compara el nuevo número de ciclos y CPI con los del Ejercicio 2

# Resolución

## EJ 1
![alt text](../images/cap4ejj.png)

## EJ 2
| Configuración | Ciclos Totales | CPI | Speedup vs. C1 |
|---|---:|---:|---:|
| C1: Single-cycle | 1005 | 1.00 | 1.00× (Base) |
| C2: 5-Stage w/o Forwarding | 1687 | 1.68 | 0.60× ($\frac{1005}{1687}$) |
| C3: 5-Stage w/ Forwarding | 1353 | 1.35 | 0.74× ($\frac{1005}{1353}$) |

**Fórmula del Speedup**

$$\text{Speedup}_{Cx} = \frac{\text{Ciclos}_{C1}}{\text{Ciclos}_{Cx}}$$

Se compara el número de ciclos de C1 (base) entre el de cada configuración, ya que el programa es el mismo. Un valor menor que 1 indica que necesita más ciclos que el monociclo. Esto se debe a que los procesadores segmentados añaden ciclos de llenado del cauce y burbujas, aunque su ciclo de reloj es mucho más corto que el del monociclo.

## EJ 3

**1. Análisis de riesgos del bucle original (C3: 5-Stage)**

* **Riesgo de datos:** en cada bit, `srli`, `andi` y `add` forman cadenas de dependencias RAW (el resultado de una instrucción lo usa la siguiente). Con forwarding (C3) se resuelven sin parar si las instrucciones dependientes no son de carga. Sin forwarding (C2) cada una genera burbujas, y de ahí la diferencia entre C2 y C3.
* **Riesgo de control:** como el conteo es branchless, el único salto que queda en el bucle de bits es el de cierre (`bnez`), que se toma casi todas las veces. Cada salto tomado se resuelve en EX y descarta las instrucciones ya captadas, y al ser un bucle de muchas vueltas esta penalización se repite cientos de veces.

**2. Código desenrollado (2 bits por iteración) y reordenado**

```asm
.data
vector:      .word 0b1111, 0b0011, 0b0101, 0b0001, 0b0000
total_unos:  .word 0

.text
la t0, vector
li a0, 0              # contador total de unos
li t1, 5              # 5 elementos del vector
la a2, total_unos
li a7,10
bucle:
    beqz t1, fin
    lw t2, 0(t0)      # cargamos elemento
    li t3, 32         # 32 bits que tenemos q mirar

bucle_bits:
    beqz t3, sig_elem
    andi t4, t2, 1    # extraemos el bit 0
    srli t5, t2, 1    # desplazamos 1 bit para llegar al bit 1
    add a0, a0, t4    # sumamos el bit 0 (rellena el hueco entre srli y andi)
    andi t5, t5, 1    # extraemos el bit 1
    srli t2, t2, 2    # desplazamos 2 bits a la derecha
    addi t3, t3, -2   # restamos 2 al contador de bits
    add a0, a0, t5    # sumamos el bit 1
    j bucle_bits

sig_elem:
    addi t0, t0, 4    # avanzamos al siguiente elemento del vector
    addi t1, t1, -1   # un elemento menos por procesar
    j bucle

fin:
    sw a0, 0(a2)      # guardamos el resultado final (9) en memoria
    ecall
```

**3. Dependencias resueltas e intercaladas**

* **Menos saltos:** el salto `j bucle_bits`, el `beqz t3,sig_elem` y el `addi t3,t3,-2` se ejecutan 16 veces por elemento en lugar de 32. En total, los saltos `j bucle_bits` pasan de 160 a 80, así que se reduce a la mitad la penalización por riesgo de control (flush en EX).
* **Menos instrucciones:** se ejecutan unas 765 instrucciones en lugar de 1005 (con 9 instrucciones por iteración de 2 bits en lugar de 6 por cada bit).
* **Reordenación:** `srli t5,t2,1` y `andi t5,t5,1` son dependientes (RAW), así que entre ellas se coloca `add a0,a0,t4`, que es independiente. Lo mismo pasa con el último `add a0,a0,t5`, que queda separado de su `andi` por `srli t2` y `addi t3`. Ninguna instrucción queda pegada a la que produce su operando, lo que ayuda sobre todo en C2 (sin forwarding).
* **Riesgo de datos del contador:** `addi t3,t3,-2` se coloca lejos del `beqz t3,sig_elem` de la siguiente vuelta (con el `add` y el `j` por medio).


**3. Dependencias resueltas e intercaladas**

* **Menos saltos:** al procesar 2 bits por iteración, el salto de cierre y el contador del bucle se ejecutan la mitad de veces, por lo que se reducen a la mitad las penalizaciones de control.
* **Reordenación:** se intercalan las instrucciones independientes de los dos bits (`andi` del bit 0, `srli`, `andi` del bit 1, `add`...) para que ninguna instrucción quede pegada a la que produce su operando.

**4. Comparativa en C3**

| Versión del código (C3: 5-Stage) | Ciclos Totales | CPI | Speedup vs. C3 original |
|---|---:|---:|---:|
| Código Ejercicio 1 (sin desenrollar) | 135 | 1.35 | 1.00× (Base) |
| Código Ejercicio 3 (desenrollado 2x y reordenado) | 95 | 1.24 | 1.42× |

$$\text{Speedup} = \frac{\text{Ciclos}_{\text{original}}}{\text{Ciclos}_{\text{desenrollado}}} = \frac{1353}{951} \approx 1.42\times$$