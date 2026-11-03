# Guia para resolver cualquier ejercicios de Ficheros

**La idea central del tema en una frase:**
> El disco se corta en **bloques**; el **inodo** guarda los punteros a esos bloques (con enlaces directos e indirectos); el **directorio** es simplemente una lista que asocia **nombres → números de inodo**.

---

# PARTE 1 — CONCEPTOS FUNDAMENTALES


## 1.1 ¿Qué es un fichero?

Es una **colección de datos relacionados**, con **nombre**, almacenada en disco y a la que el SO da un servicio genérico: crear, abrir, leer, escribir, cerrar, borrar.

**Atributos del fichero (los que guarda el inodo):**

| Atributo | Ejemplo | ¿Quién lo lleva? |
|---|---|---|
| **Nombre** | `informe.txt` | El **directorio** (NO el inodo) |
| **Tipo** | regular, directorio, enlace... | Inodo |
| **Tamaño** | 55.000.000 bytes | Inodo |
| **Ubicación** | nº de inodo / punteros a bloques | Inodo |
| **Propietario y permisos** | maria, `rwxr-x---` | Inodo |
| **Fechas** | creación, mtime, atime | Inodo |
| **Contador de enlaces** | `i_links = 3` | Inodo |
| **Datos** | el contenido | Los **bloques de datos** en disco |

> **Truco clave:** el **nombre vive en el directorio**, los **datos y punteros viven en el inodo**. Por eso dos nombres pueden apuntar al mismo fichero (enlaces duros) y por eso borrar el nombre no borra el fichero si alguien lo tiene abierto.

## 1.2 El sistema de ficheros (FS)

Parte del SO que gestiona: estructura de directorios, asignación de espacio, gestión de **espacio libre**, protección y fiabilidad. Se organiza en **capas**:

```
  Aplicaciones  (read/write/open/close)
        │
  Lógica del FS  (directorios, rutas, permisos, inodos)
        │
  Capa de asignación  (cómo se mapean ficheros → bloques)
        │
  Capa física / controlador de disco  (sectores, pistas, colas)
```

## 1.3 Directorios, rutas y montaje

- **Directorio:** fichero que contiene una lista de entradas **(nombre, nº de inodo)**. Por eso "borrar un fichero" = quitar su entrada del directorio.
- **Ruta absoluta:** empieza en la raíz → `/home/maria/pepe.txt`
- **Ruta relativa:** desde el *working directory* del proceso → `./pepe.txt`
- **`.`** = este directorio, **`..`** = el padre.
- **`mount` (montar):** unir un sistema de ficheros de un dispositivo en un punto del árbol (`/mnt/usb`). El SO mantiene una tabla de montajes.

## 1.4 Descriptores y operaciones

```
  open("/fichero") ──► el SO devuelve un nº de descriptor (fd: 0,1,2,3...)
  read(fd, buf, n) ──► copia n bytes del fichero al buffer
  write(fd, buf, n)──► añade n bytes (¿en la posición actual? ¿al final?)
  lseek(fd, pos)   ──► mueve el puntero de posición (acceso directo)
  close(fd)        ──► libera el descriptor
```

| Operación | Nota de examen |
|---|---|
| `read`/`write` secuenciales | usan el puntero actual, lo mueven |
| `lseek` | da **acceso directo** dentro del fichero |
| `truncate` | cambia el tamaño sin borrar el nombre |
| `unlink` | quita el nombre; si `i_links = 0` y no hay fds abiertos → se libera |

## 1.5 Tipos de fichero

- **Regular:** el típico (texto, binario).
- **Directorio:** una lista de nombres.
- **Enlace simbólico (symlink):** un inodo que guarda la **ruta** a otro fichero (como un "atajo"). Puede apuntar a otro disco e incluso a un fichero que ya no existe (enlace roto).
- **Especial de dispositivo:** `/dev/sda` (bloque) o `/dev/tty` (carácter).
- **Pipe (FIFO) y socket:** comunicación entre procesos.

---

# PARTE 2 — MÉTODOS DE ASIGNACIÓN DE ESPACIO EN DISCO


## 2.1 Asignación CONTIGUA

El fichero ocupa bloques **seguidos**.

| Ventajas | Desventajas |
|---|---|
| Acceso **secuencial** súper rápido (y directo: `dirección = inicio + n`) | **Fragmentación externa** (hay que compactar) |
| Fácil saber cuánto ocupa | **Difícil crecer** (¿y si no hay hueco después?) |
| Pocos metadatos | Hay que reservar espacio de antemano |

## 2.2 Asignación ENLAZADA (y la familia FAT)

Cada bloque guarda el **puntero al siguiente**. El último bloque apunta a una marca de fin.

```
  fichero ──► [B5] ──► [B7] ──► [B12] ──► FIN
```

| Ventajas | Desventajas |
|---|---|
| Sin fragmentación externa | **Solo acceso secuencial** (para ir al bloque n hay que recorrer n−1) |
| Crecimiento fácil | Un **puntero roto** deja el resto del fichero inaccesible |
| | Los punteros **ocupan espacio** dentro de los bloques de datos |

**FAT (File Allocation Table):** variante en la que **todos los punteros se juntan en una sola tabla** al principio del disco. Así el disco queda limpio (solo datos) y se puede hacer acceso directo (la FAT se cachea en memoria).

```
  FAT:  [2] [5] [7] [12] ... (una entrada por cluster)
         │   │   │    │
         ▼   ▼   ▼    ▼
  datos: [B2][B5][B7][B12]
```

## 2.3 Asignación INDEXADA (los INODOS)

Cada fichero tiene un **inodo** con punteros a **todos** sus bloques → **acceso directo** sin recorrer nada. El problema: un inodo pequeño no puede guardar punteros para ficheros gigantes → se usan **enlaces indirectos** (bloques que solo contienen punteros).

## 2.4 Comparativa 
| | Contigua | Enlazada (FAT) | Indexada (inodo) |
|---|---|---|---|
| Fragmentación **externa** | **Sí** | No | No |
| Fragmentación **interna** | Sí (último bloque) | Sí (último bloque) | Sí (último bloque) |
| Acceso **directo** | Sí (fácil) | No (salvo FAT) | **Sí** |
| Fiabilidad de un puntero roto | — | Pierde el resto del fichero | Pierde un bloque o una rama |
| Coste metadatos | Mínimo | Punteros en datos o FAT | **Bloques de índice + inodo** |
| Crecimiento | Difícil | Fácil | Fácil |

---
# PARTE 3 — INODOS


## 3.1 Estructura del inodo

```
   ┌──────────────── INODO (número = identificador del fichero) ────────────────┐
   │  tipo · propietario · permisos rwx · nº enlaces · tamaño · fechas          │
   │  marcas: usado / sucio / ...                                               │
   │  ┌──────────────────────────────────────────────────────────────────┐      │
   │  │ punteros a bloques:                                              │      │
   │  │   0..i-1   → BLOQUES DIRECTOS (van directamente a los datos)     │      │
   │  │   i        → indirecto SIMPLE     (bloque de enlaces)            │      │
   │  │   i+1      → indirecto DOBLE      (raíz → bloques → datos)       │      │
   │  │   i+2      → indirecto TRIPLE     (raíz → 2º → 3º → datos)       │      │
   │  └──────────────────────────────────────────────────────────────────┘      │
   └─────────────────────────────────────────────────────────────────────────────┘
```

**En disco** (esquema tipo Unix clásico / ext2):

```
   INODO
   ├── directo 0 ──► bloque de datos
   ├── directo 1 ──► bloque de datos
   ├── ...
   ├── directo 9 ──► bloque de datos
   ├── indirecto simple ──► [PUNTEROS] ──► bloque ──► ...
   ├── indirecto doble  ──► [PUNTEROS] ──► [PUNTEROS] ──► datos
   └── indirecto triple ──► [PUNTEROS] ──► [PUNTEROS] ──► [PUNTEROS] ──► datos
```

**Linux ext2/ext3 clásico:** 12 directos + 1 simple + 1 doble + 1 triple.
**Unix System V / ejercicios:** 10 directos + 1 simple + 1 doble + 1 triple (o lo que diga el enunciado).
**ext4 moderno:** usa **extents** (trozos contiguos: "empieza en bloque X, tiene Y bloques") en vez de punteros uno a uno → menos metadatos y ficheros gigantes sin triple indirecto.

## 3.2 Por qué existe cada nivel

| Nivel | Para qué | Coste |
|---|---|---|
| **Directos** | Ficheros **pequeños**: se leen con **1 sola** consulta al disco | 0 bloques extra |
| **Indirecto simple** | Ficheros **medianos** | 1 bloque de índice |
| **Indirecto doble** | Ficheros **grandes** | 1 + P bloques de índice |
| **Indirecto triple** | Ficheros **enormes** | 1 + P + P² bloques de índice |

> **Idea de examen:** los punteros indirectos son un **compromiso**: gastas unos bloques de más en metadatos, pero a cambio el inodo se queda pequeño y **acceso directo** a cualquier bloque.

## 3.3 Inodo en memoria, enlaces duros y simbólicos

- Al hacer `open`, el inodo del disco se carga en la **tabla de inodos en memoria** (con bit "en uso", "modificado", bloqueado...).
- **Enlace duro (hard link):** **dos entradas de directorio** apuntando al **mismo nº de inodo**. `i_links` cuenta cuántos nombres lo referencian. Se borra cuando `i_links = 0` y no hay procesos con el fichero abierto.
  - *No se pueden crear hard links a directorios (para no formar ciclos) ni cruzar particiones.*
- **Enlace simbólico (soft link):** un inodo **nuevo** de tipo symlink que solo guarda la **ruta** de destino. Sí puede cruzar discos y sí puede quedarse roto.

```
  hard link:   dirA/uno ──┐
                          ├──► inodo 47 ──► datos
              dirB/dos ───┘        (i_links = 2)

  soft link:   dirC/atajo ──► inodo 88 (tipo symlink, guarda "dirA/uno") ──► dirA/uno
```

---
# PARTE 4 — FÓRMULAS

## 4.1 Variables 
| Símbolo | Significado | Ejemplo típico |
|---|---|---|
| $B$ | **Tamaño de bloque** (bytes) | 1 KB, 2 KB, 4 KB |
| $a$ | **Tamaño de la dirección de bloque** (bits) | 32 bits (4 bytes) |
| $i$ | Nº de **enlaces directos** del inodo | 10, 12, 2 |
| $S$ | Tamaño del fichero (bytes) | 55.000.000 |
| $D$ | Nº de **bloques de datos** del fichero | ⌈S / B⌉ |

## 4.2  P = cuántos punteros cabe en un bloque de índice

$$P = \frac{B}{a/8} = \frac{8 \cdot B}{a}$$

> **Ejemplo:** $B = 4$ KB, $a = 32$ bits (4 bytes): $P = 4096 / 4 = \mathbf{1024}$ punteros.

**Tabla de P para los valores típicos:**

| B ↓ / a → | 16 bits (2 B) | **32 bits (4 B)** | 64 bits (8 B) |
|---|---|---|---|
| **1 KB** | 512 | **256** | 128 |
| **2 KB** | 1024 | **512** | 256 |
| **4 KB** | 2048 | **1024** | 512 |
| **8 KB** | 4096 | **2048** | 1024 |

## 4.3  TAMAÑO MÁXIMO DEL FICHERO

$$\boxed{S_{máx} = B \cdot \left( i + P + P^2 + P^3 \right)}$$

*(Si solo hay directos + simple + doble: $S_{máx} = B \cdot (i + P + P^2)$. Si falta el triple: quita el $P^3$.)*

> **Ejemplo:** $B = 4$ KB, $a = 32$ bits, $i = 10$ (System V):
> $P = 1024$
> $S_{máx} = 4096 \cdot (10 + 1024 + 1024^2 + 1024^3) = 4096 \cdot 1.074.791.434 = \mathbf{4.402.345.713.664}$ **bytes** ≈ 4.402 GB (≈ 4.100 GiB)


| Nivel | Bloques de datos | Espacio |
|---|---|---|
| Directos (10) | 10 | 40 KB |
| Simple | $P = 1.024$ | 4 MB |
| Doble | $P^2 = 1.048.576$ | 4 GB |
| Triple | $P^3 = 1.073.741.824$ | 4 TB |
| **Total** | **1.074.791.434** | **≈ 4,4 TB** |


| B | P | $S_{máx}$ |
|---|---|---|
| 1 KB | 256 | 17.247.250.432 B ≈ 16 GiB + 64 MiB + 256 KiB + 10 KiB |
| 2 KB | 512 | 275.415.846.912 B ≈ 256 GiB + 512 MiB + 1 MiB + 20 KiB |
| 4 KB | 1.024 | 4.402.345.713.664 B ≈ 4 TiB + 4 GiB + 4 MiB + 40 KiB |

KB | 1.024 | 4.402.345.713.664 B ≈ 4 TiB + 4 GiB + 4 MiB + 40 KiB |

## 4.4 Bloques de datos de un fichero de tamaño S

$$D = \left\lceil \frac{S}{B} \right\rceil \quad \text{(redondeo hacia arriba)}$$

> $S = 55.000.000$ y $B = 2048$: $55.000.000 / 2048 = 26.855,47$ → $D = \mathbf{26.856}$ bloques.

## 4.5  ALGORITMO: repartir D bloques por niveles (paso a paso)

1. Calcula $D = \lceil S/B \rceil$.
2. **Directos:** consume $\min(D, i)$ bloques. Resto: $R_1 = \max(0,\ D - i)$.
3. Si $R_1 > 0$ → hace falta **1 bloque indirecto simple** y consume $\min(R_1, P)$ bloques de datos. Resto: $R_2 = R_1 - \min(R_1, P)$.
4. Si $R_2 > 0$ → **doble**: 1 bloque raíz + $\lceil \text{usados} / P \rceil$ bloques de 2.º nivel, donde $\text{usados} = \min(R_2, P^2)$. Resto: $R_3 = R_2 - \min(R_2, P^2)$.
5. Si $R_3 > 0$ → **triple**: 1 raíz + $\lceil \text{usados} / P^2 \rceil$ de 2.º nivel + $\lceil \text{usados} / P \rceil$ de 3.º nivel, con $\text{usados} = \min(R_3, P^3)$.
6. **Bloques totales en disco** = $D$ (datos) + todos los bloques de índice calculados.

> **Truco:** el $\lceil\ \rceil$ (redondeo hacia arriba) es lo que hace fallos tontos: 52 bloques de 2.º nivel si necesitas 26.334 punteros con $P = 512$ → $26.334/512 = 51,4$ → **52**.

## 4.6 Bloques que contienen ENLACES (índices) al tamaño máximo

Al llegar al tamaño máximo, **todos** los niveles están llenos:

$$N_{\text{enlaces}} = \underbrace{1}_{\text{simple}} + \underbrace{(1 + P)}_{\text{doble}} + \underbrace{(1 + P + P^2)}_{\text{triple}}$$

$$N_{\text{enlaces}} = 3 + 2P + P^2 + P^3 \quad (\text{con los tres niveles})$$

> **Ejemplo:** $P = 1024$ (4 KB, 32 bits):
> simple: 1 · doble: 1 + 1.024 = 1.025 · triple: 1 + 1.024 + 1.048.576 = 1.049.601
> **Total = 1.050.627 bloques de enlaces** (más el inodo, si lo cuentan).


## 4.7 ACCESOS A DISCO para acceder al BYTE X

*(Supuestos estándar: el **inodo está en memoria**, la **caché de disco está vacía**, no hay caché de páginas.)*

**Paso 1:** número de bloque lógico: $\ n = \lfloor X / B \rfloor$
**Paso 2:** ¿en qué nivel cae?

| ¿Dónde está el bloque n? | Accesos a disco | Desglose |
|---|---|---|
| $n < i$ (directo) | **1** | 1 (el dato) |
| $i \le n < i + P$ (simple) | **2** | 1 (bloque de enlaces) + 1 (dato) |
| $i + P \le n < i + P + P^2$ (doble) | **3** | raíz + 2.º nivel + dato |
| resto (triple) | **4** | raíz + 2.º + 3.º + dato |

> **Regla fácil:** *accesos = 1 (dato) + nº de niveles de punteros que haya que recorrer antes.*

> **Ejemplo:** byte $2.453.700$ con $B = 4$ KB, $i = 10$:
> $n = \lfloor 2.453.700 / 4096 \rfloor = \mathbf{599}$ (sobra 196 bytes)
> $599 \ge 10$ → no es directo. $599 - 10 = 589 \le 1024$ → **indirecto simple** → **2 accesos**.

## 4.8 ¿Cuántos INODOS caben en una partición?

Al formatear, el SO reserva una región para los inodos. Cada fichero consume **exactamente uno** (sean de 0 bytes o de 1 TB):

$$N_{\text{inodos}} = \left\lfloor \frac{\text{tamaño de la región de inodos}}{\text{tamaño de inodo}} \right\rfloor$$

> **Ejemplo:** región de inodos de 64 MB e inodos de 256 bytes:
> $67.108.864 / 256 = \mathbf{262.144}$ **inodos** → máximo 262.144 ficheros.
>
> **Por eso** un usuario puede "llenar" un disco creando **millones de ficheros vacíos**: se agotan los inodos aunque quede espacio libre para datos. La solución es crear más inodos al formatear (o agrandarlos).

## 4.9 ¿Cuántas ENTRADAS DE DIRECTORIO caben en un bloque?

$$N = \left\lfloor \frac{B}{\text{tamaño de la entrada}} \right\rfloor$$

> **Ejemplo (FAT):** $B = 512$ B, entrada fija de 32 B → **16 entradas por bloque**.
> Un directorio con 1.000 ficheros ocupa $\lceil 1000 / 16 \rceil = \mathbf{63}$ **bloques** = 32.256 bytes.
>
> **En ext:** las entradas son **variables** (nº de inodo + longitud + tipo + nombre) → depende de la longitud de los nombres; un bloque de 4 KB con nombres de 8 caracteres alberga unas 400 entradas.

## 4.10 Coste de leer un fichero entero 
| Situación | Accesos a disco (inodo en memoria, sin caché) |
|---|---|
| Fichero pequeño (todo directo) | 1 por bloque de datos = $D$ |
| Fichero con indirectos | $D$ (los datos) + 1 por cada bloque de índice que se recorra |
| **Fichero en FAT** (cadena en RAM) | $D$ (la cadena está cacheada; el coste real es la **fragmentación**: saltos por todo el disco) |

---
# PARTE 5 — FAT12 / FAT16 / FAT32 

---

## 5.1 Estructura de una partición FAT

```
┌─────────────┬──────────┬──────────┬───────────────────┬──────────────────────┐
│ Sector de   │  FAT 1   │  FAT 2   │ Directorio raíz   │  DATOS (clusters)    │
│ arranque    │ (tabla)  │ (copia)  │ (FAT16: FIJO)     │  cluster 2, 3, 4...  │
│ (BPB)       │          │          │ 512 entradas ×32B │                      │
└─────────────┴──────────┴──────────┴───────────────────┴──────────────────────┘
```

- **Cluster (unidad de asignación):** agrupación de $k$ bloques. El SO asigna **clusters**, no bloques sueltos.
- La **FAT** tiene **una entrada por cluster** (+ 2 reservadas: cluster 0 = "media", cluster 1 = "fin de fichero").
- Valores de la entrada (FAT16): `0x0000` = libre, `0xFFF7` = defectuoso, `0xFFF8-0xFFFF` = fin de fichero, otro = **número del siguiente cluster**.

## 5.2 Fórmulas de la FAT

$$\text{Nº de clusters} = \frac{\text{Tamaño de la partición}}{\text{Tamaño de cluster}}$$

$$\text{Entradas de la FAT} = \text{Nº de clusters} + 2$$

$$\text{Tamaño de la FAT} = \text{Entradas} \times \text{bytes por entrada}$$

*(y se redondea al bloque: por ejemplo a múltiplos de 512 B)*

| Tipo | Bits/entrada | Bytes/entrada | Nº clusters mínimo | Nº clusters máximo |
|---|---|---|---|---|
| **FAT12** | 12 (empaquetado, 1,5 B) | 1,5 | 1 | 4.084 |
| **FAT16** | **16** | **2** | 4.085 | **65.535** |
| **FAT32** | 32 (solo 28 usados) | 4 | 65.536 | ≈ 268.435.456 |

**Volumen máximo** (con cluster de 4 KB):
- FAT16: $65.535 \times 4\text{ KB} = \mathbf{256\ MB}$ → por eso en la práctica FAT16 usa clusters grandes (32 KB → **2 GB**, el clásico máximo de FAT16).
- FAT32: $268.435.456 \times 4\text{ KB} = 1\text{ TB}$ (con clusters de 8 KB → 2 TB).

> hay dos límites simultáneos: **(1)** que el nº de clusters no supere 65.535 y **(2)** que la FAT (2 B × clusters) no ocupe demasiado. Con clusters de 1 KB la FAT "gasta" 2 bytes por kilobyte = **0,2% solo en tabla**.


## 5.3 El caso típico: "partición grande + bloque pequeño" (espacio inutilizable)

> **Ejemplo resuelto:** partición de **8 GB** con bloques de **1 KB** en **FAT16**.
>
> 1. Nº de bloques = $8\text{ GB} / 1\text{ KB} = 8.388.608$ bloques (2²³).
> 2. FAT16 solo admite $2^{16} = 65.536$ entradas → solo puede referenciar **65.536 bloques de 1 KB = 64 MB**.
> 3. **Espacio inutilizable** = $8.388.608 - 65.536 = \mathbf{8.323.072\ \text{KB} = 7,94\ \text{GB}}$ (el **99,2%** del disco).
> 4. Además, la propia FAT ocupa $65.536 \times 2\text{ B} = 131.072\text{ B} = 128\text{ KB}$ → de los 64 MB, otros 128 KB son tabla.
> 5. **Justificación:** para aprovechar los 8 GB con FAT16 habría que aumentar el cluster a $8\text{ GB}/65.536 = \mathbf{128\ KB}$ (pero entonces el "bloque" ya no es de 1 KB) → y aparece la **fragmentación interna**: cada fichero desperdicia de media hasta 128 KB en su último cluster.

>  **Conclusión que hay que saber escribir:** *FAT16 no puede gestionar discos grandes con bloques pequeños porque su tabla tiene como mucho 65.536 entradas; o se agrandan los clusters (perdiendo espacio por fragmentación interna) o queda espacio inutilizado; para eso existen FAT32/exFAT/NTFS.*


## 5.5 Ejemplo completo: partición de 1 GB en FAT16 con clusters de 32 KB

1. **Clusters:** $1\ \text{GB} / 32\ \text{KB} = 1.073.741.824 / 32.768 = \mathbf{32.768}$ clusters (≤ 65.535 → vale FAT16)
2. **Entradas de la FAT:** $32.768 + 2 = 32.770$
3. **Tamaño de la FAT:** $32.770 \times 2\ \text{B} = 65.540\ \text{B}$ → redondeado a bloques de 512 B: $\lceil 65.540/512 \rceil = \mathbf{129}$ **bloques = 66.048 B**
4. **Dos copias de la FAT:** 258 bloques ≈ **129 KB**
5. **Directorio raíz fijo:** 512 entradas × 32 B = **16.384 B** = 32 bloques
6. **Espacio para datos:** $1\ \text{GB} - 129\ \text{KB} - 16\ \text{KB} - 1\ \text{sector} \approx$ **1.073.592.832 B ≈ 1023,85 MB**
7. **Fragmentación interna:** cada fichero deja de usar **hasta 31 KB** en su último cluster (de media, ~16 KB).

## 5.6 ¿Y si quiero una partición de 4 GB en FAT16?

- $4\ \text{GB} / 65.535 \approx \mathbf{64\ KB}$ por cluster.
- Con clusters de 64 KB saldrían 65.536 clusters → **en el límite** del máximo teórico de FAT16 (65.535).
- Así que en la práctica se usan clusters de **128 KB** → 32.768 clusters ✓, pero **desperdiciando hasta 127 KB por fichero**.
- **Conclusión de examen:** *por esto la industria pasó a FAT32 (28 bits → hasta ~268 millones de clusters): para discos grandes con clusters pequeños, o FAT32/exFAT/NTFS o se pierde un montón de espacio.*

---

# PARTE 6 — ESTRUCTURAS DE DIRECTORIO

---

| Estructura | Cómo busca | Ventaja | Problema |
|---|---|---|---|
| **Lista lineal** | recorre todo | súper simple | lento con muchos ficheros |
| **Tabla hash** | calcula hash del nombre | acceso casi instantáneo | difícil hacerla grande / reorganizar |
| **Árbol jerárquico** | recorre componente a componente | rutas, organización | coste del recorrido |
| **B-tree** (NTFS `$MFT`) | árbol balanceado | rápido y ordenado | complejo |

**Forma de la entrada:**
- **Unix/ext:** entrada variable = *(nº de inodo, longitud del nombre, tipo, nombre)* → el directorio es un **fichero normal** que el SO interpreta. (Unix no necesita el tipo porque está en el inodo.)
- **FAT:** entrada **fija de 32 bytes** = *nombre 8,3 (11 B) + atributos + cluster inicial + tamaño*. Con LFN se encadenan entradas extra para nombres largos (máx. 255).
- **NTFS:** `$MFT` (Master File Table) = fichero con registros de 1 KB; los directorios son B-trees de índices → búsqueda $O(\log n)$.

---

# PARTE 7 — GESTIÓN DEL ESPACIO LIBRE

---

| Método | Idea | Cálculo típico de examen |
|---|---|---|
| **Bitmap** (mapa de bits) | 1 bit por bloque: 1 = libre | nº de bloques ÷ 8 = bytes del bitmap |
| **Lista enlazada** | punteros de los bloques libres (GNU Hurd) | — |
| **Agrupamiento** | cada bloque libre guarda un grupo de punteros (Linux) | — |
| **Contadores + listas** | nº de bloques libres + lista (NTFS) | — |
| **La propia FAT** | FAT12/16/32: la tabla **ya es** el bitmap | ver Parte 5 |

> **Ejemplo de bitmap:** disco de **1 TB** con bloques de **4 KB**:
> nº de bloques = $2^{40}/2^{12} = 2^{28}$ → bitmap = $2^{28}$ bits = $2^{25}$ bytes = **32 MB** (0,003% del disco).

---