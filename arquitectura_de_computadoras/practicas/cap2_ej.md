# Tema 2: Ejercicios

> Se admiten soluciones alternativas

**2.1 Sumar los valores 1 a 1000, acumulando la suma en el registro a0, y mostrar el
resultado por la consola**

```asm
.text

li a0,0 # Inicializamos el acumulador a 0 
li t0,1 # To será el contador que usaremos, en este caso inicializamos a 1
li t1,1000 # t1 es el límite (queremos llegar hasta este número)

bucle:
    bgt t0,t1,fin # bgt significa saltar si es mayor (be greater than)
    add a0,a0,t0 # vamos sumando en el acumulador
    addi t0,t0,1 # vamos sumando en el contador
    j bucle # vuelve al inicio del bucle (j= JUMP)
    
fin:
    li a7,1
    ecall

    li a7,10
    ecall
    
```

**2.2 Sumar los valores impares entre 1 y 1000 en el registro a0 y mostrar el resultado
por la consola**

(Exactamente igual que el anterior pero tenemos que añadir la línea marcada)
```asm
.text
li a0,0
li t0,1
li t1,1000

bucle2:
    bgt t0,t1,fin2 # salta si t0 > 1000
    add a0,a0,t0 
    addi t0,t0,2 # Vamos sumando el contador de 2 en 2 para que sea impar
    j bucle2
    
fin2:
    li a7,1
    ecall

    li a7,10
    ecall
```

**2.3 Mostrar por la consola los números 40 a 122 y el carácter que corresponde a cada
uno de esos códigos, para conseguir un resultado similar al de la imagen inferior.
Consulta las llamadas del sistema de Ripes para saber cómo imprimir el carácter.**

Para consultar las llamadas recordemos que tenemos que ir a `help` > `system calls` y podemos ver que para los chars tenemos que usar el valor `11`

```asm
.text
li s0,40 # inicializamos el primer registro a 40
li s1,122 # el segundo registro marca el límite

bucle3:
    bgt s0,s1,fin3 # salta si 40 > 122 a fin
    mv a0,s0
    li a7,1 # Imprimimos el número entero
    ecall
    li a0,32 # 32 en formato ascii marca ' '
    li a7,11
    ecall
    mv a0,s0
    li a7,11
    ecall
    li a0,10 # 10 en formato ascii representa un salto de linea
    li a7,11
    ecall
    addi s0,s0,1 # vamos al siguiente número del bucle
    j bucle3
fin3:
    li a7,10 # salimos del programa
    ecall

```

**2.4 Imprime por la consola las tablas de multiplicar de los números a 1 a 10 con un
aspecto similar al de la imagen inferior**

```asm
.text
li s0,1 # s0 = Fila (empieza en la tabla del 1)
li s2,10 # s2= Multiplica hata el 10

bucle_filas:
    bgt s0,s2,fin4 # si el núm de tabla > 10 terminamos
    li s1,1 # s1 = Columna
    
bucle_columnas:
    bgt s1,s2,siguiente_fila # Si el multiplicador > 10 salta al bucle de la siguiente fila
    mv a0,s0
    li a7,1
    ecall
    
    # Imprimimos la x en ascii
    li a0,120 # ASCII 120=x
    li a7,11
    ecall
    
    # Mostramos la columna
    mv a0,s1
    li a7,1
    ecall
    
    # Mostramos '='
    li a0,61
    li a7,11
    ecall
    
    # Mostramos el resultado
    mul t0,s0,s1
    mv a0,t0
    li a7,1
    ecall
    
    # Imprimimos el espacio
    li a0,32 # Ascii 32 = ' '
    li a7,11
    ecall
    
    addi s1,s1,1
    j bucle_columnas
    
siguiente_fila:
    li a0,10
    li a7,11
    ecall
    
    addi s0,s0,1
    j bucle_filas
fin4:
    li a7,10
    ecall
```

**2.5 Almacenar en memoria un vector con los valores 7, 4, 23, 12, 6, 20, 17, 8,
3, 10 y mostrar por consola la media aritmética. Para ello se ha de calcular su
suma y también contar cuántos valores hay en el vector**

```asm
.data
vector: .word 7,4,23,12,6,20,17,8,3,10 # Inicializamos los números enteros 32 bits (4 cada uno)
fin_vector: #almacenará donde termina la memoria del vector

.text
la s0,vector # s0 = puntero a la base del vector
la s1,fin_vector # s1=puntero al fin del vecctor
li t0,0 # t0= Suma acumulada
li t1,0 # t1= contador de elementos

bucles:
    bge s0,s1,calcular_media # bge compara si s0 es >= a s1
    lw t2,0(s0) # carga en t2 el valor apuntado por s0
    add t0,t0,t2 # suma=suma + valor leido
    addi t1,t1,1 # contador=contador+1
    addi s0,s0,4 # para apuntar al proximo elemento
    j bucles
calcular_media:
    div a0,t0,t1 # a0=suma/contador
    li a7,1
    ecall

    li a7,10
    ecall
    

```

**2.6 Almacenar en memoria un vector con los valores 7, 4, 23, 12, 6, 20, 17, 8,
3, 10 y escribir un programa que muestre por consola la suma de aquellos
que ocupan posiciones impares, asumiendo que al primer 7 le corresponde la
posición 1 (impar)**

```asm
.data
    vector2: .word 7,4,23,12,6,20,17,8,3,10
    fin_vector2:
        
.text
    la s0,vector2
    la s1,fin_vector2
    li a0,0
    
.bucle:
    bge s0,s1,fin6 # si s0>=s1 salta a fin
    lw t0,0(s0)
    add a0,a0,t0 # a0=a0+t0
    addi s0,s0,8 # vamos aumentando el contador de programa, como solo quiere la posiciones impares nos saltamos la siguiente
    j bucle
fin6:
    li a7,1
    ecall
    
    li a7,10
    ecall
```

**2.7 Modifica el programa del ejercicio previo para que sume todos aquellos valores
del vector que sean números impares, independientemente de la posición que
ocupen en el vector, y muestre el resultado por la consola**

```asm
.data
    vector4: .word 7,4,23,12,6,20,17,8,3,10
    fin_vector4:
        
.text
    la s0,vector4
    la s1,fin_vector4
    
    lw t0,0(s0)
    mv a0,t0 # a0=menor
    mv a1,t0 # a1=mayor
    addi s0,s0,4 # para seguir avanzando
bucle8:
    bge s0,s1,mostrar_resultados # si s0==s1
    lw t0,0(s0)
    blt t0,a0,actualizar_menor # Branch if less than (saltar si t0<a0)
comprobar_mayor:
    bgt t0,a1,actualizar_mayor
siguiente:
    addi s0,s0,4
    j bucle8
actualizar_menor:
    bgt t0,a1,actualizar_mayor
actualizar_mayor:
    mv a1,t0
    j siguiente
mostrar_resultados:
    li a7,1
    ecall
    
    li a0,32 # imprimimos un espacio
    li a7,11
    ecall
    
    mv a0,a1
    li a7,1
    ecall
    
    li a7,10
    ecall
```

**2.8 Usando el mismo vector del ejercicio 2.6, escribe un programa para buscar el
menor y el mayor valor almacenándolos en a0 y a1, respectivamente. Muestra
ambos valores por la consola**

```asm
# Ejercicio 8
.data
    vector4: .word 7,4,23,12,6,20,17,8,3,10
    fin_vector4:

.text
    la s0,vector4
    la s1,fin_vector4

    lw t0,0(s0)
    mv a0,t0 # a0=menor
    mv a1,t0 # a1=mayor
    addi s0,s0,4 # siguiente elemento

bucle8:
    bge s0,s1,mostrar_resultados # si llega al final
    lw t0,0(s0)
    blt t0,a0,actualizar_menor # t0 < a0
comprobar_mayor:
    bgt t0,a1,actualizar_mayor # t0 > a1
siguiente:
    addi s0,s0,4
    j bucle8

actualizar_menor:
    mv a0,t0 # nuevo menor
    j comprobar_mayor

actualizar_mayor:
    mv a1,t0 # nuevo mayor
    j siguiente

mostrar_resultados:
    mv s2,a1 # guardamos el mayor antes de cambiar a0
    li a7,1
    ecall # imprime menor

    li a0,32 # espacio
    li a7,11
    ecall

    mv a0,s2
    li a7,1
    ecall # imprime mayor

    li a7,10
    ecall # salir
```

**2.9 Almacenar en memoria el vector de valores 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
11, 12, 13, 14, 15, 16. Escribir un programa que lo trate como una matriz de
4×4, como en el listado de la derecha, y calcule la suma de cada una de las filas y
las muestre por consola**

```asm

.data
    matriz: .word 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
    fin_matriz:
        
.text
    la s0,matriz # s0= Puntero de memoria que recorre la matriz
    li s1,4 # s1=num de filas (4)
    li s2,4 # s2=num de columnas por fila(4)
    li t0,0 # t0= Contador de filas hechas
    
bucle_filas2:
    bge t0,s1,finMat
    li t1,0 # t1= Contador de columnas
    li a0,0 # a0=suma de la fila actual
    
bucle_columnas2:
    bge t1,s2,mostrar_fila
    lw t2,0(s0)
    add a0,a0,t2
    
    addi s0,s0,4
    addi t1,t1,1
    j bucle_columnas2
    
mostrar_fila:
    li a7,1
    ecall
    
    li a0,10 # salto de linea en ascii
    li a7,11 # sevicio 11= imprimir caracter

    addi t0,t0,1
    j bucle_filas2
finMat:
    li a7,10
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
    vector11: .word 6, 1, 6, 7, 2, 3, 6, -3, 6, 1, -2, 3, -5, 2, 6
    final_vector:
        
.text
    la s0,vector11
    la s1,final_vector
    lw t0,0(s0) # t0= primer valor a buscar
    li a0,0 # a0= contador de coincidencias
bucle11:
    bge s0,s1,finalV # si llega al final del vector salta 
    lw t1,0(s0) # Elemento actual
    bne t1,t0,sig # si no es igual salta
    addi a0,a0,1 # si es igual , contador ++
    
sig:
    addi s0,s0,4 # siguiente elemento 
    j bucle
finalV:
    li a7,1
    ecall
    li a7,10
    ecall
    
```

**2.12 Usa el mismo vector del ejercicio previo pero cambia el programa para que
cuente cuántos valores negativos hay y lo muestre por consola.**

```asm

.data
    v12: .word 6, 1, 6, 7, 2, 3, 6, -3, 6, 1, -2, 3, -5, 2, 6
    f_vector:
.text
    la s0,vector
    la s1,f_vector
    
    li a0,0 # contador de negativos
bucle12:
    bge s0,s1,fin12
    lw t0,0(s0) # t0= elemento actual
    
    bge t0,zero,sigg # si t0>= 0 salta
    addi a0,a0,1 # si es negativo contador ++
    
sigg:
    addi s0,s0,4 # siguiente elemento 
    j bucle12
    
fin12:
    li a7,1
    ecall
    li a7,10
    ecall
```

**2.13 Usa el vector de valores del ejercicio 2.9 interpretado como una matriz de 4×4.
Escribe una función que tome como entrada una fila en a1 y una columna en a2
y devuelva en a0 el valor contenido en esa posición de la matriz. La función solo
podrá alterar el contenido de los registros temporales t0-t6. Llama a la función
para mostrar por consola los valores en las posiciones (0,0), (1,1), (2,2) y
(3,3)**

