
# Práctica 8: Sistemas de Detección de Intrusiones (IDS) y Análisis de Seguridad

## 1. Conceptos Generales de los Sistemas de Detección de Intrusiones (IDS)

### Definición

Un **Sistema de Detección de Intrusiones (IDS)** es una herramienta de seguridad que analiza diferentes fuentes de información de un sistema para detectar accesos no autorizados, actividades maliciosas o comportamientos anómalos.

### Mecanismos de detección

- **Detección basada en firmas:** reconoce patrones de ataques conocidos mediante reglas estáticas predefinidas.
- **Detección basada en anomalías:** identifica comportamientos que se alejan del funcionamiento habitual del sistema.

### Tipos de IDS según la fuente de datos

- **HIDS (Host-based IDS):** supervisa los elementos internos de un equipo, como logs, integridad de binarios, llamadas al sistema y procesos en memoria. Ejemplos: Fail2ban y Rootkit Hunter.
- **NIDS (Network-based IDS):** captura y analiza el tráfico de red para detectar posibles ataques. Ejemplo: Suricata.

---

## 2. Detección Basada en Archivos de Registro: Fail2ban

### Funcionamiento general

**Fail2ban** supervisa continuamente los archivos de registro (*logs*) del sistema, como `/var/log/auth.log` para SSH, utilizando expresiones regulares para detectar patrones sospechosos:

- Intentos fallidos de autenticación.
- Ataques de fuerza bruta.
- Múltiples intentos de acceso desde una misma IP.

### Acción y respuesta automática

Cuando se supera el número de intentos fallidos configurado, Fail2ban bloquea temporalmente la IP de origen mediante el cortafuegos (`nftables` o `iptables`) u otros mecanismos como `/etc/hosts.deny`.

### Estructura y ficheros de configuración

| Fichero o directorio | Función |
|---|---|
| `/etc/fail2ban/fail2ban.conf` | Configuración global del demonio: nivel de logs, socket y rutas. |
| `/etc/fail2ban/jail.conf` | Define las cárceles (*jails*) y sus valores por defecto. No se recomienda modificarlo porque puede sobrescribirse al actualizar. |
| `/etc/fail2ban/jail.local` | Configuración personalizada que prevalece sobre `jail.conf`. Permite activar cárceles y establecer parámetros. |
| `/etc/fail2ban/filter.d/` | Contiene los filtros basados en expresiones regulares que identifican patrones en los logs (ej. `sshd.conf`). |
| `/etc/fail2ban/action.d/` | Contiene las acciones para aplicar y retirar bloqueos (ej. `nftables-multiport.conf`). |

### Directivas clave de configuración

- **`bantime`:** duración del bloqueo de una IP. Se expresa en segundos o formatos como `10m` o `1h`.
- **`maxretry`:** número máximo de intentos fallidos permitidos antes del bloqueo.
- **`findtime`:** intervalo de tiempo en el que se contabilizan los fallos. Si se alcanza `maxretry` dentro de ese periodo, se bloquea la IP.
- **`port`:** puerto o servicio protegido (ej. `ssh`, `22` o `http`).
- **`banaction`:** acción utilizada para bloquear la IP (ej. `nftables-multiport`).

### Comandos principales y registros

**Consultar el estado general y las cárceles activas:**

```bash
sudo fail2ban-client status
```

**Consultar el estado de la cárcel SSH:**

```bash
sudo fail2ban-client status sshd
```

Muestra los fallos registrados y las IPs bloqueadas.

**Registro de eventos:**

`/var/log/fail2ban.log`

Registra las acciones realizadas:

- `Ban`: IP bloqueada.
- `Unban`: IP desbloqueada.

---

## 3. Comprobación de Integridad de Ficheros Ejecutables (SHA-256)

### Principio de integridad

Consiste en comprobar que los archivos ejecutables y las librerías del sistema no han sido modificados, dañados o sustituidos por versiones maliciosas.

### Propiedades de las funciones hash

Una función hash genera una huella digital de longitud fija a partir del contenido de un archivo.

**SHA-256** genera un hash de 256 bits, representado por 64 caracteres hexadecimales.

Propiedades principales:

- **Longitud fija:** siempre genera un hash de la misma longitud.
- **Determinismo:** un mismo archivo siempre genera el mismo hash.
- **Efecto avalancha:** una modificación mínima provoca un cambio significativo en el hash.
- **Integridad:** permite detectar modificaciones comparando el hash actual con el original.

### Flujo operativo de auditoría

#### 1. Creación del baseline (estado base)

```bash
find /usr/bin/ -type f -exec sha256sum {} \; > fichero.txt
```

Recorre `/usr/bin/`, calcula el hash SHA-256 de cada archivo y guarda los resultados en `fichero.txt`, creando el estado de referencia (*baseline*).

#### 2. Verificación de integridad

```bash
sha256sum -c fichero.txt
```

Recalcula los hashes y los compara con los almacenados:

- `OK`: el archivo no ha cambiado.
- `FAILED`: el archivo ha cambiado o no coincide con el original.

#### 3. Filtrado de alteraciones

```bash
sha256sum -c fichero.txt | grep -E "FAILED|no coincide"
```

Utiliza `grep` para mostrar únicamente los mensajes relacionados con errores de integridad.

### Análisis del comando anidado

```bash
find /usr/bin/ -type f -exec sha256sum {} \; | sha256sum
```

**Funcionamiento:**

1. `find /usr/bin/ -type f`: localiza todos los archivos normales de `/usr/bin/`.
2. `-exec sha256sum {} \;`: calcula el hash de cada archivo.
3. `|`: envía la salida del primer comando al segundo.
4. `sha256sum`: calcula un único hash global del listado generado.

**Utilidad práctica:**

Obtiene una única huella de 64 caracteres hexadecimales que representa el conjunto de hashes y rutas.

Si cambia respecto al valor de referencia, significa que el listado ha cambiado porque se ha añadido, eliminado o modificado algún archivo.

**Importante:** permite detectar cambios en el conjunto, pero no identificar directamente qué archivo ha cambiado.

---

## 4. Detección Basada en la Integridad del Sistema: Rootkit Hunter (`rkhunter`)

### Definición de Rootkit

Un **rootkit** es un conjunto de herramientas maliciosas diseñadas para ocultar procesos, archivos o conexiones de red en un sistema comprometido y mantener el acceso con privilegios de superusuario (`root`).

### Funcionamiento de rkhunter

**Rootkit Hunter (`rkhunter`)** es una herramienta HIDS que analiza el sistema para detectar rootkits, puertas traseras (*backdoors*) y configuraciones sospechosas mediante comprobaciones de seguridad y comparación con valores de referencia.

### Pruebas y verificaciones realizadas

- **Comprobación de binarios:** compara los hashes de los ejecutables esenciales con sus valores de referencia.
- **Búsqueda de archivos y directorios ocultos:** inspecciona rutas sensibles como `/dev`, `/tmp` y `/var/tmp` en busca de estructuras anómalas.
- **Módulos del kernel:** busca módulos sospechosos y alteraciones relacionadas con rootkits LKM (*Loadable Kernel Module*).
- **Configuraciones y permisos:** revisa puertos abiertos, usuarios con UID 0 adicionales a `root` y configuraciones de seguridad.

### Comandos de uso

**Análisis interactivo:**

```bash
sudo rkhunter --check
```

Ejecuta las comprobaciones y requiere pulsar `Intro` entre bloques de pruebas.

**Análisis sin pausas interactivas:**

```bash
sudo rkhunter --check --sk
```

Ejecuta el análisis completo omitiendo las pausas (*skip keypress*).

**Registro del análisis:**

`/var/log/rkhunter.log`

Almacena las comprobaciones, resultados y advertencias.

### Significado de los avisos (Warnings)

Los *warnings* no significan necesariamente que el equipo esté infectado. Pueden deberse a:

- **Falsos positivos:** elementos legítimos detectados como sospechosos.
- **Actualizaciones de software:** los binarios cambian su hash y dejan de coincidir con los valores de referencia.
- **Cambios de configuración:** permisos u opciones consideradas poco seguras.
- **Modificaciones legítimas:** cambios que todavía no se han actualizado en la base de referencia.

Cuando se han realizado cambios legítimos y se ha comprobado que el sistema es seguro, se puede actualizar la base de referencia:

```bash
sudo rkhunter --propupd
```

Actualiza los valores de referencia de los archivos supervisados. No debe utilizarse para ignorar advertencias sin investigarlas previamente.

---

## 5. Detección Basada en Tráfico de Red: Suricata

### Definición

**Suricata** es un motor IDS/IPS de código abierto (*open-source*), multihilo y de alto rendimiento que inspecciona el tráfico de red en tiempo real.

Puede funcionar como:

- **NIDS (Network Intrusion Detection System):** detecta ataques y genera alertas.
- **NIPS (Network Intrusion Prevention System):** además de detectar amenazas, puede bloquear el tráfico malicioso.

### Conjunto de reglas (Ruleset)

Suricata utiliza conjuntos de reglas o firmas para identificar patrones de actividad maliciosa.

Uno de los más conocidos es **Emerging Threats Open**, que permite detectar:

- Ataques contra servicios y aplicaciones.
- Malware y tráfico de botnets.
- Explotación de vulnerabilidades.
- Actividades de red sospechosas.

### Modos de análisis del tráfico

#### 1. Análisis en vivo (tiempo real)

Captura e inspecciona directamente los paquetes que circulan por una interfaz de red, por ejemplo `eth1`, para detectar amenazas durante la comunicación.

#### 2. Replicación de captura (Replay)

Reproduce una captura de tráfico almacenada en un archivo `.pcap` para que Suricata pueda analizar los paquetes.

```bash
sudo tcpreplay -i eth1 -t example.com-4.pcap
```

- `tcpreplay`: herramienta para reproducir capturas de tráfico.
- `-i eth1`: interfaz de red por la que se envían los paquetes.
- `-t`: reproduce los paquetes a la máxima velocidad posible.
- `example.com-4.pcap`: archivo con la captura de tráfico.

Los paquetes se retransmiten por la interfaz para que puedan ser inspeccionados.

#### 3. Análisis directo offline

Analiza directamente un archivo `.pcap` sin transmitir los paquetes por una interfaz de red.

```bash
ids-replay example.com-4.pcap
```

Procesa el contenido de la captura para detectar posibles amenazas sin necesidad de reinyectar el tráfico.

### Archivos de registro y monitorización

| Fichero o comando | Función |
|---|---|
| `sudo ids-alerts -f` | Visor de alertas en tiempo real que muestra la información de Suricata de forma estructurada. |
| `/var/log/suricata/fast.log` | Archivo de texto plano que almacena las alertas en formato simplificado, una línea por evento. |
| `/var/log/suricata/eve.json` | Archivo JSON con información detallada y estructurada de los eventos. |

**Información mostrada por `ids-alerts -f`:**

- Marca temporal.
- Prioridad de la alerta.
- Mensaje de la regla activada.
- Dirección IP y puerto de origen.
- Dirección IP y puerto de destino.

**Contenido de `fast.log`:**

Almacena las alertas de forma simplificada para facilitar su lectura.

**Contenido de `eve.json`:**

Contiene información detallada de los eventos:

- Cabeceras IP, TCP y UDP.
- Metadatos del protocolo.
- Identificador y mensaje de la firma activada.
- Información del tráfico y, cuando corresponde, carga útil del paquete.

Permite integrar Suricata con otras herramientas de monitorización y análisis de seguridad.

---

## 6. Resumen general de las herramientas IDS

| Herramienta | Tipo | Función principal |
|---|---|---|
| **Fail2ban** | HIDS | Analiza los logs y bloquea IPs que realizan demasiados intentos fallidos. |
| **SHA-256** | Comprobación de integridad | Detecta modificaciones en archivos mediante sus hashes. |
| **Rootkit Hunter** | HIDS | Busca rootkits, archivos sospechosos y modificaciones del sistema. |
| **Suricata** | NIDS/NIPS | Inspecciona el tráfico de red para detectar y prevenir ataques. |

### Idea clave para el examen

- **Fail2ban:** detecta ataques mediante los registros del sistema.
- **SHA-256:** comprueba la integridad de los archivos.
- **rkhunter:** busca rootkits y anomalías en el sistema operativo.
- **Suricata:** analiza el tráfico de red para detectar amenazas.
