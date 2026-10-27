# Resumen de los comandos de las prácticas 5 y 6 de SSOO

> Muchos de los comandos y sus opciones se pueden recordar con el comando **man**, aún así es recomendable conocerlos y mirarse las explicaciones sobre las prácticas

## 1. Introducción a la Virtualización y Sistemas Operativos
### Conceptos Fundamentales de Virtualización

* **Virtualización**: Tecnología que permite crear representaciones basadas en software (virtuales) de recursos físicos como procesadores, memoria, almacenamiento y redes

* **Hipervisor / VMM (Virtual Machine Monitor)**: Software, firmware o hardware que crea, gestiona y ejecuta máquinas virtuales

* **Host (Sistema Anfitrión)**: El entorno físico real (hardware y SO base) sobre el que se ejecuta el hipervisor

* **Guest (Sistema Invitado / SO Invitado)**: El sistema operativo que se ejecuta dentro de la máquina virtual de manera aislada

* **Máquina Virtual (VM)**: Entorno de computación virtualizado que funciona como un sistema informático independiente dentro del hardware host. El SO invitado corre sobre la máquina virtual

```text
+-------------------------------------------------------------+
|              Sistema Operativo Invitado (Guest)              |
+-------------------------------------------------------------+
|                     Máquina Virtual (VM)                     |
+-------------------------------------------------------------+
|                     Hipervisor (VMM)                        |
+-------------------------------------------------------------+
|           Hardware Físico / Sistema Anfitrión (Host)        |
+-------------------------------------------------------------+
```

### Tipos de Hipervisores
### Hipervisor Tipo 1 (Nativo / Bare-Metal)

* **Arquitectura**: Se ejecuta directamente sobre el hardware físico sin ningún sistema operativo intermediario

* **Rendimiento**: Máxima eficiencia y menor latencia al tener acceso directo a los recursos de hardware

* **Uso principal**: Entornos de producción, centros de datos y servidores empresariales

> Ejemplos: VMware ESXi, Microsoft Hyper-V Server, Proxmox VE, Xen.

### Hipervisor Tipo 2 (Alojado / Hosted)

* **Arquitectura**: Se ejecuta como una aplicación sobre un sistema operativo anfitrión convencional (Windows, Linux, macOS)

* **Rendimiento**: Menos eficiente debido a la capa adicional del SO anfitrión

* **Uso principal**: Desarrollo, pruebas, docencia y uso personal

> Ejemplos: Oracle VM VirtualBox, VMware Workstation, Parallels Desktop.

### Configuración de Almacenamiento y Recursos en VirtualBox

* **VDI (VirtualDisk Image)**: Formato nativo de Oracle VirtualBox (`.vdi`)

* **VMDK (Virtual Machine Disk)**: Formato desarrollado por VMware, muy compatible entre plataformas (`.vmdk`)

* **VHD (Virtual Hard Disk)**: Formato nativo de Microsoft (`.vhd`)

**Formatos de exportación / despliegue:**

* **OVA / OVF**: Formatos estándar para empaquetar y distribuir servicios virtualizados completos (appliances) para ser importados en múltiples equipos físicos

### Herramientas de Integración: Guest Additions
Las **Guest Additions** son un conjunto de controladores (drivers) y aplicaciones que se instalan **dentro del sistema operativo invitado** (normalmente desde una imagen ISO virtual como `VBoxGuestAdditions.iso`) una vez finalizada la instalación del SO

| Funcionalidad | Descripción | 
| -- | -- | 
| **Vídeo y Resolución** | Soporte para aceleración 3D y redimensionado automático de la pantalla al cambiar el tamaño de la ventana. | 
| **Integración del ratón** | Transición fluida del cursor entre el anfitrión y el invitado sin necesidad de liberar manualmente el ratón. | 
| **Integración de datos** | Portapapeles compartido (copiar/pegar) y función de arrastrar y soltar (drag and drop) | 
| **Carpetas compartidas** | Permite acceder a directorios del anfitrión directamente desde el invitado. | 
| **Sincronización horaria** | Mantiene la hora de la VM sincronizada con el reloj del equipo físico. | 

### Concepto de Distribución Linux

```text
+-------------------------------------------------------------------------+
| Software de Aplicación (Ofimática, navegadores, reproductores media)   |
+-------------------------------------------------------------------------+
| Entorno Gráfico (X Window System / Wayland + GNOME, KDE, XFCE, etc.)    |
+-------------------------------------------------------------------------+
| Bibliotecas y Herramientas del Sistema (Proyecto GNU, gestores de pkg) |
+-------------------------------------------------------------------------+
|                             Núcleo (Kernel) Linux                       |
+-------------------------------------------------------------------------+
```

* **Linux Live CD/USB:** Modalidad de inicio que permite ejecutar el sistema operativo directamente desde un medio ejecutable secundario (CD, DVD, memoria USB) en la memoria RAM, **sin necesidad de modificar ni instalar nada en el disco duro**

* **Imágenes ISO**: Formato estándar de archivo que contiene la copia exacta de un medio óptico de instalación. En virtualización se prefiere montar archivos `.iso` directamente en la unidad virtual porque ofrece mayor velocidad y comodidad de instalación frente a medios físicos.
### Asignación de RAM

* Debe balancearse entre las necesidades del sistema anfitrión y del invitado

* **Criterio habitual**: Mantener la asignación en la "zona verde" de la interfaz (habitualmente entre un 25% y un 50% de la RAM física total). Si se asigna demasiada RAM, se desestabiliza el anfitrión; si se asigna muy poca, el invitado recurrirá al disco (swap) ralentizando su ejecución

### Discos Virtuales
* **Reserva dinámica**: El archivo de disco crece progresivamente a medida que el SO invitado guarda datos, ahorrando espacio en el disco físico real

* **TAMAÑO FIJO**: Ocupa todo el espacio asignado desde su creación, ofreciendo un rendimiento de lectura/escritura ligeramente superior

### Particionamiento del Disco y Sistema de Archivos en Linux

Una **partición** es una división **lógica** (no física) de una unidad de almacenamiento que permite al sistema operativo tratar cada sección como una unidad independiente

### Esquema de Particionado Tradicional (MBR)

* **Particiones primarias**: Divisiones directas del disco (máximo 4 por disco en esquemas MBR tradicionales)

* **Partición extendida**: Tipo especial de partición primaria utilizada para superar el límite de 4 particiones. Sirve como contenedor para crear múltiples particiones lógicas

### Jerarquía de Directorios Básica en Linux
A diferencia de Windows (que usa letras de unidad como `C:` o `D:`), Linux organiza todo el sistema en un único árbol jerárquico a partir del directorio raíz (`/`).

* `/` (Raíz): Punto de montaje principal donde reside la estructura base del sistema

* `/home` : Directorio reservado para las carpetas personales y configuraciones de los usuarios estándar del sistema

* `/boot` : Contiene los archivos necesarios para el arranque del sistema operativo

### Memoria de Intercambio (Swap) en Linux
### Naturaleza de la Swap

* Es un espacio en disco (gestionado mediante una partición dedicada de tipo swap o un archivo de intercambio `swapfile`) que el kernel de Linux utiliza como extensión de la memoria RAM física

* No forma parte de la jerarquía de archivos tradicionales y no se monta en una ruta del sistema de archivos (como `/home` o `/root`)


### Funcionamiento y Eficiencia
* **Mecanismo de seguridad**: La swap evita que el sistema colapse por falta de memoria (Out Of Memory - OOM) cuando la RAM física se llena, enviando páginas de memoria inactivas al disco

* **Impacto en la eficiencia**: El acceso al disco duro/SSD es significativamente más lento que a la RAM física. Si el sistema recurre constantemente a la swap (fenómeno llamado thrashing), el rendimiento global del sistema disminuye, por lo que usar swap no aumenta la velocidad del sistema

* **Hibernación**: Para que el sistema pueda hibernar (guardar el estado completo de la RAM en el almacenamiento secundario y apagarse), el espacio de swap disponible debe ser al menos igual o superior a la memoria RAM instalada.

## 2. Administración de Software (`dpkg` y `apt`)

Nomenclatura del Paquete Debian (`.deb`)

$$\text{nombrePaquete}\_\text{version}-\text{revision}\_\text{arquitectura.deb}$$

Ejemplo: `zsh_5.9-6ubuntu2_amd64.deb` (zsh = programa, 5.9 = versión upstream, 6ubuntu2 = revisión/parche distro, amd64 = arquitectura)

---
### Comparativa Fundamental: `dpkg` vs `apt`

| Característica | `dpkg` | `apt` / `apt-get` | 
| -- | -- | -- | 
| **Nivel** | Bajo nivel (herramienta base) | Alto nivel (interfaz sobre `dpkg`) | 
| **Dependencias** | **No** resuelve dependencias automáticamente | **Sí** descarga e instala dependencias requeridas | 
| **Repositorios** | Trabaja solo con archivos `.deb` locales | Busca, descarga e instala desde servidores remotos | 
| **Uso Principal** | Consultas locales e instalación de ficheros `.deb` | Gestión completa del ciclo de vida del software | 

#### Código de Estado de dpkg `-l` (3 Caracteres)

```
Posición 1: Estado Deseado   --->  [i]nstall, [r]emove, [p]urge, [h]old, [u]nknown
Posición 2: Estado Actual    --->  [i]nstalled, [c]onfig-files, [U]npacked, [F]/[H]alffailed, [n]ot-installed
Posición 3: Estado de Error  --->  [ ] sin error, [R]einst-required
```

* `ii`: Correctamente instalado y configurado

* `rc`: Desinstalado (remove), pero conserva archivos de configuración en `/etc/`

#### Comandos de Referencia Rápida: Gestión de Paquetes

#### Consultas e Inspección Local (`dpkg`)

* **Listar paquetes instalados / filtrar:**

```bash
dpkg -l ['patron']
```
* **Listar todos los archivos instalados por un paquete:**

```bash
dpkg -L <paquete>
```

* **Verificar la integridad de los archivos instalados:**

```bash
dpkg --verify / dpkg -v
```
* **Ver estado detallado de un paquete instalado:**
```bash
dpkg -s <paquete>
```

### Gestión Remota y Repositorios (`apt` / `apt-get`)

* **Sincronizar índice local con repositorios:**
```bash
sudo apt update
```

* **Actualizar paquetes sin instalar/eliminar otros:**
```bash
sudo apt upgrade -y
```

* **Actualización completa (resuelve dependencias complejas, instala/elimina paquetes):**
```bash
sudo apt full-upgrade
```
* **Instalar paquete o fichero `.deb` local (resolviendo dependencias):**

```bash
sudo apt install <paquete_o_fichero.deb>
```

* **Descargar sin instalar (guarda en `/var/cache/apt/archives/`):**

```bash
sudo apt-get install -d <paquete>
```

* **Desinstalación estándar (mantiene `/etc/`):**

```bash
sudo apt remove <paquete>
```
* **Desinstalación completa (borra paquete y configuración):**

```bash
sudo apt purge <paquete>
```

* **Limpiar dependencias huérfanas y su configuración:**

```bash
sudo apt autoremove --purge
```

* **Ver información detallada de un paquete (repositorio o instalado):**

```bash
apt show <paquete>
```

* **Consultar repositorio de origen, versión e instalación prioritaria:**

```bash
apt policy <paquete>
```

* **Gestionar bloqueos de versión (`hold`):**

```bash
sudo apt-mark hold <paquete>     # Congela actualización
sudo apt-mark unhold <paquete>   # Libera actualización
apt-mark showhold                # Lista paquetes congelados
```

## 3. Administración de Usuarios y Grupos
### Archivos Clave del Sistema

| Archivo                            | Acceso          | Función y Estructura Principal                                                 |
| ---------------------------------- | --------------- | ------------------------------------------------------------------------------ |
| `/etc/passwd`                      | Lectura pública | Información de usuarios (7 campos): `usuario:x:UID:GID:GECOS:home:shell`       |
| `/etc/shadow`                      | Solo root       | Contraseñas cifradas de usuarios y políticas de caducidad (9 campos).          |
| `/etc/group`                       | Lectura pública | Lista de grupos (4 campos): `grupo:x:GID:miembros`                             |
| `/etc/gshadow`                     | Solo root       | Contraseñas cifradas y administradores de grupos.                              |
| `/etc/login.defs`                  | Sistema         | Define variables por defecto (`UID_MIN`, `UID_MAX`, etc.).                     |
| `/etc/default/useradd`             | Lectura pública | Valores por defecto de `superadd` (shell, base del HOME, plantilla)            |
| `/etc/skel`                        | Plantilla       | Archivos base (`.bashrc`, `.profile`) que se copian al HOME del nuevo usuario. |
| `/etc/shells`                      | Lectura pública | Shells válidas instaladas en el sistema                                        |
| `/etc/sudoers` y `/etc/sudoers.d/` | Solo root       | Quién puede usar `sudo` y para qué                                             |

### Rangos de UID / GID
* `0`: reservado exclusivamente para `root`
* `1` a `999`: cuentas de sistema/servicios (bin, daemon, www-data). Sin contraseña, shell nologin
* `1000` en adelante: usuarios estándar/ordinarios

### Comandos de Gestión de Usuarios
* **Creación: `useradd` vs `adduser`**

    * **`useradd`** (Comando base de bajo nivel):
    ```bash
    sudo useradd [opciones] <usuario>
    ```
    * `-m`: Crea el directorio HOME (copiando `/etc/skel`)

    * `-s /bin/bash`: Define la shell por defecto

    * `-g <grupo>`: Asigna el grupo primario.

    * `-G <g1,g2>`: Asigna grupos secundarios (separados por comas)

    * `-c` "Nombre Completo": Define el campo GECOS

    * `-e YYYY-MM-DD`: Establece fecha de caducidad de la cuenta

    * `-r`: Crea una cuenta de sistema (UID < UID_MIN)

    * `adduser` (Asistente interactivo en Perl, específico de Debian/Ubuntu):
    Crea el HOME, copia plantillas, asigna la shell `/bin/bash` e interactúa para definir la contraseña y datos GECOS de forma guiada.

* **Modificación: `usermod`**
    ```bash
    sudo usermod [opciones] <usuario>
    ```
    * `-aG <g1,g2>`: Añade a grupos secundarios sin eliminar los actuales (Importante usar siempre `-a`)

    * `-l <nuevo_nombre>`: Cambia el login del usuario

    * `-d /ruta -m`: Cambia el directorio HOME y desplaza físicamente los archivos

    * `-s /ruta/shell`: Cambia la shell de inicio

    * `-L` / `-U`: Bloquea / Desbloquea la cuenta

* **Eliminación: `userdel`**
    * **Borrado simple (mantiene `$HOME`):**
    ```bash
    sudo userdel <usuario>
    ```
    * **Borrado completo (elimina `$HOME` y buzón de correo):**
    ```bash
    sudo userdel -r <usuario>
    ```

* **Comandos de Gestión de Contraseñas y Expiración**

`passwd`
* **Cambiar contraseña propia o de un usuario (root):**
```bash
passwd [usuario]
```

* **Bloquear / Desbloquear cuenta:**
```bash
sudo passwd -l <usuario>
sudo passwd -u <usuario>
```

* **Caducar contraseña (fuerza cambio en el siguiente inicio de sesión):**

```bash
sudo passwd -e <usuario>
```

* **Ver estado de la contraseña (`P` = Válida, `L` = Bloqueada, `NP` = Sin clave):**
```bash
passwd -S <usuario>
```

``chage``
* **Consultar estado y caducidad de la cuenta:**
```bash
chage -l <usuario>
```

* **Configurar caducidad y tiempos límite:**
```bash
sudo chage -m <dias_min> -M <dias_max> -W <dias_aviso> -E <YYYY-MM-DD> <usuario>
```

* `-d 0`: Fuerza la expiración de la clave (cambio obligatorio en próximo inicio de sesión)

## Comandos de Gestión de Grupos
### Creación, Modificación y Borrado
* **Crear un grupo:**
```bash
sudo groupadd [-g GID] <nombre_grupo>
```

* **Renombrar un grupo:**
```bash
sudo groupmod -n <nuevo_nombre> <nombre_actual>
```

* **Borrar un grupo (no debe ser grupo primario de ningún usuario):**
```bash
sudo groupdel <nombre_grupo>
```

### Gestión de Miembros con `gpasswd`
```bash
sudo gpasswd [opciones] <grupo>
```

* `-a <usuario>`: Añade un usuario al grupo

* `-d <usuario>`: Elimina un usuario del grupo

* `-M <u1,u2>`: Sustituye la lista completa de miembros del grupo por la especificada

* `-A <u1,u2>`: Define a los administradores del grupo

### Cambio Temporal de Grupo Primario: `newgrp`
```bash
newgrp <grupo>   # Inicia una subshell donde el grupo indicado es el primario activo
exit             # Cierra la subshell y vuelve al grupo primario original
```
### Consultas Rápidas de Información e Identidad

| Comando | Función | 
| -- | -- | 
| `id [usuario]` | Muestra UID, GID primario y lista de grupos secundarios con sus IDs | 
| `groups [usuario]` | Muestra los nombres de los grupos a los que pertenece el usuario | 
| `whoami` | Muestra el nombre del usuario con la sesión activa actual | 
| `who` | Muestra los usuarios conectados actualmente al sistema | 
| `getent passwd <usuario>` | Consulta la entrada del usuario en las bases del sistema (ficheros locales, LDAP, etc.) | 
| `finger <usuario>` | Información detallada del usuario y datos GECOS (`apt install finger`) | 

### Mantenimiento Post-Eliminación (Búsqueda de Archivos Huérfanos)
Cuando se elimina un usuario o grupo sin borrar sus archivos, estos conservan sus ID numéricos

* **Buscar archivos huérfanos por UID/GID antiguo:**

```bash
sudo find / -uid <UID_antiguo>
sudo find / -gid <GID_antiguo>
```

* **Reasignar propiedad en lote:**

```bash
sudo find / -gid <GID_antiguo> -exec chgrp <nuevo_grupo> {} \;
sudo find / -uid <UID_antiguo> -exec chown <nuevo_usuario> {} \;
```

