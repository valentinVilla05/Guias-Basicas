## 1.- Introducción y definición de sistema operativo

El **sistema operativo** se define como el conjunto de programas que **controlan directamente los recursos hardware** de un computador, fundamentalmente la CPU, la memoria principal y los periféricos, para proporcionar una **maquina virtual** o "maquina extendida". Esta abstracción es más sencilla de programar y utilizar que el hardware físico subyacente.

El SO es la **capa de software más baja** y la única con potestad para interactuar directamente con la electrónica. Su existencia se justifica por la necesidad de interponer una capa mediana entre la complejidad del hardware y las necesidades de las aplicaciones.

Recursos bajo **el control del sistema operativo**:

- **CPU**: Gestión de registros y ejecución de instrucciones.
- **Memoria princiapl**: Control del espacio de almacenamiento volátil y direccionamiento.

* **Periféricos**: Gestión de discos, interfaces de red, dispositivos de entrada y salida.

## 2.- Arquitectura del sistema: Núcleo vs. Programas del sistema.

No todo el software que se distribuye bajo el nombre de un SO forma parte de su estructura crítica.

| **Características**           | **Núcleo (Kernel)**                                              | **Programas del sistema**                                          |
| ----------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------ |
| **Naturaleza**                | El SO propiamente dicho. Código que **acepta** llamadas          | Aplicaciones de utilidad que **realizan** llamadas al sistema      |
| **Modo de ejecución**         | **Privilegiado** (Modo Núcleo)                                   | Aplicaciones de utilidad que **realizan** llamadas al sistema      |
| **Funciones/Ejemplos**        | Gestión de procesos, memoria virtual, sistema de ficheros y real | Intérprete de órdenes (shell). compiladores editores y utilidades. |
| **Mecanismo de comunicación** | Atiende peticiones mediante interrupciones y traps               | Solicita servicios al núcleo mediante la interfaz de llamadas      |

### Controladores de dispositivos (Drivers)

Ubicadas en la base del núcleo, los **drivers** actúan como módulos traductores. Su misión es convertir las **operaciones genéricas** del núcleo en las **órdenes específicas** del hardware de un fabricante concreto. Esta modularidad permite que el sistema sea extensible sin necesidad de rediseñar el núcleo ante cada nuevo componente físico.

## 3.- La interfaz y le mecanismo de abstracción.

El concepto de **interfaz** es la piedra angular del diseño de sistemas. Se define como la parte accesible desde el exterior de un objeto que permite su uso sin conocer su complejidad interna.

- **Capas de software**: Una capa de nivel i que consume la interfaz del nivel inferior (i-1) para ofrecer el nivel superior (i+1) una interfaz manejable.

- **Traductor de interfaces**: El SO traduce una interfaz de hardware "incómoda" (registros, señales binarias, gestión de sectores) en una interfaz "cómoda" para el programador basada en abstracciones como **ficheros** y **procesos**.

- **Aislamiento y protección**: El SO tiene la potestad de "cerrar" el acceso a los niveles inferiores, el sistema garantiza la integridad del hardware y el aislamiento entre procesos.

```text
┌  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  ─┐
│                                CAPA DE NIVEL  i+1                            │
└- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ┘
┌──────────────────────────────────────────────────────────────────────────────┐
│                                INTERFAZ DE LA CAPA i                         │
└──────────────────────────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────────────────────────┐
│                                Capa de nivel i                               │
│                                                                              │
│       traduce: usa la interfaz de abajo y publica una más sencillas          │
└──────────────────────────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────────────────────────┐
│                            INTERFAZ DE LA CAPA i - 1                         │
└──────────────────────────────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────────────────────────────┐
│                                Capa de nivel i - 1                           │
│                                                                              │
│               Sus detalles quedan ocultos para la capa i + 1                 │
└──────────────────────────────────────────────────────────────────────────────┘
```

## 4.- Las dos visiones del sistema operativo

### Visión 1: Maquina extendida (hacia arriba).

Desde el punto de vista del programador, SO **virtualiza** el hardaware. Toma un recurso físico limitado y presenta una "copia lógica" más simple y segura. Así, cada programa actíua bajo la ilusión de poseer un procesador delicado y un espacio de memoria propio y enorme, independientemente de la realidad física del sistema.

### Visión 3: Administrador de recursos (Hacia abajo).

Desde la perspectiva del arquitecto, el SO gestiona los recursos escasos y arbitra un **conflicto de intereses** permanente:

- 1. **Maximizar el aprovechamiento**: Evitae la ociosidad de los recursos caros.
- 2. **Repartir con equidad**: Garantizar que todos los usuarios y tareas reciban atención.
     Casi ninguna decisión mejora ambos objetivos simultáneamente; favorecer la eficiencia suele perjudicar la equidad y viceversa.

#### Gestión de recursos específicos.

- **Tiempo de CPU**: El SO debe decidir qué proceso ejecuta y por cuánto tiempo. Es un "ciclo de control" donde el SO debe ceder el mando para que el trabajo progrese.
- **Espacio de memoria**: El reparto es simultáneo (varios procesos en memoria). El hardware debe intervenir para proteger las zonas de memoria impidiendo accesos cruzados.
- **Dispositivos de E/S**: Al ser recursos indivisibles, el reparto consiste en la **Planificación del disco** (u otros disspositivos), gestionando y ordenando la **cola de peticiones** para optimizar el acceso.

## 5.- Evolución: De monoprogramación a multiprogramación.

### Monoprogramación

Los sistemas de flujo único dedicaban la máquina a una sola tarea. El problema es la disparidad de velocidades: el procesador es órdenes de magnitud más rápido que los periféricos. Durante las esperas de la E/S, la CPU permanece ociosa.

_Ejemplo:_ En una tarea que alterna cómputa y E/S, la CPU podría estar ocupada solo 8 de cada 13 unidades de tiempo.

```text
┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬────┬────┬────┬────┬
│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │ 10 │ 11 │ 12 │ 13 │
├───┴───┴───┼───┴───┼───┴───┼───┴───┴───┴────┴────┴────┴────┴
│   CPU     │  E/S  │  CPU  │    A ha terminado
└───────────┴- - - -┴───────┘
┌- - - - - - - - - - - - - -┐──────────┬- - - - -┬──────┐
│       ESPERANDO           │   CPU    │  E/S    │ CPU  │
│ esperando a que A acabe   │          │         │      │
└- - - - - - - - - - - - - -┴──────────┴- - - - -┴──────┘
┌───────────┐- - - -┬───────┬──────────┐- - - - ┬──────┐
│    A      │ Ocio  │   A   │     B    │  Ocio  │   B  │
└───────────┴- - - -┴───────┴──────────┴- - - --┴──────┘
┌- - - - - -┐───────┌- - - - - - - - - ┌────────┌- - - ┐
│     Lib   │   A   │  Lib  |    Lib   │    B   │ Lib  |
└- - - - - -┘───────└- - - - - - - - - └────────└- - - ┘
┌- - - - - - - - - - - - - - - - - - - - - - - - - - - - ┐
│ tiempo · un trabajo no empieza hasta que el anterior ha│
│               concluido por completo                   │
│- - - - - - - - - - - - - - - - - - - - - - - - - - - - │
│ CPU ocupada 8 de 13 unidades (61,5 %) los dos recursos │
│        se turnan en lugar de trabajar a la vez         │
└- - - - - - - - - - - - - - - - - - - - - - - - - - - - ┘

```

### Multiprogramación

La solución consiste en mantener varios programas en memoria simultáneamente. Si el proceso activo se detiene por una E/S, el SO realiza un **cambio de contexto** y entre la CPU a otro proceso preparado.

- Eficiencia: En el mismo escenario, el aprovechamiento sube el **88,9%** terminando el trabajo en 9 unidades en lugar de 13.

- **Grado de multiprogramación**: Es el número de procesos residentes en memoria.
- **Hiperpaginación (Thrasing)**: Representa el límite negativo. Es un **compromiso de diseño** (punto óptimo): Si aumentamos excesivamente el número de procesos, el sistema dispone de tan poca memoria por proceso que dedica más tiempo a mover datos (paginar) que a ejecutar código útil, colpasando el rendimiento.

```text
┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐
│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │
├───┴───┴───┼───┴───┼───┴───┼───┴───┴───┘
│    CPU    │  E/S  │  CPU  │
└───────────┴- - - -┴───────┘
┌- - - - - -┬───────┬- - - - - -┬───────┐
│ preparado │  CPU  │    E/S    │  CPU  │
└- - - - - -┴───────┴- - - - - -┴───────┘
┌───────────┬───────┬───────────┬- -┬───┐
│     A     │   B   │     A     │Oci│ B │
└───────────┴───────┴───────────┴- -┴───┘
┌- - - - - -┬───────┬───────────┬- - - -┐
│   libre   │   A   │     B     │ libre │
└- - - - - -┴───────┴───────────┴- - - -┘
┌- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ┐
│ tiempo · las líneas verticales marcan los instantes en que la CPU cambia     │
│                               de trabajo                                     │
│- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - │
│      CPU ocupada 8 de 9 unidades (89 %) · solo queda parada mientras A       │
│                    ya ha terminado y B sigue en E/S                          │
└- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ┘


```

## 6.- Mecanismos hardware de soporte: Interrupciones y DMA

La multiprogrmación es inviable sin soporte hardware. El mecanismo fundamental es la **interrupción**, una señal eléctrica que obliga al procesador a **suspender la instrucción en curso** y saltar a una **Rutina de tratamient de interrupción (RTI)** del SO.

Es vital notar que la RTI no es "gratuita": **Atender una interrupción consume tiempo de CPU**. Sin embargo, es infinitamente más eficiente que una "espera activa" (bucle de consulta).

| **Emisor**            | **Función/Propósito**                     | **Consecuencia y vínculo al SO**                                         |
| --------------------- | ----------------------------------------- | ------------------------------------------------------------------------ |
| **Reloj del sistema** | Generar señales a intervalos fijos        | **Tiempo compartido:** Permite al SO recuperar el control forzosamente   |
| **Dispositivo E/S**   | Notificar que una operación ha concluido  | **Multiprogramación:** Desbloquea procesos que esperaban datos           |
| **Controlador DMA**   | Avisar que una transferencia ha terminado | **Eficiencia:** Los datos ya están en memoria sin intervención de la CPU |

## 7.- Tiempo compartidos y sistema multiusuario.

El **tiempo compartido** es una evolución de la multiprogramación orientada a la interactividad. Se basa en el **"cuanto" de tiempo** (quantum): el reloj interrumpe periódicamente para que el SO rote la CPU entre todos los procesos. Esto evita que un proceso de cálculo intensivo monopolice el sistema.

- **Sistemas multiusuario**: Añaden una capa de complejidad al reparto de recursos mediante dos conceptos clave:
  - **Identidad**: El SO debe conocer al propietario de cada proceso y fichero.
  - **Protección**: Garantizar que los usuarios no interfieren entre sí. Este modelo, nacido para amortizar maquinas costosas en los años 70, es hoy la base de la **computación en la nube**, donde la contabilidad y el aislamiento entre miles de clientes son críticas.

* **Solo multiprogramación**: La conmutacion depende del proceso en ejecución

```text
En la CPU se ejecuta:
┌────────────────────────────────┬───────┬───────┐
│     P1 - cálculo prolongado    │  P2   │   P3  │
└────────────────────────────────┴───────┴───────┘
P2 y P3 esperan sin obtener CPU
```

- **Tiempo compartido**: el reloj limita cuánto puede retener la CPU cada proceso

```text
En la CPU se ejecuta:
┌──────────┬- - ┬───────┬- - ┬───────┬- - ┬─────────┬- - ┬───────┬- - ┬───────┐
│     P1   │       P2   │    |   P3  │    |  P1     │    |  P2   │    |   P3  │
└──────────┴- - ┴───────┴- - ┴───────┴- - ┴─────────┴- - ┴───────┴- - ┴───────┘

Duran un "cuanto" y hay interrupciones de reloj a intervalos fijos con independencia de la que haga el proceso.

┬- - ┬
│    |  ---> franjas del sistema operativo: atiende la interrupcuón y
┴- - ┴  decide quien sigue (cambio de contexto).

Los tres progresan a la vez: cada usuario percibe una respuesta aunque hay otros programas ejecutándose.
```

## 8.- Panorama actual y sistemas de tiempo real

La arquitectura del SO se adopta según el recurso que resulte crítico en cada ámbito, variando las escalas de memoria y cómputo de forma masiva:

- **Empotrado/Tiempo Real**: (Escala: KBs de memeoria). Recurso crítico: **Cumplimiento de plazos**.

- **Móvil**: (Escala: 8-16GB de memoria). Recurso críticos: **Energía (batería)** y optimización de bateria.

- **Escritorio/Portatil**: (16-32GB de memoria). Recurso crítico: **Tiempo de respuesta** al usuario.

- **Servidor/Nube**: (Cientos de GB): Recurso crítico: **Aislamiento** y rendimiento global del conjunto.

### Sistemas de tiempo real (RTOS)

Aquí la correción depende de la precisión temporal. El criterio es garantizar plazos, incluso si esto implica dejar la CPU ociosa (sacrificando aprovechamiento por predictibilidad).

- **Tiempo real estricto (Hard RT)**: El incumplimiento de un plazo equivale a un fallo catastrófico.

- **Tiempo real flexible (Soft RT)**: El incumplimiento degrada la cálidad pero el dato sigue siendo útil.

## 9.- Resumen y conceptos clave

- **Dualidad funcional**: El SO es Maquina extendida (abstracción) y Administrador de Recursos (eficiencia/equidad).
- **Frontera privilegiada**: El kernel ejecuta en modo privilegiado; los programas del sistema en modo usuario.
- **Ciclo de control**: El SO debe ceder la CPU para que se ejecute trabajo útil, dependiendo de la interrupciones para recuperar el mando.
- **Multiprogramación**: Técnica hardware esencial que sustenta el tiempo compartido y evita monopolios de CPU.
- **DMA e interrupciones de E/S**: El binomio que permite que el procesador realice cómputo útil mientras los datos se transfieren.
- **Compromiso de diseño**: El grado de multiprogramación tiene un punto óptimo, superarlo conduce a la **hiperpaginación**.
- **Tiempo real**: Cambio de paradigma donde el plazo garantizado prevalece sobre el aprovechamiento del procesador.
