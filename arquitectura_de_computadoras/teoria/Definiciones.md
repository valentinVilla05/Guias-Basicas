# DEFINICIONES: Arquitectura de computadores

## **Segmentación (pipelining)**

**Segmentación:** Técnica de implementación por la cual se **solapa el procesamiento de múltiples instrucciones**. Es una de las claves principales para construir CPUs rápidas

- Incrementa el rendimiento aumentando la **productividad** (instrucciones por segundo), no reduciendo el tiempo de ejecución individual de cada instrucción
- En un procesador segmentado **todas las instrucciones pasan por todas las etapas**, a diferencia de un procesador secuencial, donde cada instrucción pasa solo por las etapas que necesita
- Si K es el número de etapas, el tiempo ideal de ejecución es:

> T_segmentado = T_sin_seg / K

**La frecuencia máxima de instrucciones está limitada por:**

- El retardo de los cerrojos / registros intermedios
- El sesgo del reloj (_clock skew_)
- La presencia de riesgos

## **Ley de Amdahl**

**Ley de Amdahl:** Regla que sirve para evaluar la **ganancia de rendimiento global** que se obtiene en un sistema al mejorar una parte específica de sus componentes o recursos

- **Parámetros:** tiempo de ejecución sin mejora y con mejora

## **Taxonomía de Flynn**

**Taxonomía de Flynn:** Clasificación tradicional y más utilizada para categorizar las arquitecturas de computadores paralelas, basada en la **multiplicidad de los flujos de instrucciones y de datos**

Flynn evalúa dos flujos independientes:

- **Flujo de instrucciones:** Secuencia de instrucciones ejecutadas por el procesador
- **Flujo de datos:** Secuencia de datos manipulados por las instrucciones

Cada flujo puede ser único o múltiple, dando lugar a **4 categorías fundamentales:**

| Categoría | Significado                         | Descripción                                                                                      |
| --------- | ----------------------------------- | ------------------------------------------------------------------------------------------------ |
| SISD      | Single Instruction, Single Data     | Una sola instrucción procesa un único flujo de datos a la vez                                    |
| SIMD      | Single Instruction, Multiple Data   | Una única instrucción se aplica simultáneamente sobre múltiples datos distintos                  |
| MISD      | Multiple Instruction, Single Data   | Múltiples instrucciones operan de forma simultánea sobre el mismo flujo de datos                 |
| MIMD      | Multiple Instruction, Multiple Data | Múltiples procesadores ejecutan distintas instrucciones sobre datos diferentes de forma autónoma |

## **Memoria virtual**

**Memoria virtual:** Mecanismo que permite la ejecución de programas cuyo tamaño **supere el de la memoria principal (RAM)**

- La memoria del programa y la memoria física se dividen en bloques de tamaño fijo llamados **páginas**

## **Silicio negro**

**Silicio negro:** Fracción de transistores de un procesador que debe mantenerse **apagada o sin energía** en un momento dado debido a limitaciones térmicas y de consumo eléctrico

## **Riesgo (hazard)**

**Riesgo:** Situación en la que las instrucciones de un cauce segmentado (pipeline) se ven afectadas por obstáculos que pueden **retrasar su procesamiento o interrumpir el flujo normal de trabajo**

- Para garantizar un resultado correcto, el procesador puede verse obligado a **detener las instrucciones (insertar burbujas)** hasta eliminar la situación

### **Riesgo estructural**

**Riesgo estructural:** Ocurre cuando el hardware **no admite el acceso simultáneo al mismo recurso físico** por parte de varias instrucciones (por ejemplo, dos instrucciones que intentan acceder a memoria en el mismo ciclo de reloj)

**Posibles soluciones:**

- Utilizar memoria de instrucciones y de datos independientes (**Harvard**)
- Insertar burbujas o instrucciones nulas para detener el cauce
- Añadir más recursos físicos

### **Riesgo de datos**

**Riesgo de datos:** Ocurre cuando una instrucción **depende de los datos o del resultado de una instrucción anterior** que todavía no ha completado su ejecución en el pipeline

**Posibles soluciones:**

- **Bypass / adelantamiento:** Pasar los datos calculados directamente entre las etapas del cauce, sin esperar a que se escriban en el banco de registros
- Diseñar el banco de registros (RegFile) para que **escriba en la primera mitad** del ciclo de reloj y **lea en la segunda mitad**
- **Reordenar el código** para alejar las dependencias
- **Frenar el cauce** cuando el adelantamiento no sea posible

### **Riesgo de control**

**Riesgo de control:** Ocurre cuando el flujo secuencial de instrucciones se ve alterado por **instrucciones de salto** que modifican el PC a un valor distinto de PC + 4. Se produce porque la instrucción captada en las etapas iniciales puede no ser la que realmente se debía ejecutar

**Posibles soluciones:**

- **Anticipar** en las primeras etapas la dirección que tomará el salto para seguir captando instrucciones. Si la predicción falla, se vacía el cauce y se abortan las instrucciones incorrectas
- **Reestructurar el código** para reducir el número de saltos condicionales ejecutados (desenrollado de bucles)
- **Reordenar el código** moviendo instrucciones útiles a las posiciones de retardo de salto

## **Granularidad**

**Granularidad:** Mide el **tamaño de las unidades de trabajo** que se ejecutan en paralelo

- **Grano fino:** Tareas muy pequeñas (instrucciones individuales). Paralelismo a nivel de instrucción y datos
- **Grano medio:** Tareas de tamaño intermedio (funciones, iteraciones de bucles o hebras/hilos). Paralelismo a nivel de hebra y procedimiento
- **Grano grueso:** Tareas muy grandes (programas completos o procesos independientes). Paralelismo a nivel de programa

## **Cauces unifuncionales**

**Cauce unifuncional:** Cauce cuyo hardware solo contempla la ejecución de **un tipo de operación o función**

- Al haber un único tipo de operación existe **un solo conjunto de latencias prohibidas**, que se gestiona con un único **vector de colisiones**

## **Cauces multifuncionales**

**Cauce multifuncional:** Cauce que contempla la ejecución de **dos o más tipos de operaciones o funciones distintas**

- Al haber distintas funciones existen **múltiples conjuntos de latencias prohibidas**, por lo que se utiliza una **matriz de colisiones** para evaluar todas las posibles interferencias cruzadas entre funciones

## **Segmentación lineal**

**Segmentación lineal:** Las operaciones pasan por todas las etapas del cauce **de forma secuencial y en orden**, sin repetir ninguna etapa ni volver hacia atrás

- Su tabla de reservas es trivial y coincide con su diagonal principal
- Es el modelo básico de cauce de los procesadores tipo **RISC**

## **Segmentación no lineal**

**Segmentación no lineal:** Las operaciones **no pasan por todas las etapas** del cauce y/o **no lo hacen en orden**

- Las etapas se pueden saltar, repetir o tener bucles de retroalimentación (volver hacia atrás)

## **Vector de colisiones**

**Vector de colisiones:** Se utiliza en **cauces unifuncionales** (todas las instrucciones ejecutan la misma operación). Es una secuencia binaria que resume de forma compacta qué latencias están permitidas y cuáles no

```
Posición en 1 → latencia prohibida
Posición en 0 → latencia permitida
```

## **Matriz de colisiones**

**Matriz de colisiones:** Se utiliza en **cauces multifuncionales** (cauces dinámicos que ejecutan distintas funciones)

## **Latencia**

**Latencia:** Número de ciclos de reloj que hay que esperar para poder **introducir una nueva operación** en el cauce de la unidad funcional

## **Latencia de inicio**

**Latencia de inicio:** Número total de ciclos de reloj que tarda una operación completa **desde que entra hasta que se completa**, pasando por las etapas correspondientes

## **Latencia óptima**

**Latencia óptima:** Aquella que produce la **menor espera posible** y, por tanto, consigue la **máxima ocupación posible** del cauce

- La latencia óptima ideal es **1**. Es fácil de conseguir en la segmentación lineal, pero raramente posible en la no lineal

## **Latencia media**

**Latencia media:** Promedio de ciclos de espera por operación a lo largo de un ciclo o bucle de ejecuciones

**Fórmula:**

> LM = Suma de latencias del ciclo / Nº de estados del ciclo

- **Mínima latencia media (MLM):** Menor latencia media de entre todos los ciclos posibles del diagrama de estados
- Encontrar la MLM es el objetivo principal en cauces no lineales para conseguir el máximo rendimiento de la unidad funcional

## **Latencia prohibida**

**Latencia prohibida:** Número de ciclos de reloj entre el inicio de una operación y el de otra que provocaría un **choque en alguna etapa** del cauce

- **Cálculo en la tabla de reservas:** si una etapa se usa en el ciclo X y también en el ciclo Y, la distancia Y - X es una latencia prohibida
