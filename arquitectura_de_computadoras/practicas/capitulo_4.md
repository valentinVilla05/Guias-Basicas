# Capítulo 4: Segmentación del Cauce y Riesgos de Control

## 1. Conceptos Fundamentales

### El Contador de Programa (`pc`) y la Etapa IF

* **Comportamiento por defecto**: En la etapa de captación (IF - Instruction Fetch), el pc se incrementa automáticamente en $+4$ bytes en cada ciclo para leer la siguiente instrucción secuencial de la memoria

* **Modificación del flujo**: Las instrucciones de salto (condicionales e incondicionales) alteran explícitamente el valor del `pc`

## 2. Procesamiento de Instrucciones de Salto (Cauce de 5 Etapas)

```
[ IF ]  --->  [ ID ]  --->  [ EX ]  --->  [ MEM ]  --->  [ WB ]
                             |
                   Cómputo de dirección
                   y evaluación de condición
                             |
                             v
                 Devuelve nuevo PC a IF (Ciclo N+1)
```


### 1. Cómputo de la dirección de destino:

* Se realiza en la etapa de ejecución (**EX**) sumando el valor actual del pc con el operando inmediato/desplazamiento

### 2. Evaluación de la condición (Saltos condicionales):

* Se verifica en el componente Branch dentro de la etapa **EX**

### 3. Actualización efectiva del pc:

* La nueva dirección se envía de vuelta a la etapa IF, por lo que el `pc` se actualiza efectivamente al pasar la instrucción a la etapa **MEM**

## 3. Riesgos de Control (Branch Hazards)
Un **riesgo de control** se produce porque el cauce de la CPU continúa captando y descodificando instrucciones secuenciales antes de saber si el salto se va a realizar o no

### El Problema de los Ciclos Perdidos
* Mientras la instrucción de salto se evalúa (pasa por **ID** y **EX**), la CPU capta 2 instrucciones innecesarias de las direcciones contiguas

* Al confirmarse el salto en **EX**, la CPU ejecuta un Flush (limpieza del cauce), descartando las instrucciones que estaban en las etapas **IF** e **ID**

* **Impacto**: Cada salto tomado penaliza la ejecución con 2 ciclos perdidos

> $$\text{Ciclos adicionales por saltos} = (\text{Iteraciones con salto tomado}) \times 2$$

## 4. Técnicas para Reducir los Riesgos de Control

### 4.1. Desenrollado de Bucles (Loop Unrolling)
Consiste en replicar el cuerpo del bucle para procesar $t$ elementos por iteración ($t$ = factor de desenrollado), reduciendo el número total de iteraciones de $N$ a $N/t$

* **Ventaja**: Disminuye directamente la cantidad de instrucciones de salto ejecutadas y, por ende, los ciclos perdidos por riesgos de control

* **Desventaja**: Incrementa el tamaño del código en memoria

### 4.2. Desenrollado y Reordenamiento
Aplicar solo desenrollado puede duplicar los riesgos de datos (load-use hazards). Para optimizar al máximo, se deben aplicar tres pasos combinados:

1. **Desenrollar**: Duplicar el cuerpo del bucle

2. **Reorganizar operaciones**: Agrupar los incrementos de punteros (ej. `addi t0, t0, 8` en lugar de dos veces +4) y del contador de iteraciones

3. **Reordenar instrucciones**: Intercalar instrucciones independientes (usando registros temporales adicionales como `a1` y `a2`) entre las cargas (`lw`) y las operaciones que usan sus datos (`add`) para eliminar los ciclos de parada por riesgo de datos

## 5. Resumen Comparativo de Rendimiento
Tomando como referencia la suma de un vector de 10 elementos en la configuración de 5 etapas con bypass:

| Versión del Programa | Ciclos Totales | CPI (Ciclos por Instrucciones) | Principales Mejoras | 
| -- | -- | -- | -- | 
| **Original** (sin desenrollar) | 97 | 1.64 | Implementación directa; penaliza 2 ciclos en 9 de las 10 iteraciones | 
| **Desenrollado ($t=2$)** | 79 | 1.49 | Se reducen las iteraciones a la mitad (5 saltos en lugar de 10) | 
| **Desenrollado y Reordenado** | 59 | 1.37 | Fusión de incrementos + eliminación de riesgos de datos mediante reordenación | 

## 6. Aspectos Avanzados y Mecanismos Hardware

* **Detección de riesgos (Hardware básico / Ripes)**: Permite continuar captando instrucciones y las elimina mediante flush si la predicción implícita (continuar secuencialmente) falla

* **Detención de captación (Stall)**: Alternativa donde la CPU frena la captación en cuanto detecta un salto hasta conocer el `pc` definitivo. No aporta beneficios de rendimiento respecto a limpiar el cauce

* **Predictor de Saltos (Branch Predictor):**

    * Presente en CPUs modernas y emuladores avanzados

    * Utiliza un historial de saltos previos y una máquina de estados para predecir en la etapa **IF** si el salto se tomará o no

    * Si la predicción es acertada, se elimina por completo la pérdida de ciclos. Si falla, se sufre la misma penalización de limpieza del cauce

