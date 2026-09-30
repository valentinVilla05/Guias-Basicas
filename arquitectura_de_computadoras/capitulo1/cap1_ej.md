### Ejercicios de capitulo 1

(Cabe recordar que hay muchas maneras de resolver los ejercicios, no solo hay una opción correcta)

**Ejercicio 1.1.** Suma los valores inmediatos 3, 5 y 7 usando solo el registro a0 y muestra
el resultado en la consola. En este y los siguientes tres ejercicios usa solo
direccionamiento inmediato y por registro.

```asm
.text

addi a0, a0, 3
addi a0, a0, 5
addi a0, a0, 7

addi a7, zero, 1
ecall

```

En este ejercicio tenemos que que sumar 3 valores de manera inmediata. Usamos la instrucción `addi` que es para sumar un registro y un número constante.

Al principio el valor de a0 es 0, a este le sumamos 3, ahora el valor de a0 = 3, le sumamos 5 y la suma se va acumulando.
Para mostrar por consola tenemos que asignar el valor '1' al registro a7 y hacemos la llamada al sistema con `ecall`

---

**Ejercicio 1.2.** Asigna a **a0** el valor 23, réstale el valor 8 y muestra el resultado por la consola.

```asm
.text

addi a0, zero, 23
addi t0, zero, 8
sub a0, a0, t0

addi a7, zero, 1
ecall
```

Este ejercicio es igual que el anterior usando direccionamientos inmediatos.
Guardamos en a0 el valor 23 (sumando 0+23), guardamos el segundo valor (8) en t0 (registro para valores temporales) y por último hacemos la resta con `sub0`

Por último mostramos el resultado por consola.

---

**Ejercicio 1.3**. Muestra por la consola el resultado de multiplicar los números 5 y 7.

```asm
.text

addi a0, zero, 5
addi t0, zero, 7
mul a0, a0, t0

addi a7, zero, 1
ecall
```

Este ejercicio es exactamente igual que el anterior pero realizando una multiplicación (`mul`) en vez de la resta.

---

**Ejercicio 1.4** Divide el valor 23 entre 4 y muestra por la consola tanto el cociente como el
resto

```asm
.text

addi t0, zero, 23
addi t1, zero, 4

div a0, t0, t1
addi a7, zero, 1
ecall

rem a0, t0, t1
addi a7, zero, 1
ecall

```

Para este ejercicio guardamos en el registro `t0` el valor 23 y en `t1` el valor. Realizamos la division con `div`, guardamos el valor en `a0` y mostramos el cociente por consola. Después guardamos el resto de la división con `rem` en a0 y volvemos a mostrar el resultado por consola.

---

**Ejercicio 1.5.** Almacena en memoria tres números y cárgalos uno a uno, sumándolos de manera acumulada en el registro a0. Este deberá ser inicializado a 0 al inicio del programa.

```asm
.data

dato1: .word 10
dato2: .word 15
dato3: .word 20

.text

lw t0, dato1
lw t1, dato2
lw t2, dato3

addi a0, zero, 0
add a0, a0, t0
add a0, a0, t1
add a0, a0, t2

addi a7, zero, 1
ecall

```

Aquí ya empezamos a declarar variables en memoria con `.data`.
Cargamos las variables con `lw`. Declaramos `a0` a 0 y sumamos los valores para mostrar la suma por consola.

---

**Ejercicio 1.6** Modifica el programa anterior para usar el direccionamiento indexado, de forma que t0 actúe como puntero para leer los tres valores desde memoria.

```asm
.data

tresValores: .word 10, 15, 20

.text

lui t0, %hi(tresValores)
addi t0, t0, %lo(tresValores)

lw a1, 0(t0)
lw a2, 4(t0)
lw a3, 8(t0)

add a0, zero, a1
add a0, a0, a2
add a0, a0, a3

addi a7, zero, 1
ecall

```

Declaramos los 3 valores que vamos a usar en memoria.

Descomponemos el registro `t0` de 32 bits en 20 y 12 bits mediante `lui` y `%hi()` y `%lo()`, cargamos los datos en `a1`, `a2`, `a3` mediante `lw` y por último sumamos y vamos acumulando el resultado en `a0`

---

**Ejercicio 1.7** Actualiza el programa del ejercicio previo de forma que, tras calcular la suma, el resultado se almacene en memoria, en una dirección previamente reservada.

```asm
.data

tresValores: .word 10, 15, 20

.bss

resultado: .word 0

.text

lui t0, %hi(tresValores)
addi t0, t0, %lo(tresValores)

lw a1, 0(t0)
lw a2, 4(t0)
lw a3, 8(t0)

add a0, zero, a1
add a0, a0, a2
add a0, a0, a3

la t0, resultado
sw a0, 0(t0)

addi a7, zero, 10
ecall

```

Al igual que el anterior, declaramos los valores en `.data` solo que en este tambien declaramos una zona de memoria en `.bss` para guardar el resultado luego. Hacemos el mismo proceso que en el anterior pero aquí una vez tenemos la suma acumulada en `a0` hacemos li siguiente:

1. Obtenemos la dirección de memoria de `resultado` en `t0` mediante `la`
2. Guardamos el dato en `t0` mediante `sw`

Y al final terminamos el programa.

---

**Ejercicio 1.8.** Modifica el programa del Ejercicio 1.4 para que el cociente y resto se guarden en
dos posiciones de memoria consecutivas, en lugar de mostrarse por la consola.

```asm
.data

valores: .word 23, 4

.bss

resultados: .word 0

.text

la t0, valores
lw a1, 0(t0)
lw a2, 4(t0)

div t1, a1, a2
rem t2, a1, a2


la t3, resultados
sw t1, 0(t3)
sw t2, 4(t3)

addi a7, zero, 10
ecall

```

Aquí el programa hace lo mismo que en el ejercicio 1.4 solo que en vez de mostrar el resultado por consola los guarda en 2 posiciones de memoria seguidas. Esto lo conseguimos guardando los resultados en t3:

1. `la t3, resultados` guardamos la posicion de memoria
2. `sw t1, 0(t3)` Escribimos el resultado de la división guardado en `t1` en la primera posición
3. `sw t2, 4(t3)` Hacemos lo mmismo con el resto de la división en la siguiente posición

---

**Ejercicio 1.9** Carga en el registro a0 el valor 75000, previamente almacenado en el segmento de datos, y envíalo a la consola.

```asm
.data

valor: .word 75000

.text

la  t0, valor #Obtenemos el valor de la memoria
lw a0, 0(t0) # Cargamos el valor en el registro a0

addi a7, zero, 1 # Imprimimos en pantalla
ecall # Llamamos al sistema

addi a7, zero, 10 # Terminamos el programa
ecall
```

Este ejercicio no tiene ninguna complejidad, es igual que todos los anteriores. Declaramos una variable en memoria, la cargamamos en un registro y la mostramos por pantalla

---

**Ejercicio 1.10.** Asigna al registro a0 el valor 75000, sin leerlo de memoria, y envíalo a la consola.

```asm
.text

li a0, 75000 # Cargamos el valor 75000 directamente en a0


addi a7, zero, 1
ecall

addi a7, zero, 10
ecall
```

En este ejercicio cargamos directamente el valor sin parar a leerlo en memoria
