# Práctica 6: Administración de Usuarios y Grupos en Linux

## 1. Introducción

* **Multiusuario**: Linux permite que múltiples usuarios trabajen de forma simultánea.

* **Tipos de usuarios:**

    * **Administrador (root)**: Control total del sistema. Por seguridad, solo debe usarse para tareas administrativas concretas

    * **Usuarios finales / de servicio**: Cuentas estándar para personas o procesos/servicios del sistema

## 2. Usuarios, Grupos, UIDs y GIDs
### Identificadores (UID y GID)

Linux identifica internamente a usuarios y grupos mediante números, no por sus nombres simbólicos:

* **UID (User ID)**: Identificador único de usuario

* **GID (Group ID)**: Identificador único de grupo

### Rangos de IDs (definidos en `/etc/login.defs`)

* `0`: Reservado para el usuario/grupo root.

* `1` a `99` (o hasta 999 según distribución): Cuentas del sistema/especiales (`bin`, `daemon`, `apache`)

    * No tienen contraseña ni permiten inicio de sesión (nologin)

    * Asumen privilegios específicos de root para servicios concretos

* `1000` en adelante (Ubuntu): Usuarios ordinarios/normales

> **Regla de asignación**: Al crear usuarios, se asigna el siguiente ID disponible. Si se elimina una cuenta, su ID no se reutiliza automáticamente para evitar que el nuevo usuario herede la propiedad de archivos antiguos

### Grupos

* Mapean conjuntos de usuarios para gestionar permisos sobre archivos y acceso al hardware

* **Grupo Primario**: Asignado por defecto al crear archivos/procesos. Es obligatorio tener al menos uno para poder hacer login

* **Grupos Secundarios**: Grupos adicionales a los que pertenece el usuario

* **Comando newgrp `<grupo>`**: Cambia temporalmente el grupo primario activo durante la sesión

## 3. Archivos Clave de Configuración

| Archivo | Acceso | Función y Estructura Principal |
|---|---|---|
| `/etc/passwd` | Lectura pública | Información de usuarios (7 campos): `usuario:x:UID:GID:GECOS:home:shell` |
| `/etc/shadow` | Solo root | Contraseñas cifradas de usuarios y políticas de caducidad (9 campos). |
| `/etc/group` | Lectura pública | Lista de grupos (4 campos): `grupo:x:GID:miembros` |
| `/etc/gshadow` | Solo root | Contraseñas cifradas y administradores de grupos. |
| `/etc/login.defs` | Sistema | Define variables por defecto (`UID_MIN`, `UID_MAX`, etc.). |
| `/etc/skel` | Plantilla | Archivos base (`.bashrc`, `.profile`) que se copian al HOME del nuevo usuario. |

### Ficheros de entorno del usuario (en su `$HOME`)

* `.bashrc`: Se ejecuta en cada shell interactivo (alias, prompt, variables locales)

* `.profile` / `.bash_profile`: Se ejecuta solo una vez al iniciar sesión (ej. variable PATH)

## 4. Gestión de Cuentas: `useradd` vs `adduser`

### Comando `useradd` (Utilidad estándar de bajo nivel)

* **Sintaxis:** `useradd` [opciones] nombreusuario

**Parámetros más comunes:**

* `-m`: Crea automáticamente el directorio `$HOME` (copiando `/etc/skel`)

* `-k /ruta`: Especifica un directorio plantilla alternativo a `/etc/skel`

* `-c "texto"`: Comentario para el campo GECOS (nombre completo, `etc.`)

* `-d /ruta`: Especifica una ruta personalizada para el directorio `HOME`

* `-g <grupo>`: Asigna el grupo primario

* `-G <g1,g2>`: Asigna grupos secundarios (separados por comas)

* `-s /shell`: Define la shell por defecto (ej. `/bin/bash`, `/sbin/nologin`, `/bin/false`)

* `-e YYYY-MM-DD`: Fecha de expiración de la cuenta

* `-u <UID>`: Asigna un UID específico. (Con `-o` permite duplicar un UID existente)

* `-r`: Crea una cuenta de sistema (UID menor a UID_MIN)

> Paso obligatorio tras **useradd**: Ejecutar **passwd <usuario>** para establecer su contraseña; de lo contrario, la cuenta permanece bloqueada

### Diferencia principal: `useradd` vs `adduser`

* `useradd`: Binario nativo GNU/Linux. Mantiene el mismo comportamiento en todas las distribuciones, pero no crea el directorio HOME por defecto (requiere la opción -m)

* `adduser`: Script en Perl (propio de distribuciones basadas en Debian/Ubuntu). Es un asistente interactivo de más alto nivel que crea el directorio HOME, copia plantillas y pide la contraseña automáticamente

## 5. Comandos Útiles de Consulta

* `id [usuario]`: Muestra el UID, GID primario y grupos secundarios de un usuario

* `finger [usuario]`: Muestra información detallada del usuario (incluyendo el campo GECOS)

### Modificar Cuentas: `usermod`
Permite editar parámetros de cuentas ya creadas

* **Sintaxis: `usermod [opciones] nombreusuario`**

**Opciones clave:**
* `-l nuevonombre`: Cambia el nombre de usuario de la cuenta

* `-d /ruta [-m]`: Cambia el directorio HOME. La opción -m mueve los archivos del HOME antiguo al nuevo

* `-g <grupo>`: Cambia el grupo primario

* `-G <g1,g2> [-a]`: Asigna grupos secundarios

> Atención: Sin -a, sobrescribe y elimina la lista de grupos previos. Usa siempre -aG para añadir grupos

* `-u <UID> [-o]`: Cambia el UID. (Si se cambia, se debe actualizar la propiedad de sus archivos con chown -R usuario /home/usuario)

* `-L / -U`: Bloquea (-L) o desbloquea (-U) la cuenta.

> Buenas prácticas: Antes de modificar un usuario, ejecuta who para comprobar que no esté conectado, ya que alterar la cuenta en uso puede causar fallos de sesión

### Control de Contraseñas: `passwd`
Permite cambiar la contraseña y gestionar el estado de la cuenta

* **Sintaxis: `passwd [opciones] nombreusuario`**

**Opciones administrativas (requieren `sudo/root`):**

* `-l`: Bloquea la cuenta (añade un ! al inicio del hash en `/etc/shadow`)

* `-u [-f]`: Desbloquea la cuenta. Con -f fuerza el desbloqueo si no tiene clave

* `-d`: Elimina la contraseña de la cuenta (la deja en blanco)

* `-S`: Muestra el estado de la contraseña (P = con clave, L = bloqueada/sin clave)

### Expiración y Caducidad: `chage`
Gestiona el envejecimiento de la contraseña y la caducidad de la cuenta

* **Sintaxis: `chage [opciones] nombreusuario`**

    * `-l`: Muestra la información de expiración de la cuenta/contraseña. (Opción accesible por el usuario normal sobre su propia cuenta)

    * `-m <días>`: Días mínimos entre cambios de contraseña (0 = sin límite).

    * `-M <días>`: Días máximos de validez de la contraseña (por defecto 99999)

    * `-W <días>`: Días de antelación para avisar al usuario de que la clave va a caducar (por defecto 7)

    * `-I <días>`: Días de inactividad tras la caducidad antes de bloquear la cuenta

    * `-E YYYY-MM-DD`: Fecha exacta en que la cuenta dejará de estar activa

    * `-d <días>`: Modifica la fecha del último cambio de clave

### Eliminación de Cuentas: `userdel`
* **Sintaxis: `userdel [-r [-f]] nombreusuario`**
* **Sin opciones**: Borra la cuenta del sistema, pero conserva su directorio HOME y archivos
* `-r`: Elimina la cuenta y su directorio HOME junto con el buzón de correo
* `-rf`: Fuerza la eliminación del HOME aunque contenga archivos que pertenezcan a otros usuarios

> Respaldo previo: Para buscar y copiar todos los archivos del usuario antes de borrarlo:
**sudo find / -user usuario1 -exec cp {} /root/usuario1 \;**
(Si ya se eliminó la cuenta sin **-r**, usa **find / -uid <ID_antiguo>**)


## 6. Elevación y Cambio de Privilegios: `su` vs `sudo`
### Comando `su` (Switch User)
Cambia la sesión de usuario activa en la terminal sin cerrar sesión

* `su usuario`: Cambia al usuario especificado pero mantiene las variables de entorno y el directorio de trabajo del usuario original

* `su - usuario`: Cambia al usuario cargando su entorno completo (cambia al directorio **$HOME** del nuevo usuario y ejecuta sus scripts de inicio `.profile/.bashrc`)

### Comando `sudo` (Switch User Do)
Permite ejecutar comandos individuales con privilegios de `root` (o de otro usuario) de forma segura y auditada

* **Ventajas sobre `su`**: No requiere compartir la contraseña de root; cada usuario usa la suya

* **Funcionamiento en Ubuntu**: La cuenta de root está bloqueada por defecto. Las tareas de administración se realizan anteponiendo sudo a las órdenes o abriendo un shell administrativo con sudo `-i`

* **Archivo de configuración (`/etc/sudoers`):**

    * Se debe editar únicamente con el comando `visudo`

    * Permite definir grupos y usuarios con permiso para usar `sudo`

    * **Sintaxis clave:**

        * `root ALL=(ALL:ALL) ALL` → Acceso total ilimitado

        * `%sudo ALL=(ALL:ALL) ALL` → Permite a los miembros del grupo `sudo` ejecutar cualquier comando

        * `%admin ALL=(ALL) ALL` → Permite privilegios de administración al grupo admin

## 7. Configurando grupos
### 1. Crear Grupos: `groupadd`

* Permite añadir nuevos grupos al sistema (requiere permisos de `root` o `sudo`)

    * **Sintaxis: `groupadd [opciones] nombregrupo`**

* **Opciones principales:**

* `-g GID`: Asigna un ID de grupo específico. Si se omite, se asigna el siguiente número disponible mayor que GID_MIN (definido en `/etc/login.defs`)

* `-o`: Se usa junto con `-g` para forzar la asignación de un `GID` que ya está en uso por otro grupo (colisión de GIDs)

* `-r`: Crea un grupo de sistema (con un `GID` inferior a `GID_MIN`)

```bash
sudo groupadd proyecto1
```

### 2. Modificar Grupos: `groupmod` y `gpasswd`
Cambiar nombre e ID del grupo: `groupmod`

* **Sintaxis: `groupmod [opciones] nombregrupo`**

* `-n nuevonombre`: Renombra el grupo

* `-g GID [-o]`: Cambia el GID asignado al grupo

### Gestionar miembros del grupo: gpasswd vs usermod
Para añadir usuarios a un grupo existen dos opciones en línea de comandos:

**1. Mediante `usermod`:**

* `sudo usermod -aG grp1,grp2 usuario`: Añade (`-a`) al usuario a los grupos secundarios sin borrar su membresía en otros grupos existentes

> Atención: Si se omite el parámetro **-a**, el usuario es eliminado de todos los grupos a los que pertenecía que no estén explícitamente en la lista

**2. Mediante gpasswd (Método recomendado por ser menos propenso a errores):**

* `-a usuario`: Añade un usuario al grupo de forma segura

* `-d usuario`: Elimina a un usuario de un grupo

* `-A u1,u2...`: Define la lista de administradores del grupo (usuarios que pueden añadir/quitar miembros o cambiar la clave del grupo)

* `-M u1,u2...`: Define la lista completa de miembros del grupo

* `-r`: Elimina la contraseña del grupo

* `-R`: Invalida el uso de `newgrp` para ese grupo


> Contraseñas de Grupo y **newgrp**: Si se ejecuta **gpasswd** sin opciones, permite asignar una clave al grupo. Se usaba históricamente para permitir el acceso mediante **newgrp** a usuarios ajenos. En distribuciones modernas (como Ubuntu) las contraseñas de grupo están prácticamente en desuso y **newgrp** se emplea para cambiar temporalmente el grupo primario activo

### 3. Comprobación de Grupos de un Usuario
* **Comando `groups`**: groups nombreusuario

* **Comando id**: id nombreusuario

* **Filtro en `/etc/group`**: cat `/etc/group | grep nombreusuario`

### 4. Eliminar Grupos: `groupdel`
* **Sintaxis: `sudo groupdel nombregrupo`**

> **Restricción**: El sistema no permitirá borrar un grupo si es el grupo primario de algún usuario. Primero debe cambiarse el grupo primario del usuario con `usermod -g`

### Procedimiento Post-Eliminación (Archivos Huérfanos)
Al eliminar un grupo, sus archivos asociados quedan asignados a un `GID` huérfano. Para corregirlo:

**1. Buscar archivos asignados al GID eliminado:**

```bash
sudo find / -gid 1000
```

**2. Reasignar propiedad de grupo con chgrp:**

```bash
sudo find / -gid 1000 -exec chgrp administradores {} \;
```

**3. Eliminar archivos si ya no son necesarios.**

### 8. Caso Práctico Integrado (Ejemplo de flujo de trabajo)

```bash
# 1. Crear usuario con comentario, HOME y shell bash
sudo useradd -c "Ada Lovelace" -s /bin/bash -m alovelace

# 2. Asignar contraseña
sudo passwd alovelace

# 3. Crear nuevo grupo 'babbage'
sudo groupadd babbage

# 4. Cambiar la shell del usuario a tcsh
sudo usermod -s /bin/tcsh alovelace

# 5. Añadir alovelace al grupo babbage manteniendo sus grupos anteriores
sudo usermod -a -G babbage alovelace

# 6. Establecer políticas de expiración
# Expiración de cuenta: 15/12/2025 | Días min clave: 10 | Días máx clave: 20
sudo chage -E 2025-12-15 -m 10 -M 20 alovelace

# 7. Verificar la configuración final del usuario
sudo chage -l alovelace
```

## Ejercicios 
**1. Revisa el archivo /etc/passwd y escribe la lista de los usuarios definidos en el mismo que tengan como shell /bin/false. ¿Qué tipo de usuarios son? ¿Por qué tienen esa shell asignada?**

```bash
grep '/bin/false$' /etc/passwd
# O si quieres ver solo los nombres de usuario:
grep '/bin/false$' /etc/passwd | cut -d: -f1
```

Son cuentas de sistema o cuentas de servicio/no interactivas (como `syslog`, `daemon`, `www-data`, etc.)

Por razones de seguridad. La shell `/bin/false` finaliza inmediatamente con un código de error, lo que **impide que nadie pueda iniciar una sesión interactiva** (ya sea localmente o mediante SSH/console/FTP) usando esas cuentas. Así se reduce la superficie de ataque en caso de que alguna contraseña fuese comprometida

**2. Visualiza el contenido de los archivos `/etc/default/useradd` y `/etc/login.defs`. Comprueba cuáles son las opciones por defecto que tendría un usuario que se creara en tu sistema. A continuación, crea una cuenta de usuario y visualiza el contenido de los archivos `/etc/passwd`, `/etc/group`, y el directorio `/home` para comprobar que los nuevos datos se han rellenado conforme a la especificación tomada de `/etc/default/useradd` y `/etc/login.defs`.**

```bash
cat /etc/default/useradd
grep -E '^(UID|GID)_(MIN|MAX)' /etc/login.defs | grep -v '#'
```

Definen la shell predeterminada (usualmente `/bin/bash`), el directorio base (normalmente `/home`), el rango de UIDs/GIDs para usuarios normales (en Ubuntu suele ser del `1000` al `60000`), el grupo por defecto o la expiración de contraseñas

```bash
# 1. Creamos la cuenta
sudo useradd -m pr6_usuario

# 2. Comprobamos la entrada en /etc/passwd (UID, GID, HOME, Shell)
cat /etc/passwd | grep pr6_usuario

# 3. Comprobamos su grupo en /etc/group
cat /etc/group | grep pr6_usuario

# 4. Verificamos que se creó su directorio HOME y se copiaron los ficheros ocultos de /etc/skel
ls -la /home/pr6_usuario
```

**3. Supongamos que se tiene un disco duro auxiliar montado en el directorio `/home2`. Supongamos que existen los grupos de usuarios `depto1` y `depto2`.**
**Se quiere crear una nueva cuenta de usuario completamente operativa para un usuario llamado Juan López (debe tener una contraseña), cuya directorio raíz deberá estar ubicado en /home2, que pertenezca a los grupos depto1 y depto2 siendo su grupo primario depto1 y con shell por defecto tcsh.**

Suponiendo que los grupos depto1 y depto2 ya están creados, la secuencia de órdenes es:

```bash
# 1. Crear el usuario con HOME en /home2/jlopez, grupo primario depto1, grupo secundario depto2 y shell tcsh
sudo useradd -c "Juan López" -d /home2/jlopez -m -g depto1 -G depto2 -s /bin/tcsh jlopez

# 2. Asignar la contraseña obligatoria para que la cuenta quede operativa
sudo passwd jlopez
```

**4. Siendo el usuario root, se quiere eliminar la cuenta del usuario user1 cuyo directorio raíz es /home/user1 y que además tiene algunos archivos en el directorio /tmp.**

**Escriba las órdenes necesarias para eliminar completamente la cuenta del usuario user1 incluyendo todos sus archivos, pero haciendo previamente una copia de seguridad de los
mismos en el directorio /root.**

Como root (o con sudo), los pasos para respaldar todo y luego borrar son:

```bash
# 1. Crear directorio para el respaldo
mkdir -p /root/user1_backup

# 2. Copiar todos los archivos propiedad de user1 (incluyendo /home/user1, /tmp y cualquier otro punto del sistema)
find / -user user1 -exec cp -r {} /root/user1_backup \; 2>/dev/null

# 3. Eliminar la cuenta borrando su HOME y su buzón de correo
userdel -r user1

# 4. Eliminar manualmente los archivos que hayan quedado en /tmp (si la opción -r no limpió directorios fuera de su $HOME)
rm -rf /tmp/*user1*
```

**5. Averigua a qué grupos pertenece el usuario con el que te hayas conectado para hacer las prácticas. Hazlo al menos de dos formas distintas. Explica cómo lo has hecho.**

Para comprobar los grupos del usuario actual ($USER):

1. Forma 1 (Comando id):

```bash
id
```
Muestra el UID, GID primario y la lista de todos los GIDs secundarios asociados al usuario actual

2. Forma 2 (Comando groups):
```bash
groups
```
mprime directamente los nombres de todos los grupos a los que pertenece la cuenta en la sesión activa

3. Forma 3 (Filtrando /etc/group)
```bash
cat /etc/group | grep "$USER"
```

Busca la cadena de texto del nombre del usuario en el archivo de base de datos de grupos `/etc/group`

**6. ¿Qué dos formas existen en Linux para añadir, con una orden, un usuario a un grupo ya creado? ¿Cuál de ellas es mejor? ¿Por qué?**

1. Usando usermod:

```bash
sudo usermod -aG nombregrupo nombreusuario
```

2. Usando gpasswd:
```bash
sudo gpasswd -a nombreusuario nombregrupo
```

**gpasswd es mejor y más segura.**

Con `gpasswd -a` agregas al usuario directamente al grupo objetivo sin tocar sus demás grupos. Con `usermod`, si por descuido se te olvida incluir la opción `-a` (append) y solo ejecutas `usermod -G grupo usuario`, el sistema eliminará al usuario de todos sus otros grupos secundarios previos, causando posibles pérdidas de permisos no deseadas

**7. Un usuario del sistema con nombre de usuario empleado1 ha olvidado su contraseña. ¿Qué harías para restablecerla?**

Como el usuario ha olvidado su clave y no la conoce, un usuario normal no puede ayudarle. Se debe actuar desde la cuenta root o usando sudo

```bash
# Restablecer la contraseña directamente sin pedir la actual
sudo passwd empleado1
```

**8. ¿Para qué se usa la contraseña de un grupo?**

La contraseña de un grupo se utiliza en combinación con la orden `newgrp`.

Permite que un usuario que **no es miembro** de un grupo pueda unirse o cambiarse temporalmente a él (convirtiéndolo en su grupo primario activo para la sesión) si conoce la contraseña del grupo

(Nota: En distribuciones modernas como Ubuntu, su uso está obsoleto y se prefieren los permisos mediante `sudo` o la inclusión explícita en `/etc/group`)

**9. Si se pudiese eliminar un grupo que sea el grupo primario de algún usuario, el sistema quedaría en una situación de funcionamiento inaceptable. ¿Cual es esa situación de funcionamiento? ¿Por qué ocurre esto?**

* **Situación de funcionamiento**: Un usuario no podría volver a hacer login en el sistema (o si ya está conectado, no podría crear archivos ni ejecutar subprocesos correctamente)

* **Por qué ocurre esto**: En Unix/Linux, todo usuario requiere obligatoriamente tener un grupo primario asignado. Cada vez que el usuario crea un archivo o proceso, el sistema necesita asociar un GID primario a ese objeto. Si se borrase el grupo primario, el usuario quedaría huérfano de GID primario en `/etc/passwd`, provocando un fallo de autenticación en la rutina de inicio de sesión (`login`)

**10. Averigua, ejecutando una orden, qué UID y GID mínimo y máximo se han definido en Linux Ubuntu (debes usar un pipeline)**

```bash
grep -E '^(UID|GID)_(MIN|MAX)' /etc/login.defs | grep -v '#'
```

