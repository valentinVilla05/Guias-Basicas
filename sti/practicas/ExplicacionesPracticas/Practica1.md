## Práctica 1: Auditorías, Vulnerabilidades y Metasploit

### Metasploit
- **Definición**: Es la plataforma o framework open-source estándar en ciberseguridad para el desarrollo, prueba y ejecución de exploits.

- **Uso principal**: Se utiliza en pruebas de penetración (*pentesting*) y auditorías de seguridad para verificar y validar la existencia de vulnerabilidades explotables en un entorno real.

- **Estructura de módulos en Metasploit**:
  - **Exploits**: Módulos que aprovechan una vulnerabilidad en el objetivo para ejecutar código.
  - **Payloads**: Código que se ejecuta en el objetivo tras una explotación exitosa.
  - **Auxiliary**: Módulos de escaneo, reconocimiento, fuzzing o verificación de credenciales que no envían payloads.
  - **Encoders**: Módulos para ofuscar o empaquetar el payload y evitar caracteres nulos (`\x00`) o firmas básicas de antivirus.

- **Diferencia entre Auditoría y Pentesting**:
  - **Auditoría de seguridad**: Revisión amplia y sistemática que abarca configuraciones, versiones de software, procedimientos y cumplimiento normativo.
  - **Prueba de intrusión (*Pentesting*)**: Subconjunto de la auditoría enfocado en intentar comprometer el sistema activamente mediante exploits (de forma manual o automatizada).
- **Análisis Forense (DFIR)**: A diferencia del pentesting (que es un enfoque *proactivo* para descubrir fallos antes de que ocurra un ataque), el análisis forense es *reactivo* y se realiza tras un incidente de seguridad para reconstruir las acciones del atacante analizando memoria RAM, registros de sistema (*logs*) e imágenes de disco.

- **Flujo básico en Metasploit**: Scanner/Reconocimiento $\rightarrow$ Selección del Exploit $\rightarrow$ Configuración del Payload (carga útil) $\rightarrow$ Ejecución (`exploit` o `run`).

- **Tipos de Payloads (Cargas Útiles)**:
  - **Single (o Inline)**: Carga útil autónoma que contiene todo el código necesario en una sola pieza. Es más estable pero ocupa más espacio en memoria.
  - **Stager**: Payload muy pequeño cuyo único propósito es establecer la conexión de red entre el objetivo y el atacante para descargar el payload principal.
  - **Stage**: El payload de mayor tamaño (como Meterpreter) que es descargado e inyectado en memoria por el *stager*.
  - **Staged vs. Stageless**: Los *staged* (nombrados en Metasploit con una barra `/`, como `linux/x86/meterpreter/reverse_tcp`) se envían en fases para ahorrar espacio en la memoria vulnerable; los *stageless* o singles (nombrados con un guion bajo `_`, como `linux/x86/meterpreter_reverse_tcp`) envían el bloque completo de golpe, evitando conexiones de red secundarias que puedan ser detectadas por firewalls o sistemas EDR.
- **Meterpreter**: Payload avanzado e interactivo que se ejecuta directamente en la memoria RAM del objetivo (sin crear procesos en disco), dificultando su detección por antivirus y proporcionando un control total del sistema.

---

### 2. Origen de las Vulnerabilidades: Configuración vs. Código

Las vulnerabilidades informáticas no tienen todas el mismo origen:

- **Fallos de Código (Vulnerabilidades en el binario/software):**
  - Provienen de errores de programación (ej. *buffer overflow*, desbordamiento de memoria) o de la introducción maliciosa de puertas traseras (*backdoors*) en el código fuente (ej. CVE-2011-2523 en `vsftpd 2.3.4`).
> **Solución**: Requieren reemplazar o reparar el ejecutable mediante un parche oficial (*patch*) o actualización de versión.

- **Fallos de Configuración:**
  - El código del software es seguro y carece de errores, pero el sistema está mal parametrizado (ej. credenciales por defecto, permisos laxos, directivas inseguras en archivos como `/etc/vsftpd.conf` o el catálogo CCE).
> **Solución**: Modificar la directiva correspondiente en los archivos de configuración sin necesidad de recompilar o actualizar el ejecutable.

---

### 3. Mitigación vs. Remediación (Parcheo)

Es fundamental distinguir entre "ocultar/bloquear" y "solucionar":

| Concepto | Mecanismo | Acción | Resultado |
|---|---|---|---|
| **Mitigación (Nivel de Red)** | Firewall (ej. `iptables`) | Filtrado de puertos, reglas de acceso. | Impide o frena el acceso externo al vector de ataque, pero **la vulnerabilidad sigue existiendo** en el software. |
| **Remediación (Nivel de Aplicación)** | Parche / Actualización (*Update*) | Sustitución o corrección del código ejecutable. | **Elimina la vulnerabilidad** de raíz manteniendo la funcionalidad legítima del servicio. |

- **Comportamiento práctico en un exploit**: Si un exploit abre una consola (*shell*) en un puerto secundario (por ejemplo, el puerto de la *backdoor* `6200/TCP`), bloquear ese puerto secundario con un firewall evita que el atacante reciba la shell, pero el servicio principal (puerto `21/TCP`) seguirá respondiendo y ejecutando la fase inicial del fallo.

---

### 4. Ciclo de Vida del Software y Repositorios

- **Sistemas EOL (*End of Life* / Fuera de Soporte)**: Sistemas operativos antiguos (ej. distribuciones añejas como Ubuntu 8.04 en la máquina vulnerable Metasploitable 2) dejan de recibir actualizaciones oficiales.

- **Errores de Repositorio (HTTP 404)**: Si el gestor de paquetes (como `apt` / `apt-get`) falla al intentar actualizar software en estos sistemas, el problema no es de sintaxis en el comando, sino que los servidores/repositorios oficiales han sido retirados o el laboratorio carece de salida a Internet.

- **Evolución de Entornos para Pentesting**:
  - **BackTrack**: La distribución histórica de auditorías de seguridad desarrollada por Offensive Security (basada en Slackware y posteriormente en Ubuntu).
  - **Kali Linux**: Sucesora directa de BackTrack (lanzada en 2013) y mantenida por Offensive Security, basada en **Debian**, adaptada a los estándares FHS y con repositorios activos actualizados de herramientas.

---

### 5. Fuentes de Información y Catálogos de Vulnerabilidades

- **Listas de correo y divulgación**:
  - **Full Disclosure**: Lista pública para la divulgación inmediata sin restricciones (*full disclosure*).
  - **Bugtraq**: Lista histórica emblemática de avisos de seguridad (1993-2021).
  - **Open Source Security (oss-security)**: Centrada en software libre y proyectos de Linux.

- **Bases de datos oficiales y métricas**:
  - **CVE (Common Vulnerabilities and Exposures)**: Registro y catálogo oficial de identificadores únicos para vulnerabilidades conocidas (gestionado por MITRE).
  - **NVD (National Vulnerability Database)**: Base de datos del NIST que enriquece cada CVE con la siguiente taxonomía:
    - **CWE (Common Weakness Enumeration)**: Clasificación del tipo o categoría técnica de debilidad en el código/diseño (ej. CWE-89 para Inyección SQL, CWE-119 para desbordamientos de memoria/buffer).
    - **CPE (Common Platform Enumeration)**: Identificador y nomenclatura estándar de productos y versiones afectadas.

- **Puntuación CVSS**.
  - **EUVD (European Vulnerability Database)**: Base de datos europea creada por ENISA (bajo la Directiva NIS2) que añade detalles de mitigación y estado de explotación.
  - **CISA KEV (Known Exploited Vulnerabilities)**: Catálogo que enumera únicamente vulnerabilidades para las cuales se ha confirmado explotación activa en el mundo real.
  - **CCE (Common Configuration Enumeration)**: Identificadores estándar para fallos y malas configuraciones de seguridad.
  - **CVSS (Common Vulnerability Scoring System)**: Sistema estandarizado para calcular la severidad de una vulnerabilidad (de 0.0 a 10.0) mediante vectores de ataque, complejidad e impacto:
  - **AV (Attack Vector)**: Vector de acceso (*Network, Adjacent, Local, Physical*).
  - **AC (Attack Complexity)**: Complejidad para ejecutar el exploit (*Low, High*).
  - **PR (Privileges Required)** y **UI (User Interaction)**: Requisitos de privilegios previos o interacción de la víctima.
  - **Impacto C/I/A**: Afección a la **C**onfidencialidad, **I**ntegridad y **D**isponibilidad (*Availability*).

---

### 6. Divulgación, Mercado 0-Day y Bug Bounty

- **Modelos de Divulgación**:
- **Full Disclosure**: Publicación completa e inmediata del fallo sin avisar previamente al desarrollador, forzando la creación rápida de parches pero exponiendo a los usuarios mientras no haya solución.
- **Coordinated Vulnerability Disclosure (CVD / Responsable)**: El descubridor notifica privadamente al fabricante y acuerdan un plazo límite antes de publicar los detalles para dar tiempo a desarrollar un parche.

- **Vulnerabilidades 0-day (Zero-Day)**:
- **Definición**: Vulnerabilidad o fallo de seguridad que es desconocido por el fabricante o para la cual **aún no existe un parche oficial**.
- **Casos reales famosos**: *WannaCry* **NO** fue un ataque 0-day propiamente dicho el día de su difusión global masiva (mayo de 2017), ya que Microsoft había publicado el parche de seguridad (boletín MS17-010) dos meses antes del ataque (marzo de 2017), aunque afectó masivamente a sistemas no actualizados que utilizaban la vulnerabilidad *EternalBlue* en SMBv1.

- **Mercados de Vulnerabilidades**:
- **Mercado Negro**: Venta ilegal de exploits y vulnerabilidades orientada a cibercrimen y ataques sin consentimiento.
- **Mercado Gris / Legal**: Empresas especializadas (brokerage) que compran exploits 0-day legalmente para venderlos exclusivamente a gobiernos y agencias de inteligencia/defensa.
- **Programas Bug Bounty**: Recompensas financieras legítimas pagadas directamente por las empresas tecnológicas a investigadores de seguridad por la notificación responsable de fallos.