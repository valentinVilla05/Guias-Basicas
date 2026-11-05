# Ejercicio 1 

Se tiene un procesador superescalar con emisión desordenada y
retirada ordenada con:
* **Captación** -> 2 instrucciones/ciclo
* **Descodificación** -> 2 instrucciones/ciclo
* **Emisión** -> 2 instrucciones/ciclo
* **Escritura** -> 2 resultados/ciclo en el ROB
* **Retirada** -> 2 instrucciones/ciclo

* Se consideran las siguientes unidades funcionales (UF) con la **latencia**
en ciclos que viene indicada entre paréntesis:
• Una UF de **carga para enteros** (1 ciclo)
• Una UF de **carga para flotantes** (1 ciclo)
• Una UF de **almacenamiento de flotantes** (1 ciclo)
• Dos **ALUS enteras** (1 ciclo)
• Dos **multiplicadores para coma flotante** (3 ciclos)
• No hay limitaciones para el número de líneas de la cola de
instrucciones, ventana de instrucciones, buffer de reorden, puertos de
lectura/escritura, etc

**Tabla**


| Instrucción |
|:---|
| `lw x3, n` |
| `addi x4, x3, 2` |
| `init: flw f1, 0(x3)` |
| `flw f0, y(x2)` |
| `fmul f2, f0, f1` |
| `fsw f2, 0(x2)` |
| `fmul f2, f0, f5` |
| `addi x2, x2, 4` |
| `fsw f2, 0(x2)` |
| `sub x5, x4, x2` |
| `bne x2, x0, init` |


> Hay varios métodos para resolver los ejercicios, lo recomendable es consultar cuál se debe hacer dependiendo del maestro, (en caso de Macarena prefiere la opción 1 mientras que Charte prefiere la opción 2)


# Método 1
> Resolución

**Consideración**: Lo recomendable para estos ejercicios, (especialmente cuanto los enunciados de los ejercicios son largos) es hacer una tabla con un resumen como este:

| Etapa | Número de unidades |
|:---|:---:|
| IF | 2 |
| ID | 2 |
| ISS | 2 |
| ROB | 2 |
| WB | 2 |


| Unidad funcional | Cantidad |
|:---|:---:|
| Load Int | 1 |
| Load Float | 1 |
| Store Float | 1 |
| ALU Int | 1 |
| Mult Float | 3 |

-----
### **También es muy necesario que tengamos en cuenta estas reglas:**
1. **Captación, Descodificación y Emisión (IF, ID, ISS):**

    * Avanzan siempre **en orden estricto** de programa.

    * Respetan el **ancho de banda máximo** (si el límite es 2, solo 2 instrucciones entran a la vez por ciclo)

2. **Ejecución (EX):**
    * Se hace **fuera de orden** (en cuanto esté libre la UF y no haya dependencias de datos RAW)

    * **Duración**: Tantas casillas/ciclos como marque la **latencia** de la UF

3. **Buffer de Reorden y Escritura (ROB, WB):**
    * **Retirada (ROB)**: Debe ser en orden estricto. Una instrucción NO se retira hasta que:
    a. Ha terminado su ejecución (EX)
    b. Todas las instrucciones anteriores ya se han retirado
    
* **Escritura (WB):** Ocurre exactamente el ciclo siguiente a la retirada ($\text{WB} = \text{ROB} + 1$).


### Paso a paso práctico para completarla
1. **Haz la tabla de resumen inicial**: Anota las latencias y los límites de ciclo (ancho de emisión y retirada) para tenerlos a la vista (*la tabla de arriba*)

2. **Rellena IF, ID y ISS en orden**: Haz avanzar las instrucciones en parejas (o según el límite) ciclo tras ciclo

3. **Calcula EX**: Mira si la instrucción necesita un dato de una instrucción anterior. Si depende de un resultado, EX no puede empezar hasta que dicho resultado esté disponible

4. **Asigna ROB y WB en orden**: Mantén la fila de ROB bloqueada si una instrucción rápida acaba antes que una instrucción lenta anterior. La rápida debe esperar en la cola del ROB

----

**Con todo eso en cuenta, resolvemos el ejercicio anterior:**


| Instrucción | IF | ID/ISS | EX | ROB | WB |
|:---|:---:|:---:|:---:|:---:|:---:|
| `lw x3, n` | 1 | 2 | 3 | 4 | 5 |
| `addi x4, x3, 2` | 1 | 2 | 4 | 5 | 6 |
| `init: flw f1, 0(x3)` | 2 | 3 | 4 | 5 | 6 |
| `flw f0, y(x2)` | 2 | 3 | 5 | 6 | 7 |
| `fmul f2, f0, f1` | 3 | 4 | 6-8 | 9 | 10 |
| `fsw f2, 0(x2)` | 3 | 4 | 9 | - | 10 |
| `fmul f2, f0, f5` | 4 | 5 | 6-8 | 9 | 11 |
| `addi x2, x2, 4` | 4 | 5 | 7 | 8 | 11 |
| `fsw f2, 0(x2)` | 5 | 6 | 10 | - | 12 |
| `sub x5, x4, x2` | 5 | 6 | 8 | 10 | 12 |
| `bne x2, x0, init` | 6 | 7 | 8 | - | 13 |

* `fmul` **(filas 5 y 7)** entran juntas a EX en el ciclo 6 porque hay 2 multiplicadores flotantes disponibles y ambas dependencias (f0, f1 y f5) quedan resueltas en el ciclo 5

* `fsw` y `bne` llevan guion (-) en ROB porque no escriben en el banco de registros; los stores modifican la memoria en WB (ciclos 10 y 12) y el salto solo resuelve su condición en EX (ciclo 8)

* `sub x5, x4, x2` **(fila 10) ejecuta en el ciclo 8** porque requiere `x2` actualizado por el `addi` de la fila 8 (que acaba en ciclo 7), pero su retirada en ROB espera al ciclo 10 para respetar el orden estricto tras la segunda multiplicación

* **Retirada de 2 en 2**: Fíjate cómo ROB y WB se agrupan en parejas (4-5, 5-6, 9-10, etc.) porque la CPU está limitada a 2 instrucciones retiradas por ciclo


# Variación 1

| Etapa | Número de unidades |
|:---|:---:|
| IF | 2 |
| ID | 2 |
| ISS | 2 |
| ROB | 2 |
| WB | 2 |

| Unidad funcional | Cantidad |
|:---|:---:|
| Load Int | 1 |
| Load Float | 1 |
| Store Float | 1 |
| ALU Int | 1 |
| **Mult Float** | **3** |

| Instrucción | IF | ID/ISS | EX | ROB | WB |
|:---|:---:|:---:|:---:|:---:|:---:|
| `lw x3, n` | 1 | 2 | 3 | 4 | 5 |
| `addi x4, x3, 2` | 1 | 2 | 4 | 5 | 6 |
| `init: flw f1, 0(x3)` | 2 | 3 | 4 | 5 | 6 |
| `flw f0, y(x2)` | 2 | 3 | 5 | 6 | 7 |
| `fmul f2, f0, f1` | 3 | 4 | 6-8 | 9 | 10 |
| `fsw f2, 0(x2)` | 3 | 4 | 9 | - | 10 |
| `fmul f2, f0, f5` | 4 | 5 | 9-11 | 12 | 13 |
| `addi x2, x2, 4` | 4 | 5 | 6 | 7 | 13 |
| `fsw f2, 0(x2)` | 5 | 6 | 12 | - | 14 |
| `sub x5, x4, x2` | 5 | 6 | 7 | 8 | 14 |
| `bne x2, x0, init` | 6 | 7 | 8 | - | 15 |

* **Cambio principal de hardware (1 solo Mult Float)**: En lugar de 2 multiplicadores, ahora solo hay 1 Multiplicador de Coma Flotante

* **Cuello de botella en `fmul` (filas 5 y 7)**: La segunda multiplicación (fmul f2, f0, f5) no puede entrar a EX en el ciclo 6 a pesar de tener los datos listos; debe esperar hasta el ciclo 9 a que la primera fmul libere la única UF disponible (ocupa ciclos 6-8)

* **Adelanto de instrucciones enteras en EX**: Como las ALU enteras están libres, `addi x2, x2, 4` ejecuta inmediatamente en el ciclo 6 (en el anterior era en el 7) y `sub x5, x4, x2` ejecuta en el ciclo 7 al recibir x2 justo a tiempo

* **Retención por orden en ROB**: Aunque `addi` y `sub` terminan en EX muy pronto (ciclos 6 y 7), sus entradas en ROB (ciclos 7 y 8) se quedan esperando en la cola hasta que las instrucciones anteriores completan. Sus escrituras finales en WB (ciclos 13 y 14) se desplazan hacia adelante porque están atrapadas detrás del cuello de botella que generó el `fmul`

* `fsw` diferido (fila 9): El segundo fsw depende directamente del resultado del segundo fmul (f2), así que su EX no empieza hasta el ciclo 12 (tras terminar fmul en el 11)


# Variación 2
| Etapa | Número de unidades |
|:---|:---:|
| IF | 2 |
| ID | 2 |
| ISS | 2 |
| ROB | 2 |
| WB | 2 |

| Unidad funcional | Cantidad | Latencia |
|:---|:---:|:---:|
| Load Int | 1 | 1 |
| Load Float | 2 | 2 |
| Store Float | 1 | 1 |
| ALU Int | 2 | 1 |
| Mult Float | 1 | 3 |

| Instrucción | IF | ID/ISS | EX | ROB | WB |
|:---|:---:|:---:|:---:|:---:|:---:|
| `lw x3, n` | 1 | 2 | 3 | 4 | 5 |
| `addi x4, x3, 2` | 1 | 2 | 4 | 5 | 6 |
| `init: flw f1, 0(x3)` | 2 | 3 | 4-5 | 6 | 7 |
| `flw f0, y(x2)` | 2 | 3 | 5-6 | 7 | 8 |
| `fmul f2, f0, f1` | 3 | 4 | 7-9 | 10 | 11 |
| `fsw f2, 0(x2)` | 3 | 4 | 10 | - | 11 |
| `fmul f2, f0, f5` | 4 | 5 | 10-12 | 13 | 14 |
| `addi x2, x2, 4` | 4 | 5 | 6 | 7 | 14 |
| `fsw f2, 0(x2)` | 5 | 6 | 13 | - | 15 |
| `sub x5, x4, x2` | 5 | 6 | 7 | 8 | 15 |
| `bne x2, x0, init` | 6 | 7 | 8 | - | 16 |

* **Cambio principal de hardware (2 `Load Float` con latencia de 2 ciclos)**: Se pasa a tener 2 unidades de carga flotante pero su latencia sube de 1 a 2 ciclos (ocupan 2 ciclos en EX)

* **Retraso en cadena sobre los `flw`**: `flw f1, 0(x3)` ejecuta en 4-5 y flw f0, y(x2) ejecuta en **5-6**

* **Efecto dominó en `fmul`**: La primera `fmul` no puede empezar EX en el ciclo 6 porque f0 no termina hasta el final del ciclo 6. Por tanto, entra a EX en los ciclos **7-9**

* **Desplazamiento del cuello de botella**: La segunda `fmul` (filas 7) debe esperar a que finalice la primera, por lo que su EX se retrasa hasta los ciclos **10-12**  

* **Retraso final en los `fsw`**: Los stores flotantes entran a EX un ciclo más tarde debido al retraso acumulado por las multiplicaciones: el primer fsw ejecuta en el ciclo 10 (tras la 1.ª fmul) y el segundo `fsw` ejecuta en el ciclo 13 (tras la 2.ª `fmul`)  

# Examen 2025 (hecho en clase con Macarena)

| Etapa | Ancho de banda / Capacidad |
|:---|:---:|
| IF | 5 |
| ID | 4 |
| ISS | 4 |
| ROB | 3 |
| WB | 3 |

| Unidad Funcional | Cantidad | Latencia |
|:---|:---:|:---:|
| Carga Ent (lw) | 1 | 1 |
| Carga Float (flw) | 2 | 2 |
| Alm Float (fsw) | 1 | 2 |
| ALU Ent (addi, sub) | 2 | 1 |
| Mult/Div Float (fmul, fdiv) | 2 | 3 |

| Instrucción | IF | ID/ISS | EX | ROB | WB |
|:---|:---:|:---:|:---:|:---:|:---:|
| `lw t0, 0x1000` | 1 | 2 | 3 | 4 | 5 |
| `addi t4, t0, 0x50` | 1 | 2 | 4 | 5 | 6 |
| `ini: flw f1, 0(t0)` | 1 | 2 | 4-5 | 6 | 7 |
| `flw f0, y(t1)` | 1 | 2 | 5-6 | 7 | 8 |
| `fmul f2, f0, f1` | 1 | 3 | 7-8-9 | 10 | 11 |
| `fsw f2, 0(t1)` | 2 | 3 | 10-11 | - | 12 |
| `fdiv f3, f0, f1` | 2 | 3 | 7-8-9 | 10 | 12 |
| `fsw f3, 4(t1)` | 2 | 3 | 12-13 | - | 14 |
| `addi t1, t1, 8` | 2 | 4 | 5 | 6 | 14 |
| `sub t2, t1, t0` | 2 | 4 | 6 | 7 | 14 |
| `bnez t1, t2, ini` | 3 | 4 | 7 | - | 15 |

* **Ancho de banda grande en IF/ID/ISS**: En el ciclo 1 entran 5 instrucciones a IF y las primeras 4 pasan a ID/ISS en el ciclo 2

* **Paralelismo en `fmul` y `fdiv`**: Como hay 2 unidades Mult/Div Float, `fmul` y `fdiv` se ejecutan en paralelo durante los ciclos **7-8-9** tras esperar a que flw f0 termine en el ciclo 6

* **Latencia de 2 en Stores (`fsw`)**: El almacenamiento flotante dura 2 ciclos en EX (10-11 y 12-13)

* **`addi` y `sub` avanzan muy rápido en EX**: addi t1 ejecuta en el ciclo 5 y sub t2 en el ciclo 6 (al no depender de flotantes), pero quedan frenados al final para escribir en WB (ciclo 14) respetando los límites del ROB.   

* **`fsw` y `bnez` llevan guion (-) en ROB**: No escriben en registros destino. Los fsw confirman en memoria en WB (ciclos 12 y 14) y el salto resuelve su condición en EX en el ciclo 7
