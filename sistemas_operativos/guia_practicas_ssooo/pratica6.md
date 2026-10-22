# Práctica 6: Administración de Usuarios y Grupos en Linux

## 1. Introducción

- **Multiusuario**: Linux permite que múltiples usuarios trabajen de forma simultánea.

- **Cuenta de usuario**: Identidad creada en el sistema. Puede representar a una persona o una identidad de la máquina (un servicio, el sistema, el administrador).

- **Tipos de usuarios:**
  - **Administrador (root)**: Control total del sistema. Por seguridad, solo debe usarse para tareas administrativas concretas

  - **Usuarios finales / de servicio**: Cuentas estándar para personas o procesos/servicios del sistema

  - **Cuenta del sistema/servivio** (`bin` `daemon`, `www-data`...): las crea el sistema o las aplicaciones. No tienen contraseña y no están pensadas para iniciar sesión (cuenta _nologin_)

## 2. Usuarios, Grupos, UIDs y GIDs

Cada usuario tiene un nombre único y simbólico. Internamente Linux lo representa con un número, su UID.

Linux admite casi cualquier carácter, pero se recomienda:

- Usar solo **letras**, **números**, **guion bajo** (\_) y **punto** (.).
- **Empezar siempre por una letra** (`u45` es válido, `45u` no).
- **Máximo 32 caracteres**. Algunas utilidades antiguas truncan a 8, aunque hoy es habitual usar nombres más largos.
- **Usar minúsculas**: Linux distingue mayúsculas de minúsculas (juan y Juan son usuarios distintos).
- Seguir un criterio fijo (inicial del nombre + apellido: `fconde`, `f.conde`, `fconde01`) facilita localizar las cuentas.

### Identificadores (UID y GID)

Linux identifica internamente a usuarios y grupos mediante números, no por sus nombres simbólicos:

- **UID (User ID)**: Identificador único de usuario

- **GID (Group ID)**: Identificador único de grupo

### Rangos de IDs (definidos en `/etc/login.defs`)

- `0`: Reservado para el usuario/grupo root.

- `1` a `99` (o hasta 999 según distribución): Cuentas del sistema/especiales (`bin`, `daemon`, `apache`)
  - No tienen contraseña ni permiten inicio de sesión (nologin)

  - Asumen privilegios específicos de root para servicios concretos

- `1000` en adelante (Ubuntu): Usuarios ordinarios/normales

> **Regla de asignación**: Al crear usuarios, se asigna el siguiente ID disponible. Si se elimina una cuenta, su ID no se reutiliza automáticamente para evitar que el nuevo usuario herede la propiedad de archivos antiguos

Los IDs de las cuentas especiales **no están estandarizados** entre distribuciones (por ejemplo, daemon no tiene el mismo UID en Red Hat que en Debian). Por eso es preferible usar siempre nombres y no números.

### Grupos

Los grupos **no son cuentas**: son una forma de organizar conjuntos de cuentas y, sobre todo, **de asignar permisos** a varios usuarios a la vez.

- Mapean conjuntos de usuarios para gestionar permisos sobre archivos y acceso al hardware

- **Grupo Primario**: Asignado por defecto al crear archivos/procesos. Es obligatorio tener al menos uno para poder hacer login

- **Grupos Secundarios**: Grupos adicionales a los que pertenece el usuario. Le dan acceso a los archivos de esos grupos según sus permisos.

- **Comando `newgrp <grupo>`**: abre una nueva shell en la que el grupo indicado pasa a ser el grupo primario activo. Los archivos que se creen en esa shell pertenecerán a ese grupo. Con `exit` se vuelve a la shell anterior. Si el usuario no es miembro del grupo, el sistema pide la contraseña del grupo (hoy casi en desuso).

```bash
newgrp adm      # los archivos nuevos tendrán como grupo "adm"
exit            # vuelve al grupo primario habitual
```

## 3. Archivos Clave de Configuración

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

---

Ejemplo del `/etc/passwd` , con 7 campos separados por :

```bash
fconde:x:1000:1000:Francisco de Asís Conde Rodríguez,,,:/home/fconde:/bin/bash
```

| Nº  | Campo                                            | En el ejemplo                          |
| --- | ------------------------------------------------ | -------------------------------------- |
| 1   | Nombre de usuario                                | `fconde`                               |
| 2   | Contraseña (`x` = está cifrada en `/etc/shadow`) | `x`                                    |
| 3   | UID                                              | `1000`                                 |
| 4   | GID del grupo primario                           | `1000`                                 |
| 5   | GECOS: nombre completo y datos de contacto       | `Francisco de Asís Conde Rodríguez,,,` |
| 6   | Directorio HOME                                  | `/home/fconde`                         |
| 7   | Shell por defecto (debe estar en /etc/shells)    | `/bin/bash`                            |

---

Ejemplo de `/etc/group`:

```
developer:x:1002:
adm:x:4:syslog,procopia
```

| Nº  | Campo                                |
| --- | ------------------------------------ |
| 1   | Nombre del grupo                     |
| 2   | Contraseña (`x` = en `/etc/gshadow`) |
| 3   | GID                                  |
| 4   | Miembros, separados por comas        |

> Los usuarios para los que un grupo es el **primario** no aparecen en el campo 4. Por eso `grep usuario /etc/group` no basta para conocer todos sus grupos: hay que usar `id` o `groups`.

---

Ejemplo de `/etc/shadow`

Una línea por usuario, con 9 campos. Solo root puede leerlo.

```
frank:$6$i9gjM4Md...:18029:0:99999:7:::
```

| Nº  | Campo                                                                                     | Opción de `chage` |
| --- | ----------------------------------------------------------------------------------------- | ----------------- |
| 1   | Nombre de usuario                                                                         |                   |
| 2   | Contraseña cifrada                                                                        | `passwd`          |
| 3   | Fecha del último cambio (días desde 01/01/1970). `0` = debe cambiarla en el próximo login | `-d`              |
| 4   | Días mínimos entre cambios                                                                | `-m`              |
| 5   | Días máximos de validez                                                                   | `-M`              |
| 6   | Días de aviso antes de que caduque                                                        | `-W`              |
| 7   | Días de inactividad tras caducar antes de bloquear                                        | `-I`              |
| 8   | Fecha de caducidad de la cuenta (días desde 01/01/1970)                                   | `-E`              |
| 9   | Reservado                                                                                 |                   |

**Valores especiales del campo 2:**

- `!` delante del hash: cuenta **bloqueada** (se puede desbloquear, el hash se conserva).
- `!` solo, sin hash: cuenta bloqueada y **sin contraseña** (es lo que deja `useradd` hasta que se ejecuta `passwd`).
- `*`: no se puede iniciar sesión con contraseña (típico de cuentas de sistema).
- El prefijo del hash indica el algoritmo: `$1$` MD5, `$5$` SHA-256, `$6$` SHA-512, `$y$` yescrypt (el de las versiones modernas de Ubuntu).

---

En cuanto a `/etc/gshadow`:

4 campos: nombre del grupo, contraseña cifrada (si empieza por `!`, nadie puede entrar con `newgrp`), **administradores** del grupo (pueden añadir y quitar miembros con `gpasswd`) y miembros.

---

Para el resto de ficheros:

- **`/etc/login.defs`**: valores por defecto al crear usuarios: rangos de UID/GID (`UID_MIN`, `SYS_UID_MIN`...), caducidad de contraseñas (`PASS_MAX_DAYS`, `PASS_MIN_DAYS`, `PASS_WARN_AGE`), si se crea un grupo privado por usuario (`USERGROUPS_ENAB`), algoritmo de cifrado, etc.
- **`/etc/default/useradd`**: shell por defecto, directorio base del HOME, plantilla (`SKEL`), días de inactividad. En Ubuntu suele traer `SHELL=/bin/sh`. Se consulta con `useradd -D`.
- **`/etc/skel/`**: contiene los ficheros que se copian al HOME de cada usuario nuevo (`.bashrc`, `.profile`, `.bash_logout`).

### Ficheros de entorno del usuario (en su `$HOME`)

Son ficheros ocultos (empiezan por punto; se ven con `ls -a`) que se copian desde `/etc/skel` al crear el usuario. Definen variables, alias, el prompt, etc.

| Fichero                          | Cuándo se ejecuta                                                 | Uso típico                       |
| -------------------------------- | ----------------------------------------------------------------- | -------------------------------- |
| `~/.profile` o `~/.bash_profile` | Solo al **iniciar sesión** (shell de login)                       | Variables de entorno como `PATH` |
| `~/.bashrc`                      | En **cada shell interactivo** (nueva ventana de terminal, SSH...) | Alias, prompt, preferencias      |
| `~/.bash_logout`                 | Al **cerrar la sesión**                                           | Tareas de limpieza               |

- En un shell de login, bash lee primero `/etc/profile` y después **el primero que exista** de `~/.bash_profile`, `~/.bash_login` y `~/.profile`.
- En Ubuntu, el `.profile` por defecto carga después el `.bashrc`.
- Relación con `su`: `su usuario` abre un shell interactivo normal (lee `.bashrc`); `su - usuario` abre un shell de **login** (lee `.profile`).

## 4. Gestión de Cuentas: `useradd` vs `adduser`

### Comando `useradd` (Utilidad estándar de bajo nivel)

- **Sintaxis:** `useradd` [opciones] nombreusuario

**Parámetros más comunes:**

| Opción          | Función                                                                                 |
| --------------- | --------------------------------------------------------------------------------------- |
| `-m`            | Crea el HOME copiando `/etc/skel`. Sin ella la cuenta no tiene directorio propio        |
| `-k /ruta`      | (con `-m`) usa otra plantilla en lugar de `/etc/skel`                                   |
| `-M`            | No crea el HOME (cuentas de sistema)                                                    |
| `-d /ruta`      | HOME personalizado (por defecto `/home/usuario`)                                        |
| `-c "texto"`    | Campo GECOS (nombre completo)                                                           |
| `-s /shell`     | Shell por defecto                                                                       |
| `-g grupo`      | Grupo primario                                                                          |
| `-G g1,g2`      | Grupos secundarios (separados por comas, sin espacios)                                  |
| `-N`            | No crea el grupo privado; asigna el grupo genérico `users` (GID 100)                    |
| `-u UID`        | UID concreto. Con `-o` permite repetir un UID existente (dos nombres, un mismo usuario) |
| `-r`            | Cuenta de sistema (UID menor que `UID_MIN`)                                             |
| `-e YYYY-MM-DD` | Fecha de caducidad de la cuenta (cuentas temporales)                                    |
| `-f días`       | Días tras caducar la contraseña antes de deshabilitar la cuenta (`-1` = nunca)          |
| `-p hash`       | Contraseña ya cifrada. Poco útil salvo en scripts: es mejor usar `passwd`               |

> Paso obligatorio tras **useradd**: Ejecutar **passwd <usuario>** para establecer su contraseña; de lo contrario, la cuenta permanece bloqueada

> **Seguridad**: un intruso suele crear una cuenta con UID 0 (equivale a root). Conviene revisar de vez en cuando `/etc/passwd` buscando UIDs 0 sospechosos.

### Diferencia principal: `useradd` vs `adduser`

- `useradd`: Binario nativo GNU/Linux. Mantiene el mismo comportamiento en todas las distribuciones, pero no crea el directorio HOME por defecto (requiere la opción -m)

- `adduser`: Script en Perl (propio de distribuciones basadas en Debian/Ubuntu). Es un asistente interactivo de más alto nivel que crea el directorio HOME, copia plantillas y pide la contraseña automáticamente

|                   | `useradd`                                           | `adduser`                                         |
| ----------------- | --------------------------------------------------- | ------------------------------------------------- |
| Qué es            | Binario estándar de GNU/Linux                       | Script en Perl de Debian/Ubuntu que usa `useradd` |
| Disponibilidad    | Todas las distribuciones                            | Solo Debian y derivadas                           |
| HOME              | Solo con `-m`                                       | Lo crea siempre                                   |
| Contraseña        | Hay que ejecutar `passwd`                           | La pide de forma interactiva                      |
| Shell por defecto | La de `/etc/default/useradd` (en Ubuntu, `/bin/sh`) | La de `/etc/adduser.conf` (`/bin/bash`)           |

## 5. Comandos Útiles de Consulta

- `id [usuario]`: Muestra el UID, el GID primario y los grupos secundarios de un usuario (o del actual si no se indica ninguno)

```bash
id                 # usuario actual
id root            # uid=0(root) gid=0(root) grupos=0(root)
id -u              # solo el UID
id -g              # solo el GID primario
id -nG             # nombres de todos los grupos
```

- `finger [usuario]`: Muestra información detallada del usuario (incluyendo el campo GECOS)

| Orden                   | Qué muestra                                                                                |
| ----------------------- | ------------------------------------------------------------------------------------------ |
| `id [usuario]`          | UID, GID primario y grupos secundarios                                                     |
| `groups [usuario]`      | Nombres de los grupos del usuario                                                          |
| `whoami`                | Usuario con el que estás trabajando                                                        |
| `who`                   | Usuarios conectados ahora mismo                                                            |
| `getent passwd usuario` | Entrada del usuario (consulta todas las fuentes del sistema, no solo el fichero)           |
| `getent group grupo`    | Entrada del grupo                                                                          |
| `finger usuario`        | Datos del usuario, incluido el campo GECOS (hay que instalarlo: `sudo apt install finger`) |

### Modificar Cuentas: `usermod`

Permite editar parámetros de cuentas ya creadas

- **Sintaxis: `usermod [opciones] nombreusuario`**

**Opciones clave:**

| Opción           | Función                                                                                                                         |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `-l nuevonombre` | Cambia el nombre de usuario                                                                                                     |
| `-d /ruta [-m]`  | Cambia el HOME. Con `-m` mueve también los archivos del antiguo                                                                 |
| `-s /shell`      | Cambia la shell                                                                                                                 |
| `-c "texto"`     | Cambia el campo GECOS                                                                                                           |
| `-g grupo`       | Cambia el grupo primario                                                                                                        |
| `-G g1,g2 [-a]`  | Establece los grupos secundarios (Sin -a, sobrescribe y elimina la lista de grupos previos. Usa siempre -aG para añadir grupos) |
| `-e YYYY-MM-DD`  | Cambia la fecha de caducidad de la cuenta                                                                                       |
| `-L` / `-U`      | Bloquea / desbloquea la cuenta                                                                                                  |
| `-u UID [-o]`    | Cambia el UID                                                                                                                   |

Puntos a tener en cuenta:

- **`-l` solo cambia el nombre de login**. El HOME y el grupo privado conservan el nombre antiguo. Hay que renombrarlos aparte (`usermod -d /home/nuevo -m` y `groupmod -n`).
- **`-u` no cambia los archivos que ya existen**. Hay que corregir la propiedad con `chown -R usuario /home/usuario` y buscar el resto con `find / -uid UIDantiguo`.
- **Los cambios de grupo se aplican al iniciar una sesión nueva**. Una sesión ya abierta conserva los grupos antiguos.

> Buenas prácticas: Antes de modificar un usuario, ejecuta who para comprobar que no esté conectado, ya que alterar la cuenta en uso puede causar fallos de sesión

### Control de Contraseñas: `passwd`

Sin opciones cambia la contraseña. Un usuario normal solo cambia la suya (pide la actual); root puede cambiar la de cualquiera sin conocer la anterior. Las contraseñas no se muestran al teclearlas.

- **Sintaxis: `passwd [opciones] nombreusuario`**

| Opción (requieren root o `sudo`) | Función                                                         |
| -------------------------------- | --------------------------------------------------------------- |
| `-l`                             | Bloquea la cuenta (añade `!` al hash en `/etc/shadow`)          |
| `-u [-f]`                        | Desbloquea. En una cuenta sin contraseña hace falta `-f`        |
| `-d`                             | **Elimina la contraseña** (cuenta sin clave). Úsalo con cuidado |
| `-e`                             | Caduca la contraseña: obliga a cambiarla en el próximo login    |
| `-S`                             | Muestra el estado de la contraseña                              |

**Estado con `passwd -S`:**

| Código | Significado       |
| ------ | ----------------- |
| `P`    | Contraseña válida |
| `L`    | Cuenta bloqueada  |
| `NP`   | Sin contraseña    |

### Expiración y Caducidad: `chage`

Gestiona el envejecimiento de las contraseñas y la caducidad de la cuenta

- **Sintaxis: `chage [opciones] nombreusuario`**
  | Opción | Función |
  |---|---|
  | `-l` | Muestra la información de caducidad |
  | `-m días` | Mínimo de días entre cambios de contraseña (0 = sin límite) |
  | `-M días` | Máximo de días de validez (por defecto 99999, es decir, nunca caduca) |
  | `-W días` | Días de aviso antes de que caduque (por defecto 7) |
  | `-I días` | Días de inactividad tras caducar antes de bloquear la cuenta |
  | `-E YYYY-MM-DD` | Fecha en que la cuenta deja de estar activa (`-1` = nunca) |
  | `-d días` | Fija el día del último cambio de contraseña (`0` = cambiarla en el próximo login) |

### Eliminación de Cuentas: `userdel`

- **Sintaxis: `userdel [-r [-f]] nombreusuario`**

- **Sin opciones**: borra la cuenta pero **conserva su HOME y sus archivos** (quedan con el UID antiguo, lo que puede dar confusión).
- **`-r`**: borra también el HOME y el buzón de correo.
- **`-rf`**: fuerza el borrado del HOME aunque contenga archivos de otros usuarios. También permite borrar una cuenta con sesión abierta, así que hay que usarlo con cuidado.
- `userdel` se niega a borrar un usuario que tenga procesos en ejecución. Comprueba antes con `who` y `pgrep -u usuario`.
- Si el grupo privado del usuario no tiene más miembros, `userdel` lo borra también.
- Los archivos del usuario fuera de su HOME (por ejemplo, en `/tmp`) no se borran con `-r`. Se localizan con `find / -user usuario` o, si la cuenta ya no existe, con `find / -uid ID`.

## 6. Elevación y Cambio de Privilegios: `su` vs `sudo`

### Comando `su` (Switch User)

Cambia la sesión de usuario activa en la terminal sin cerrar sesión

- `su usuario`: Cambia al usuario especificado pero mantiene las variables de entorno y el directorio de trabajo del usuario original. Es decir, no cierra la sesión.

> En Ubuntu la cuenta root está bloqueada, así que `su -` (sin usuario) falla por no tener contraseña. Por eso se usa `sudo -i`.

- `su - usuario`: Cambia al usuario cargando su entorno completo (cambia al directorio **$HOME** del nuevo usuario y ejecuta sus scripts de inicio `.profile/.bashrc`)

### Comando `sudo` (Switch User Do)

Permite ejecutar comandos individuales con privilegios de `root` (o de otro usuario) de forma segura y auditada

- **Ventajas sobre `su`**: No requiere compartir la contraseña de root; cada usuario usa la suya

- **Funcionamiento en Ubuntu**: La cuenta de root está bloqueada por defecto. Las tareas de administración se realizan anteponiendo sudo a las órdenes o abriendo un shell administrativo con sudo `-i`

- **Archivo de configuración (`/etc/sudoers`):**
  - Se debe editar únicamente con el comando `visudo`

  - Permite definir grupos y usuarios con permiso para usar `sudo`

  - Para añadir reglas propias es mejor crear un fichero en `/etc/sudoers.d/` con `sudo visudo -f /etc/sudoers.d/nombre`.

  - **Sintaxis clave:**
    - `root ALL=(ALL:ALL) ALL` → Acceso total ilimitado

    - `%sudo ALL=(ALL:ALL) ALL` → Permite a los miembros del grupo `sudo` ejecutar cualquier comando

    - `%admin ALL=(ALL) ALL` → Permite privilegios de administración al grupo admin

    - Formato de una regla: `quién  dónde=(como_quién:como_grupo)  qué_órdenes`

## 7. Configurando grupos

### 1. Crear Grupos: `groupadd`

- Permite añadir nuevos grupos al sistema (requiere permisos de `root` o `sudo`)
  - **Sintaxis: `groupadd [opciones] nombregrupo`**

- **Opciones principales:**

| Opción   | Función                                                            |
| -------- | ------------------------------------------------------------------ |
| `-g GID` | GID concreto (si se omite, el siguiente libre mayor que `GID_MIN`) |
| `-o`     | (con `-g`) permite repetir un GID existente                        |
| `-r`     | Grupo de sistema (GID menor que `GID_MIN`)                         |

```bash
sudo groupadd proyecto1
```

### 2. Modificar Grupos: `groupmod` y `gpasswd`

Cambiar nombre e ID del grupo: `groupmod`

- **Sintaxis:** `groupmod [opciones] nombregrupo`

- `-n nuevonombre`: Renombra el grupo

- `-g GID [-o]`: Cambia el GID asignado al grupo

> Cambiar el GID **no actualiza** los archivos que ya tenían el GID antiguo (hay que localizarlos con `find -gid` y corregirlos con `chgrp`). Usar `-o` crea una colisión de GIDs y es peligroso.

### Gestionar miembros del grupo: gpasswd vs usermod

Para añadir usuarios a un grupo existen dos opciones en línea de comandos:

**1. Mediante `usermod`:**

- `sudo usermod -aG grp1,grp2 usuario`: Añade (`-a`) al usuario a los grupos secundarios sin borrar su membresía en otros grupos existentes

> Atención: Si se omite el parámetro **-a**, el usuario es eliminado de todos los grupos a los que pertenecía que no estén explícitamente en la lista

**2. Mediante gpasswd (Método recomendado por ser menos propenso a errores):**

| Opción de `gpasswd` | Función                                                                    |
| ------------------- | -------------------------------------------------------------------------- |
| `-a usuario`        | Añade un miembro                                                           |
| `-d usuario`        | Quita un miembro                                                           |
| `-A u1,u2`          | Define los **administradores** del grupo (**sustituye** la lista anterior) |
| `-M u1,u2`          | Define los **miembros** del grupo (**sustituye** la lista anterior)        |
| `-r`                | Elimina la contraseña del grupo                                            |
| `-R`                | Impide el uso de `newgrp` con ese grupo                                    |
| (sin opciones)      | Establece la contraseña del grupo                                          |

**Contraseñas de Grupo** y **newgrp**: Si se ejecuta **gpasswd** sin opciones, permite asignar una clave al grupo. Se usaba históricamente para permitir el acceso mediante **newgrp** a usuarios ajenos. En distribuciones modernas (como Ubuntu) las contraseñas de grupo están prácticamente en desuso y **newgrp** se emplea para cambiar temporalmente el grupo primario activo

### 3. Comprobación de Grupos de un Usuario

- **Comando `groups`**: groups nombre_usuario

- **Comando id**: id nombre_usuario

- **Filtro en `/etc/group`**: cat `/etc/group | grep nombreusuario`

### 4. Eliminar Grupos: `groupdel`

- **Sintaxis: `sudo groupdel nombregrupo`**

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
sudo chage -E 2025-12-15 -m 10 -M 20 alovelace # en este caso el usuario ya se crearía caducado

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

- **Situación de funcionamiento**: Un usuario no podría volver a hacer login en el sistema (o si ya está conectado, no podría crear archivos ni ejecutar subprocesos correctamente)

- **Por qué ocurre esto**: En Unix/Linux, todo usuario requiere obligatoriamente tener un grupo primario asignado. Cada vez que el usuario crea un archivo o proceso, el sistema necesita asociar un GID primario a ese objeto. Si se borrase el grupo primario, el usuario quedaría huérfano de GID primario en `/etc/passwd`, provocando un fallo de autenticación en la rutina de inicio de sesión (`login`)

**10. Averigua, ejecutando una orden, qué UID y GID mínimo y máximo se han definido en Linux Ubuntu (debes usar un pipeline)**

```bash
grep -E '^(UID|GID)_(MIN|MAX)' /etc/login.defs | grep -v '#'
```
