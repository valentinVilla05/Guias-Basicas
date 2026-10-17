# Examen del Año pasado de la Práctica 3

## Ejercicio 1 – 2/10 puntos - Archivos Eje1.s y P3.pdf   

Escribe un programa ajustado a las siguientes directivas:   En el segmento de datos se tiene un conjunto de pesos de personas expresadas en kilos, almacenadas como números enteros de 32 bits:


El programa deberá contar **cuántos kilos son mayores que 58 kilos**, y el resultado **deberá almacenarse en memoria**, en un espacio reservado a tal efecto en el segmento de datos sin inicializar, como un número entero de 32 bits.   

Crea un documento y adjunta en él una captura de pantalla del panel Memory tras haber ejecutado el programa, en la que se vea el código en el editor y el conteo de espacios en la memoria.   

![alt text](../images/resolucionej1e3.png)

## Ejercicio 2 – 3/10 puntos - Archivo P3.pdf   

Ejecuta el programa del **ejercicio 1** en las **configuraciones de procesador Single-cycle processor (C1), 5-Stage processor w/o Forwarding unit (C2) y 5-stage processor (C3)** y anota en cada caso el **número de ciclos y CPI**.

Incluye en el documento creado antes una **tabla con los ciclos, CPI y mejora en rendimiento de cada una de las configuraciones**, calculando a partir de C1 una estimación de lo que se tardaría en un procesador sin cauce segmentado. 

Explica brevemente la fórmula que hayas empleado para hacer el cálculo de la mejora en rendimiento. Incluye una captura de pantalla de la ejecución en cada configuración en la que se aprecien los datos usados en la tabla.   

> Para cambiar la configuración del procesador tenemos que darle al icono que hay justo debajo de File 


> Resolución

**Si configuramos Single-cycle processor**

![alt text](../images/1s.png)

**Si configuramos 5-Stage processor w/o Forwarding unit**

![alt text](../images/2s.png)

**Si configuramos 5-Stage processor**

![alt text](../images/s3.png)


| Configuración de procesador | Ciclos | Instrucciones | CPI | Aceleración / Mejora respecto C1 | 
| -- | -- | -- | -- | -- |
| **C1: Single-cycle processor** | 90 | 90 | 1 | 1x | 
| **C2: 5-Stage processor w/o Forwarding** | 178 | 90 | 1,98 | 0,51x | 
| **C3: 5-Stage processor** (con Forwarding) | 164 | 90 | 1,82 | 0,55x | 

### Explicación y Formulas empleadas

1. Cálculo de la mejora en rendimiento (Speedup)La mejora en rendimiento o Speedup ($S$) de una configuración respecto a la base (C1 - Monociclo) se calcula dividiendo los ciclos del procesador base entre los ciclos del procesador evaluado (asumiendo que el periodo de reloj $T_{clk}$ se mantiene constante para la comparación teórica):

$$\text{Speedup} (S) = \frac{\text{Ciclos}_{C1}}{\text{Ciclos}_X}$$

Para C2 (5-Stage sin Forwarding):$$S_{C2} = \frac{90}{178} \approx 0,51\times$$

Para C3 (5-Stage con Forwarding):$$S_{C3} = \frac{90}{164} \approx 0,55\times$$

**2. Análisis de los resultados**

* **Monociclo (C1)**: Ejecuta exactamente 1 instrucción por ciclo ($\text{CPI} = 1,00$), requiriendo 90 ciclos para completar las 90 instrucciones.

---
* **Segmentado sin Forwarding (C2)**: Al no contar con unidad de reenvío de datos, el procesador debe introducir burbujas (stalls) cada vez que una instrucción necesita un dato producido por una instrucción anterior que aún no ha terminado. Además, los saltos introducen penalización por riesgo de control. Esto eleva el número total de ciclos a 178 ($\text{CPI} = 1,98$).

----
* **Segmentado con Forwarding (C3)**: La presencia de la unidad de reenvío (Forwarding unit) resuelve gran parte de las dependencias de datos directamente entre etapas del cauce sin tener que parar la ejecución. Esto reduce los ciclos totales a 164 ($\text{CPI} = 1,82$), logrando una ligera mejora respecto a C2.

## Ejercicio 3 – 3/10 puntos - Archivos Eje2.s y P3.pdf  

Inicia un nuevo programa en Ripes y copia en él el código del ejercicio 1. **Identifica las detenciones por riesgos de datos que detectes, usa las herramientas que necesites, y descríbelas de forma concisa en el documento**. 

A continuación, **reordena el código para evitar esos riesgos** y verifica que el resultado es correcto, examinando en el panel Memory el conteo de espacios. 

Incluye en el documento una captura de pantalla en la que se vean los ciclos y CPI de esta versión del programa con la configuración C2. Agrega una versión actualizada de la tabla creada en el ejercicio 2, en la que incluyas los datos de la versión reordenada y el cálculo de rendimiento.   

> Resolución

**Identificamos riesgos de datos en el código**

```asm
bucle:
    beqz a1,fin 
    lw a2,0(t0)        # 1. Carga a2 desde la memoria
    bgtu a2,t1,mayor   # 2. Usa a2 (Dependencia de datos RAW: Load-Use Hazard)
    j siguiente

mayor:
    addi a0,a0,1 
    j siguiente
    
siguiente:
    addi t0,t0,4       # 3. Modifica t0
    addi a1,a1,-1      # 4. Modifica a1
    j bucle            # 5. Salto al inicio (Riesgo de control)
```

* **Riesgo Load-Use:** Ocurre entre `lw a2,0(t0)` y `bgtu a2,t1,mayor`. En la configuración C2 (sin Forwarding), la instrucción bgtu intenta leer a2 antes de que lw escriba el dato en el banco de registros, insertando burbujas (stalls)

**Código reordenado**

Separamos la carga `lw` de la comparación `bgtu` intercalando el avance de puntero y el decremento del contador:

![alt text](../images/reordenado.png)

**Comparativa de rendimiento** 


| Configuración de procesador | Ciclos | Instrucciones | CPI | Aceleración / Mejora respecto C1 | 
| -- | -- | -- | -- | -- |
| **C1: Single-cycle processor** | 90 | 90 | 1 | 1x | 
| **C2: 5-Stage processor w/o Forwarding** | 178 | 90 | 1,98 | 0,51x | 
| **C3: 5-Stage processor** (con Forwarding) | 164 | 90 | 1,82 | 0,55x | 
| **C2: 5-Stage w/o Forwarding** (Reordenado) | 128 | 80 | 1,6 | 0,625x | 

## Ejercicio 4 – 2/10 puntos - Archivos Eje3.s y P3.pdf   

Parte del código de Eje2.s, **activa la configuración de CPU 5-stage processor w/o forwarding or hazard unit y ejecuta el programa**. Identifica en la vista del cauce segmentado de Ripes dónde hay riesgos de datos que produzcan un funcionamiento incorrecto del programa (si es que existen). En caso afirmativo introduce de forma manual, con la instrucción `nop`, las detenciones precisas para que el programa produzca un resultado correcto. Explica brevemente en el documento qué cambios has realizado y porqué.

 Si no has tenido que hacer cambio alguno, entrega como Eje3.s una copia del código que tenías en Eje2.s. 

 > Resolución

Al configurar la CPU en 5-stage processor w/o forwarding or hazard unit, el procesador no resuelve los riesgos de datos ni inserta burbujas (stalls) de forma automática. Si hay dependencias Read-After-Write (RAW), las instrucciones leen valores desactualizados del banco de registros, produciendo un funcionamiento incorrecto.


**Identificación de riesgos y solución con `nop`**

Tomando el código original del Ejercicio 1 (el de `Eje2.s`), un registro escrito en la etapa WB tarda 2 ciclos en estar disponible para ser leído en la etapa ID. Al no haber unidad de Hazards, debemos insertar instrucciones `nop` (No Operation) manualmente para separar los productores de los consumidores:

![alt text](../images/ej4.png)

**Explicación**
**1. Riesgo Load-Use (lw $\rightarrow$ bgtu)**: La instrucción `lw a2, 0(t0)` escribe en a2 en la etapa WB. Sin unidad de reenvío ni de paradas, la instrucción bgtu leería un valor antiguo de a2. Se introducen 2 nop entre ambas para dar margen a que el dato se escriba en el banco de registros.

**2. Riesgo en el control del bucle (addi a1 $\rightarrow$ beqz a1)**: Al final de cada iteración se modifica a1. Para evitar que en la siguiente iteración beqz lea el valor desactualizado de a1, se añaden 2 `nop` tras la etiqueta `bucle:`