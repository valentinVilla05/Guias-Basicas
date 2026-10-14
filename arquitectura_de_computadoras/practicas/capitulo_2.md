# Capítulo 2: Bucles y Condicionales

La posibilidad de ejecutar o salir de cierto bloque de instrucciones según que se cumpla una determinada condición la haremos con if/ else o la capacidad de repetir la ejecución de un bloque con for o while con ensamblador mediante la **alteración del flujo del programa** que permite cambiar el contenido del **contador de programa**.

## Instrucciones de salto

Modifican `pc` asignándole un valor general que será simbolizado por `etiquetas` sin tener que calcular manualmente las distintas direcciones

A las instrucciones anteriores de la tabla le añadiremos otras 8 más que serán las instrucciones de salto

| Instrucción          | Condición                            |
| -------------------- | ------------------------------------ |
| `beq` rs1, rs2, imm  | salta si rs1= rs2                    |
| `bne` rs1, rs2, imm  | salta si rs1 $\neq$ rs2              |
| `bge` rs1, rs2, imm  | salta si rs1 $\geq$ rs2              |
| `bgeu` rs1, rs2, imm | igual que `bge` pero sin signo       |
| `blt` rs1, rs2, imm  | salta si rs1 $<=$ rs2                   |
| `bltu` rs1, rs2, imm | Igual que la anterior pero sin signo |

> Rango de los saltos: los condicionales usan un desplazamiento de 12 bits (≈ ±4 KB) y `jal` uno de 20 bits (≈ ±1 MB).

El valor inmediato + `pc` determina a donde debe saltar `pc` en el caso que se cumpla la condición sobre ambos registros limitado a 12 bits

También se definen otras seudoinstrucciones como `bgt`, `bgtu`, `ble` y `bleu`,
que toman los mismos argumentos que las instrucciones previas, y `beqz`, `bnez`,
`bgez`, `blez` y `bgtz` en las que rs2= `zero` **SIEMPRE**

La seudoinstrucción `bnez` compara el contenido de `a0` con el registro `zero` y si no coinciden , ejecuta el salto de forma que el bucle se repetirá hasta que `a0` contenga `0`

![alt text](../images/corre.png)

Ejemplo de `if/else`: se ejecuta `a0 = a1 - a2` si `a1 >= a2` y `a0 = a2 - a1` en caso contrario. Se salta a `mayora2` cuando `a2 >= a1`, y `j fin` evita ejecutar también el `else`.

**Bucle** (cuenta atrás de 10 a 1):

```asm
    li a0, 10
    li a7, 1
repite:
    ecall              # imprime a0
    addi a0, a0, -1
    bnez a0, repite    # repite mientras a0 != 0
```

Equivalente en C: `for (int a0 = 10; a0 > 0; a0--) ...`

## Saltos Incondicionales

- `jal` rd, imm : Es de tipo U que cuenta con 2 operandos. En `rd` se guarda `pc` actual y después el valor de `pc` pasa a ser `pc + imm` con un desplazamiento de 20 bits.

- `jalr` rd, rs, imm: Es una instrucción de tipo I que cuenta con tres operandos. En rd se guardará el actual contenido del `pc`, y después se actualizará asignándole el resultado de la suma `rs + imm`. Esto nos permite saltar a cualquier punto del programa, sin las limitaciones de los desplazamientos de 12 o 20 bits respecto a la posición actual de `pc`.

Como primer parámetro podemos usar el registro `ra` (`x1`) para la seudoinstrucción `jal imm` -> `jal x1, imm` de forma que no es obligatorio expresar de forma explícita el registro de destino.

- `jal imm` equivale a `jal x1, imm` (guarda el retorno en `ra`)
- `j imm` equivale a `jal x0, imm` (salta sin guardar retorno, se descarta `pc`)

> Nota: en la especificación oficial de RISC-V, los saltos condicionales son de tipo **B** y `jal` es de tipo **J**. El libro los llama tipo S y tipo U.

## Llamadas a Subrutinas

`call` se guarda en `ra` la dirección de pc `pc + 4`, es decir, la instrucción siguiente.

`ret` toma a `ra` la dirección de retorno, enviando a `x0` el actual valor de `pc`. `ret` equivale a `jalr x0, ra, 0`

`call`/`ret` no permiten llamadas anidadas sin guardar `ra` porque se perdería la dirección de retorno

## Llamadas del sistema en Ripes (`ecall`)

El número de la función se carga en `a7` y el argumento en `a0`.

| `a7` | Función                             |
| ---- | ----------------------------------- |
| 1    | Imprimir entero (decimal)           |
| 4    | Imprimir cadena (dirección en `a0`) |
| 10   | Terminar el programa                |
| 11   | Imprimir carácter                   |
| 34   | Imprimir entero en hexadecimal      |

...

![ecalls](../images/ecalls.png)

## Otras instrucciones

### Instrucciones Lógicas

- Se usan las que hemos visto anteriormente: `and`, `andi`.... Y se añaden otras
- `or`/`ori`: OR bit a bit entre `rs1` y `rs2` (o `imm`)
- `xor`/`xori`: XOR bit a bit entre `rs1` y `rs2` (o `imm`)

| Instrucción         | Funcionamiento                                                                                           |
| ------------------- | -------------------------------------------------------------------------------------------------------- |
| `sll` rd, rs1, rs2  | Desplaza el valor en rs1 hacia la izquierda tantos bits como rs2 y guarda en rd                          |
| `slli` rd, rs1, imm | Igual pero con un valor inmediato                                                                        |
| `srl` rd, rs1, rs2  | Desplaza el contenido de rs1 hacia la derecha tantos bits indique `rs2` y guarda en rd                   |
| `srli` rd, rs1, imm | igual pero con inmediato                                                                                 |
| `sra` rd, rs1, rs2  | Desplaza el contenido de `rs1` hacia la derecha tantos bits como indique `rs2` y tomando el bit de signo |
| `srai` rd, rs1, imm | Como `sra` pero con inmediato                                                                            |

Algunos trucos para tratar con estas instrucciones:

- `sll`/`srl` desplazan **todos** los bits por igual (lógico). `sra` conserva el bit de signo (aritmético).
- Desplazar _n_ bits a la izquierda equivale a **multiplicar por 2ⁿ**, y a la derecha a **dividir por 2ⁿ**. Es más eficiente que `mul`/`div`.
- **Par o impar**: `andi t0, a0, 1` deja 0 si es par y 1 si es impar. Después se usa `beqz`.

### Instrucciones de comparación

**Estas no alteran el valor de `pc`** se limitan a almacenar `0` o `1`

| Instrucción          | Operandos | Signo     |
| -------------------- | --------- | --------- |
| `slt` rd, rs1, rs2   | registros | con signo |
| `sltu` rd, rs1, rs2  | registros | sin signo |
| `slti` rd, rs1, imm  | inmediato | con signo |
| `sltiu` rd, rs1, imm | inmediato | sin signo |

Intercambiando los operandos se obtiene el equivalente a `sgt`.

**Ejemplo**: contar valores menores que 5 **sin saltos condicionales**:

```asm
    la t0, notas
    li t1, 10          # nº de elementos
    li a0, 0           # contador
bucle:
    lw a2, 0(t0)
    slti a1, a2, 5     # a1 = 1 si a2 < 5
    add a0, a0, a1     # suma 0 o 1
    addi t1, t1, -1
    addi t0, t0, 4
    bnez t1, bucle
```

Como vemos/veremos en teoría, evitar saltos es importante en un procesador segmentado (riesgos de control).

> Si `rs1 < rs2` entonces `rd = 1` y en caso contrario `rd = 0`

### Otras seudoinstrucciones

- `not` rd, rs: complemento a uno de rs y almacena en rd. Equivale a `xori rd, rs, -1`.
- `neg` rd, rs: complemento a 2 de rs y almacena en rd. Equivale a `sub rd, x0, rs`.
- `nop` no hace nada solo consume uno o más ciclos de reloj. Equivale a `addi x0, x0, 0`.

### ---Recordatorio---

**Complemento a uno**: invierte todos los bits

**Complemento a dos**: invirtiendo todos los bits y sumando 1

## Almacenamiento temporal de datos en la pila

Una función puede modificar cualquiera de sus registros temporales: `t0` a `t6` o registros `a0` a `a7`. Si el código que la llama necesita conservar alguno, debe guardarlo él mismo. El resto de registros (`s0`-`s11`) los debe preservar la propia función si los usa.

| Registros                  | Los preserva                  |
| -------------------------- | ----------------------------- |
| `t0`-`t6`, `a0`-`a7`, `ra` | Quien llama (_caller_)        |
| `s0`-`s11`, `sp`           | La función llamada (_callee_) |

En Ripes, al pasar el ratón sobre un registro aparece `Saver: Caller` o `Saver: Callee`.

**Pasos**

**1. Reservar en la pila el espacio necesario**: como crece hacia **abajo** tenemos que restar el valor a `sp` y siempre ha de ser un múltiplo de 16

**2. Guardar el contenido de los registros apropiados en el espacio reservado de la pila**: Se usa el registro sp y un desplazamiento

**3. Realizar la tarea que la función tenga encomendada**

**4. Restaurar el contenido de los registros del paso 2 cargándolos desde la pila con los mismos desplazamientos sobre `sp`**

**5. Ajustar el registro `sp` para liberar el espacio del paso 1**

![almacenarEnPila](../images/almacenarPilaEjemplo.png)

Ejemplo `pow(base, exp)`: la función usa 5 registros (`ra`, `gp`, `s0`, `s1`, `s2`), es decir, 5 × 4 B = 20 B. Como `sp` debe ser múltiplo de 16, se reservan **32 B** (`addi sp, sp, -32`). Cada registro se guarda con un desplazamiento distinto (0, 4, 8, 12, 16) y se restaura con los mismos al final, antes de `addi sp, sp, 32`.

## La pila para transferir parámetros a funciones

El número de registros de la CPU es limitado por lo que será preciso recurrir a la memoria para almacenar datos, (se usará en funciones con muchos parámetros)

Hasta 8 registros de `a0` a `a7` están destinados a facilitar la transferencia de parámetros al invocar a una función y del noveno argumento en adelante se pasan por la pila. 

**SE USAN EN ORDEN**; si solo necesitamos 2 -> `a0` y `a1`

![funcionAvg](../images/avg.png)

Ejemplo `avg` (media de 10 valores): los 8 primeros van en `a0`-`a7`, y el 9º y el 10º se guardan en la pila desde `main` (`sw t0, 0(sp)` y `sw t0, 4(sp)`). Al terminar, `main` libera el espacio con `addi sp, sp, 16`.

Dentro de `avg`, `s0` se usa como **frame pointer**: `addi s0, sp, 16` guarda el valor original de `sp` antes de reservar espacio, para leer los parámetros extra con `lw t0, 0(s0)` y `lw t0, 4(s0)`. El resultado se devuelve en `a0`.

## Funciones recursivas y la pila

Cuando escribimos una función de lenguaje de alto nivel, el compilador genera en cada llamada un `stack frame` con los parámetros y la dirección de retorno. Por ejemplo para calcular un factorial

```c
int factorial(int n){
    if(n==1)
        return n;
    else
        return n*factorial(n-1);
}
```

![alt text](../images/factorial.png)

Un compilador en C produce el código ensamblador preciso para ir ajustando el registro `sp`, almacenar y extraer datos de la pila. Y se tendrá que implementar de forma manual:

![alt text](../images/imfacto.png)

Las tres primeras líneas hacen `stack frame` y guardan en la pila la dirección de retorno y valor actual del parámetro de entrada. Después se actualiza ese parámetro y con un condicional se determina si ha alcanzado el caso base. Se produce una nueva llamada a la misma función si no se da el caso. Al llegar al caso base se recupera de la pila el parámetro y se hace la operación correspondiente

# RESUMEN DE LAS INSTRUCCIONES RISC-V

## 1. Saltos condicionales

| Instrucción | Operandos | ¿Qué hace? | Ejemplo / Notas |
|---|---|---|---|
| `beq` | `rs1, rs2, etiqueta` | Salta si `rs1 == rs2`. | `beq t0, t1, fin` |
| `bne` | `rs1, rs2, etiqueta` | Salta si `rs1 != rs2`. | `bne a0, zero, bucle` |
| `blt` | `rs1, rs2, etiqueta` | Salta si `rs1 < rs2` (con signo). | `blt a0, t0, menor` |
| `bltu` | `rs1, rs2, etiqueta` | Salta si `rs1 < rs2` (sin signo). | Comparación sin signo. |
| `bge` | `rs1, rs2, etiqueta` | Salta si `rs1 >= rs2` (con signo). | `bge a2, a1, mayor` |
| `bgeu` | `rs1, rs2, etiqueta` | Salta si `rs1 >= rs2` (sin signo). | Comparación sin signo. |

### Seudoinstrucciones de salto

| Seudoinstrucción | Se traduce como | ¿Qué hace? |
|---|---|---|
| `beqz rs, etiqueta` | `beq rs, zero, etiqueta` | Salta si `rs == 0`. |
| `bnez rs, etiqueta` | `bne rs, zero, etiqueta` | Salta si `rs != 0`. |
| `bgtz rs, etiqueta` | `blt zero, rs, etiqueta` | Salta si `rs > 0`. |
| `bgt rs1, rs2, etq` | `blt rs2, rs1, etq` | Salta si `rs1 > rs2`. |
| `ble rs1, rs2, etq` | `bge rs2, rs1, etq` | Salta si `rs1 <= rs2`. |

---

## 2. Saltos incondicionales y funciones

Cambian el flujo de ejecución sin comprobar ninguna condición.

| Instrucción | Operandos | ¿Qué hace? | ¿Para qué se usa? |
|---|---|---|---|
| `jal` | `rd, etiqueta` | Guarda `pc + 4` en `rd` y salta a `etiqueta`. | Llamadas a funciones o saltos con retorno. |
| `jalr` | `rd, rs, imm` | Guarda `pc + 4` en `rd` y salta a la dirección `rs + imm`, poniendo a cero el bit menos significativo. | Saltos a direcciones almacenadas en registros y retornos. |
| `j` | `etiqueta` | Equivale a `jal zero, etiqueta`. | Saltar sin guardar dirección de retorno. |
| `call` | `etiqueta` | Llama a una función y guarda la dirección de retorno en `ra`. | Ejecutar una subrutina. |
| `ret` | Ninguno | Equivale a `jalr zero, ra, 0`. | Volver de una función. |

---

## 3. Operaciones lógicas (manipulación de bits)

| Instrucción | Operandos | Operación |
|---|---|---|
| `and` | `rd, rs1, rs2` | `rd = rs1 AND rs2` (bit a bit). |
| `andi` | `rd, rs1, imm` | `rd = rs1 AND imm`. |
| `or` | `rd, rs1, rs2` | `rd = rs1 OR rs2` (bit a bit). |
| `ori` | `rd, rs1, imm` | `rd = rs1 OR imm`. |
| `xor` | `rd, rs1, rs2` | `rd = rs1 XOR rs2` (bit a bit). |
| `xori` | `rd, rs1, imm` | `rd = rs1 XOR imm`. |
| `sll` | `rd, rs1, rs2` | Desplazamiento lógico a la izquierda. |
| `slli` | `rd, rs1, imm` | Desplazamiento lógico a la izquierda usando un inmediato. |
| `srl` | `rd, rs1, rs2` | Desplazamiento lógico a la derecha. |
| `srli` | `rd, rs1, imm` | Desplazamiento lógico a la derecha usando un inmediato. |
| `sra` | `rd, rs1, rs2` | Desplazamiento aritmético a la derecha. |
| `srai` | `rd, rs1, imm` | Desplazamiento aritmético a la derecha usando un inmediato. |

### Diferencias entre desplazamientos

- `sll`: desplaza los bits a la izquierda e introduce ceros por la derecha.
- `srl`: desplaza los bits a la derecha e introduce ceros por la izquierda.
- `sra`: desplaza los bits a la derecha conservando el bit de signo.

---

## 4. Instrucciones de comparación (Set Less Than)

Guardan `1` si la condición es verdadera y `0` si es falsa.

| Instrucción | Operandos | Condición evaluada | Resultado en `rd` |
|---|---|---|---|
| `slt` | `rd, rs1, rs2` | `rs1 < rs2` (con signo). | `1` si es menor; `0` si no. |
| `sltu` | `rd, rs1, rs2` | `rs1 < rs2` (sin signo). | `1` si es menor; `0` si no. |
| `slti` | `rd, rs1, imm` | `rs1 < imm` (con signo). | `1` si es menor; `0` si no. |
| `sltiu` | `rd, rs1, imm` | Comparación menor que inmediata sin signo. | `1` si es menor; `0` si no. |

### Ejemplo

```asm
slt t0, a0, a1
Si a0 < a1, se guarda 1 en t0. Si no, se guarda 0.
```

## 5. Memoria, pila y sistema

| Instrucción | Operandos | ¿Qué hace? | Uso habitual |
|---|---|---|---|
| `lw` | `rd, imm(rs)` | Lee 4 bytes de memoria en la dirección `rs + imm` y los guarda en `rd`. | `lw ra, 0(sp)` (cargar desde la pila). |
| `sw` | `rs2, imm(rs1)` | Escribe 4 bytes de `rs2` en la dirección `rs1 + imm`. | `sw ra, 0(sp)` (guardar en la pila). |
| `ecall` | Ninguno | Solicita un servicio al sistema operativo o simulador, según el valor de `a7`. | Imprimir en pantalla, leer datos o salir del programa. |

### Ejemplos

```asm
lw t0, 0(sp)      # Carga una palabra desde la dirección apuntada por sp
sw ra, 0(sp)      # Guarda ra en la dirección apuntada por sp
ecall             # Solicita un servicio al sistema
```
> Importante: **lw** y **sw** no modifican automáticamente sp. Para gestionar la pila, normalmente se utiliza **addi** para actualizar el puntero


## 6. Otras seudoinstrucciones útiles

| Seudoinstrucción | Se traduce como | Función |
|---|---|---|
| `li rd, imm` | `addi rd, zero, imm` / `lui` (según el valor) | Carga una constante en un registro. |
| `mv rd, rs` | `addi rd, rs, 0` | Copia el valor del registro `rs` en `rd`. |
| `la rd, etiqueta` | Varias instrucciones | Carga la dirección de memoria de una variable o cadena. |
| `not rd, rs` | `xori rd, rs, -1` | Complemento a uno: invierte todos los bits de `rs`. |
| `neg rd, rs` | `sub rd, zero, rs` | Complemento a dos: cambia el signo del valor de `rs`. |
| `nop` | `addi zero, zero, 0` | No realiza ninguna operación útil. |

### Ejemplos

```asm
li a7, 10         # Carga una constante en a7
mv t0, a0         # Copia el valor de a0 en t0
la a0, mensaje    # Carga la dirección de mensaje en a0
not t0, t1        # Invierte todos los bits de t1
neg t0, t1        # Cambia el signo de t1 y guarda el resultado en t0
nop               # No realiza ninguna operación útil
```
## 7. Resumen rápido para memorizar

| ¿Qué quiero hacer? | Instrucción | ¿Qué hace? |
|---|---|---|
| Saltar si dos registros son iguales. | `beq` | Salta si `rs1 == rs2`. |
| Saltar si dos registros son diferentes. | `bne` | Salta si `rs1 != rs2`. |
| Saltar si un registro es menor que otro (con signo). | `blt` | Salta si `rs1 < rs2`. |
| Saltar si un registro es menor que otro (sin signo). | `bltu` | Compara los valores sin signo. |
| Saltar si un registro es mayor o igual que otro (con signo). | `bge` | Salta si `rs1 >= rs2`. |
| Saltar si un registro es mayor o igual que otro (sin signo). | `bgeu` | Compara los valores sin signo. |
| Saltar directamente a una etiqueta. | `j etiqueta` | Salta sin comprobar ninguna condición. |
| Llamar a una función. | `call etiqueta` | Salta a una función y guarda la dirección de retorno. |
| Volver de una función. | `ret` | Regresa al punto desde donde se llamó a la función. |
| Comparar dos registros y guardar el resultado. | `slt` / `sltu` | Guarda `1` si el primero es menor y `0` si no. |
| Hacer una operación AND entre bits. | `and` / `andi` | Conserva los bits que son `1` en ambos operandos. |
| Hacer una operación OR entre bits. | `or` / `ori` | Pone `1` si alguno de los bits es `1`. |
| Hacer una operación XOR entre bits. | `xor` / `xori` | Pone `1` si los bits son diferentes. |
| Desplazar bits a la izquierda. | `sll` / `slli` | Desplaza los bits a la izquierda e introduce ceros. |
| Desplazar bits a la derecha introduciendo ceros. | `srl` / `srli` | Desplaza los bits a la derecha sin conservar el signo. |
| Desplazar bits a la derecha conservando el signo. | `sra` / `srai` | Desplaza los bits a la derecha conservando el bit de signo. |
| Leer una palabra de memoria. | `lw` | Carga 4 bytes de memoria en un registro. |
| Escribir una palabra en memoria. | `sw` | Guarda 4 bytes de un registro en memoria. |
| Cargar una constante en un registro. | `li` | Guarda un valor inmediato en un registro. |
| Copiar el valor de un registro. | `mv` | Copia el valor de un registro a otro. |
| Cargar una dirección de memoria. | `la` | Guarda la dirección de una variable o cadena en un registro. |
| Invertir todos los bits. | `not` | Cambia los `0` por `1` y los `1` por `0`. |
| Cambiar el signo de un número. | `neg` | Calcula el opuesto del valor. |
| No realizar ninguna operación útil. | `nop` | No modifica ningún registro ni dato útil. |
| Solicitar un servicio al sistema. | `ecall` | Ejecuta un servicio, como imprimir o finalizar el programa. |

### Diferencia entre comparaciones con signo y sin signo

- **Con signo:** `blt`, `bge`, `slt`, `slti`. Interpretan los valores como números positivos o negativos.
- **Sin signo:** `bltu`, `bgeu`, `sltu`, `sltiu`. Interpretan los valores como números no negativos, sin bit de signo.

### Diferencia entre saltar y comparar

- **Saltos:** `beq`, `bne`, `blt`, `bge`, etc. Cambian el flujo del programa si se cumple una condición.
- **Comparaciones:** `slt`, `sltu`, `slti`, `sltiu`. No saltan; guardan `1` o `0` en un registro.
