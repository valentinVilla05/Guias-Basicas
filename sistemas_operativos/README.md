# Sistemas Operativos — Temario de teoría

El temario oficial recorre las **cuatro grandes responsabilidades** del sistema operativo —procesos, memoria, entrada/salida y almacenamiento— repartidas en **10 temas** agrupados en **4 bloques**.

---

## Índice

| Bloque                                                      | Temas                                                                        |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------- |
| [I. Fundamentos](#bloque-i--fundamentos)                    | 1. Introducción a los SO · 2. Estructuras de los SO                          |
| [II. Procesos](#bloque-ii--procesos)                        | 3. Gestión de Procesos · 4. Gestión de Hilos · 5. Planificación              |
| [III. Memoria](#bloque-iii--memoria)                        | 6. Gestión de la memoria · 7. Memoria virtual                                |
| [IV. E/S y almacenamiento](#bloque-iv--es-y-almacenamiento) | 8. Gestión de la E/S · 9. Planificación del disco · 10. Sistemas de Archivos |

**Repaso previo:** el temario da por conocido el capítulo de arquitectura (bus del sistema, ciclo de instrucción, mecanismo de interrupción, técnicas de E/S, jerarquía de memoria y localidad, pila, multinúcleo).

---

## Bloque I — Fundamentos

Qué es un sistema operativo y cómo está construido por dentro.

### Tema 1. Introducción a los Sistemas Operativos

Las dos visiones del SO: **máquina extendida** (proveedor de abstracciones cómodas sobre el hardware) y **administrador de recursos** (árbitro de CPU, memoria y dispositivos).

### Tema 2. Estructuras de los Sistemas Operativos

Cómo se organiza internamente el SO y cómo se accede a él desde los programas.

---

## Bloque II — Procesos

La abstracción central: dar a cada programa la ilusión de un procesador propio.

### Tema 3. Gestión de Procesos

El proceso como unidad de ejecución y de asignación de recursos.

### Tema 4. Gestión de Hilos

Separar la unidad de ejecución (hilo) de la unidad de propiedad de recursos (proceso).

### Tema 5. Planificación de procesos e hilos

Qué proceso ejecuta y durante cuánto tiempo: políticas frente a mecanismos.

---

## Bloque III — Memoria

Dar a cada programa la ilusión de una memoria propia e ilimitada.

### Tema 6. Gestión de la memoria

Repartir la memoria física entre varios procesos con protección entre ellos.

### Tema 7. Memoria virtual

Ejecutar procesos que no caben enteros en memoria principal.

---

## Bloque IV — E/S y almacenamiento

Comunicar con dispositivos mucho más lentos que el procesador y guardar la información de forma persistente.

### Tema 8. Gestión de la entrada y salida

Cómo el SO abstrae la enorme variedad de dispositivos bajo una interfaz uniforme.

### Tema 9. Planificación del disco

Ordenar las peticiones para reducir el tiempo de búsqueda.

### Tema 10. Sistemas de Archivos

La abstracción de fichero con nombre y su organización sobre el disco.

---
