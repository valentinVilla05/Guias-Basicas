## Guía para resolver ejercicios de Memoria de cualquier tipo 

## 1. Conceptos Fundamentales

**1. Memoria Virtual (lógica)**: Es el espacio de direcciones que "ve" un proceso. cada proceso cree que tiene toda la memoria solo para él

**2. Memoria Física (RAM)**: Es el chip de memoria real en la placa base del ordenado

**3. Página**: Es el bloque o "trozo" en el que se divide la memoria virtual

**4. Marco de página (Frame)**: Es el hueco de la memoria RAM donde encaja exactamente el tamaño de una página. **Una página y un marco tienen exactamente el mismo tamaño**

**5. Desplazamiento (offset)**: Es la posición exacta dentro de una página o marco 

**6. TLB (Translation Lookaside Buffer)**: Es una memoria caché super rápida que guarda las traducciones recientes de "Página -> Marco" para no tener que consultar la RAM dos eveces

## 2. Tabla de Conversión a Bytes

> En estos ejercicios es muy frecuente la conversión de datos que nos dan en el enunciado del ejercicio , por lo tanto es importante saber la tabla de equivalencias

$$2^k \text{ Bytes} \longrightarrow k \text{ bits}$$

| Unidad | Equivalencia en Bytes | Potencia de 2 | N de Bit | 
| -- | -- | -- | -- |
| **1 byte** | 1 B | 2^0 B | 0 bits | 
| **1KB (KiloByte)** | 1.024 B | 2^10 B | 10 bits | 
| **1 MB (Megabyte)** | 1.024 KB | 2^20 B | 20 bits | 
| **1 GB (Gigabyte)** | 1.024 MB | 2^30 B | 30 bits | 

```
Cálculo rápido
Si nos dan que el tamaño es por ejemplo : 256 MB

1. 256 = 2^8
2. MB = 2^20
3. Multiplicas: 2^8 * 2^20 = 2^28 Bytes -> 28 bits
```

## 3. Formulario y Estructura de Direcciones

### **1. Dirección Virtual (Lógica)**

Se divide en 2 partes:

> total bits Dirección Virtual = $log_2$ (Memoria Virtual del Proceso)

**Desplazamiento (d)**:

d = $log_2$  (Tamaño de Página)

**Número de Página (p)**

p = Total bits Virtuales - d

### **2. Dirección Física**

También se divide en dos partes, (el desplazamiento $d$ es exactamente el mismo)

**Número de Marco (f)**

* f= Total bits Físicos - d

**B. Capacidad de Procesos en Ram**

$$\text{Nº máximo de procesos} = \frac{\text{Tamaño Memoria Física}}{\text{Tamaño Memoria Virtual de un proceso}}$$

**C. Tiempo Efectivo de Acceso ($T_m$ con TLB)**

Cuando la CPU busca un dato:

* **Si ACIERTA en TLB ($h$)**: Accede a la TLB ($t_{\text{tlb}}$) + Accede al dato en RAM ($t_{\text{ram}}$).

* **Si FALLA en TLB ($1 - h$)**: Accede a la TLB ($t_{\text{tlb}}$) + Consulta la Tabla de Páginas en RAM ($t_{\text{ram}}$) + Accede al dato en RAM ($t_{\text{ram}}$).

Fórmula:

> $$T_m = h \cdot (t_{\text{tlb}} + t_{\text{ram}}) + (1 - h) \cdot (t_{\text{tlb}} + 2 \cdot t_{\text{ram}})$$


**Fórmula Simplificada (Usa esta para ir más rápido):**

$$T_m = t_{\text{tlb}} + (2 - h) \cdot t_{\text{ram}}$$

Donde:

**$h$: Tasa de aciertos** (*hit rate*) expresada en decimal (ej: $92\% = 0.92$).   

**$t_{\text{tlb}}$: Tiempo de acceso a la TLB**.   

**$t_{\text{ram}}$: Tiempo de acceso a la memoria RAM**
