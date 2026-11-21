# Guias-Basicas — Resumen del Sistema de Memoria

**Ubicación:** `/home/maria/Escritorio/Guias-Basicas/`
**Total archivos:** 2,250 (7 asignaturas)
**Idioma:** Español (respuesta) y pruebas por tema desde Resumen.md + Ejercicios/

---

## 1. Arquitectura de Computadoras (AC)

### Pipeline
- `Tseg = Tinicio + (N-1) * Tseg` (para N instrucciones en K etapas)
- RAW ineludible (bloqueo de la etapa de ejecución); WAR/WAW → renombrado de registros
- Tabla de Reordenamiento (ROB): `#`/Evento/Destino/Valor/Ultimo
- Tema 4.3: Renombrado de Saltos (RS): Codificación/OpSim/IS/JT/VS1
- Predicción de salto: BHT 1-bit / 2-bit, BTB, GHR
- CPI < 1 → IPC (máquina de retardo)

### Memoria Cache
- Tiempo efectivo de acceso: `EAT = (1-p)·tRAM + p·tfallo`
- Asociatividad, línea (bloque), etiqueta (tag), políticas de escritura
- Real: A53 (Cortex-A), Nehalem, Zen4, A14 Firestorm

### Memoria Virtual
- Paginación por demanda, tablas de páginas (1/2 niveles, invertida)
- Fallo de página: servicio 5 pasos (legal, marco libre, lectura disco, actualizar TP, reiniciar instrucción)
- Bit de modificación (dirty): 1 transferencia (no modificada) o 2 (modificada)
- Thrashing, hiperpaginación

### E/S
- DMA (acceso directo a memoria), interrupciones, spooling, buffer cache

---

## 2. Estructuras de Datos (ED)

### Complejidad
- Vector: acceso O(1), inserción/extracción O(n)
- Hash abierto: O(1) promedio (λ≤0.7), peor O(n); rehash O(n) si λ>0.7
- Hash cerrado: lineal i, cuadrática i², doble i·h2(x)
- Árboles: ABB O(log n) promedio; AVL balanceado; heaps
- Grafos: matriz O(V²) espacio, lista O(V+E) tiempo
- Quadtree: O(log₄ n) promedio; octree 3D

### STL
- `vector` (acceso aleatorio, insert/push_back O(n)), `deque` (ambos extremos), `list` (inserción O(1) en posición)

### Estructura del archivo (estructura-de-datos/)
- `01_fundamentos/`: big-O, notación, ficheros
- `02_Estructuras Lineales/`: vectores, matrices, listas, pilas, colas
- `03_Estructuras no Lineales/`: árboles, AVL, heaps, conjuntos, dispersión, grafos, quadtrees
- `Resumen.md`: síntesis completa
- `Ejercicios/`: pruebas de aplicación

---

## 3. Sistemas Operativos (SO)

### Seguridad
- Tríada CIA: Confidencialidad, Integridad, Disponibilidad
- Riesgo: `R = d × pd` (magnitud × probabilidad)
- CVE: `CVE-AAAA-NNNN` (único por vulnerabilidad)
- CVSS: 0-10 (0=Ingenua, 0.1-3.9=Baja, 4-6.9=Media, 7-8.9=Alta, 9-10=Crítica)
- Ventana de exposición: tiempo entre CVEs y parche; zero-day (sin parche)

### Procesos
- PCB, estado (nuevo/listo/ejecutando/termiando/blockeado)
- Planificación: FCFS, SJF, Prioridad, Round Robin
- Conmutación de contexto, simultaneidad, sincronización

### Memoria
- Gestión: particiones estáticas/dinámicas, paginación, segmentación
- MMU: traducción lógico→física, bit de presencia, TLB
- EAT: `EAT = (1-p)·tRAM + p·tfallo` → `EAT ≈ 200 + 7,999,800·p` ns (ejemplo)
- Paginación por demanda, fallo de página, thrashing
- Reemplazo: FIFO, LRU, Segunda Oportunidad, RLU

### E/S y Ficheros
- E/S: DMA, spooling, buffer cache, planificación de discos (SCAN/ELEVATOR)
- Ficheros: tipos POSIX (regular, directorio, enlace simbólico, dispositivo), inodo, permisos UNIX (r/w/x, SetUID/SetGID/Sticky), enlaces duros/simbólicos
- Sistema de ficheros: bitmap de bloques libres, caché de disco, journaling

---

## 4. Física (Fis)

### Modelado UML
- Diagramas de interacción: secuencia, comunicación, general de interacción, tiempos
- Diagramas de clases: asociaciones (binaria, n-aria, reflexiva), cardinalidad, agregación/composición, clases abstractas/concreta, herencia, polimorfismo
- Casos de uso: escenarios básicos/alternativos, navibilidad
- Persistencia: estereotipos `«boundary»`/`«control»`/`«entity»`, perfiles UML, JPA/DAO

### Programación
- Diagramas de actividad, máquinas de estados, patrones (Singleton, Factory, etc.)
- Tarjetas CRC (Clase-Responsabilidad-Colaboración)
- Arquitectura: MVC/MVVM, Clean Architecture, hexagonal

---

## 5. Fundamentos de Bases de Datos (BBDD)

### SQL
- DDL: CREATE, ALTER, DROP, TRUNCATE
- DML: SELECT (con JOINs, subconsultas), INSERT, UPDATE, DELETE
- JOINs: INNER, LEFT, RIGHT, FULL, CROSS
- Subconsultas correlacionadas, funciones de agregado

### Álgebra Relacional
- Operadores: proyección, selección, unión, intersección, diferencia, producto cartesiano, join
- Derivación de esquemas relacionales

---

## 6. GitHub

### Comandos esenciales
- `status`, `add`, `commit`, `push`, `pull`, `branch`, `merge`, `rebase`, `log`, `remote`, `diff`, `show`
- `clone`, `fork`, `pull request`, `checkout`
- Configuración: `.gitignore`, tags, aliases

---

## 7. Programación / Taller de Informática (STI)

### UML 2.5.1
- Diagrama de clases (sintaxis, elementos, relaciones)
- Diagrama de secuencia (mensajes síncronos/asíncronos, fragmentos)
- Diagrama de comunicación (números de secuencia)
- Diagrama de casos de uso, máquinas de estados
- Persistencia con JPA/Hibernate, DAO

### Arquitectura
- MVC/MVVM, Clean Architecture, arquitectura hexagonal
- Patrones de diseño básicos

---

## Guía de trabajo

1. **Respuesta:** siempre en español
2. **Generación de exámenes:** usar `Resumen.md` + `Ejercicios/` para crear preguntas
3. **Estructura general:** cada asunto tiene `teoria/` (conceptos) + `practicas/` (prácticas)
4. **Verificar:** `find ~/Escritorio/Guias-Basicas/ -type f 2>/dev/null | wc -l` → 2,250
