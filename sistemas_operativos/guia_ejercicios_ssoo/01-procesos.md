# Guia para resolver cualquier ejercicios de Procesos

> Esta guía va a ser un poco extensa ya que también se tocan conceptos teóricos que son muy importantes

# PARTE I – EL PROCESO

## 1. Explicación con un ejemplo 
Durante toda la guía vamos a pensar el ordenador como un restaurante con una sola sartén:
| Elemento del restaurante	| Equivalente en el ordenador | 
| -- | -- | 
Una receta escrita en un papel, guardada en un cajón | 	Un programa (archivo en el disco, quieto, "muerto") |
Un cocinero ejecutando esa receta	| Un proceso (el programa en marcha)
| La única sartén del restaurante | 	La CPU (el procesador; supondremos 1 solo núcleo)
| La cola de pedidos de la caja	 | La cola de listos (procesos esperando la sartén)
| El jefe de cocina que decide quién cocina ahora	| El planificador (scheduler)
| Los minutos que una receta ocupa la sartén | 	La ráfaga (CPU burst)
| El cronómetro de 2 minutos que le pones a cada plato antes de pasarlo al siguiente	| El quantum (Round Robin)
| El timbre de la caja, la alarma del horno, la llamada del proveedor	| Las interrupciones
| Guardar los ingredientes del plato actual en su cajetín y sacar los del siguiente	| El cambio de contexto | 

## 2. Programa vs. Proceso
* **Definiciones**

    * **Programa** = conjunto pasivo de instrucciones (código) guardado en un archivo en el disco.

    > Es solo texto binario esperando. No consume CPU ni recursos. Como la receta en el cajón.

* **Proceso** = programa en ejecución. Es una entidad activa: ya está cargado en memoria, tiene recursos asignados y la CPU trabajando para él

>  Un proceso es la unidad de trabajo de un sistema operativo; es un programa en ejecución, junto con todo el estado que necesita para continuar su ejecución: código, datos, pila, registros del procesador y el contador de programa.


**Ejemplos**
* Abres dos ventanas de Chrome → hay 1 programa (chrome.exe) y 10 procesos (uno por pestaña/capa).

* Si copias un archivo 3 veces a la vez → hay 1 programa copiador y 3 procesos distintos

* **Formula**
> PROCESO = PROGRAMA + ESTADO DE EJECUCIÓN (contexto)

Dos procesos creados del mismo programa son distintos entre sí porque **tienen estados distintos** (`PCB` distinto, `PID` distinto, momentos de llegada distintos)


> **Mención rápida: hilos (threads)**
Un proceso puede tener varios hilos: varios flujos de ejecución dentro del mismo proceso que comparten la misma memoria. Para el planificador moderno, a veces el planificador de CPU planifica hilos, no procesos. (No lo necesitas para los ejercicios de FCFS/SJF, pero es bueno saber que existe (sobre todo para concurrentes))


## 3. El PCB
**PCB = Process Control Block** (en español: Bloque de Control de Proceso).

Cada proceso que existe en el sistema tiene **una ficha** (un registro en una tabla) que **guarda todo lo necesario para poder pararlo y retomarlo después sin perder nada**. Es la "tarjeta de identidad" del proceso. 

### ¿Qué guarda el PCB?
| Campo | Qué es | Ejemplo | 
| -- | -- | -- | 
| **Identificación** | PID (número único), PID del padre, usuario | PID=101, PPID=1, user=maria | 
| **Estado actual** | ¿Está listo, ejecutando, bloqueado? | "listo" | 
| **Registros del procesador** | Contador de programa (PC), registros generales, puntero de pila (SP), acumuladores | PC = 0x004015F2 | 
| **Información de planificación** | Prioridad, puntero a su cola, quantum restante | prioridad=3 | 
| **Información de memoria** | Tabla de páginas, base, límite | pág. 0x1A00 | 
| **Información de E/S** | Archivos abiertos, dispositivos asignados | fichero.txt (lectura) | 
| **Contabilidad** | Tiempo de CPU consumido, tiempo total de vida | 120 ms de CPU | 

### 4. Los estados del proceso

| Estado | Qué es | Analogía |
|---|---|---|
| **Nuevo** | Creado, aún no admitido en memoria | Ticket nuevo en el mostrador |
| **Listo** | En memoria, **quiere la CPU** y espera su turno | Plato esperando en la barra |
| **Ejecutando** | Tiene la CPU (solo 1 por núcleo) | Plato en la sartén |
| **Bloqueado** | **No puede seguir**: espera un **evento** (E/S, sleep) | Plato en el microondas |
| **Terminado** | Acabó; el SO libera sus recursos | Plato servido |

> Si falta RAM, el SO saca procesos al disco(**listo-suspendido** y **bloqueado-suspendido**)

> Diferencia clave:
* **Listo** espera la CPU
* **Bloqueado** espera un **evento**

Aunque le des la CPU a un bloqueado este no avanzará


### Diagrama 
```
                                 ┌────────────── preempción ──────────────┐
                                 │  (expira el quantum o llega un         │
                                 │   proceso más prioritario)             │
                                 ▼                                        │
  ┌──────────┐   admitir   ┌──────────┐  despachar  ┌──────────────┐      │
  │   NUEVO  │ ──────────▶ │  LISTO   │ ──────────▶ │  EJECUTANDO  │──────┘
  └──────────┘             └────▲─────┘             └──────┬───────┘
                                │                          │
                                │ evento:                  │ pide E/S
                                │ E/S terminada            ▼
                                │                    ┌───────────┐
                                │                    │ BLOQUEADO │
                                │                    └─────┬─────┘
                                │                          │
                                └──────────────────────────┘

                     EJECUTANDO ──── termina ────▶ [TERMINADO]
```

**Las 6 flechas explicadas una a una**

1. **Nuevo → Listo** = *admisión*. El SO carga el proceso en RAM y lo pone en la cola de
   listos.
2. **Listo → Ejecutando** = *despacho (dispatch)*. El planificador elige a ese proceso y le
   da la CPU.
3. **Ejecutando → Listo** = *preempción*. Se le quita la CPU **sin que haya terminado**.
   Causas: expiración del **quantum** o llegada de un proceso **más prioritario**.
4. **Ejecutando → Bloqueado** = *bloqueo*. El proceso pide algo que tarda (disco, teclado,
   sleep).
5. **Bloqueado → Listo** = *despertar*. El evento ocurrió (terminó la E/S), ya puede
   competir por la CPU.
6. **Ejecutando → Terminado** = *finalización*. Terminó su ráfaga. El SO libera sus recursos.
### 5. Cambio de contexto

Guarda el estado del proceso saliente en su PCB y cargar el del entrante. Es **tiempo muerto** (Overhead): mientras el SO guarda y carga, nadie trabaja. Por eso se intentan pocos cambios

* **Concurrencia vs Paralelismo**: Con varios procesos y 1 CPU , lso procesos se **intercalan** ("parecen" que van a la vez). Hace falta más de un núcleo (varias cosas **en el mismo instante**)


### 6. Planificación de la CPU

> Desde esta parte se orientan más a los ejercicios como tal , pero era necesario tener las nociones previas o no sabremos que estamos haciendo

**Decidir que proceso listo recibe la CPU y durante cuanto tiempo**. Lo hace el **planificador de corto tiempo** .

* **No Apropiativo**: Al proceso NO se le quita la CPu hasta que termina o se bloquea

* **Apropiativo**: El SO puede quitarle la CPU (quantum superado o por la llegada de un proceso más prioritario) ejemplo: RR y SRTF

### 7. Métricas 

| Magnitud | Fórmula | Qué mide |
|---|---|---|
| **Ráfaga (T)** | dato del enunciado | CPU total que necesita |
| **Tr (retorno/turnaround)** | `t_fin − t_llegada` | Vida total del proceso |
| **Te (espera)** | `Tr − T` | Tiempo muerto en cola |
| **R (respuesta)** | `t_primer_uso − t_llegada` | Rapidez de la primera vez que ejecuta |
| **Promedio** | `suma / nº de procesos` | Compara algoritmos |
| **% de espera** | `100 × Te prom / Tr prom` | % de su vida esperando |

Regla de oro: **`Tr = Te + T`** (siempre que no haya bloqueos). Verificación: `Σ Tr = Σ T + Σ Te`.

### 8. Los algorítmos

#### 8.1 FIFO - El primero en llegar , primero en servirse (no apropiativo)

Ordena por llegada y encadena ráfagas completas


Orden por llegada: P1(0), P2(1), P3(2), P4(3). Como P1 llega a 0 y no se interrumpe, va
entero: 0→5. P2 va después: 5→8. P3: 8→16. P4: 16→18.

```
 0    5      8           16      18
 +----+------+-----------+-------+
 | P1 |  P2  |    P3     |  P4   |
 +----+------+-----------+-------+
```

| Proceso | Llegada | T | t_fin | Tr | Te |
|---|---|---|---|---|---|
| P1 | 0 | 5 | 5 | **5** | **0** |
| P2 | 1 | 3 | 8 | **7** | **4** |
| P3 | 2 | 8 | 16 | **14** | **6** |
| P4 | 3 | 2 | 18 | **15** | **13** |
| **Media** | | | | **41/4 = 10,25** | **23/4 = 5,75** |
> Sufre el efecto **convoy**: Si el primero es largo, todos esperan 

#### 8.2 SJF - El trabajo más corto pasa primero


Cuando hay que elegir, gana el de **menor ráfaga T**. Produce el **menor tiempo de espera
promedio posible** (óptimo). Empates -> por orden de llegada

- **t = 0**: solo está P1 → corre entero 0→5.
- **t = 5**: en cola hay P2(T=3), P3(T=8), P4(T=2). ¿Menor T? **P4 (2)** → corre 5→7.
- **t = 7**: quedan P2(T=3) y P3(T=8). ¿Menor? **P2** → corre 7→10.
- **t = 10**: queda P3 → corre 10→18.

```
 0    5    7     10           18
 +----+----+-----+-----------+
 | P1 | P4 |  P2 |    P3     |
 +----+----+-----+-----------+
```

| Proceso | Llegada | T | t_fin | Tr | Te |
|---|---|---|---|---|---|
| P1 | 0 | 5 | 5 | **5** | **0** |
| P2 | 1 | 3 | 10 | **9** | **6** |
| P3 | 2 | 8 | 18 | **16** | **8** |
| P4 | 3 | 2 | 7 | **4** | **2** |
| **Media** | | | | **34/4 = 8,50** | **16/4 = 4,00** |

**Tr prom = 8,50 · Te prom = 4,00**

#### 8.3 SRTF — Menor TIEMPO RESTANTE, primero (SRT apropiativo)


| Instante | ¿Qué pasa? | Decisión | Restantes |
|---|---|---|---|
| t=0 | Solo P1 | P1 corre | P1:5 |
| t=1 | Llega P2 (T=3). P1 le queda 4 | 4 > 3 → **P1 pierde la CPU**: para P1, corre P2 | P1:4, P2:3 |
| t=2 | Llega P3 (T=8). A P2 le quedan 2 | 2 < 8 → **sigue P2** | P1:4, P2:2, P3:8 |
| t=3 | Llega P4 (T=2). A P2 le quedan 2 | 2 = 2 → **empate, sigue P2** | P1:4, P2:2, P3:8, P4:2 |
| t=4 | **P2 termina** | Elige el menor: P4 (2) | P1:4, P3:8, P4:2 |
| t=6 | **P4 termina** | Elige el menor: P1 (4) | P1:4, P3:8 |
| t=10 | **P1 termina** | Queda P3 | P3:8 |
| t=18 | **P3 termina** | FIN | — |

```
 0  1    4   6      10          18
 +--+----+---+------+-----------+
 |P1| P2 | P4|  P1  |    P3     |
 +--+----+---+------+-----------+
```

#### 8.4 Round Robin - ronda con cronómetro (apropiativo)
 
Cada proceso recibe la CPU un trocito fijo (**quantum q**). Si no termina, suena la alarma
(interrupción de reloj), se le pone **al final de la cola** y sigue el siguiente


- q pequeño → todos avanzan a la vez: buena **respuesta**, pero muchos cambios de contexto.
- q grande → se convierte en FCFS. Típico: 10-100 ms (≈10× el coste de un cambio de contexto).

**Ejemplo canónico resuelto con q = 2**

| Paso | Cola al empezar | Corre | Trozo | Sucede | Cola al final |
|---|---|---|---|---|---|
| 1 | [P1] | P1 | 0–2 | Quedan 3. Llega P3 (t=2) | [P2, P3, P1] |
| 2 | [P2,P3,P1] | P2 | 2–4 | Queda 1. Llega P4 (t=3) | [P3, P1, P4, P2] |
| 3 | [P3,P1,P4,P2] | P3 | 4–6 | Quedan 6 | [P1, P4, P2, P3] |
| 4 | [P1,P4,P2,P3] | P1 | 6–8 | Queda 1 | [P4, P2, P3, P1] |
| 5 | [P4,P2,P3,P1] | P4 | 8–10 | T=2 → **termina** | [P2, P3, P1] |
| 6 | [P2,P3,P1] | P2 | 10–11 | Termina en 1 ms | [P3, P1] |
| 7 | [P3,P1] | P3 | 11–13 | Quedan 4 | [P1, P3] |
| 8 | [P1,P3] | P1 | 13–14 | Termina en 1 ms | [P3] |
| 9 | [P3] | P3 | 14–16 | Quedan 2 | [P3] |
| 10 | [P3] | P3 | 16–18 | **FIN** | — |

```
 0   2   4   6   8  10 11 13 14 16 18
 +---+---+---+---+---+--+--+--+--+--+
 |P1 |P2 |P3 |P1 |P4 |P2|P3|P1|P3|P3|
 +---+---+---+---+---+--+--+--+--+--+
```

| Proceso | Llegada | T | t_fin | Tr | Te | R (1er uso) |
|---|---|---|---|---|---|---|
| P1 | 0 | 5 | 14 | **14** | **9** | 0 → **0** |
| P2 | 1 | 3 | 11 | **10** | **7** | 2 → **1** |
| P3 | 2 | 8 | 18 | **16** | **8** | 4 → **2** |
| P4 | 3 | 2 | 10 | **7** | **5** | 8 → **5** |
| **Media** | | | | **47/4 = 11,75** | **29/4 = 7,25** | **2,00** |

>  Conclusión: **cuanto más grande el quantum, menos cambios de contexto y más se parece a
FCFS.**

#### 8.5 Por prioridades - Gana el de prioridad más alta

Puede ser no preemptivo (termina entero) o preemptivo (si llega uno más prioritario, lo interrumpe).
Empate -> por orden de llegada. **Lee siempre la convición del enunciado**


**Ejemplo canónico — versión NO PREEMPTIVA**

- **t = 0**: solo P1 → corre 0→5.
- **t = 5**: listos P2(prio 1), P3(prio 3), P4(prio 1) → gana **P3 (3)** → corre 5→13.
- **t = 13**: quedan P2 y P4 con **empate (prio 1)** → desempate por llegada: **P2**
  (llegó antes) → corre 13→16. Luego **P4** → corre 16→18.

```
 0    5           13      16      18
 +----+-----------+-------+-------+
 | P1 |    P3     |  P2   |  P4   |
 +----+-----------+-------+-------+
```

| Proceso | Llegada | T | t_fin | Tr | Te |
|---|---|---|---|---|---|
| P1 | 0 | 5 | 5 | **5** | **0** |
| P2 | 1 | 3 | 16 | **15** | **12** |
| P3 | 2 | 8 | 13 | **11** | **3** |
| P4 | 3 | 2 | 18 | **15** | **13** |
| **Media** | | | | **46/4 = 11,50** | **28/4 = 7,00** |

#### Problemas del algorítmo


- **Hambre (starvation):** un proceso de prioridad baja puede quedarse esperando **para
  siempre** si siempre hay procesos de prioridad alta. Solución clásica: **envejecimiento
  (aging)** → aumentar la prioridad a los que llevan mucho tiempo esperando.
- **Inversión de prioridad:** un proceso de prioridad alta queda bloqueado esperando a uno
  de prioridad baja (típico con mutex/semáforos). Problema serio en sistemas reales


#### 8.6 HRRN — mayor ratio de respuesta

Para cada candidato calculas `ratio = (w + s) / s` (w = tiempo ya esperado, s = ráfaga) y eliges
el **mayor**. Es SJF + premio por antigüedad: quien lleva esperando gana ventaja → **no hay
hambre** y es **óptimo entre los no preemptivos**


**Ejemplo canónico resuelto**

- **t = 0**: solo P1 → corre 0→5.
- **t = 5** candidatos:
  - P2: w = 5−1 = 4, s = 3 → (4+3)/3 = **2,33**
  - P3: w = 5−2 = 3, s = 8 → (3+8)/8 = **1,38**
  - P4: w = 5−3 = 2, s = 2 → (2+2)/2 = **2,00**
  - Mayor ratio → **P2** → corre 5→8.
- **t = 8** candidatos:
  - P3: w = 8−2 = 6, s = 8 → 14/8 = **1,75**
  - P4: w = 8−3 = 5, s = 2 → 7/2 = **3,50**
  - Mayor → **P4** → corre 8→10.
- **t = 10**: solo P3 → corre 10→18.

```
 0    5      8     10           18
 +----+------+-----+-----------+
 | P1 |  P2  | P4  |    P3     |
 +----+------+-----+-----------+
```

| Proceso | Llegada | T | t_fin | Tr | Te |
|---|---|---|---|---|---|
| P1 | 0 | 5 | 5 | **5** | **0** |
| P2 | 1 | 3 | 8 | **7** | **4** |
| P3 | 2 | 8 | 18 | **16** | **8** |
| P4 | 3 | 2 | 10 | **7** | **5** |
| **Media** | | | | **35/4 = 8,75** | **17/4 = 4,25** |


#### 8.7 Colas multinivel

Varias colas con distinta prioridad; se elige siempre de la más alta. En la **realimentación**
(feedback), los procesos **cambian de cola según su comportamiento**: el que gasta todo su
quantum baja de cola; el que se bloquea pronto (interactivo) se queda arriba.

#### 8.7.1 Colas multinivel **estática**


Hay **varias colas** con **distinta prioridad** (ej.: cola de procesos del sistema (la más
alta), cola interactiva, cola de trabajos por lotes (la más baja)). El planificador
**siempre** elige de la cola más alta; solo si está vacía, mira la siguiente.

- Entre colas puede usarse: **prioridad fija** (siempre gana la de arriba → hambre de
  abajo), **Round Robin** entre colas o **asignación de porcentaje de CPU** (ej. 70% a la
  interactiva, 30% a la de lotes).

  Problema: la asignación es **estática**: un proceso no cambia de cola nunca. Un
  proceso de "lotes" que resulta ser interactivo seguirá abajo toda su vida.

#### 8.7.2 Colas multinivel de realimentación (feedback) **dinámica**


Misma idea, pero **los procesos pueden moverse entre colas** según su comportamiento:

- Todas las colas compiten (normalmente con RR y **quantums decrecientes**: q=8, q=4,
  q=2...).
- Un proceso que **gasta todo su quantum** (se comporta como "largo") **baja** a la cola
  inferior.
- Un proceso que **se bloquea pronto** (se comporta como "interactivo") **conserva o sube**
  de cola.


## 21. Tabla comparativa

Con el **ejemplo anterior**

| Algoritmo | Tipo | Tr promedio | Te promedio | ¿Óptimo? | ¿Hambre? |
|---|---|---|---|---|---|
| **FCFS** | no preemptivo | 10,25 | 5,75 | No | No |
| **SJF** | no preemptivo | 8,50 | 4,00 | **Sí** (espera mínima) | Sí |
| **SRTF** | preemptivo | **8,00** | **3,50** | **Sí** (espera mínima) | Sí |
| **RR (q=2)** | preemptivo | 11,75 | 7,25 | No | **No** (equitativo) |
| **Prioridad (no prec.)** | no preemptivo | 11,50 | 7,00 | No | Sí |
| **HRRN** | no preemptivo | 8,75 | 4,25 | **Sí** (no preemptivo) | **No** |


----

## Conclusiones


> 1. **SJF/SRTF** son los **mejores en promedio** (menor espera).
> 2. **RR** es el mejor para **interactividad** (buen tiempo de respuesta) pero empeora los
>    promedios por tantos cambios de contexto.
> 3. **FCFS** es el más simple pero sufre **efecto convoy**.
> 4. **Prioridad** es muy usado en la realidad pero sufre **hambre** (solución: aging).
> 5. **HRRN** combina lo mejor de SJF sin hambre.