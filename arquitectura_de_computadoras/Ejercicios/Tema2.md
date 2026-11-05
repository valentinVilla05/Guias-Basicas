## Ejercicio 1.
* Procesador RISC-V con detección de riesgos de datos y **adelantamientos**.

* Lectura y escrrituras en el banco de registros se realizan en mitades de ciclo diferentes.

* Todas las unidades tienen un **ciclo de latencia**

> En los problemas siempre nos darán 2 tablas (1 la tabla de partida indicando las soluciones) y otra extra por si nos equivocamos

>IMPORTANTE:
* Las **cargas** sueltan en dato en **memoria**

* Las **operaciones aritméticas** sueltan el dato en Ejecución

| Introducción | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
| -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | 
| **lw `s0`,0,t0** | IF | ID | E | MEM | WB | | 
| **add a1,a1,`s0`** | | IF | `ID` $*1$ | - | E | MEM | WB 
| **addi t0,t0,4** | | | IF | - | ID | E | MEM | WB | 
| **lw `s0`,0,t0** | | | | - | IF | ID | E | MEM | WB |
| **add a2,a1,`s0`** | | | | - |  |IF | `ID` $*2$ | - | E | MEM | WB |
| **addi t0,t0,4** | | | | - |  | | IF | - | ID | E | MEM | WB |
| **blt t0,t1,ini** | | | | - | | | |  - | IF | ID | E | MEM | WB 

**Explicaciones**

$*1$ : Necesitamos `s0` el cual todavía se está ejecutando y no se ha almacenado en memoria (YA QUE ES UNA INSTRUCCIÓN DE **CARGA**), por lo que no podemos decodificar la instrucción de forma correcta . Posteriormente se guarda en memoria `s0` correctamente y ya si podemos seguir con el flujo del procesador

$*2$: Ocurre exactamente igual, el dato está en ejecución y todavía no ha llegado a memoria, por lo que no se puede decodificar correctamente ya que no se han leido bien los datos

Registros adelantados por bypass:

    `s0` es adelantado por la instrucción 2
    `t0` es adelantado en la instrucción 4
    `s0` es adelantado en la instrucción 5
    `t0` es adelantado en la instrucción 7
## Ejercicio 2.

| Instrucción | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 
| -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| **lw `s0`,0(t0)** | IF | ID | E | MEM | WB | 
| **add a1,a1,`s0`** |  | IF | `ID` $*1$ | - | E | MEM | WB
| **addi t0,t0,4** | | | IF | - | ID | E | MEM | WB | 
| **lw `s1`,0(t0)** | | | | - | IF | ID | E | MEM | WB | 
| **add a2,a2,`s1`** | | | | - | | IF | `ID` $*2$ | - | E | MEM | WB | 
| **add a3,a1,a2** | | | | - | | | IF | - | ID | E | MEM | WV
| **addi t0,t0,4** | | | | - | | | | - | IF | ID | E | MEM | WB| 
| **sub a4,a3,s0** | | | | - | | | | - | | IF | ID | E | MEM | WB | 
| **add a5,a4,s1** | | | | - | | | | - | | | IF | ID | E | MEM | WB | 
| **blt t0,t1,ini** | | | | - | | | | - | | | | IF | ID | E | MEM | WB | 


$*1$ : Ocurre exactamente igual que en ejercicio 1, `lw` es una operación de carga por lo que `s0` se actualiza en **MEM** , no se puede decodificar correctamente la instrucción en **add** 

$*2$: Igual, estamos ante una instrucción de carga, **no suelta el dato hasta mem** por que no se puede Decodificar correctamente porque el dato `s1` no es correcto aún

## Ejercicio 3
| Instrucción | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 
| -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| **lw `s0`,0(t0)** | IF | ID | EX | MEM | WB |
| **add a1,a1,`s0`** ($*1$) | | IF | ID | - | EX | MEM | WB |
| **addi t0,t0,4** | | | IF | - | ID | EX | MEM | WB |
| **lw `s1`,0(t0)** | | | | - | IF | ID | EX | MEM | WB | 
| **add a2,a2,`s1`** ($*2$)| | | | - | | IF | ID | - | EX  | MEM | WB | 
| **mul a3,a1,a2** | | | | - | | | IF | - | ID | EX | EX ($*3$) | MEM | WB |
| **addi t0,t0,4** | | | |  - | | | | - | IF | ID | `-` | EX ($*4$) | MEM | WB
| **sub a4,a3,s0** | | | | - | | | | - | | IF | - | ID | E | MEM | WB | 
| **add a5,a4,s1** | | | | - | | | | - | | | - | IF | ID | E | MEM | WB | 
| **lw s2,0(t0)** | | | | - | | | | - | | | - | - | IF | ID | E | MEM | WB |

$*1$: En este caso , la instrucción `lw` almacena en s0 el resultado en la etapa de `mem` por lo que no podremos pasar los datos de esta antes

$*2$: Exactamente igual

$*3$: La multiplicación es una operación más compleja que la suma y la resta, porl o que requirere **2 ciclos de reloj** en lugar de 1

$*4$: La instrucción addi actualiza el registro temporal t0 tras la ejecución de esta por lo tanto tendremos que posponer las siguientes instrucciones

## Ejercicio 4
| Instrucción | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 
| -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | 
| **lui t0,0x10000** | IF | ID | EX | MEM | WB | 
| **lw a0,0,t0** | | IF | ID | EX | MEM | WB | 
| **addi a0,a0,1** | |  | IF | ID | - | `EX` | MEM | WB | 
| **lw a1,4,t0** | | | | IF | - | ID | EX | MEM | WB | 
| **addi a1,a1,4** | | | | | | IF | ID | - | `EX` | MEM | WB | 
| **add a2,a0,a1** | | | | | | | IF | - | ID | EX | MEM | WB | 
| **addi t0,t0,4** | | | | | | | | - | IF | ID | EX | MEM | WB | 
| **blt t0,t1,bucle** | | | | | |  | | - |  | IF | ID | EX | MEM | WB  

En ambas `EX` marcadas ocurre igual, en este caso la instrucción previa es lw que representa la carga , por lo que el registro de destino únicamente será actualizado tras `MEM`