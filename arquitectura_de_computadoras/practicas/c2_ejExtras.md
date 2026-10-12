# Examen de la práctica 2 del año pasado y ejercicios similares

## Ejercicio 1 – 4/10 puntos - Eje1.s
Escribe un programa ajustado a las siguientes directivas:

* Se tiene **almacenado en memoria un vector** con el número de calificaciones *(entre $0$ y $10$)* que los estudiantes han obtenido en una asignatura. Los valores de dicho vector serán los siguientes: `10, 3, 5, 7, 8, 9, 6, 2, 4, 5`.

* El programa deberá calcular la **media de las calificaciones** en dicha asignatura, así como **cuántos de ellos superan dicha asignatura**, suponiendo que se aprueba con una calificación igual o mayor que $5$. **Las calificaciones aprobadas se mostrarán por consola.**

## Ejercicio 2 – 6/10 puntos - Eje2.s
Escribe un programa ajustado a las siguientes directivas:

* Se tiene **almacenado en memoria un vector** con la capacidad en litros que contienen varios depósitos, valores que nunca pueden ser negativos. Los valores en dicho vector serán los siguientes: 

`125000, 195200, 75000, 765500, 607000, 1200000, 140000, 658000, 704000, 1305000`.

* Escribe una función que tome como entrada los siguientes argumentos y que **devuelva en `a0`** el número de depósitos que pueden contener dicha capacidad:

* `a0` – La dirección donde comienzan el vector con las capacidades en litros.

* `a1` – El número de depósitos que tiene el vector de capacidades en litros.

* `a2` – La capacidad en litros a partir de la cual se quiere contar el número de depósitos.

* La función deberá **guardar en la pila la dirección de retorno** (registro `ra`) y **cualquier otro registro que modifique**, recuperándolos antes de volver. Al hacer comparaciones debe tenerse presente que **son palabras de 32 bits sin signo** .

* Desde el cuerpo principal del programa, llama a la anterior función dos veces para contar los satélites que distan más de $100\,000$ y $1\,000\,000$ de kilómetros, mostrando por la consola ambos resultados.


## Resolución del Examen

> Se admiten soluciones alternativas 
### Ejercicio 1

![alt text](../images/ej1-2025.png)

Resultado esperado: 

```
10 5 7 8 9 6 5 
Media: 5
```

### Ejercicio 2
![alt text](../images/ej2-2025.png)

![alt text](../images/img2-2025_2.png)

``` Resultado esperado
9
2
```

## Ejercicios parecidos

## Ejercicio 1 – Estructura tipo Bucle / Filtrado Directo
Escribe un programa en ensamblador RISC-V ajustado a las siguientes directivas:
* Se tiene **almacenado en memoria** un vector con las temperaturas (en grados Celsius, valores enteros que pueden ser positivos o negativos) registradas en una estación meteorológica a lo largo de 10 días: `-3, 12, 8, 0, 15, -1, 22, 18, 5, 11`.

* El programa deberá **calcular la temperatura media del periodo, así como contar cuántos días se registraron temperaturas sobre cero ($> 0$)**. Las temperaturas positivas se **mostrarán por consola**.

* Agrega un comentario al inicio del programa con vuestros nombres y un comentario al final donde expliquéis brevemente el planteamiento o la estrategia general seguida.

```asm

.data
vector: .word -3,12,8,0,15,-1,22,18,5,11
espacio: .string " "
salto: .string "\n"

.text
la t0, vector  # cargamos la dirección del vector en t0
li t1, 10      # cargamos el tamaño en t1
li t2, 0       # queremos las temperaturas mayores que 0
li t4, 0       # contador de elementos con temperatura mayor que 0
li t5, 0       # acumulador para la suma total (media)

bucle:
    beqz t1, fin
    lw t3, 0(t0)        # leemos la temperatura actual
    add t5, t5, t3      # acumulamos para la media
    ble t3, t2, menor   # si la temperatura es <= 0 no es positiva

mayor:
    addi t4, t4, 1      # sumamos al contador de temperaturas > 0
    li a7, 1
    mv a0, t3           # mostramos la temperatura en pantalla
    ecall
    la a0, espacio
    li a7, 4
    ecall

menor:
    addi t0, t0, 4      # apuntamos a la siguiente dirección
    addi t1, t1, -1
    j bucle

fin:
    # Imprimir salto de línea
    la a0, salto
    li a7, 4
    ecall

    # Imprimir la media (suma total / 10)
    li a6, 10
    div a0, t5, a6
    li a7, 1
    ecall

    li a7, 10
    ecall

```
## Ejercicio 2 – Estructura tipo Función / Pila / Comparación Sin Signo

Escribe un programa en ensamblador RISC-V ajustado a las siguientes directivas:

* Se tiene **almacenado en memoria** un vector con el saldo en cuentas bancarias (valores de 32 bits sin signo en euros): 
`4500, 120000, 8500, 310000, 950, 670000, 50000, 1500000, 2300, 890000`.

* Escribe una función que tome como entrada los siguientes argumentos y que devuelva en a0 el número de cuentas que superan un cierto saldo:

* `a0` – La dirección de memoria donde comienza el vector de saldos.

* `a1` – El número de cuentas contenidas en el vector.

* `a2` – El umbral de saldo a partir del cual se quiere realizar el recuento.

La función deberá guardar en la pila la dirección de retorno (ra) y los registros que modifique, recuperándolos antes de volver (ret). Las comparaciones deben realizarse considerando que son palabras de 32 bits sin signo.

Desde el cuerpo principal del programa (main), llama a la función dos veces para contar las cuentas con más de 100.000 € y con más de 500.000 €, mostrando ambos resultados por consola.

Agrega los comentarios de inicio y explicación final correspondientes.

```asm
.data
saldo: .word 4500, 120000, 8500, 310000, 950, 670000, 50000, 1500000, 2300, 890000
salto: .string "\n"

.text
main:
la a0,saldo # cargamos la dirección de memoria donde comienza en a
li a1,10 # número de cuentas
li a2,100000 # humbral del recuento

jal ra, cuentas
li a7,1
ecall

la a0,salto
li a7,4
ecall

la a0,saldo
li a1,10
li a2,500000
jal ra, cuentas

li a7,1
ecall

li a7,10
ecall

cuentas:
    addi sp,sp,-16 # almacenamos 4 lugares en la pila
    sw ra,0(sp)
    sw t0,4(sp)
    sw t1,8(sp)
    sw t2,12(sp)
    
    li t0,0 # contador de veces que se supera dicho saldo
    mv t1,a0 # puntero 
    
bucle2:
    beqz a1,fin2
    lw t2,0(t1) # lee la primera posición del vector
    bleu t2,a2,siguiente
    addi t0,t0,1
    
siguiente:
    addi t1,t1,4
    addi a1,a1,-1
    j bucle2
fin2:
    mv a0,t0 # devuelve el resultado a a0
    
    lw ra,0(sp)
    lw t0,4(sp)
    lw t1,8(sp)
    lw t2,12(sp)
    addi sp,sp,16
    
    ret

```
## Ejercicio 3 – Mezcla Examen (Procesamiento de Stock)
Escribe un programa en ensamblador RISC-V ajustado a las siguientes directivas:

Se tiene almacenado en memoria un vector con las unidades de stock de varios productos de un almacén (palabras de 32 bits sin signo): 
`50, 1200, 0, 850, 3400, 12, 9500, 430, 2100, 6000`.

Escribe una función que reciba en `a0` la dirección del vector, en a1 la cantidad de productos y en `a2` el stock mínimo de seguridad. La función debe devolver en `a0` cuántos productos están en riesgo por tener un stock estrictamente menor que dicho valor mínimo.

La función debe ser segura con el uso de la pila (`sp, ra y registros modificados`) y usar comparaciones sin signo (`bltu/bleu`).

Desde `main`, invoca la función dos veces comprobando los límites de `100` unidades y `1.000` unidades, imprimiendo ambos conteos por pantalla.

Incluye los comentarios explicativos exigidos.


```asm
.data
vector2: .word 50,1200,0,850,3400,12,9500,430,2100,6000
salto: .string "\n"

.text
main:
    # Primera llamada (límite 100)
    la a0,vector2
    li a1,10
    li a2,100
    jal ra,vectorS
    
    li a7,1
    ecall

    la a0,salto
    li a7,4
    ecall

    # Segunda llamada (límite 1000)
    la a0,vector2
    li a1,10
    li a2,1000
    jal ra,vectorS

    li a7,1
    ecall

    li a7,10
    ecall

vectorS:
    addi sp,sp,-16
    sw ra,0(sp)
    sw t0,4(sp)
    sw t1,8(sp)
    sw t2,12(sp)
    
    li t0,0 # contador
    mv t1,a0 

bucle3:
    beqz a1,fin3
    lw t2,0(t1)              # leemos el stock actual del vector
    bgeu t2,a2,siguiente3    # si es >= límite, NO está en riesgo (saltamos)
    addi t0,t0,1             # si es estrictamente menor (<), sumamos 1
    
siguiente3:
    addi t1,t1,4
    addi a1,a1,-1
    j bucle3
    
fin3: 
    mv a0,t0
    
    lw ra,0(sp)
    lw t0,4(sp)
    lw t1,8(sp)
    lw t2,12(sp)
    addi sp,sp,16
    
    ret
```