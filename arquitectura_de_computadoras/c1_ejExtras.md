# Ejercicios Extras Basados en La Práctica
> La resolución de los ejercicios de cada bloque están al final del documento (se admiten soluciones alternativas)
## Bloque 1: Operaciones y Registros 
**Ejercicio P1.1 (Cálculo combinado)**
Calcula la siguiente expresión utilizando únicamente registros: $(12 - 4) \times 3$. Guarda el resultado final en a0 y muéstralo por consola

---
**Ejercicio P1.2 (División e intercambio de resto/cociente)**
Divide `35` entre `6`. Muestra primero por consola el **resto** y **después el cociente**

---
**Ejercicio P1.3 (Manipulación de inmediatos superiores)**
Sin usar la sección `.data`, asigna al registro `a0` el valor `0x12345000` en una sola instrucción y luego súmale `0x678`. Muestra el resultado por consola.

---
**Ejercicio 1.4: Intercambio de Registros sin Memoria (Swap)**
Inicializa t0 = 15 y t1 = 40. Intercambia sus valores de forma que t0 pase a ser 40 y t1 pase a ser 15 usando un tercer registro auxiliar (t2). Muestra t0 por consola

---------
**Ejercicio 1.5: Evaluación de Polinomio simple ($ax^2 + b$)** Dados $a = 2$, $x = 5$ y $b = 3$, calcula la expresión $2 \cdot 5^2 + 3$. Almacena el resultado en a0 y muéstralo

-----
**Ejercicio 1.6: Promedio Entero de 4 Valores** Calcula el promedio entero de los números 10, 23, 17 y 34. Acumula la suma en a0, efectúa la división en a0 e imprímelo**

----
**Ejercicio 1.7: Multiplicación Eficiente sin mul (Desplazamientos)**
Asigna a t0 el valor 9. Multiplícalo por 8 sin usar la instrucción mul, únicamente usando desplazamiento a la izquierda (slli). Muestra el resultado en a0

----
**Ejercicio 1.8: Descomposición en Minutos y Segundos**
Dado un tiempo total de 185 segundos en el registro t0, calcula cuántos minutos completos y cuántos segundos restantes representa. Imprime primero los minutos y luego los segundos

---
**Ejercicio 1.9: Formar una Máscara de Bits (Aislamiento de Byte)**
Dado el registro t0 = 0xABCD1234, utiliza la instrucción andi (AND Inmediato) para aislar únicamente el último byte (0x34). Imprime el valor resultante en decimal

---
**Ejercicio 1.10: Construcción de un Número de 32 bits Completo**
Carga en a0 el valor exacto hexadecimal 0xDEADBEEF sin usar la sección .data.
(Pista: lui carga los 20 bits superiores. addi suma un signo extendido de 12 bits, por lo que si el bit 11 del número inferior es 1, habrá un acarreo negativo que hay que compensar en el lui)

----

## 2: Carga, Almacenamiento y Punteros
**Ejercicio 2.1: Lectura Básica y Suma Simple**
Declara dos números enteros en memoria (`n1: .word 12` y `n2: .word 8`). Léelos desde la memoria RAM a dos registros, súmalos en a0 e imprime el resultado

**Ejercicio 2.2: Sobrescritura en Memoria (Lectura $\rightarrow$ Modificación $\rightarrow$ Escritura)** Declara un número `x: .word 15` en `.data`. Cárgalo en un registro, súmale 5 y guarda el nuevo resultado de vuelta en la misma posición de memoria x. Al final, vuelve a leerlo desde la RAM e imprímelo en consola.

**Ejercicio 2.3: Intercambio de Valores en RAM (Swap)**
Declara en .data dos variables: `v1: .word 100` y `v2: .word 500`. Intercambia los datos de las posiciones de memoria para que v1 pase a almacenar 500 y v2 pase a almacenar 100

**Ejercicio 2.4: Acceso Indexado por Desplazamiento Fijo**
Dado un vector `datos: .word 10, 20, 30, 40` en `.data`, calcula la suma del primer elemento (10) y el cuarto elemento (40) usando desplazamientos numéricos explícitos (offset(t0)). Guarda el resultado en a0 e imprímelo

**Ejercicio 2.5: Puntero Móvil en Inverso**
Dado un vector `arr: .word 5, 10, 15` en `.data`, inicializa un registro puntero t0 apuntando directamente al último elemento (15). Carga los tres elementos recorriendo el puntero hacia atrás mediante `addi t0, t0, -4`, acumula la suma en a0 e imprímela

**Ejercicio 2.6: Uso Correcto de la Sección `.bss`**
Dado un array de 3 elementos `vector: .word 7, 14, 21`, acumula la suma en a0 usando un puntero. Guarda este resultado en una variable reservada en la sección `.bss` llamada total: `.word 4`

**Ejercicio 2.7: Operación Aritmética Completa entre Vectores** Dados dos vectores en memoria `A: .word 2, 4, 6` y `B: .word 1, 3, 5`, calcula la resta elemento a elemento `($A[0]-B[0]$, $A[1]-B[1]$, $A[2]-B[2]$)`, acumula estas tres restas en a0 e imprímelo por consola

**2.8: Generación e Inserción de un Resultado en Memoria intermedia** Dados tres valores `p1: .word 4`, `p2: .word 5`, `p3: .word 0` (el tercero está vacío/en 0). Multiplica p1 por p2, guarda el producto directamente en la posición de memoria de p3 y luego imprime p3

**Ejercicio 2.9: Copia de Vector a Bloque Reservado en `.bss`**
Dado el vector `origen: .word 100, 200` en `.data`, copia el primer elemento al primer hueco de `destino: .word 8` en `.bss`, y el segundo elemento al segundo hueco de destino

**Ejercicio 2.10: Puntero de Lectura/Escritura Simultánea**
Guarda un arreglo `serie: .word 3, 6, 9` en `.data`. Lee cada elemento con un puntero `t0`, doblaló (multiplícalo por 2) y sobrescribe la misma posición de memoria. Al finalizar, el arreglo en RAM debe ser `6, 12, 18`


# RESOLUCIONES
## Bloque 1
![alt text](/images/b1.png)
![alt text](/images/b12.png)

## Bloque 2
![alt text](/images/b21.png)
![alt text](/images/b22.png)
![alt text](/images/b23.png)
![alt text](/images/b24.png)