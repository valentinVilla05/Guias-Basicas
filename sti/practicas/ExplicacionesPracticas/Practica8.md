
# Práctica 8: Sistemas de Detección de Intrusiones (IDS) y Análisis de Seguridad

## 1. Conceptos Generales de los Sistemas de Detección de Intrusiones (IDS)

### Definición

Un **Sistema de Detección de Intrusiones (IDS)** es una herramienta de seguridad que analiza diferentes fuentes de información de un entorno informático para detectar accesos no autorizados, actividades maliciosas o comportamientos anómalos respecto al funcionamiento normal del sistema.

### Mecanismos de detección

Los IDS utilizan principalmente dos métodos:

- **Detección basada en firmas:** reconoce patrones de ataques conocidos mediante reglas estáticas predefinidas.
- **Detección basada en anomalías:** identifica comportamientos que se alejan del funcionamiento habitual del sistema.

### Tipos de IDS según la fuente de datos

- **HIDS (Host-based Intrusion Detection System):** supervisa los elementos internos de un equipo individual, como archivos de registro, integridad de binarios, llamadas al sistema y procesos en memoria.

  Ejemplos: Fail2ban y Rootkit Hunter.

- **NIDS (Network-based Intrusion Detection System):** captura y analiza el tráfico que circula por una interfaz o segmento de red para detectar posibles ataques mediante firmas y patrones sospechosos.

  Ejemplo: Suricata.

---

## 2. Detección Basada en Archivos de Registro: Fail2ban

### Funcionamiento general

**Fail2ban** es una herramienta de seguridad que supervisa continuamente los archivos de registro (*logs*) del sistema operativo para detectar comportamientos sospechosos.

Por ejemplo, puede analizar `/var/log/auth.log`, donde se registran los intentos de autenticación SSH.

Utiliza expresiones regulares para identificar patrones de ataque, como:

- Intentos fallidos de autenticación.
- Ataques de fuerza bruta.
- Múltiples intentos de acceso desde una misma dirección IP.

### Acción y respuesta automática

Cuando Fail2ban detecta un número de eventos anómalos que supera el límite configurado, ejecuta automáticamente una acción defensiva sobre la dirección IP de origen.

Normalmente, esta acción consiste en bloquear temporalmente la IP mediante el cortafuegos del sistema, utilizando herramientas como `nftables` o `iptables`.

También puede utilizar mecanismos de restricción como `/etc/hosts.deny`, dependiendo de la configuración.

### Estructura y ficheros de configuración

| Fichero o directorio | Función |
|---|---|
| `/etc/fail2ban/fail2ban.conf` | Configuración global del demonio Fail2ban: nivel de registro, socket y rutas de ejecución. |
| `/etc/fail2ban/jail.conf` | Fichero base donde se definen las cárceles (*jails*) y sus valores predeterminados. No se recomienda modificarlo directamente porque puede sobrescribirse al actualizar el paquete. |
| `/etc/fail2ban/jail.local` | Fichero de configuración personalizada. Sus valores prevalecen sobre los de `jail.conf`. Permite activar cárceles y establecer parámetros específicos. |
| `/etc/fail2ban/filter.d/` | Contiene los filtros basados en expresiones regulares que identifican patrones sospechosos en los logs (ej. `sshd.conf`). |
| `/etc/fail2ban/action.d/` | Contiene las acciones que permiten aplicar y retirar bloqueos a nivel de red o sistema (ej. `nftables-multiport.conf`). |

### Directivas clave de configuración

- **`bantime`:** duración del bloqueo de una dirección IP. Se expresa en segundos o mediante formatos temporales como `10m` o `1h`.
- **`maxretry`:** número máximo de intentos fallidos permitidos antes de activar el bloqueo.
- **`findtime`:** intervalo de tiempo durante el cual se contabilizan los intentos fallidos. Si se alcanza `maxretry` dentro de este periodo, se aplica el bloqueo.
- **`port`:** puerto o servicio que se desea proteger (ej. `ssh`, `22` o `http`).
- **`banaction`:** acción que se ejecuta para bloquear la dirección IP, definida mediante un fichero del directorio `action.d` (ej. `nftables-multiport`).

### Comandos principales y registros

**Consultar el estado general de Fail2ban:**

```bash
sudo fail2ban-client status
```

Muestra el estado del servicio y la lista de cárceles (*jails*) activas.

**Consultar el estado de la cárcel SSH:**

```bash
sudo fail2ban-client status sshd
```

Muestra información específica de la protección SSH, como los intentos fallidos registrados y las direcciones IP bloqueadas.

**Consultar el registro de eventos:**

```bash
/var/log/fail2ban.log
```

Contiene información sobre las acciones realizadas por Fail2ban, incluyendo:

- `Ban`: dirección IP bloqueada.
- `Unban`: dirección IP cuyo bloqueo ha sido retirado.

---

## 3. Comprobación de Integridad de Ficheros Ejecutables (SHA-256)

### Principio de integridad

La comprobación de integridad consiste en verificar que los archivos ejecutables y las librerías del sistema no han sido modificados, dañados o sustituidos por versiones maliciosas.

Para ello se utilizan funciones hash criptográficas, como **SHA-256**.

### Propiedades de las funciones hash

Una función hash genera una huella digital de longitud fija a partir del contenido de un archivo.

En el caso de SHA-256, el resultado siempre tiene una longitud de 256 bits, representados mediante 64 caracteres hexadecimales.

Sus principales propiedades son:

- **Longitud fija:** independientemente del tamaño del archivo, el hash siempre tiene la misma longitud.
- **Determinismo:** un mismo archivo siempre genera el mismo hash.
- **Efecto avalancha:** una modificación mínima en el contenido del archivo provoca un cambio significativo en su hash.
- **Integridad:** permite detectar si un archivo ha sido modificado respecto a una huella de referencia.

### Flujo operativo de auditoría

#### 1. Creación del baseline (estado base)

```bash
find /usr/bin/ -type f -exec sha256sum {} \; > fichero.txt
```

Recorre el directorio `/usr/bin/`, localiza todos los archivos normales, calcula su hash SHA-256 y almacena los resultados en `fichero.txt`.

Este archivo representa el estado de referencia o *baseline* del sistema.

#### 2. Verificación de integridad

```bash
sha256sum -c fichero.txt
```

Lee los hashes almacenados en `fichero.txt`, vuelve a calcular el hash actual de cada archivo y compara ambos valores.

Los resultados pueden ser:

- `OK`: el archivo mantiene el mismo contenido que cuando se creó el baseline.
- `FAILED`: el archivo ha cambiado o no coincide con el hash original.

#### 3. Filtrado de alteraciones

```bash
sha256sum -c fichero.txt | grep -E "FAILED|no coincide"
```

Utiliza `grep` para filtrar la salida del comando anterior y mostrar únicamente los mensajes relacionados con archivos que presentan errores de integridad.

### Análisis del comando anidado

```bash
find /usr/bin/ -type f -exec sha256sum {} \; | sha256sum
```

**Funcionamiento:**

1. `find /usr/bin/ -type f`: localiza todos los archivos normales del directorio `/usr/bin/`.
2. `-exec sha256sum {} \;`: calcula el hash SHA-256 de cada archivo encontrado.
3. `|`: envía la salida del primer comando al segundo mediante una tubería.
4. `sha256sum`: calcula un único hash global a partir del texto recibido.

**Utilidad práctica:**

Permite obtener una única huella digital de 64 caracteres hexadecimales que representa el listado completo de hashes y rutas de los archivos.

Si el hash global cambia respecto al valor de referencia, significa que el listado ha cambiado. Esto puede deberse a que algún archivo se ha añadido, eliminado o modificado.

**Importante:** este método permite detectar cambios en el conjunto, pero no identifica directamente qué archivo ha cambiado. Para localizarlo es necesario comparar los hashes individuales.

---

## 4. Detección Basada en la Integridad del Sistema: Rootkit Hunter (`rkhunter`)

### Definición de Rootkit

Un **rootkit** es un conjunto de herramientas maliciosas diseñadas para ocultar la presencia de procesos, archivos o conexiones de red en un sistema comprometido.

Su objetivo suele ser mantener el acceso al equipo con privilegios elevados, normalmente de superusuario (`root`), evitando ser detectado.

### Funcionamiento de rkhunter

**Rootkit Hunter (`rkhunter`)** es una herramienta de auditoría de seguridad de tipo HIDS que analiza el sistema local para detectar posibles rootkits, puertas traseras (*backdoors*) y configuraciones sospechosas.

Realiza comprobaciones sobre diferentes componentes del sistema y compara determinados elementos con valores de referencia y patrones conocidos.

### Pruebas y verificaciones realizadas

- **Comprobación de binarios del sistema:** compara las huellas hash de los ejecutables esenciales con sus valores de referencia para detectar posibles modificaciones.

- **Búsqueda de archivos y directorios ocultos:** inspecciona ubicaciones sensibles, como `/dev`, `/tmp` o `/var/tmp`, en busca de archivos y estructuras anómalas.

- **Módulos del kernel:** comprueba la existencia de módulos sospechosos y posibles alteraciones relacionadas con rootkits de tipo LKM (*Loadable Kernel Module*).

- **Configuraciones y permisos:** revisa puertos abiertos, usuarios con UID 0 adicionales a `root` y configuraciones de seguridad de los archivos del sistema.

### Comandos de uso

**Ejecutar el análisis en modo interactivo:**

```bash
sudo rkhunter --check
```

Realiza las comprobaciones de seguridad y requiere pulsar `Intro` para continuar entre los diferentes bloques de pruebas.

**Ejecutar el análisis sin pausas interactivas:**

```bash
sudo rkhunter --check --sk
```

Ejecuta el análisis completo omitiendo las pausas que requieren pulsar una tecla (*skip keypress*).

**Consultar el registro del análisis:**

```bash
/var/log/rkhunter.log
```

Contiene el registro detallado de las comprobaciones realizadas, los resultados obtenidos y las posibles advertencias.

### Significado de los avisos (Warnings)

Los avisos (*warnings*) generados por `rkhunter` no significan necesariamente que el equipo esté infectado.

Pueden aparecer por diferentes motivos:

- **Falsos positivos:** detección de elementos que parecen sospechosos, pero que son legítimos.
- **Actualizaciones de software:** algunos binarios pueden cambiar su hash después de una actualización, haciendo que no coincidan con los valores de referencia anteriores.
- **Cambios de configuración:** determinadas opciones o permisos pueden considerarse poco seguros.
- **Modificaciones legítimas:** cambios realizados por el administrador que todavía no se han actualizado en la base de referencia.

Cuando se han realizado actualizaciones legítimas y se ha comprobado que el sistema es seguro, se puede actualizar la base de referencia de propiedades mediante:

```bash
sudo rkhunter --propupd
```

Este comando actualiza los valores de referencia de los archivos supervisados. No debe utilizarse para ignorar advertencias sin investigar previamente su origen.

---

## 5. Detección Basada en Tráfico de Red: Suricata

### Definición

**Suricata** es un motor de detección y prevención de intrusiones de código abierto (*open-source*), que permite inspeccionar y analizar el tráfico de red en tiempo real.

Es una herramienta de tipo NIDS/NIPS:

- **NIDS (Network Intrusion Detection System):** detecta posibles ataques y genera alertas.
- **NIPS (Network Intrusion Prevention System):** además de detectar amenazas, puede aplicar acciones para bloquear o impedir el tráfico malicioso.

Destaca por su capacidad de procesamiento multihilo y su rendimiento en la inspección de paquetes.

### Conjunto de reglas (Ruleset)

Suricata utiliza conjuntos de reglas o firmas para identificar patrones de actividad maliciosa.

Uno de los conjuntos más conocidos es **Emerging Threats Open**, que contiene reglas para detectar diferentes amenazas, como:

- Ataques contra servicios y aplicaciones.
- Tráfico relacionado con malware.
- Comunicaciones de botnets.
- Intentos de explotación de vulnerabilidades.
- Actividades de red sospechosas.

Las reglas permiten identificar patrones conocidos y generar alertas cuando el tráfico coincide con alguno de ellos.

### Modos de análisis del tráfico

#### 1. Análisis en vivo (tiempo real)

Suricata captura e inspecciona directamente los paquetes que circulan por una interfaz de red.

Por ejemplo, puede supervisar la interfaz `eth1` para analizar el tráfico que pasa por ella.

Este modo permite detectar amenazas mientras se produce la comunicación.

#### 2. Replicación de captura (Replay)

Permite reproducir una captura de tráfico almacenada en un archivo `.pcap` para que pueda ser analizada por el sistema de detección.

```bash
sudo tcpreplay -i eth1 -t example.com-4.pcap
```

**Funcionamiento:**

- `tcpreplay`: herramienta que permite reproducir capturas de tráfico.
- `-i eth1`: indica la interfaz de red por la que se enviarán los paquetes.
- `-t`: reproduce los paquetes a la máxima velocidad posible.
- `example.com-4.pcap`: archivo que contiene la captura de tráfico.

De esta manera, los paquetes almacenados se vuelven a transmitir por la interfaz de red para que Suricata pueda inspeccionarlos.

#### 3. Análisis directo offline

Permite analizar directamente un archivo `.pcap` sin necesidad de transmitir los paquetes a través de una interfaz de red.

```bash
ids-replay example.com-4.pcap
```

**Funcionamiento:**

Procesa directamente el contenido de la captura almacenada para analizar los paquetes y detectar posibles amenazas.

A diferencia de `tcpreplay`, no necesita reinyectar el tráfico en una interfaz de red.

### Archivos de registro y monitorización

Suricata genera diferentes registros que permiten consultar las alertas y analizar los eventos detectados.

| Fichero o comando | Función |
|---|---|
| `sudo ids-alerts -f` | Visor de alertas en tiempo real que presenta la información de Suricata de forma estructurada. |
| `/var/log/suricata/fast.log` | Archivo de texto plano que almacena las alertas en un formato sencillo de una línea por evento. |
| `/var/log/suricata/eve.json` | Archivo JSON que almacena información detallada y estructurada de los eventos detectados. |

**Información mostrada por `ids-alerts -f`:**

- Marca temporal del evento.
- Prioridad de la alerta.
- Mensaje de la regla que se ha activado.
- Dirección IP y puerto de origen.
- Dirección IP y puerto de destino.

**Contenido de `fast.log`:**

Almacena las alertas de forma simplificada, facilitando su lectura y consulta rápida.

**Contenido de `eve.json`:**

Almacena información más detallada de los eventos en formato JSON, incluyendo:

- Cabeceras IP, TCP y UDP.
- Metadatos del protocolo.
- Identificador y mensaje de la firma activada.
- Información del tráfico y, cuando corresponde, datos de la carga útil del paquete.

Este formato resulta especialmente útil para integrar Suricata con otras herramientas de monitorización y análisis de seguridad.

---

## 6. Resumen general de las herramientas IDS

| Herramienta | Tipo | Función principal |
|---|---|---|
| **Fail2ban** | HIDS | Analiza los logs y bloquea automáticamente IPs que realizan demasiados intentos fallidos. |
| **SHA-256** | Comprobación de integridad | Detecta modificaciones en archivos mediante la comparación de sus huellas digitales. |
| **Rootkit Hunter** | HIDS | Busca rootkits, archivos sospechosos y modificaciones en componentes del sistema. |
| **Suricata** | NIDS/NIPS | Analiza el tráfico de red para detectar y, según su configuración, prevenir ataques. |

### Idea clave para el examen

- **Fail2ban:** detecta ataques mediante los registros del sistema.
- **SHA-256:** comprueba que los archivos no hayan sido modificados.
- **rkhunter:** busca rootkits y anomalías en el sistema operativo.
- **Suricata:** inspecciona el tráfico de red para detectar amenazas.
