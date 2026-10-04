# Tema 4: Seguridad en Sistemas Operativos

## 4.1. El Papel del Sistema Operativo
* **Funciones clave:** Interfaz de comunicación (GUI/CLI) y gestión/gestores de abstracciones (archivos, dispositivos y procesos)

* **El dilema de la complejidad:** A más capas de abstracción y código, mayor superficie de ataque ("La complejidad es enemiga de la seguridad")

> Ejemplo: Linux supera los 30M de líneas de código y Windows los 50M.

* **Defensa:** Basada en modularidad, mínimo privilegio y revisión continua (auditorías, análisis estático, fuzzing y parcheado constante)

## 4.2. Gestión de Usuarios y Privilegios
Es la base para saber quién interactúa con el sistema antes de aplicar permisos.

* **Tipos de cuentas:**

    * **Humanos:** Usuarios reales

    * **Servicio / Sistema:** Cuentas sin persona asociada (ej. `www-data`, `apache`) para aislar procesos y limitar el impacto si el servicio es comprometido

* **Privilegios y Procesos: Los procesos heredan los permisos del usuario que los ejecuta**

* **Escalada de Privilegios:**

    * **Vertical:** Pasar de usuario estándar a administrador/root

    * **Horizontal:** Acceder a recursos de otro usuario del mismo nivel

    * **Cadena de exploits:** Combinación de una vulnerabilidad de aplicación + una vulnerabilidad local de escalada de privilegios

* **Protecciones en el Administrador (`root` / `Administrator`):**

    * **Mínimo privilegio**: Elevar permisos solo cuando sea necesario (`sudo` en UNIX/Linux; UAC en Windows).

    * **Mecanismos adicionales:** Restricciones de kernel como Lockdown en Linux.

* **Grupos y RBAC**: Asignación de permisos a grupos (roles) en lugar de a usuarios individuales para simplificar la administración. Los permisos efectivos son la unión de todos sus grupos

## 4.3. El Sistema de Ficheros
Determina sobre qué se actúa. En sistemas UNIX, todo se representa como un archivo (dispositivos, sockets, etc.), por lo que proteger el sistema de ficheros equivale a proteger toda la máquina

**Controles de Acceso**

**1. Permisos Tradicionales (UNIX)**:
    
* **Categorías:** Propietario ($u$), Grupo ($g$), Otros ($o$)
* **Permisos:** Lectura ($r=4$), Escritura ($w=2$), Ejecución ($x=1$)
* **Bits Especiales**:
    * **SetUID:** El proceso se ejecuta con los privilegios del propietario del archivo(ej. `/usr/bin/passwd` para modificar `/etc/shadow`)
    * **SetGID:** Análogo al SetUID para el grupo
    * **Sticky Bit:** Impide borrar archivos de otros en un directorio compartido (ej. `/tmp`)

**2. Listas de Control de Acceso (ACLs)**: Permiten granularidad fina (permisos a usuarios/grupos específicos fuera de la terna UNIX estándar). Modelo nativo en Windows NTFS

**3. Protección contra Acceso Físico:**

* **Cifrado de disco:** LUKS (Linux), BitLocker (Windows), FileVault (macOS). Suelen integrarse con un chip TPM

* **Borrado seguro:** Sobrescritura aleatoria para evitar recuperación magnética (shred, DBAN). En discos SSD, la reubicación física (wear leveling) exige borrado criptográfico (destruir la clave de cifrado)

### Integridad y Amenazas al Sistema de Archivos
* **Tipos de alteración:** En datos (*pérdida de confidencialidad/integridad*) o en programas (*código malicioso, malware, rootkits*)

* **Fallas de Hardware:** Sectores dañados, fallos de alimentación y Bit Rot (corrupción silenciosa por degradación magnética)

    * **Prevención:** Memtest, `fsck/chkdsk`, discos RAID (1, 5, 10), SAI/UPS y copias de seguridad

    > Nota clave: RAID no sustituye a las copias de seguridad; protege ante fallos físicos de discos, no ante corrupciones lógicas o borrados.

* **Fallas de Software:** Bugs del kernel, mala coordinación, errores de usuario o sobrecarga

* **Alteraciones Provocadas:** Malware (ransomware, troyanos) e intrusiones dirigida

### Prevención de Alteraciones
* **Firma Digital:** Garantiza origen e integridad del software antes de instalarlo (apt, dnf, etc.)

* **Funciones Hash:** Monitorización de integridad en archivos críticos comparando firmas con una base de datos segura (ej. Tripwire, AIDE, OSSEC)

* **Journaling (Bitácoras):** Registra los cambios antes de escribirlos físicamente en disco para reparar la consistencia tras fallos o cortes de luz (ej. ext4, NTFS, XFS)

