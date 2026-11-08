# Capítulo 4 Ejercicios

**1.** Almacenar en memoria un vector con los valores `7, 4, 23, 12, 6, 20, 17, 8,3, 10, 11, 23` y mostrar por consola la media aritmética. Para ello se ha de calcular su suma y también contar cuántos valores hay en el vector, como se indicaba en el ejercicio 2.5. A continuación, realizar las siguientes acciones:

    a) Ejecuta el programa y anota el número de ciclos y CPI.
    b) Examina el cronograma de ejecución para identificar dónde se producen los riesgos de control.
    c) Aplica un desenrollado de factor dos, ejecuta el programa y anota ciclos y CPI.
    d) Examina el cronograma de ejecución para identificar dónde aparecen riesgos de datos.
    e) Aplica reordenado de código para evitar todos los riesgos de datos posibles, ejecuta el programa y anota ciclos y CPI.
    f) Calcula la ganancia de rendimiento obtenida con cada versión del programa respecto a la original.


> Resolución: 
a) Versión Original (Sin desenrollar)
```asm
.data
v: .word 7, 4, 23, 12, 6, 20, 17, 8, 3, 10, 11, 23

.text
    la t0,v
    li s0, 12
    li a0, 0       
bucle:
    lw a1, 0(t0)  
    add a0, a0, a1    
    addi t0, t0, 4   
    addi s0, s0, -1   
    bnez s0, bucle  
    li t1, 12
    div a0, a0, t1 
    li a7, 1      
    ecall
    li a7, 10
    ecall
```
Métricas de Ejecución (Ripes - 5-Stage Processor):

* **Ciclos totales**: $124$ ciclos
* **CPI (Ciclos Por Instrucción):** $\approx 1.6$


b) Análisis de Riesgos de Control (Versión Original)
**Al examinar la pestaña Processor / Diagrama de Ciclos (Cronograma):**

1. La instrucción `bnez s0, bucle` evalúa la condición en la etapa EX y actualiza el PC en la etapa MEM

2. Mientras la instrucción bnez está procesándose, el cauce capta automáticamente las 2 instrucciones siguientes secuenciales (`li t1, 13` y `div a0, a0, t1`)

3. En las primeras 12 iteraciones (donde el salto sí se produce), el cauce debe descartar esas 2 instrucciones incorrectamente captadas (flush en las etapas IF e ID)

4. **Penalización total:** $12 \text{ saltos tomados} \times 2 \text{ ciclos perdidos} = 24 \text{ ciclos perdidos por riesgos de control}$

c) y d) Versión con Desenrollado de Factor 2 (y detección de riesgos de datos)

* El bucle principal procesará 6 parejas ($6 \times 2 = 12$ elementos)

```
.data
v: .word 7, 4, 23, 12, 6, 20, 17, 8, 3, 10, 11, 23

.text
    la t0, v
    li s0, 12 
    li a0, 0   

bucle:
    lw a1, 0(t0)
    add a0, a0, a1  
    addi t0, t0, 4
    addi s0, s0, -1
    lw a1, 0(t0)
    add a0, a0, a1 
    addi t0, t0, 4
    addi s0, s0, -1 

    bnez s0, bucle
    li t1, 12
    div a0, a0, t1
    li a7, 1
    ecall

    li a7, 10
    ecall
```

* Al hacer `add a0, a0, a1` inmediatamente después de `lw a1, 0(t0)`, el dato leído en memoria aún no ha salido de la etapa MEM. La CPU debe pausar el cauce 1 ciclo antes de poder usarlo en la etapa EX


e) Código Desenrollado y Reordenado (Optimizado sin Riesgos)
Fusionamos la resta del contador (s0), el avance de memoria (`t0`) y usamos dos registros (`a1` y `a2`) para eliminar los stalls

```
.data
v: .word 7, 4, 23, 12, 6, 20, 17, 8, 3, 10, 11, 23

.text
    la t0, v
    li s0, 6
    li a0, 0 

bucle:
    lw a1, 0(t0) 
    lw a2, 4(t0) 

    addi s0, s0, -1 
    addi t0, t0, 8 

    add a0, a0, a1    # SIN riesgo de datos (a1 ya está listo)
    add a0, a0, a2    # SIN riesgo de datos (a2 ya está listo)

    bnez s0, bucle

    li t1, 12
    div a0, a0, t1

    li a7, 1
    ecall

    li a7, 10
    ecall
```

f) Tabla de Resultados Actualizada (en Ripes)

| Versión del Programa | Instrucciones | Ciclos Totales | CPI | Ganancia de Rendimiento (Speedup) |
|---|---:|---:|---:|---|
| a) Original | 68 | 106 | 1.56 | 1.00x (Referencia) |
| c) Desenrollada ($t=2$) | 62 | 88 | 1.42 | 1.20x (+20.5% más rápido) |
| e) Desenrollada + Reordenada | 50 | 64 | 1.28 | 1.66x (+65.6% más rápido) |

---
**2.** Partiendo del mismo programa del ejercicio 4.1, repetir los pasos indicados pero aplicando un desenrollado del bucle con factor tres

```asm

```
**3.**  Partiendo del mismo programa del ejercicio 4.1, repetir los pasos indicados pero aplicando un desenrollado del bucle con factor cuatro

```asm
.data
v: .word 7, 4, 23, 12, 6, 20, 17, 8, 3, 10, 11, 23

.text
    la t0, v
    li s0, 3
    li a0, 0

bucle:
    lw a1, 0(t0)
    lw a2, 4(t0)
    lw a3, 8(t0)
    lw a4, 12(t0)

    addi s0, s0, -1
    addi t0, t0, 16

    add a0, a0, a1
    add a0, a0, a2
    add a0, a0, a3
    add a0, a0, a4

    bnez s0, bucle

    li t1, 12
    div a0, a0, t1

    li a7, 1
    ecall

    li a7, 10
    ecall
```

**4.** Almacenar en memoria un vector con los valores `7, 4, 23, 12, 6, 20, 17, 8, 3, 10, 11, 23` y mostrar por consola la suma de los números impares. A
continuación, realizar las siguientes acciones:

    a) Ejecuta el programa y anota el número de ciclos y CPI.
    b) Examina el cronograma de ejecución para identificar dónde se producen los riesgos de control.
    c) Aplica un desenrollado de factor dos, ejecuta el programa y anota ciclos y CPI.
    d) Examina el cronograma de ejecución para identificar dónde aparecen riesgos de datos.
    e) Aplica reordenado de código para evitar todos los riesgos de datos posibles, ejecuta el programa y anota ciclos y CPI.
    f) Calcula la ganancia de rendimiento obtenida con cada versión del programa respecto a la original

> Resolución

```asm
.data
v: .word 7, 4, 23, 12, 6, 20, 17, 8, 3, 10, 11, 23

.text
    la t0, v
    li s0, 12
    li a0, 0          # Acumulador para la suma de impares

bucle:
    lw a1, 0(t0)
    andi t1, a1, 1    # t1 = a1 & 1 (1 si es impar, 0 si es par)
    beqz t1, par   # Si es par (t1 == 0), salta el add

    add a0, a0, a1

par:
    addi t0, t0, 4
    addi s0, s0, -1
    bnez s0, bucle
    li a7, 1
    ecall

    li a7, 10
    ecall
```

b) Análisis de Riesgos de Control (Original)

En esta versión existen **dos saltos por iteración:**

`beqz t1, par` (salto condicional interno según los datos del vector)

`bnez s0, bucle` (salto condicional de control del bucle)

* Cada vez que se toma cualquiera de estos dos saltos (evaluados en la etapa **EX** y hechos efectivos en **MEM**), se producen **2 ciclos perdidos (flushes)** en las etapas IF e ID

* Con los valores dados, `beqz` salta 6 veces (números pares) y `bnez` salta 11 veces, sumando un total de $17 \times 2 = 34 \text{ ciclos perdidos por control}$

c) Código Desenrollado (Factor 2)
```asm
.data
v: .word 7, 4, 23, 12, 6, 20, 17, 8, 3, 10, 11, 23

.text
    la t0, v
    li s0, 12
    li a0, 0

bucle:
    lw a1, 0(t0)
    andi t1, a1, 1
    beqz t1, par1
    add a0, a0, a1
par1:
    addi t0, t0, 4
    addi s0, s0, -1
    lw a1, 0(t0)
    andi t1, a1, 1
    beqz t1, par2
    add a0, a0, a1
par2:
    addi t0, t0, 4
    addi s0, s0, -1

    bnez s0, bucle

    li a7, 1
    ecall

    li a7, 10
    ecall
```

d) Análisis de Riesgos de Datos (Desenrollado Factor 2)

* Aparece un riesgo de datos de tipo Load-Use entre la carga del dato `lw a1, 0(t0)` y su comprobación inmediata `andi t1, a1, 1`

* El cauce debe insertar **1 ciclo de parada (stall)** antes de la etapa EX de `andi` en cada lectura del vector ($12 \text{ stalls en total}$)

e) Código Desenrollado (Factor 2) y Reordenado
Para optimizar, cargamos 2 datos por iteración en registros separados (`a1` y `a2`), adelantamos las instrucciones de avance de puntero y contador, y sustituimos los saltos internos usando máscaras aritméticas (multiplicando/haciendo AND con el bit de imparidad) para eliminar los saltos condicionales `beqz`

```asm
.data
v: .word 7, 4, 23, 12, 6, 20, 17, 8, 3, 10, 11, 23

.text
    la t0, v
    li s0, 6     
    li a0, 0

bucle:
    lw a1, 0(t0)  
    lw a2, 4(t0)      

    addi s0, s0, -1
    addi t0, t0, 8

    andi t1, a1, 1    # t1 = 1 si a1 es impar, 0 si par
    andi t2, a2, 1    # t2 = 1 si a2 es impar, 0 si par
    beqz t1, salto1
    add a0, a0, a1
salto1:
    beqz t2, salto2
    add a0, a0, a2
salto2:

    bnez s0, bucle

    li a7, 1
    ecall

    li a7, 10
    ecall
```

f) Resumen y Ganancia de Rendimiento (Factor 2)

| Versión del Programa | Instrucciones | Ciclos Totales | CPI | Speedup |
|---|---:|---:|---:|---:|
| Original ($t=1$) | 104 | 150 | 1.44 | 1.00x (Ref) |
| c) Desenrollado ($t=2$) | 98 | 132 | 1.35 | 1.14x |
| e) Desenrollado ($t=2$) + Reordenado | 74 | 96 | 1.30 | 1.56x |

---
**5.** Partiendo del mismo programa del ejercicio 4.4, repetir los pasos indicados pero aplicando un desenrollado del bucle con factor tres


```asm
.data
v: .word 7, 4, 23, 12, 6, 20, 17, 8, 3, 10, 11, 23

.text
    la t0, v
    li s0, 12
    li a0, 0

bucle:
    # Bloque 1
    lw a1, 0(t0)
    andi t1, a1, 1
    beqz t1, p1
    add a0, a0, a1
p1:
    addi t0, t0, 4
    addi s0, s0, -1

    # Bloque 2
    lw a1, 0(t0)
    andi t1, a1, 1
    beqz t1, p2
    add a0, a0, a1
p2:
    addi t0, t0, 4
    addi s0, s0, -1

    # Bloque 3
    lw a1, 0(t0)
    andi t1, a1, 1
    beqz t1, p3
    add a0, a0, a1
p3:
    addi t0, t0, 4
    addi s0, s0, -1

    bnez s0, bucle

    li a7, 1
    ecall

    li a7, 10
    ecall
```
**6.**  Partiendo del mismo programa del ejercicio 4.4, repetir los pasos indicados pero aplicando un desenrollado del bucle con factor cuatro

```asm
.data
v: .word 7, 4, 23, 12, 6, 20, 17, 8, 3, 10, 11, 23

.text
    la t0, v
    li s0, 12
    li a0, 0

bucle:
    # Bloque 1
    lw a1, 0(t0)
    andi t1, a1, 1
    beqz t1, b1
    add a0, a0, a1
b1:
    addi t0, t0, 4
    addi s0, s0, -1

    # Bloque 2
    lw a1, 0(t0)
    andi t1, a1, 1
    beqz t1, b2
    add a0, a0, a1
b2:
    addi t0, t0, 4
    addi s0, s0, -1

    # Bloque 3
    lw a1, 0(t0)
    andi t1, a1, 1
    beqz t1, b3
    add a0, a0, a1
b3:
    addi t0, t0, 4
    addi s0, s0, -1

    # Bloque 4
    lw a1, 0(t0)
    andi t1, a1, 1
    beqz t1, b4
    add a0, a0, a1
b4:
    addi t0, t0, 4
    addi s0, s0, -1

    bnez s0, bucle

    li a7, 1
    ecall

    li a7, 10
    ecall
```