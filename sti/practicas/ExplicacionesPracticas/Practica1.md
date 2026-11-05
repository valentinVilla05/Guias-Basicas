## Práctica 1: Auditorías, Vulnerabilidades y Metasploit

- **Definición**: Es la plataforma o framework open-source estándar en ciberseguridad para el desarrollo, prueba y ejecución de exploits.

- **Uso principal**: Se utiliza en pruebas de penetración (*pentesting*) y auditorías de seguridad para verificar y validar la existencia de vulnerabilidades explotables en un entorno real.

- **Diferencia entre Auditoría y Pentesting**:
  - **Auditoría de seguridad**: Revisión amplia y sistemática que abarca configuraciones, versiones de software, procedimientos y cumplimiento normativo.
  - **Prueba de intrusión (*Pentesting*)**: Subconjunto de la auditoría enfocado en intentar comprometer el sistema activamente mediante exploits (de forma manual o automatizada).

- **Flujo básico en Metasploit**: Scanner/Reconocimiento $\rightarrow$ Selección del Exploit $\rightarrow$ Configuración del Payload (carga útil) $\rightarrow$ Ejecución.

- **Tipos de Payloads (Cargas Útiles)**:
  - **Single (o Inline)**: Carga útil autónoma que contiene todo el código necesario en una sola pieza. Es más estable pero ocupa más espacio en memoria.
  - **Stager**: Payload muy pequeño cuyo único propósito es establecer la conexión de red entre el objetivo y el atacante para descargar el payload principal.
  - **Stage**: El payload de mayor tamaño (como Meterpreter) que es descargado e injectado en memoria por el *stager*.
  - **Staged vs. Stageless**: Los *staged* se envían en fases para ahorrar espacio en la memoria vulnerable; los *stageless* (o *singles*) envían el bloque completo de golpe.
  - **Meterpreter**: Payload avanzado e interactivo que se ejecuta directamente en la memoria RAM del objetivo (sin crear procesos en disco), dificultando su detección por antivirus y proporcionando un control total del sistema.

---

### 2. Origen de las Vulnerabilidades: Configuración vs. Código

Las vulnerabilidades informáticas no tienen todas el mismo origen:

- **Fallos de Código (Vulnerabilidades en el binario/software):**
  - Provienen de errores de programación (ej. *buffer overflow*, desbordamiento de memoria) o de la introducción maliciosa de puertas traseras (*backdoors*) en el código fuente (ej. CVE-2011-2523 en `vsftpd 2.3.4`).
  - **Solución**: Requieren reemplazar o reparar el ejecutable mediante un parche oficial (*patch*) o actualización de versión.

- **Fallos de Configuración:**
  - El código del software es seguro y carece de errores, pero el sistema está mal parametrizado (ej. credenciales por defecto, permisos laxos, directivas inseguras en archivos como `/etc/vsftpd.conf` o el catálogo CCE).
  - **Solución**: Modificar la directiva correspondiente en los archivos de configuración sin necesidad de recompilar o actualizar el ejecutable.

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

---

### 5. Fuentes de Información y Catálogos de Vulnerabilidades

- **Listas de correo y divulgación**:
  - **Full Disclosure**: Lista pública para la divulgación inmediata sin restricciones (*full disclosure*).
  - **Bugtraq**: Lista histórica emblemática de avisos de seguridad (1993-2021).
  - **Open Source Security (oss-security)**: Centrada en software libre y proyectos de Linux.

- **Bases de datos oficiales y métricas**:
  - **CVE (Common Vulnerabilities and Exposures)**: Registro y catálogo oficial de identificadores únicos para vulnerabilidades conocidas (gestionado por MITRE).
  - **NVD (National Vulnerability Database)**: Base de datos del NIST que enriquece cada CVE con la puntuación de severidad CVSS, el tipo de debilidad (CWE) y los productos afectados (CPE).
  - **EUVD (European Vulnerability Database)**: Base de datos europea creada por ENISA (bajo la Directiva NIS2) que añade detalles de mitigación y estado de explotación.
  - **CISA KEV (Known Exploited Vulnerabilities)**: Catálogo que enumera únicamente vulnerabilidades para las cuales se ha confirmado explotación activa en el mundo real.
  - **CVSS (Common Vulnerability Scoring System)**: Sistema estandarizado para calcular la severidad de una vulnerabilidad (de 0.0 a 10.0) mediante vectores de ataque, complejidad e impacto.

---

### 6. Divulgación, Mercado 0-Day y Bug Bounty

- **Modelos de Divulgación**:
  - **Full Disclosure**: Publicación completa e inmediata del fallo sin avisar previamente al desarrollador, forzando la creación rápida de parches pero exponiendo a los usuarios mientras no haya solución.
  - **Coordinated Vulnerability Disclosure (CVD / Responsable)**: El descubridor notifica privadamente al fabricante y acuerdan un plazo límite antes de publicar los detalles para dar tiempo a desarrollar un parche.

- **Vulnerabilidades 0-day (Zero-Day)**:
  - **Definición**: Vulnerabilidad o fallo de seguridad que es desconocido por el fabricante o para la cual **aún no existe un parche oficial**.
  - **Casos reales famosos**: *WannaCry* **NO** fue un ataque 0-day propiamente dicho el día de su difusión global masiva, ya que Microsoft había publicado el parche de seguridad (boletín MS17-010) dos meses antes del ataque, aunque afectó masivamente a sistemas no actualizados.

- **Mercados de Vulnerabilidades**:
  - **Mercado Negro**: Venta ilegal de exploits y vulnerabilidades orientada a cibercrimen y ataques sin consentimiento.
  - **Mercado Gris / Legal**: Empresas especializadas (brokerage) que compran exploits 0-day legalmente para venderlos exclusivamente a gobiernos y agencias de inteligencia/defensa.
  - **Programas Bug Bounty**: Recompensas financieras legítimas pagadas directamente por las empresas tecnológicas a investigadores de seguridad por la notificación responsable de fallos.