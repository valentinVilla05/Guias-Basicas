# Ejercicios extras de la práctica 1

Estos ejercicios son los que el profesor **Pedro Jose (aka: Pedro J)** pone como opcionales para sus grupos. Es recomendable saber hacerlos o entenderlos ya que están muy completos y pueden servir para el examen

## 1. Condicionantes, Entorno y Planificación de la Práctica

### 1.1 Punto de partida necesario

Para poder abordar la práctica hace falta:
**1. Virtual-Box**

**2. La ISO de Ubuntu 24.04 LTS**

**3. El sistema Actualizado** (`sudo apt update &&  sudo apt upgrade`)

**4. Las Guest Additions**

**5. Un margen de 5GB a 10Gb de espacio**

## 2. Anatomía de la Máquina Virtual en el Anfitrión

### 2.1. Archivos principales en la carpeta de la VM

En el sistema anfitrión la carpeta de la máquina virtual contiene los siguientes ficheros:

- `.vbox`: Fichero de configuración de la máquina virtual en formato XML

- `.vbox-prev`: Copia de seguridad del archivo de configuración XML

- `.vdi` (**VirtualBox Disk Image**): Fichero que representa el disco duro virtual del sistema invidatado

- Carpeta `Snapshots`: Almacena los estados e imágenes de diferencia creados al tomar instantaneas

---

Cuestión 1: comandos raros ????

### 2.2 Comportamiento del disco de asignación Dinámica

- **Asignación dinámica vs. Reserva completa:**
- En la asignación dinámica, el fichero `.vdi` ocupa inicialmente solo el tamaño del SO instalado y crece hasta dentro del límite que le determinemos (que por defecto son `25GB`)

- _Penalización_: Introduce una leve pérdida de rendimiento al escribir bloques nuevos por la sobrecarga de asignación en tamaño real

- **El fenómeno del borrado de archivos:**
- Si se genera un fichero grande dentro de la máquina virtual , el fichero `.vdi` del alfitrión aumentará el tamaño

- Al borrar dicho fichero dentro del invitado , el **fichero** `.vdi` **No reduce su tamaño en el anfitrión**. EL sistema de archivos del invitado solo marca los bloques como "libres", pero VirtualBox no libera ese espacio automáticamente a no ser de que usemos `VBoxManage modifymedium compact`

### 2.3. El proceso Hipervisor

Virtualbox es un **hipervisor de Tipo 2**: Cuando la Vm se está ejecutando, en el administrador de tareas del anfitrión se observa como un proceso más del sistema operativo

## 3. Instantáneas como Red de Seguridad (Ejercicio E2)

### 3.1 Elementos que guarda una instantánea

Una instantánea guarda tres componentes principales:

**1. La configuración de la máquina virtual**

**2. El estado del disco duro virtual (mediante un fichero `.vdi`)**

**3. El estado de la memoria RAM (solo se toma la instantánea si VM está en ejecución)**

### 3.2 Funcionamiento de las instantáneas

- Al crear una instantánea, el fichero `.vdi` se congela y pasa a ser solo de lectura

- Los nuevos ficheros dentro de la carpeta `Snapshots` almacenan los cmabios o diferencias respecto al estado original

- Restaurar una instantánea anterior deshace **todos** los cambiso realizados posteriormente

## 4. Identificación del Núcleo y de la Distribución

### 4.1. Comandos de inspección del sistema

- `uname -s`: Muestra el nombre del núcleo (LINUX)
- `uname -r`: Muestra la versión de publicación del núcleo
- `uname -m`: Muestra la arquitectura del hardware (ej. `x86_64`)
- `uname -a`: Muestra toda la información del sistema
- `cat /etc/os-release`: Muestra la información de la distribución instalada
- `ls /boot/vmlinuz*`: Lista los núcleos instalados en el sistema

### 4.2. Evolución de la numeración del núcleo

- **Criterio clásico (X.Y.Z)**: Históricamente, en la versión `X.Y.Z`, si Y era un número par indicaba un núcleo estable, e impar un núcleo en desarrollo. _Este criterio quedó en desuso hace tiempo_

- **Novedad de Ubuntu 26.04**: Incorpora la serie de núcleo `7.0`, mientras que 24.04 usa la serie `6.8`

### 4.3. Novedades clave en herramientas (GNU frente a Rust)

En **Ubuntu 26.04 LTS**, las utilidades báscias del sistema las proporciona el paquete `rust-coreutils` (reimplementación en lenguaje Rust), en lugar del paquete clásico `coreutils` de GNU

- Comandos como `ls` o `cat` provienen de Rust

- Los comandos de modificación de archivos (`cp`, `mv`, `rm`) siguen siendo las versiones originales de GNU

- Las utilidades de GNU siguen disponibles anteponiendo el prefijo `gnu` (ej. `gnuls`)

## 5. Esquemas de Particionado: Anfitrión frente a Invitado

### 5.1. Comparativa entre MBR y GPT

- **MBR (Master Boot Record):**
  - Límite máximo de **4 particiones primarias** o 3 primarias y 1 extendida
  - Límite de tamaño del disco de **2 TB**
- **GPT (GUID Partition Table)**
  - Resuelve las limitaciones de MBR permitiendo hasta 128 particiones en Windows/Linux

  - Soporta discos de mayor capacidad y requiere una partición del sistema EFI para el arranque en sistemas UEFI modernos

### 5.2. Dispositivos en Linux

Linux trata todos los dispositivos de almacenamiento como si fueran ficheros. Por ejemplo:

- `/dev/sda`: El disco duro completo
- `/dev/sda1`, `/dev/sda2`: Las particiones individuales del disco sda

## 6. Memoria de Intercambio (Swap)

### 6.1. ¿Partición o Fichero de Swap?

- **Comprobación:** Mediante el comando `swapon --show` y `grep -i swap /etc/fstab`

- **Tendencia moderna:** Las instalaciones actuales de Ubuntu ya no crean una partición de swap dedicada, sino que utilizan un fichero de intercambio llamado `/swapfile` en la raíz del sistema

### 6.2. Funciones de la Swap y su impacto

**1. Paginación**: Permite mover bloques de memoria inactivos de la RAM al disco para liberar RAM

**2. Hibernación:** Guarda todo el estado de la RAM en el disco para apagar el equipo manteniendo la sesión

> Consideraciones: En una máquina virtual la función de hibernación no tiene sentido ya que el hipervisor gestiona el pausado o guardado de la VM

## 7. Recorrido por la Jerarquía de Directorios FHS

### 7.1. Unificación `/usr-merge`

Históricamente, los directorios `/bin`, `/sbin` y `/lib` eran independientes de `/usr`. En las versiones actuales de Ubuntu:

- `/bin`, `/sbin` y `/lib` son enlaces simbólicos apuntando a /usr/bin, /usr/sbin y /usr/lib respectivamente

### 7.2. Sistemas de archivos virtuales y `/tmp`

- `/proc`: Es un sistema de archivos virtual generado dinámicamente en la memoria RAM por el núcleo Linux. Por ejemplo, `/proc/uptime` cambia en cada ejecución indicando el tiempo que lleva encendido el sistema

- `/tmp` como `tmpfs`:
  - En **Ubuntu 24.04**, `/tmp` es un directorio estándar almacenado en la partición raíz

  - A partir de Ubuntu **26.04**, `/tmp` se monta por defecto como un sistema `tmpfs` (en la memoria RAM)

  - _Consecuencia:_ Todo el contenido de `/tmp` desaparece por completo al reiniciar el sistema y su uso consume memoria RAM

## 8. Gestión de Paquetes y Dependencias

### 8.1. Diferencias entre `dpkg` y `apt`

- `dpkg`: Herramienta de bajo nivel. Instala o elimina paquetes .deb locales pero no resuelve dependencias automáticas

- `apt`: Herramienta de alto nivel. Trabaja contra repositorios remotos, descarga los paquetes necesarios y gestiona/resuelve automáticamente todas las dependencias

### 8.2. Niveles de desinstalación en APT

- `sudo apt remove <paquete>`: Elimina los binarios del programa, pero conserva los archivos de configuración (el paquete pasa al estado rc - Residual Config)

- `sudo apt purge <paquete>`: Elimina los binarios y borra completamente los archivos de configuración

- `sudo apt autoremove`: Elimina paquetes que se instalaron automáticamente como dependencias y que ya no son necesarios

### 8.3. Novedades de APT 3 en Ubuntu 26.04

Ubuntu 26.04 incluye **APT 3**, introduciendo el historial de transacciones y deshacer cambios:

- `apt history-list`: Muestra el historial de instalaciones/borrados
- `sudo apt history-undo <ID>:` Deshace automáticamente una transacción anterior.
- **Obsolescencia**: Se elimina el comando clásico apt-key

## 9. Configuración del Arranque con GRUB

### 9.1. La Regla de Oro al editar GRUB

NUNCA se debe editar directamente el fichero `/boot/grub/grub.cfg`

- _Razón_: Es un fichero generado automáticamente por el sistema y cualquie cambio se sobrescribirá al actualizar el núcleo

- **Procedimiento correcto:**
  **1. Editar el archivo de configuración base: `/etc/default/grub`**
  **2. Aplicar los cambios en el sistema ejecutando: `sudo update-grub`**

### 9.2. Generación del Disco RAM Inicial (`initrd`)

- **Ubuntu 24.04**: Utiliza la herramienta `initramfs-tools` (comando `update-initramfs`)

- **Ubuntu 26.04**: Sustituye la herramienta predeterminada por dracut

## 10. Distribución de la Máquina Virtual en Formato OVA

### 10.1. Naturaleza del fichero OVA

Un fichero **.OVA (Open Virtual Appliance)** es un archivo comprimido basado en el formato estándar `tar`. Puede comprobarse su contenido interno sin extraerlo con la orden:

```bash
tar tvf Nombre_Maquina.ova
```

### 10.2. Contenido de un paquete OVA

Un archivo `.ova` empaqueta internamente los siguientes elementos:

**1. Descriptor OVF** (`.ovf`): Archivo XML que define las características hardware de la VM

**2. Manifiesto (.mf)**: Contiene los sumas de verificación (checksums SHA) para verificar la integridad

**3. imagen de disco duro: Normalmente convertida a formato `.vmdk`**
