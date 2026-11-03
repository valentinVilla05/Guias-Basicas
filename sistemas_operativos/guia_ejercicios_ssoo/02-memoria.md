## Guía para resolver ejercicios de Memoria de cualquier tipo 

**La idea central de todo el tema en una frase:**

> El **proceso** trabaja con **direcciones virtuales**, la **RAM** usa **direcciones físicas**, y la **tabla de páginas (+ TLB) es el diccionario que traduce unas en otras**

# 1. Conceptos Fundamentales

## 1.1 Los dos espacios de direcciones


| | **Espacio Virtual (lógico)** | **Espacio Físico (RAM)** |
|---|---|---|
| ¿Quién lo ve? | El **proceso** | El **hardware / bus de memoria** |
| ¿Quién lo crea? | El SO le da su propio espacio | Depende del chip (la RAM real) |
| ¿Tamaño típico? | 4 GB (32 bits), 256 TB (64 bits) | 2 GB, 8 GB, 16 GB... |
| ¿Empieza en? | 0 (cada proceso empieza en 0) | 0 |
| ¿Es único? | **No**: todos los procesos tienen el suyo (y muchos empiezan en 0) | **Sí**: es el que hay |

**Analogía:** el proceso vive en una *dirección de mentira* que él solo entiende (como el "piso 3, puerta 5" de un hotel: cada hotel tiene un piso 3), y la RAM es la calle real con números de porta únicos. La tabla de páginas es el *recepcionista* que traduce.


```
  CPU (proceso)
      │  genera DIRECCIÓN VIRTUAL
      ▼
   ┌─────┐   ¿está en la TLB?  SÍ ──► traducción ya conocida
   │ MMU │──┤
   └─────┘   NO ──► lee la TABLA DE PÁGINAS en RAM ──► marco
      │
      ▼  DIRECCIÓN FÍSICA (marco + desplazamiento)
   ┌─────┐
   │ RAM │  guarda/lee el dato
   └─────┘
```

## 1.2 Conceptos esenciales

- **Página:** trozo de tamaño **fijo** del espacio **virtual**. Potencia de 2 (4 KB, 64 KB, 2 MB...).
- **Marco (frame):** trozo de tamaño **fijo** de la **RAM**. **Mismo tamaño que la página** (por eso encajan 1 a 1).
- **Desplazamiento (offset):** posición **dentro** de la página/marco. Ej: "byte 5 de la página 7".
- **Tabla de páginas:** lista en RAM con **una entrada por página** del proceso → dice en qué marco está + permisos + bits de estado.
- **MMU:** hardware que traduce direcciones en nanosegundos.
- **TLB:** caché diminuta y rapidísima de traducciones ya hechas (página → marco).
- **Bit de validez (V):** 1 = la página está en RAM; 0 = no está → al tocarla, **page fault**.
- **Bit de modificación / dirty (M):** 1 = se ha escrito → antes de descartarla hay que guardarla en disco.
- **Bit de referencia (R):** 1 = se ha usado hace poco (para decidir a quién echar).
- **Swap / intercambio:** zona del disco con páginas que no caben en RAM.

### Fragmentación 

| | **Paginación** | **Segmentación** |
|---|---|---|
| Tamaño de los trozos | Fijo (páginas) | Variable (segmentos) |
| Fragmentación **interna** | **Sí** (sobra dentro del último marco) | No |
| Fragmentación **externa** | **No** (todo trozo de RAM es un marco) | **Sí** (huecos entre segmentos) |
| ¿Hay que compactar? | No | Sí |

---

# PARTE 2 — CONVERSIONES Y BITS 

## 2.1 La regla de oro

$$\boxed{2^k \text{ Bytes} \;\Longleftrightarrow\; k \text{ bits}}$$

**Por qué:** si hay $2^k$ cosas que numerar, necesitas $k$ bits, porque $k$ bits dan $2^k$ combinaciones (0 hasta $2^k - 1$)


## 2.2 Tabla de equivalencias (de memoria)

| Unidad | En bytes | Potencia de 2 | Bits |
|---|---|---|---|
| 1 B | 1 | $2^0$ | 0 |
| 1 KB | 1.024 B | $2^{10}$ | 10 |
| 1 MB | 1.024 KB = 1.048.576 B | $2^{20}$ | 20 |
| 1 GB | 1.024 MB | $2^{30}$ | 30 |
| 1 TB | 1.024 GB | $2^{40}$ | 40 |


## 2.3 Método de 3 pasos: tamaño → bits

> **Ejemplo: 256 MB**
> 1. $256 = 2^8$
> 2. $MB = 2^{20}$
> 3. $2^8 \cdot 2^{20} = 2^{28}$ Bytes → **28 bits**

> **Ejemplo: 4 KB** (la página típica)
> $4 = 2^2$, $KB = 2^{10}$ → $2^{12}$ → **12 bits** ← esto es el **desplazamiento**

> **Ejemplo: 2 GB**
> $2 = 2^1$, $GB = 2^{30}$ → $2^{31}$ → **31 bits** ← esta es la **dirección física**

> **Ejemplo: 16 MB** → $2^4 \cdot 2^{20} = 2^{24}$ → 24 bits

### Cuando el número NO es potencia de 2 (caso del 3 GB)

$3$ GB $= 3 \times 2^{30}$ Bytes. **No se puede expresar como $2^k$**, así que:

- Para contar **cuántas páginas de 4 KB** caben:
  $$\frac{3 \times 2^{30}}{2^{12}} = 3 \times 2^{18} = 786.432 \text{ páginas}$$
- Para saber **cuántos bits necesito para numerar** esas posiciones:
  $$\lceil \log_2(3 \times 2^{30}) \rceil = 32 \text{ bits} \quad (\text{porque } 2^{31} < 3\cdot2^{30} < 2^{32})$$




# PARTE 3 — ESTRUCTURA DE LAS DIRECCIONES

---

## 3.1 Dirección virtual = página + desplazamiento

```
   DIRECCIÓN VIRTUAL (p. ej. 32 bits)
   ┌──────────────────────┬──────────────────┐
   │  NÚMERO DE PÁGINA p  │ DESPLAZAMIENTO d │
   │     (bits altos)     │   (bits bajos)   │
   └──────────────────────┴──────────────────┘
```

$$d = \log_2(\text{Tamaño de Página})$$

$$p = \text{bits totales de la dirección virtual} - d$$

> **Ejemplo resuelto:** proceso de **4 GB** ($2^{32}$) con páginas de **4 KB** ($2^{12}$):
> - bits virtuales $= \log_2(2^{32}) = 32$
> - $d = \log_2(2^{12}) = 12$ bits
> - $p = 32 - 12 = \mathbf{20}$ **bits** → el proceso puede tener $2^{20} = 1.048.576$ páginas

$$\text{bits físicos} = \log_2(\text{RAM})$$

$$f = \text{bits totales de la dirección física} - d$$

> **Continuación del ejemplo:** RAM de **2 GB** ($2^{31}$):
> - bits físicos $= 31$
> - $f = 31 - 12 = \mathbf{19}$ **bits** → la RAM tiene $2^{19} = 524.288$ marcos
> - **Comprobación:** 19 (marco) + 12 (desplazamiento) = 31 bits

### Comprobaciones

1. $p = \text{bits}_v - d$
2. $f = \text{bits}_f - d$
3. $2^p$ = nº de páginas posibles · $2^f$ = nº de marcos de la RAM

> $p$ y $f$ **no tienen por qué valer lo mismo**. La página la decide el tamaño de página y la RAM (aquí 20 y 19 bits). En un proceso de 4 GB con RAM de 4 GB sí coincidirían (20 y 20)


## 3.3 Traducir una dirección concreta (paso a paso)

**Enunciado típico:** *dirección virtual `0x80001234`, páginas de 4 KB; la tabla dice que la página `0x80001` está en el marco `5`. ¿Dirección física?*

**Paso 1** — Saca el desplazamiento. Página de 4 KB = 12 bits = **3 dígitos hex** → los 3 últimos dígitos:
$$d = \texttt{0x234}$$

**Paso 2** — El resto es el número de página:
$$p = \texttt{0x80001}$$

**Paso 3** — Busca en la tabla: página `0x80001` → **marco 5**.

**Paso 4** — Monta la dirección física = marco + mismo desplazamiento:
$$\text{física} = \texttt{0x00005234}$$

> **Truco visual:** solo se sustituyen los bits altos; **los 3 últimos dígitos hex se quedan idénticos**:
> `0x8000**1234**` → `0x0000**5**234` (el `1` de la página pasa a ser el `5` del marco).

**Si el bit de validez de esa página es 0** → la página **no está en RAM** → **page fault** (el SO tiene que traerla antes de poder traducir).

## 3.4 Cálculos sobre la tabla de páginas

| Qué | Fórmula | Ejemplo (4 GB, 4 KB, 4 B/entrada) |
|---|---|---|
| Nº de entradas | $2^{p}$ o virtual/página | $2^{20} = 1.048.576$ |
| Tamaño de la tabla | entradas × bytes/entrada | $2^{20} \times 4$ B = **4 MB** |
| Nº de marcos de la RAM | RAM / página = $2^{f}$ | $2^{31}/2^{12} = 2^{19}$ |
| Tabla invertida (1 entrada por marco) | $2^{f}$ × bytes/entrada | $2^{19} \times 4$ B = 2 MB |


## 3.5 Número máximo de procesos en la RAM

$$\text{Nº máximo de procesos} = \frac{\text{Tamaño Memoria Física}}{\text{Tamaño Memoria Virtual de un proceso}}$$

> **Advertencia:** es la fórmula **pesimista**: asume que cada proceso usa **toda** su memoria virtual a la vez. Con paginación bajo demanda caben **muchos más** procesos (cada uno solo tiene sus páginas en uso). Úsala si así la dieron, pero di esa suposición si te lo preguntan.

> **Ejemplo:** RAM 2 GB ($2^{31}$), procesos de 512 MB ($2^{29}$): $2^{31}/2^{29} = \mathbf{4}$ procesos.

---


# PARTE 4 — PAGINACIÓN

---

## 4.1 Paginación de UN nivel (la base)

**Idea:** cortar el espacio virtual en **páginas** y la RAM en **marcos** del mismo tamaño, y llevar la cuenta en la tabla de páginas.

### Estructura de una entrada de la tabla

```
   ENTRADA DE LA TABLA DE PÁGINAS (p. ej. 4 bytes = 32 bits)
   ┌──────────────┬───┬───┬───┬─────────────┐
   │ Nº de marco  │ V │ M │ R │ permisos    │
   │ (los bits    │val│dirt│ref│ rwx, u/s   │
   │  físicos)    │   │   │   │             │
   └──────────────┴───┴───┴───┴─────────────┘
```


| Bit | Significado | ¿Para qué sirve? |
|---|---|---|
| **V** (validez) | 1 = en RAM, 0 = fuera | Si es 0 y se accede → **page fault** |
| **M** (modificación / dirty) | 1 = se ha escrito | Si es 1, hay que **escribirla en disco** antes de reutilizar el marco |
| **R** (referencia) | 1 = usada recientemente | Para los algoritmos de reemplazo (LRU, Clock...) |
| permisos | lectura/escritura/ejecución, usuario/supervisor | Protección (que un proceso no escriba donde no debe) |


### Traducción (1 nivel)

1. Separar la dirección virtual → `p | d`
2. Entrada `p` de la tabla → obtener **marco** (si V=0 → page fault)
3. $\text{dirección física} = \text{marco} \times \text{tamaño página} + d$

### Coste SIN TLB

**2 accesos a memoria** por cada dato: uno para leer la tabla, otro para el dato.

## 4.2 Paginación de DOS o MÁS niveles

**Problema que resuelve:** con 32 bits y 4 KB, la tabla tiene $2^{20}$ entradas = **4 MB contiguos** por proceso. En vez de reservar 4 MB seguidos, **paginamos la propia tabla**: el número de página se parte en varios campos.

### Estructura de 2 niveles (32 bits, páginas de 4 KB, entrada de 4 B)

```
   │ índice TABLA RAÍZ (10 bits) │ índice SUBTABLA (10 bits) │ desplazamiento (12 bits) │
```

- Los 20 bits de número de página se reparten **10 + 10**.
- **Por qué 10:** para que cada tabla quepa en **exactamente una página**:
  $$\text{bits por nivel} = \log_2\left(\frac{\text{tamaño página}}{\text{bytes por entrada}}\right) = \log_2\left(\frac{4096}{4}\right) = \log_2(1024) = 10$$
- Raíz: $2^{10} \times 4$ B = **4096 B = 1 página** 
- Cada subtabla: igual, 4 KB. **Solo se crean las subtablas que se usan.**
---
### Traducción (2 niveles) — 3 accesos a memoria

1. Campo 1 → mira en la **raíz** (guardada en el registro **PTBR**) → marco de la subtabla
2. Campo 2 → mira en la **subtabla** → marco de la página
3. Marco + desplazamiento → dirección física (+ 1 acceso más para el **dato**)
----
### Reparto de bits (cómo lo piden en examen)

| Pregunta | Cómo se resuelve |
|---|---|
| ¿Cuántos bits por nivel para que cada tabla quepa en 1 página? | $\log_2(\text{página}/\text{bytes entrada})$ |
| ¿Cuántas entradas tiene cada tabla? | $2^{\text{bits de ese nivel}}$ |
| ¿Cuánto ocupa la tabla raíz? | $2^{b_1} \times$ bytes entrada |
| ¿Cuántos accesos a memoria hace la traducción? | nº de niveles (+1 si cuentan el dato) |

**Regla general del coste con $n$ niveles:** en un **fallo de TLB** hay que leer **$n$ entradas de tabla + 1 dato**.

## 4.3 Tabla invertida (para que no crezca con los procesos)

- Una entrada **por cada marco de RAM** (no por página): guarda *(proceso, página)* que lo ocupa.
- **Ventaja:** tamaño fijo y pequeño ($2^{f}$ entradas), no depende del nº de procesos.
- **Desventaja:** para traducir hay que **buscar** (lineal o con **hash**), más lento.
- La usan máquinas reales como PowerPC, SPARC, Itanium.

---

# PARTE 5 — TLB (el acelerador)


## 5.1 Qué es y por qué existe

Sin TLB, **cada** acceso a memoria cuesta **2 idas a RAM** (tabla + dato), y la RAM es lenta. La TLB es una **caché de traducciones página→marco** dentro de la MMU:

- **Muy rápida** (1-10 ns) y **muy pequeña** (64-1024 entradas).
- Es **asociativa**: se busca por contenido ("¿alguien tiene la traducción de esta página?"), no por número.
- Aprovecha la **localidad**: un programa usa siempre las mismas pocas páginas → casi siempre acierta ($h$ típico del 95%-99%).

## 5.2 Los dos caminos

```
   CPU pide un dato
        │
        ▼
   ¿Traducción en TLB?
     ├── SÍ (prob. h)      → t_tlb  +  dato en RAM (t_ram)          = t_tlb + t_ram
     └── NO (prob. 1−h)    → t_tlb  +  tabla en RAM (t_ram)
                             + dato en RAM (t_ram)                   = t_tlb + 2·t_ram
```


## 5.3 FÓRMULA DEL TIEMPO EFECTIVO DE ACCESO

**Fórmula completa (los dos casos):**

$$T_m = h \cdot (t_{\text{tlb}} + t_{\text{ram}}) + (1 - h) \cdot (t_{\text{tlb}} + 2 \cdot t_{\text{ram}})$$

**Desarrollo (para entenderla, no memorizarla a ciegas):**

$$T_m = \underbrace{h\,t_{\text{tlb}} + h\,t_{\text{ram}}}_{\text{acierto}} + \underbrace{(1-h)\,t_{\text{tlb}} + (1-h)\,2t_{\text{ram}}}_{\text{fallo}}$$

El TLB **siempre** se consulta (acierte o falle) → agrupando $t_{\text{tlb}}(h + 1 - h) = t_{\text{tlb}}$:

$$\boxed{T_m = t_{\text{tlb}} + (2 - h) \cdot t_{\text{ram}}}$$

**Dónde está la $h$ dentro de la versión simplificada:** cada acierto "ahorra" un acceso a RAM, y hay $h$ de aciertos → se resta $h$ al 2.

Donde:

- **$h$** = tasa de aciertos del TLB (*hit rate*) en **decimal** (92% = 0,92)
- **$t_{\text{tlb}}$** = tiempo de acceso a la TLB
- **$t_{\text{ram}}$** = tiempo de **cada** acceso a la RAM (tanto para la tabla como para el dato)

### Truco de comprobación

| Caso | Con la fórmula | Sentido |
|---|---|---|
| $h = 1$ (todo acierto) | $t_{\text{tlb}} + 1 \cdot t_{\text{ram}}$ | Solo TLB + dato |
| $h = 0$ (todo fallo) | $t_{\text{tlb}} + 2 \cdot t_{\text{ram}}$ | TLB + tabla + dato |
| Sin TLB | $2 \cdot t_{\text{ram}}$ | Tabla + dato |

Si tu resultado no encaja con estos extremos → **hay un error**


**Preguntas de examen que salen de este mismo enunciado:**

| Pregunta | Respuesta |
|---|---|
| ¿Sin TLB? | $2 \times 100 = \mathbf{200}$ ns |
| ¿Con acierto del 100%? | $10 + 100 = \mathbf{110}$ ns |
| ¿Con acierto del 0%? | $10 + 200 = \mathbf{210}$ ns |
| ¿Ahorro respecto a no tener TLB? | $(200-118)/200 = \mathbf{41\%}$ |
| ¿Cuánto más rápido es? | $200/118 = \mathbf{1,69\times}$ |

## 5.5 Despejes (cuando la incógnita es otra)

**¿Qué $h$ hace falta para lograr $T_m$?**

$$h = 2 - \frac{T_m - t_{\text{tlb}}}{t_{\text{ram}}}$$

> *Ej: ¿$h$ para $T_m = 120$ ns con 10 y 100?* → $h = 2 - \frac{120-10}{100} = 2 - 1{,}10 = 0{,}90$ → **90%**

**¿Qué $t_{\text{ram}}$ hace falta?** → $t_{\text{ram}} = \dfrac{T_m - t_{\text{tlb}}}{2 - h}$

**¿Qué $t_{\text{tlb}}$ hace falta?** → $t_{\text{tlb}} = T_m - (2-h)\cdot t_{\text{ram}}$

## 5.6 Variantes según el enunciado

| Situación | Fórmula | Accesos a RAM en un fallo de TLB |
|---|---|---|
| Sin TLB | $T_m = 2\,t_{\text{ram}}$ | 2 siempre |
| TLB + tabla de 1 nivel | $T_m = t_{\text{tlb}} + (2-h)\,t_{\text{ram}}$ | 2 |
| TLB + tabla de **2 niveles** | $T_m = t_{\text{tlb}} + (3-h)\,t_{\text{ram}}$ | 3 |
| TLB + tabla de **n niveles** | $T_m = t_{\text{tlb}} + (n+1-h)\,t_{\text{ram}}$ | $n+1$ |

> **Regla:** en el fallo se leen **1 entrada por nivel de tabla** + **1 dato**; el TLB se paga siempre.

> **Ejemplo 2 niveles:** 10 ns, 100 ns, $h = 0{,}95$ → $10 + (3-0{,}95)\times100 = \mathbf{215}$ ns
> (check: $0{,}95 \times 110 + 0{,}05 \times 310 = 104{,}5 + 15{,}5 = 215$)

## 5.7 Con caché de datos además (AMAT)

$$\text{AMAT} = h_c \cdot t_{\text{hit}} + (1 - h_c) \cdot t_{\text{ram}}$$

Y si la tabla también pasa por la caché, misma estructura con AMAT en lugar de $t_{\text{ram}}$:

$$T_m = t_{\text{tlb}} + (2 - h) \cdot \text{AMAT}$$

> **Ejemplo:** caché $h_c = 0{,}95$, $t_{\text{hit}} = 2$ ns, RAM 100 ns; TLB 10 ns, $h = 0{,}98$:
> - AMAT $= 0{,}95 \times 2 + 0{,}05 \times 100 = 1{,}9 + 5 = 6{,}9$ ns
> - $T_m = 10 + (2 - 0{,}98) \times 6{,}9 = \mathbf{17{,}04}$ ns

---

# PARTE 6 — MEMORIA VIRTUAL Y PAGE FAULT


## 6.1 Paginación bajo demanda

Las páginas **no se cargan todas**: solo se cargan cuando el proceso las toca. Así un proceso de 4 GB puede "vivir" en una máquina con 1 GB. La parte que no está en RAM está en el **disco (swap)**


## 6.2 Manejo de un page fault (los pasos, preguntan mucho)

1. El proceso toca una página con **V = 0** → **interrupción (trap)** al SO.
2. El SO comprueba: ¿es un fallo **legítimo** (dirección válida, página no cargada) o un **error del programa** (dirección prohibida)?
   - Error del programa → **segfault: se mata el proceso**.
3. Localiza la página en **disco** (swap o fichero).
4. Elige un **marco**: libre si lo hay; si no, **víctima** con el algoritmo de reemplazo.
5. Si la víctima tiene **M = 1 (dirty)** → **escribirla** primero en disco.
6. **Leer** la página requerida del disco al marco.
7. **Actualizar la tabla** (marco nuevo, V=1, M=0, R=1).
8. **Repetir la instrucción** que falló (la CPU reintenta el acceso).

## 6.3 Efecto en el tiempo de acceso

$$T_m = (1 - p) \cdot T_{\text{normal}} + p \cdot T_{\text{fault}}$$

- $p$ = probabilidad de page fault (ej. $10^{-6}$: una vez entre un millón)
- $T_{\text{fault}} \approx 8\text{-}10$ ms $\approx 8.000.000$ ns (disco)

> **Ejemplo:** $T_{\text{normal}} = 118$ ns, $p = 10^{-6}$, $T_{\text{fault}} = 8$ ms:
> $T_m \approx 0{,}000118 + 8 \approx \mathbf{8\ µs}$
>
> **Conclusión que hay que saber escribir:** aunque los fallos son rarísimos, **un page fault cuesta lo que decenas de miles de accesos a memoria**, así que domina el tiempo total. Por eso importa tanto elegir bien a quién echar.

## 6.4 Por qué el bit dirty es importante

- Víctima **limpia (M=0)**: basta con **leer** la nueva página (1 sola E/S).
- Víctima **sucia (M=1)**: primero **escribir** la vieja y luego **leer** la nueva (2 E/S → el fault es el doble de caro).

---

# PARTE 7 — ALGORITMOS DE REEMPLAZO (el ejercicio de la tablita)


**Qué dan:** una **cadena de referencia** (ej. `7,0,1,2,0,3,0,4,2,3,...`) y un **nº de marcos**.
**Qué piden:** rellenar la tabla marco a marco y contar los **fallos** (marcas ✓).

### Reglas de oro

1. Los marcos **empiezan vacíos** → las primeras páginas distintas **fallan siempre**.
2. Si la página **ya está** → acierto (marcar R=1 en el algoritmo del reloj).
3. Si está llena → aplica el algoritmo para elegir **víctima**.

### Los 4 algoritmos

| Algoritmo | ¿A quién echa? | ¿Cómo se implementa? | Anomalía de Belady* |
|---|---|---|---|
| **FIFO** | la **más antigua** (llegó primero) | cola / puntero circular | **SÍ** (más marcos = más fallos) |
| **LRU** | la que **más tiempo sin usarse** | lista `[más vieja → más nueva]` | No (es de pila) |
| **Óptimo (OPT)** | la que **más tardará en usarse** (mira hacia delante) | imposible en la práctica | No (es de pila) |
| **Clock (Second Chance)** | la de **bit R = 0** del anillo | hardware | No |

\* **Anomalía de Belady:** con FIFO puede pasar que **más marcos den más fallos**. Con LRU y OPT **nunca** ocurre (más marcos ⇒ igual o menos fallos). Si en un ejercicio te sale que 4 marcos da más fallos que 3 con FIFO → **no te has equivocado, es Belady**.

### Método de resolución (igual para todos)

1. Dibuja tabla: **filas = marcos**, **columnas = cada acceso**.
2. Rellena columna a columna:
   - ¿La página ya está? → copia la columna (acierto).
   - ¿Hay hueco? → métela (fallo ✓).
   - ¿Llena? → aplica el algoritmo y sustituye (fallo ✓).
3. Cuenta las ✓ = nº total de fallos. Si piden **tasa**: fallos / nº total de accesos.

### Mini ejemplo FIFO, cadena `1,2,3,4,1,2,5`, 3 marcos

```
Ref:   1   2   3   4   1   2   5
M1:    1   1   1   4   4   4   5      (sale: 1→3→2→... por orden de llegada)
M2:        2   2   2   1   1   1
M3:            3   3   3   2   2
Fallo:  ✓   ✓   ✓   ✓   ✓   ✓   ✓   = 7 fallos
```
*(Hazlo tú en columna a columna marcando quién es el más viejo en cada sustitución.)*

### LRU en una frase operativa
> Mantén la lista de recencia `[más vieja ... más nueva]`. Cada acceso: si está, **muévela al final**; si no está, **saca la primera** y mete la nueva **al final**. Fallo = sacar la primera.

### OPT en una frase operativa
> En cada fallo, **mira hacia delante** en la cadena: de las páginas que tienes, elige la que se usará **más tarde** (o que no volverá a usarse).

### Clock (Second Chance) en una frase operativa
> Los marcos en un **anillo** con puntero. Al buscar víctima: si R=1 → **R=0 y avanza**; si R=0 → **esa se va** y avanza el puntero.

---

# PARTE 8 — WORKING SET Y THRASHING


- **Working set** = conjunto de páginas que un proceso ha usado en una **ventana reciente** de tiempo. Cada proceso necesita **su** working set en RAM para ir fino.
- **Thrashing** = el SO da tan pocos marcos a cada proceso que **falla constantemente**, la CPU se queda esperando I/O y el sistema se para.
  - **Causa:** grado de multiprogramación demasiado alto (demasiados procesos peleando por pocos marcos).
  - **Soluciones:** modelo del working set, **PFF** (Page Fault Frequency) y bajar el nº de procesos.
- **PFF:** si el proceso falla **más** de un umbral → **más marcos**; si falla **menos** de otro umbral → **menos marcos** (se los prestas a otro).
- **Reemplazo local:** echa de los marcos de **su propio proceso** (aislado). **Global:** echa de **toda la RAM** (mejor uso, pero un proceso puede ahogar a otro).

---


# PARTE 9 — SEGMENTACIÓN 

- Divide en **segmentos de tamaño variable** (código, datos, pila) → la dirección es **(segmento, desplazamiento)**.
- **Tabla de segmentos:** entrada = *(límite, base, permisos)*.
- Comprobación: **desplazamiento < límite** → si no, **trap de segmentación** (error del programa).
- Dirección física = **base + desplazamiento**.
- **Tiene fragmentación externa** → hace falta **compactar**.
- **Segmentación paginada:** cada segmento se pagina por dentro (lo mejor de ambos mundos).

> **Ejemplo:** segmento 2 con base 14000 y límite 600; dirección `(2, 100)`:
> 100 < 600 → física = 14000 + 100 = **14100**.

---
