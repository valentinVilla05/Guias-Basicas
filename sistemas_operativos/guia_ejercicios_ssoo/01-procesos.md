# Guia para resolver cualquier ejercicios de Procesos

> Esta guía va a ser un poco extensa ya que también se tocan conceptos teóricos que son muy importantes y también se explica claramente el funcionamiento de cada una de las partes y componentes

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
|| Estado | Qué es | Analogía |
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
Nuevo --admitir--> Listo <--termina E/S--+--despachar--> Ejecutando --termina--> Terminado
                                         ^   |   |
                                         |   +---+--pide E/S--> Bloqueado
                                    (preempción: quantum o llega otro más urgente)
```

* **Ejecutado -> Listo** = Le quitan la CPU sin haber terminado

* **Ejecutado -> Bloqueado** = Pidió E/S

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

| Proceso | Llegada | T | t_fin | Tr | Te |
|---|---|---|---|---|---|
| P1 | 0 | 5 | 5 | 5 | 0 |
| P2 | 1 | 3 | 8 | 7 | 4 |
| P3 | 2 | 8 | 16 | 14 | 6 |

```
 0    5      8           16      18
 +----+------+-----------+-------+
 | P1 |  P2  |    P3     |  P4   |
 +----+------+-----------+-------+
```

**Tr prom = 10,25 · Te prom = 5,75**

> Sufre el efecto **convoy**: Si el primero es largo, todos esperan 

#### 8.2 SJF - El trabajo más corto pasa primero


Cuando hay que elegir, gana el de **menor ráfaga T**. Produce el **menor tiempo de espera
promedio posible** (óptimo). Empates -> por orden de llegada

- t=0: solo P1 → 0-5. t=5: entre P2(3), P3(8), P4(2) → gana **P4** → 5-7.
  t=7: P2(3) < P3(8) → 7-10. t=10: P3 → 10-18.

| Proceso | Llegada | T | t_fin | Tr | Te |
|---|---|---|---|---|---|
| P1 | 0 | 5 | 5 | 5 | 0 |
| P2 | 1 | 3 | 8 | 7 | 4 |
| P3 | 2 | 8 | 16 | 14 | 6 |

```
 0    5    7     10           18
 +----+----+-----+-----------+
 | P1 | P4 |  P2 |    P3     |
 +----+----+-----+-----------+
```

**Tr prom = 8,50 · Te prom = 4,00**

#### 8.3 SRTF — Menor TIEMPO RESTANTE, primero (SRT apropiativo)

| Proceso | Llegada | T | t_fin | Tr | Te |
|---|---|---|---|---|---|
| P1 | 0 | 5 | 5 | 5 | 0 |
| P2 | 1 | 3 | 8 | 7 | 4 |
| P3 | 2 | 8 | 16 | 14 | 6 |


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

#### 8.5 Por prioridades - Gana el de prioridad más alta

Puede ser no preemptivo (termina entero) o preemptivo (si llega uno más prioritario, lo interrumpe).
Empate -> por orden de llegada. **Lee siempre la convición del enunciado**

#### 8.6 HRRN — mayor ratio de respuesta*

Para cada candidato calculas `ratio = (w + s) / s` (w = tiempo ya esperado, s = ráfaga) y eliges
el **mayor**. Es SJF + premio por antigüedad: quien lleva esperando gana ventaja → **no hay
hambre** y es **óptimo entre los no preemptivos**.

#### 8.7 Colas multinivel (bonus)

Varias colas con distinta prioridad; se elige siempre de la más alta. En la **realimentación**
(feedback), los procesos **cambian de cola según su comportamiento**: el que gasta todo su
quantum baja de cola; el que se bloquea pronto (interactivo) se queda arriba.
