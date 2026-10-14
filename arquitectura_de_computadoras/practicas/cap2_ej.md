# Tema 2: Ejercicios

> Se admiten soluciones alternativas

**2.1 Sumar los valores 1 a 1000, acumulando la suma en el registro a0, y mostrar el
resultado por la consola**

```asm
.text
li t0,1
li t1,1000
li a0,0

bucle1:
    add a0,a0,t1
    beq t0,t1,fin1 # si t0=t1 salta a fin1
    addi t1,t1,-1
    j bucle1
fin1:
    li a7,1
    ecall

```

**2.2 Sumar los valores impares entre 1 y 1000 en el registro a0 y mostrar el resultado
por la consola**

(Exactamente igual que el anterior pero tenemos que añadir la línea marcada)

```asm
.text
li t0,1
li t1,999
li a0,0

bucle2:
    add a0,a0,t1
    beq t0,t1,fin2
    addi t1,t1,-2 # aquí decrementamos saltandonos los pares
    j bucle2
fin2:
    li a7,1
    ecall
```

**2.3 Mostrar por la consola los números 40 a 122 y el carácter que corresponde a cada
uno de esos códigos, para conseguir un resultado similar al de la imagen inferior.
Consulta las llamadas del sistema de Ripes para saber cómo imprimir el carácter.**

Para consultar las llamadas recordemos que tenemos que ir a `help` > `system calls` y podemos ver que para los chars tenemos que usar el valor `11`

```asm
.data
cod: .string "Código "
car: .string "  - Carácter "
sep: .string ", "
salto: .string \n
.text
li t0,40
li t1,122
la t2,cod
la t3,car
la t4,sep
la t5,salto
bucle3:
    beq t0,t1,fin3
    li a7,4 # sirve para que se muestre un string
    mv a0,t2
    ecall
    mv a0,t0 # movemos el número
    li a7,1 # imprime el número actual
    ecall
    mv a0,t3 # para mostrar carácter
    li a7,4
    ecall
    mv a0,t0 # para mostrar el número como un caracter
    li a7,11
    ecall
    addi t0,t0,1
    li a7,4
    mv a0,t5  # opcional pero es para verlo más limpio con un salto de línea
    ecall
    j bucle3
fin3:
    li a7,10
    ecall
```

**2.4 Imprime por la consola las tablas de multiplicar de los números a 1 a 10 con un
aspecto similar al de la imagen inferior**

```asm
.data
x: .string "x"
igual: .string "="
espacio: .string " "
nueva_linea: .string "\n"

.text
li t0,1       # tabla actual (del 1 al 10)
li t1,10      # límite máximo
la t2,x
la t3,igual
la t5,espacio
la t6,nueva_linea
li t4,1       # multiplicador (del 1 al 10)

bucle4:
    mv a0,t0  # mostramos el primer número
    li a7,1
    ecall
    mv a0,t2  # mostramos x
    li a7,4
    ecall
    mv a0,t4  # mostramos el multiplicador
    li a7,1
    ecall
    mv a0,t3  # mostramos =
    li a7,4
    ecall

    mul a0,t0,t4 # resultado
    li a7,1
    ecall

    mv a0,t5     # espacio entre operaciones
    li a7,4
    ecall
    beq t4,t1,siguiente_tabla # Si t4 == 10, hemos terminado la fila actual
    addi t4,t4,1              # Si no, avanzamos el multiplicador
    j bucle4

siguiente_tabla:
    mv a0,t6     # Imprimimos salto de línea
    li a7,4
    ecall

    beq t0,t1,fin4 # Si ya estábamos en la tabla del 10, terminamos
    addi t0,t0,1   # Pasamos a la siguiente tabla (2, 3...)
    li t4,1        # Reiniciamos el multiplicador a 1
    j bucle4

fin4:
    li a7,10
    ecall
```

**2.5 Almacenar en memoria un vector con los valores 7, 4, 23, 12, 6, 20, 17, 8,
3, 10 y mostrar por consola la media aritmética. Para ello se ha de calcular su
suma y también contar cuántos valores hay en el vector**

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

**2.6 Almacenar en memoria un vector con los valores 7, 4, 23, 12, 6, 20, 17, 8,
3, 10 y escribir un programa que muestre por consola la suma de aquellos
que ocupan posiciones impares, asumiendo que al primer 7 le corresponde la
posición 1 (impar)**

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

**2.7 Modifica el programa del ejercicio previo para que sume todos aquellos valores
del vector que sean números impares, independientemente de la posición que
ocupen en el vector, y muestre el resultado por la consola**

```asm
.data
vector3: .word 7,4,23,12,6,20,17,8,3,10
fin3:

.text
la t0,vector3
la t1,fin3
li a0,0

bucle7:
    lw a1,0(t0)
    andi a2,a1,1
    beqz a2,noimpar
    add a0,a0,a1
noimpar:
    addi t0,t0,4
    blt t0,t1,bucle7

    li a7,1
    ecall
```

**2.8 Usando el mismo vector del ejercicio 2.6, escribe un programa para buscar el
menor y el mayor valor almacenándolos en a0 y a1, respectivamente. Muestra
ambos valores por la consola**

```asm
# Ejercicio 8
.data
vector4: .word 7,4,23,12,6,20,17,8,3,10
fin4:

.text
la t0,vector4
la t1,fin4
lw a0,0(t0) # valor menor
lw a1,0(t0) # valor mayor
# tenemos que asignar por defecto el primero de los elementos del vector

bucle8:
    beq t0,t1,fin8 # si t0=t1
    lw a2,0(t0) # cargamos la primera dirección
    blt a2,a0,menor # si a2<a0 saltamos a menor
    bgt a2,a1,mayor # si a2>a1 saltamos a mayor
    # si no se da ningún caso
    j siguiente

mayor:
    mv a1,a2
menor:
    mv a0,a2
    j siguiente
siguiente:
    addi t0,t0,4
    j bucle8
fin8:
    li a7,1
    ecall
    mv a0,a1
    li a7,1
    ecall

```

**2.9 Almacenar en memoria el vector de valores 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
11, 12, 13, 14, 15, 16. Escribir un programa que lo trate como una matriz de
4×4, como en el listado de la derecha, y calcule la suma de cada una de las filas y
las muestre por consola**

```asm
.data
matriz: .word 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
espacio: .string " "
nueva_linea: .string "\n"

.text
la t0, matriz        # Dirección base de la matriz
la s0, espacio
la s1, nueva_linea

li t1, 4             # Contador de filas (4 filas en total)

bucle_filas:
    beq t1, zero, fin9   # Si t1 == 0, hemos procesado las 4 filas

    li t2, 4         # Contador de elementos por fila (4 columnas)
    li t3, 0         # Acumulador de la suma para la fila actual

bucle_columnas:
    beq t2, zero, imprimir_suma  # Al terminar los 4 elementos, imprimimos

    lw t4, 0(t0)     # Cargamos el número actual
    add t3, t3, t4   # Sumamos al acumulador de la fila

    addi t0, t0, 4   # Avanzamos al siguiente entero en memoria
    addi t2, t2, -1  # Decrementamos contador de columnas
    j bucle_columnas

imprimir_suma:
    # Imprimir el resultado de la suma de la fila
    mv a0, t3
    li a7, 1
    ecall

    # Imprimir un salto de línea
    mv a0, s1
    li a7, 4
    ecall

    addi t1, t1, -1  # Decrementamos contador de filas
    j bucle_filas

fin9:
    li a7, 10        # Finalizar el programa
    ecall


```

**2.10. Modificar el programa anterior para que calcule y muestre la suma de cada una de las columnas de la matriz**

```asm

.data
matrizEj10: .word 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16

.text
la s0,matrizEj10 # S0 apunta a la dirección base
li s1,0 # s1=columna actual
li s2,4 # Límite de columnas

bcolumnas:
    bge s1,s2,finalP # si termino las 4 columnas
    li s3,0 # s3= fila actual
    li a0,0 # a0=acumulador suma columna

bfilas:
    # Desplazmiento de elemento
    bge s3,s2,mostrar_col
    slli t0,s3,2 # t0=fila * 4
    add t0,t0,s1 # t0=fila * 4 + columna
    slli t0,t0,2 # t0=desplazamiento en bytes (*4)

    add t1,s0,t0 # dirección del elemento
    lw t2,0(t1) # cargar el elemento
    add a0,a0,t2  # acumular suma
    addi s3,s3,1 # siguiente fila
    j bfilas

mostrar_col:
    li a7,1
    ecall

    li a7,10 # salto de linea
    li a7,11
    ecall

    addi s1,s1,1 # siguiente col
    j bcolumnas

finalP:
    li a7,10
    ecall

```

**2.11 Almacenar en memoria el vector de valores 6, 1, 6, 7, 2, 3, 6, -3, 6, 1,-2, 3, -5, 2, 6. Escribir un programa que cargue el primer valor del vector, cuente cuántas veces aparece en él y muestre el conteo por consola**

```asm

.data
vectorCont: .word 6,1,6,7,2,3,6,-3,6,1,-2,3,-5,2,6
fin:

.text
la t0,vectorCont
la t1,fin
li a0,0 # contador de apariciones
lw t3,0(t0) # valor buscado
bucle11:
    beq t0,t1,fin11
    lw t4,0(t0) # obtenemos el primer valor
    beq t3,t4,aparece
    addi t0,t0,4
    j bucle11

aparece:
    addi a0,a0,1
    addi t0,t0,4
    j bucle11
fin11:
    li a7,1
    ecall

```

**2.12 Usa el mismo vector del ejercicio previo pero cambia el programa para que
cuente cuántos valores negativos hay y lo muestre por consola.**

```asm
.data
vectorConta: .word 6,1,6,7,2,3,6,-3,6,1,-2,3,-5,2,6
finC:

.text
la t0,vectorConta
la t1,finC
la a0,0 # va a servir para contar las veces que hay un valor negativo
li t2,0 # va a servir para comparar con blt
.text
bucle12:
beq t0,t1,fin12
lw t4,0(t0) # obtenemos el primer valor del vector
blt t4,t2,negativo # si t4<t2 salta a negativo
addi t0,t0,4
j bucle12

negativo:
    addi a0,a0,1
    addi t0,t0,4
    j bucle12

fin12:
    li a7,1
    ecall
```

**2.13 Usa el vector de valores del ejercicio 2.9 interpretado como una matriz de 4×4.
Escribe una función que tome como entrada una fila en a1 y una columna en a2
y devuelva en a0 el valor contenido en esa posición de la matriz. La función solo
podrá alterar el contenido de los registros temporales t0-t6. Llama a la función
para mostrar por consola los valores en las posiciones (0,0), (1,1), (2,2) y
(3,3)**

```asm
.data
matriz: .word 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
espacio: .string " "

.text
main:
    li a1,0 # fila 0
    li a2,0 # columna 0
    jal ra,obtener_elemento
    jal ra,imprimir_resultado

    li a1,1 # fila 1
    li a2,1 # columna 1
    jal ra,obtener_elemento
    jal ra,imprimir_resultado

    li a1,2 # fila 2
    li a2,2 # columna 2
    jal ra,obtener_elemento
    jal ra,imprimir_resultado

    li a1,3 # fila 3
    li a2,3 # columna 3
    jal ra,obtener_elemento
    jal ra,imprimir_resultado

    li a7,10
    ecall

    obtener_elemento:
        la t0,matriz
        # Indice = (fila*4)
        slli t1,a1,2
        add t1,t1,a2

        slli t1,t1,2

        add t2,t0,t1

        lw a0,0(t2)

        ret

    imprimir_resultado:
        li a7,1
        ecall

        la a0,espacio
        li a7,4
        ecall

        ret
```

**Ejercicio 2.15. Escribe una función que tome como entrada —en el registro a0— un valor
numérico y que muestre por consola la secuencia desde 0 hasta a0. Para ello la
función operará de forma recursiva, de manera que ella misma se llamará con
a0 -1 una vez tras otra hasta alcanzar el caso base: que a0 sea igual a 0. Utiliza a pila para guardar tanto la dirección de retorno como los valores que tomará
a0 en cada llamada. Por último, llama a dicha función desde la parte inicial del
programa probando con distintos valores.**

```asm

li a0,15
call recursiva
li a7,10
ecall

recursiva:
    addi sp,sp,-8 # reserva espacio para 2 datos
    sw ra,0(sp) # guarda el valor de retorno a la posición 0 de la pila
    sw a0,4(sp)  # guarda el valor de a en la posición 4 para recuperarlo después


    beqz a0,finrecursiva # si a0 es 0 va a fin
    addi a0,a0,-1 # si no desciende y se vuelve a llamar
    call recursiva

finrecursiva:
    lw a0,4(sp) # recupera el valor de a
    call numero # llama a esto para recuperar el número q tenemos y mostrarlo
    lw ra,0(sp) # recupera de la pila la dirección de retorno
    addi sp,sp(8) # suma 8 para liberar el espacio de la pila
    ret

numero:
    li a7,1
    ecall
    li a7,11
    li a0,13 # para saltar linea
    ecall
    ret

```

**Ejercicio 2.16. El máximo común divisor (MCD) de dos números se calcula de forma muy
sencilla mediante un proceso recursivo como el que muestra el programa en
lenguaje C mostrado al margen. Escribe una implementación análoga de forma
que los registros a1 y a2 contengan los dos números de entrada y a0 el MCD
encontrado que, en último término, sería 1 si ambos números no comparten
ningún otro factor. Llama desde el cuerpo del programa a la función con distintos
valores para verificar su funcionamiento**

```asm

    li a1, 15
    li a2, 30
    call mcd

    # Mostrar el resultado (a0) por consola
    li a7, 1
    ecall

    # Salir del programa
    li a7, 10
    ecall

mcd:
    addi sp, sp, -12    # Espacio para 3 datos
    sw ra, 0(sp)
    sw a1, 4(sp)
    sw a2, 8(sp)

    rem t0, a2, a1      # 1. Calculamos a = a2 % a1 (resto)

    beqz t0, caso_base  # 2. Si el resto es 0, vamos al caso base

    # 3. Paso recursivo: mcd(a, b) -> mcd(t0, a1_antiguo)
    mv a2, a1           # El nuevo segundo argumento (a2) es el a1 actual (b = a1)
    mv a1, t0           # El nuevo primer argumento (a1) es el resto (a)
    call mcd

    # 4. Al volver de la recursión, limpiamos la pila
    lw ra, 0(sp)
    addi sp, sp, 12
    ret

caso_base:
    # Caso base: return b (que es a1)
    mv a0, a1           # El resultado a devolver va en a0

    # Restauramos la pila antes de volver
    lw ra, 0(sp)
    addi sp, sp, 12
    ret

```

**Ejercicio 2.17. Escribe un programa en el que inicialmente se tiene en memoria el vector
primos: .word 2, 3, 5, 7, 11, 13 con los seis primeros números primos. El
programa deberá completar la tabla, agregando los primos adicionales que
encuentre hasta llegar al 100. Con este fin escribe una función que tomando como
entrada un número —en el registro a1— y el número de primos que se tienen
actualmente en el vector —en el registro a2— verifique si dicho número es primo
o no. Para ello, no hay más que comprobar si el número en a1 es divisible por
cualquiera de los valores existentes en el vector. La función devolverá el valor 1
en el registro a0 si el número es primo o 0 en caso contrario. Llama a la función
desde un bucle en el cuerpo principal del programa, guardando cada nuevo
primo en la tabla e incrementando a2. Usa el panel Memory para comprobar el
vector en memoria, como se aprecia en la Figura 2.4. La función que comprueba
si un número es primo puede escribirse tanto de forma iterativa como recursiva.
¿Qué versión es más compleja? ¿Qué versión es más eficiente?**

```asm
.text

.data
primos: .word 2, 3, 5, 7, 11, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
espacio: .string " "

.text
li a2, 6        # Cantidad inicial de primos
li a1, 15       # Primer número a probar si es primo
li t0, 100      # Límite máximo a probar

bucle_principal:
    bgt a1, t0, fin_programa  # Si a1 > 100, terminamos

    jal ra, es_primo          # Llamamos a la función

    # Al volver, a0 vale 1 (primo) o 0 (no primo)
    beqz a0, siguiente_numero # Si a0 == 0, no es primo, probamos el siguiente

    # Si es primo lo tenemos que guardar en el vector
    la t1, primos
    slli t2, a2, 2            # t2 = a2 * 4 bytes (desplazamiento)
    add t1, t1, t2            # t1 = dirección donde guardar el nuevo primo
    sw a1, 0(t1)              # Guardamos a1 en la memoria
    addi a2, a2, 1            # Incrementamos el contador de primos

    # Mostrar el primo encontrado
    mv a0, a1
    li a7, 1                  # Imprimir entero
    ecall
    la a0, espacio
    li a7, 4                  # Imprimir espacio
    ecall

siguiente_numero:
    addi a1, a1, 1            # Probamos el siguiente número (16, 17, 18...)
    j bucle_principal

fin_programa:
    li a7, 10
    ecall

#  a1 = número, a2 = cantidad de primos actual
#  a0 = 1 (si es primo), a0 = 0 (si no lo es)
es_primo:
    addi sp, sp, -4           # Guardamos solo ra (es el único registro imprescindible)
    sw ra, 0(sp)

    la t1, primos     # Apuntamos al inicio del vector
    li t5, 0          # Contador de cuántos primos hemos probado (0, 1, 2...)

bucle_comprobacion:
    beq t5, a2, es_primo_si   # Si ya probamos con todos los primos del vector y ninguno lo dividió, ES PRIMO

    lw t3, 0(t1)              # Cargar el primo actual
    rem t4, a1, t3            # t4 = a1 % t3
    beqz t4, es_primo_no      # Si el resto es 0, ES DIVISIBLE -> NO ES PRIMO

    addi t1, t1, 4            # Siguiente posición del vector (+4 bytes)
    addi t5, t5, 1            # Avanzar contador de primos probados
    j bucle_comprobacion

es_primo_no:
    li a0, 0                  # Retorna 0
    j fin_es_primo

es_primo_si:
    li a0, 1                  # Retorna 1

fin_es_primo:
    lw ra, 0(sp)              # Recuperamos la dirección de retorno
    addi sp, sp, 4
    ret
```
