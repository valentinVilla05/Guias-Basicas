# Ejercicios Práctica 3
> Single-cycle processor (C1), 5-Stage processor w/o forwarding unit (C2) y 5-stage processor (C3)

Ejercicio 3.1. Toma el código del ejercicio 2.5 de la práctica anterior y lleva a cabo el siguiente trabajo:

a) Ejecuta el código en la configuración C1 y calcula cuál sería el número de ciclos en un procesador sin segmentación del cauce de ejecución. El CPI será igual a 1.

b) Ejecuta el código en la configuración C2, anota el número de ciclos y CPI. Calcula la mejora en rendimiento respecto a la configuración anterior.

c) Repite el paso anterior pero con la configuración C3.

d) Identifica las detenciones que se estén produciendo en el programa y reordena el código para evitarlas. Anota los ciclos y CPI de esta nueva versión en la configuración C3 y calcula la mejora de rendimiento.

Código del ejercicio 2.5

```asm
.data
vector: .word 7,4,23,12,6,20,17,8,3,10
fin:

.text
la t0,vector
li a0,0 # acumulador de la suma
li a1,0 # contador de elementos
la t1,fin

bucle5:
    lw a2,0(t0) # cargamos los datos como hacíamos antes
    add a0,a0,a2 # vamos sumando
    addi a1,a1,1 # incrementamos el contador
    addi t0,t0,4 # incrementamos el valor para que apunte al próximo dato
    blt t0,t1,bucle5 # se repite mientras t0< dirección fin del vector

    div a0,a0,a1
    li a7,1
    ecall
```

a) Ponemos como configuración **Single-cycle processor**

Nos saldrá un resultado similar a este: 

![alt text](../images/ej3s1.png)

**Explicación:**
En la arquitectura monociclo (C1), cada instrucción se ejecuta en un único ciclo de reloj completo, por lo que el CPI es ideal e igual a 1. El código consta de 6 instrucciones de inicialización, 50 instrucciones ejecutadas durante las 10 iteraciones del bucle y 3 instrucciones finales para la división y el `ecall`. Dado que no existen la segmentación ni los riesgos (hazards), el procesador ejecuta las 59 instrucciones en exactamente 59 ciclos

b) Ponemos como configuración **5-Stage processor w/o forwarding unit**

![alt text](../images/ej3s12.png)

**Explicación:**
Al activar la segmentación en 5 etapas pero carecer de unidad de reenvío (forwarding), el procesador se ve obligado a insertar ciclos de detención (stalls o burbujas) cada vez que una instrucción necesita un dato producido por una instrucción anterior que aún no ha escrito en el banco de registros. Esto penaliza el rendimiento elevando el CPI a 2.15 y aumentando el total a 127 ciclos

**Rendimiento respecto a C1**

$$\text{Ganancia de velocidad (Speedup)} = \frac{\text{Ciclos}_{C1}}{\text{Ciclos}_{C2}} = \frac{59}{127} \approx 0.465$$

c) Ponemos como configuración **5-Stage processor**

![alt text](../images/ej3s13.png)

**Explicación:**
La inclusión de la unidad de reenvío (forwarding unit) permite enviar los resultados de las etapas EX o MEM directamente a las instrucciones siguientes en EX sin esperar a la etapa WB. Esto elimina la mayoría de las detenciones por dependencias de datos. Sin embargo, el total baja a 93 ciclos (CPI = 1.58) y no a 59 debido a las penalizaciones de salto en las iteraciones del bucle y al riesgo de carga impredecible (load-use hazard) entre `lw` y `add`

* **Cálculo de rendimiento:**
    * **Respecto a C1 (Single-cycle):**
    $$\text{Speedup}_{C3/C1} = \frac{59}{93} \approx 0.634$$

    * **Respecto a C2 (Sin forwarding):**
    $$\text{Speedup}_{C3/C2} = \frac{127}{93} \approx \mathbf{1.365\times} \quad (\text{un } 36.5\% \text{ más rápido})$$

d ) Identificación de detenciones y reordenación de código

* **Identificación del riesgo:**
En el bucle original, la instrucción `add a0,a0,a2` utiliza inmediatamente el registro a2 cargado por `lw a2,0(t0)`. Dado que lw entrega el dato al final de la etapa MEM, la unidad de reenvío no puede evitar insertar 1 ciclo de detención (load-use hazard stall) en cada una de las 10 iteraciones

* **Código reordenado:**
Reorganizamos las instrucciones dentro de bucle5 interponiendo instrucciones independientes (`addi`) entre la carga `lw` y la suma `add`

![alt text](../images/mejora.png)

Nuevos Resultados
![alt text](../images/resultados.png)

CPI optimizado: $\frac{83}{59} \approx \mathbf{1.41}$.

**Mejora de rendimiento del código reordenado (en C3):**
$$\text{Speedup} = \frac{93}{83} \approx \mathbf{1.12\times} \quad (\text{un } 12\% \text{ de mejora})$$

**Ejercicio 3.2. Toma el código del ejercicio 2.6 de la práctica anterior y repite los pasos indicados para el 3.1.**

código del ejercicio 2.6
```asm
.data
vector2: .word 7,4,23,12,6,20,17,8,3,10
fin2:

.text
la t0,vector2
la t1,fin2
li a0,0 # acumulador de suma
li a1,0 # contador de elementos

bucle6:
    lw a2,0(t0)
    add a0,a0,a2
    addi a1,a1,1 # incrementamos el contador
    addi t0,t0,8 # salta a los impares
    blt t0,t1,bucle6
    li a7,1
    ecall
```

a) Ponemos como configuración **Single-cycle processor**

![alt text](../images/ej3ss2.png)

**Explicación:**
En la configuración monociclo (C1), cada instrucción se ejecuta en 1 solo ciclo de reloj ($CPI = 1$). El programa realiza 6 instrucciones de inicialización, 5 iteraciones del bucle (al saltar de 8 en 8 bytes se procesan 5 elementos de los 10 totales, ejecutando 5 instrucciones por iteración = 25 instrucciones) y 2 instrucciones finales (`li a7,1` y `ecall`). En total se completan 33 instrucciones en 33 ciclos.

b) Ponemos como configuración **5-Stage processor w/o forwarding unit**

![alt text](../images/ej3ss21.png)

**Explicación:**
Al no disponer de unidad de reenvío (forwarding unit), el procesador introduce burbujas o ciclos de detención (stalls) en el cauce para resolver las dependencias de datos (como el uso de `a2` tras `lw` o de `a0` tras `add`) y los riesgos de control provocados por los saltos. Esto eleva el CPI a 2.15 y requiere un total de 71 ciclos

* **Cálculo de rendimiento respecto a C1:**
$$\text{Speedup}_{C2/C1} = \frac{\text{Ciclos}_{C1}}{\text{Ciclos}_{C2}} = \frac{33}{71} \approx 0.465$$

c) Ponemos como configuración **5-Stage processor**

![alt text](../images/ej3ss22.png)

**Explicación:**
Con la unidad de reenvío activa (forwarding unit), los datos producidos en EX o MEM se redirigen directamente a las instrucciones siguientes, eliminando la mayoría de paradas de datos. El total de ciclos disminuye a 52 ciclos ($CPI = 1.58$). No alcanza los 33 ciclos debido a la penalización por el salto condicional `blt` y al riesgo de carga (load-use hazard) entre `lw` y `add`

* **Cálculo de rendimiento:**

**Respecto a C1 (Single-cycle)**:

$$\text{Speedup}_{C3/C1} = \frac{33}{52} \approx 0.635$$

**Respecto a C2 (Sin forwarding):**

$$\text{Speedup}_{C3/C2} = \frac{71}{52} \approx \mathbf{1.365\times} \quad (\text{un } 36.5\% \text{ más rápido})$$

d) Identificación de detenciones y reordenación de código

**Identificación del riesgo:
En el bucle `bucle6`, la instrucción `add a0,a0,a2` utiliza inmediatamente el registro a2 que acaba de ser cargado por `lw a2,0(t0)`. Como el dato de memoria no está disponible hasta el final de MEM, la unidad de reenvío no puede evitar provocar 1 ciclo de detención (load-use hazard stall) en cada una de las 5 iteraciones (5 ciclos de parada en total)

**Código reordenado (optimizado):**
Intercalamos las instrucciones independientes de incremento (`addi`) entre la carga lw y la suma `add:`

![alt text](../images/ej3ss23.png)

**Nuevos resultados en C3 tras la reordenación:**
![alt text](../images/ej3ss24.png)

* **Mejora de rendimiento del código reordenado (en C3):**

$$\text{Speedup} = \frac{52}{47} \approx \mathbf{1.106\times} \quad (\text{un } 10.6\% \text{ de mejora})$$

