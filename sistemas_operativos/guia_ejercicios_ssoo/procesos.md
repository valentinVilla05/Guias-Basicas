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

