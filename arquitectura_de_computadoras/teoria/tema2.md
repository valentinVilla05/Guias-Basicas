## Tema 2: Procesos Segmentados

### Nivel de Abstracción

![alt text](/images/abstrac.png)

### Conceptos Iniciales:

* **Procesador (CPU)**: es la parte activa del ordenador que realiza todo el trabajo (manipulación de datos y toma de decisiones)
* **Datapath (ruta de procesos)**: Es la parte del procesador que contiene el hardware necesario para realizar las operaciones requeridas por el procesador
* **Control**: Es la parte del procesador que indica el datapath lo que debe hacer

### Tipo de Programa
> T = N x CPI x Tc

`N` = Número de instrucciones:
* Está determinado por:
    * Algoritmo
    * Lenguaje de programación
    * Compilador
    * Arquitectura del conjunto de Instrucciones (ISA)


`CPI` = Ciclos de reloj por instrucción:
* Está determinado por:
    * ISA
    * Implementación del procesador
    * Procesador simple: RISC_V de ciclo único CPI= 1 
    * Instrucciones de varios ciclos, CPI > 1
    * Procesadores superescalares , CPI < 1 

`Tc` = Tiempo de ciclo (T=1 /frecuencia) 
* Determinado por:
    * Microarquitectura
    * Técnica
    * Presupuesto de energía

## Introducción a la segmentación (Pipeline)

* **Pipeline:** Dividir el procesador de una instrucción en etapas y solapar varias instrucciones a la vez. Mientras una instrucción está en una etapa, otra puede utilizar otra etapa del procesador. Puede hacer las CPUs rápidas

![alt text](/images/pipeline.png)

* `IF`: Captar instrucción
* `ID`: Decodificar / Leer registros
* `EX`: Ejecutar
* `MEM`: Acceso a memoria
* `WB`: Escribir resultado en registros

Se intenta equilibrar las etapas, el periodo de reloj queda limitado por la etapa más lenta


## Rendimiento en un procesador Segmentado
Si el pipeline tiene `K` etapas equilibradas, la mejora máxima ideal de rendimiento puede aproximarse a:

> $Tsegmentado$ = $TsinSegmentar / K$

* La segmentación (pipeline) **mejora el rendimiento** al permitir que varias instrucciones se procesan simultáneamente en diferentes etapas del procesador

* Su principal beneficio es aumentar la productividad (`throughput`): una vez lleno el pipeline, puede completarse una instrucción por ciclo

* La segmentación no reduce la latencia de una instrucción individual. Puede aumentarla ligeramente debido al coste de registro entre etapas

* La segmentación mejora principalmente el rendimiento no el tiempo necesario para ejecutar una instrucción

* El rendimiento depende de cómo se emiten las instrucciones

## Emisión de instrucciones:

La emisión es el momento en el que una instrucción pasa de la etapa de decodificación a la parte de ejecución

> Es decir cuando pasa de ID a EX

* **CPE (Ciclos por emisión):** número de ciclos de reloj que transcurren entre la emisión de una instrucción y la siguiente

* **IPE (Instrucciones por Emisión)**: número de instrucciones que pueden emitirse simultáneamente

**Formulas**

> CPI = CPE / IPE

>Tcpu = N x CPE / IPE x Tc

**Pipeline Ideal**

![alt text](/images/pipeline_ideal.png)

* Una vez lleno el pipeline se emite una nueva instrucción en cada ciclo de reloj

* Un CPI próximo a 1 indica que el pipeline mantiene un flujo continuo de instrucciones

### Definiciones Adicionales:

* * **Latencia:** Tiempo total transcurrido desde que un elemento entra al sistema hasta que se completa. Es la suma de las duraciones de cada etapa individual y no disminuye por el uso del pipeline.
* **Throughput (Rendimiento)**: Cantidad de elementos completados por unidad de tiempo. En régimen permanente (pipeline lleno), la velocidad de salida la dicta únicamente el tiempo de procesamiento de la etapa más lenta.
* **Ganancia (Speedup)**: Factor de mejora en rendimiento respecto a un procesamiento secuencial. Nunca alcanza el máximo teórico (igual al número de etapas) debido a las ineficiencias de inicio y fin: las fases de llenado y vaciado, donde no todas las etapas del pipeline operan al 100% de su capacidad.


## RISC-V Segmentado
5 etapas del RISC-V

![alt text](/images/etapas.png)

### Representación de las 5 etapas