# Autoevaluación de P05: ejercicios de consolidación
Esta sección es para preguntas que se encuentran en : [platea](https://ssoo-uja.gitlab.io/so-uja/practicas/p05/autoevaluacion.html#e1) y que dijo pedro J que era recomendable hacerlas porque iban a caer similares

### **1. Comandos a ejecutar en la máquina.**

 A continuación se muestra el desglose ordenado y separado de los comandos del enunciado para ejecutarlos correctamente en la terminal:

**Bloque 1: Configuración de los repositorios**

```bash
# Crear directorio de trabajo e ir a él
mkdir -p ~/so/p05/ejercicios && cd ~/so/p05/ejercicios

# Listar archivos en /etc/apt/sources.list.d/
ls /etc/apt/sources.list.d/

# Contar líneas que no son comentarios en /etc/apt/sources.list
grep -v '^#' /etc/apt/sources.list | wc -l

# Contar el número de bloques en ubuntu.sources (Ubuntu 24.04+)
grep -c '^Types' /etc/apt/sources.list.d/ubuntu.sources

# Consultar URIs, Suites y Componentes configurados
grep -E '^(URIs|Suites|Components)' /etc/apt/sources.list.d/ubuntu.sources
```

**Bloque 2: Los índices y sus prioridades**
```bash
# Contar el número de índices de paquetes reconocidos por APT
apt-cache policy | grep -c 'Packages$'

# Agrupar y contar índices por su prioridad
apt-cache policy | grep -E '^ +[0-9]+ ' | awk '{print $1}' | sort | uniq -c

# Consultar si hay arquitecturas extranjeras habilitadas
dpkg --print-foreign-architectures
```

**Bloque 3: Dos versiones de `gallery-dl`**
```bash
# Consultar política y versiones disponibles de gallery-dl
apt-cache policy gallery-dl

# Simular la instalación estándar
apt-get -s install gallery-dl | grep '^Inst gallery'

# Simular la instalación desde el repositorio noble-backports
apt-get -s install -t noble-backports gallery-dl | grep '^Inst gallery'

# Consultar prioridades forzando la rama noble-backports
apt-cache policy -t noble-backports gallery-dl

# Comparar si la versión adaptada es menor en la ordenación de dpkg
dpkg --compare-versions 2.0-1~bpo24.04.1 lt 2.0-1 ; echo $?
```
**Bloque 4: Una actualización y un paquete instalado**

```bash
# Consultar política del paquete mc
apt-cache policy mc

# Comparar versiones con época (3:4.8.30-1build2 > 4.8.31-1)
dpkg --compare-versions 3:4.8.30-1build2 gt 4.8.31-1 ; echo $?

# Consultar política del paquete bash (instalado)
apt-cache policy bash
```

### 2. **Respuestas a las Cuestiones**

**Cuestión E1.1: Lee `ubuntu.sources`**
**Número de bloques:** 2

**Líneas del formato antiguo de sources.list que equivalen a los dos bloques:**

```c
deb http://archive.ubuntu.com/ubuntu/ noble main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu/ noble-updates main restricted universe multiverse
deb http://archive.ubuntu.com/ubuntu/ noble-backports main restricted universe multiverse
deb http://security.ubuntu.com/ubuntu/ noble-security main restricted universe multiverse
```
----
**Cuestión E1.2: Contenido de `/etc/apt/sources.list`**

**Líneas que no son comentarios: 0**

> (En Ubuntu 24.04 Noble Numbat, el archivo tradicional /etc/apt/sources.list está vacío o solo contiene comentarios, ya que la configuración utiliza el nuevo formato DEB822 ubicado en /etc/apt/sources.list.d/ubuntu.sources)

---
**Cuestión E1.3: Cuenta los índices de paquetes**
**Índices (líneas que terminan en Packages)**: 12 (varía según los componentes activos, típicamente entre 12 y 16)

**Líneas con prioridad 100 en el recuento por prioridad:** 1 (corresponde al archivo /var/lib/dpkg/status del paquete instalado)

---
**Cuestión E1.4: Las dos versiones de `gallery-dl`**
**Versión que instalaría apt-get -s install gallery-dl:** `1.26.9-1` (o la versión base de noble)

**Versión que instalaría con -t noble-backports:** `2.0-1~bpo24.04.1`

**Prioridad de esa versión con -t noble-backports:** 500 (al usar `-t target`, la prioridad asignada a esa rama pasa a ser 500 o 990 dependiendo de las preferencias del sistema)

---
**Cuestión E1.5: ¿Por qué APT no elige la versión de noble-backports sin `-t`?**
Respuesta correcta:

Porque APT instala primero la versión de mayor prioridad, y solo entre versiones de la misma prioridad elige la más reciente: 500 gana a 100.

(Los repositorios backports tienen por defecto prioridad 100 para evitar que se instalen paquetes no probados exhaustivamente a menos que el usuario lo indique de forma explícita)

---
**Cuestión E1.6: Comparación de versiones en `gallery-dl` y sufijo `~bpo`
Código de terminación de `dpkg --compare-versions 2.0-1~bpo24.04.1 lt 2.0-1` ; `echo $?: 0` (verdadero / éxito)**

**Respuesta correcta:**

Para que la versión adaptada se considere más antigua que la misma versión publicada en la siguiente versión de Ubuntu, que la sustituirá al actualizar el sistema.

(El carácter `~` tiene una prioridad especial en el algoritmo de ordenación de versiones de dpkg: hace que la cadena se ordene antes que la versión sin el sufijo)

---
**Cuestión E1.7: La tabla de versiones de mc
Distribución de la que procede el candidato: noble-updates**

**Respuesta correcta:**

Porque las dos versiones tienen la misma prioridad, 500, y entonces APT elige la de número de versión mayor

---
**Cuestión E1.8: La tabla de versiones de bash (paquete instalado)**

**Respuesta correcta:**

marca la versión instalada, y `/var/lib/dpkg/status`, la base de datos de dpkg, la ofrece con prioridad 100, la que se asigna a la versión ya instalada

---
**Cuestión E1.9: Comparación de versiones y función de la época
Código de terminación de `dpkg --compare-versions 3:4.8.30-1build2 gt 4.8.31-1` ; `echo $?: 0` (verdadero / éxito)

**Respuesta correcta:**

Para que la nueva numeración se considere mayor que la antigua cuando el autor cambia su esquema de versiones y un número nuevo parecería menor.

(La época es el prefijo N: que antecede al número de versión y anula el orden léxico estándar)

## Práctica 5 — Ejercicio 2: Anatomía de un paquete

**1. Comandos a ejecutar en la máquina
A continuación se muestran los bloques de comandos del enunciado desglosados y comentados:**

**Bloque 1: Descargar `mc` sin privilegios**
```C
# Crear directorio de trabajo e ir a él
mkdir -p ~/so/p05/ejercicios/anatomia && cd ~/so/p05/ejercicios/anatomia

# Descargar el paquete deb del repositorio sin instalarlo
apt download mc

# Listar el archivo descargado para observar el nombre en el sistema de archivos
ls *.deb

# Consultar la versión y la ruta en el repositorio según los metadatos de APT
apt-cache show mc | grep -E '^(Version|Filename)'
```

**Bloque 2: Examinar la parte de control sin instalar**
```
# Ver información completa de control del paquete deb
dpkg-deb -I mc_*.deb

# Consultar campos específicos de control (Dependencias y Provisión de funcionalidades)
dpkg-deb -f mc_*.deb Depends
dpkg-deb -f mc_*.deb Provides

# Listar ficheros de configuración declarados
dpkg-deb -I mc_*.deb conffiles

# Consultar la base de datos de dpkg sobre un paquete no instalado pero referenciado (mc)
dpkg -l mc ; echo $?

# Consultar sobre un paquete completamente desconocido para dpkg (lynx)
dpkg -l lynx ; echo $?

# Comprobar la relación de 'Breaks' en un paquete base esencial como findutils
dpkg -s findutils | grep '^Breaks'
```
**Bloque 3: Extraer y probar un paquete independiente de arquitectura (`cowsay`)**

```bash
# Descargar el paquete cowsay
apt download cowsay

# Consultar arquitectura y dependencias directas
dpkg-deb -f cowsay_*.deb Architecture Depends

# Ver rutas específicas instaladas por el paquete
dpkg -c cowsay_*.deb | grep -E 'games/|default'

# Contar cuántos archivos de dibujo (.cow) incluye
dpkg -c cowsay_*.deb | grep -c '\.cow$'

# Extraer el contenido del paquete sin instalarlo en el sistema raíz
mkdir extraido && dpkg-deb -x cowsay_*.deb extraido

# Intentar ejecutar el binario directamente (fallará por no encontrar sus recursos en /usr)
./extraido/usr/games/cowsay Hola ; echo $?

# Ejecutar especificando la ruta de búsqueda de vacas mediante variable de entorno
COWPATH=$PWD/extraido/usr/share/cowsay/cows ./extraido/usr/games/cowsay Hola
```
**Bloque 4: Identificar las partes comprimidas del paquete `.deb`**

```C
# Analizar la estructura interna de los archivos deb descargados (formato ar / compresión)
file mc_*.deb cowsay_*.deb

# Volver al directorio de ejercicios
cd ..
```

### 2. Respuestas a las Cuestiones
**Cuestión E2.1: Descomposición de la versión de mc y sufijo ubuntu0.1. Dada una versión típica como 3:4.8.30-1ubuntu0.1 (o similar en Noble Numbat):**

**Época:** 3

**Versión del autor del programa:** `4.8.30`

**Revisión de Debian:** `1ubuntu0.1`

**Respuesta correcta:**

Que Ubuntu ha modificado el paquete después de publicar la versión, como primera corrección sobre una revisión ubuntu0

---
**Cuestión E2.2: Comparación del nombre descargado con Filename. Carácter que representa %3a en el nombre del fichero descargado: : (los dos puntos de la época se codifican como %3a en las URLs del campo Filename de los repositorios)**

¿Aparece la época en el campo Filename del repositorio?: No (la época no forma parte del nombre del archivo .deb en los servidores del repositorio)

Arquitectura del fichero de mc: amd64 (o arm64 dependiendo de la plataforma de la VM)

----
**Cuestión E2.3: Parte de control de mc y dependencia exacta de mc-data**

**Guiones del responsable que contiene (marcados con *)**: postinst, postrm, prerm (o según indique `dpkg-deb -I`, habitualmente postinst y postrm)

**Ficheros de configuración que declara**: `/etc/mc/mc.ext` (y/o los enumerados en conffiles, p. ej. `/etc/mc/mc.menu`, `/etc/mc/ini`)

**Respuesta correcta:**

Porque los dos paquetes se construyen a partir del mismo código fuente y deben corresponder a la misma versión: los datos de una versión no sirven a otra

---
**Cuestión E2.4: dpkg -l sobre paquetes no instalados y conocimiento de mc**

**Dos primeros caracteres de la línea de mc: un (uninstalled / no select)**

**Código de terminación de dpkg -l lynx: 1 (falla porque no existe ninguna mención en la base de datos)**

**Respuesta correcta:**

Porque findutils, que está instalado, nombra a mc en su campo Breaks, y dpkg conserva una entrada para cada paquete que aparece en las relaciones de los instalados

---
**Cuestión E2.5: El paquete cowsay
Arquitectura: all (indica paquete independiente de la arquitectura)**

Código de terminación de `./extraido/usr/games/cowsay` Hola: 2 (o 1, devuelve error por no encontrar los archivos `.cow` en `/usr/share/cowsay/cows`)

¿Funciona con COWPATH?: Sí (al definir COWPATH apuntando al directorio extraído encuentra las plantillas de dibujos)

---
**Cuestión E2.6: Extraer un paquete no es instalarlo**
**Respuesta modelo:**

**Falla porque las rutas dentro del código de cowsay están prefijadas para buscar los datos en /usr/share/cowsay/cows. Al extraerlo en un directorio local, los ficheros no están en esa ruta global**

**Una instalación completa:**

1. Copia los ficheros en sus ubicaciones definitivas del sistema (`/usr/bin`, `/usr/share`, `etc.`)

2. Ejecuta los guiones de control del responsable (postinst, preinst)

3. Registra el paquete y sus ficheros en la base de datos de dpkg (`/var/lib/dpkg/status` e info)

4. Resuelve y verifica las dependencias con otros paquetes


**Cuestión E2.7: La salida de file y el contenido de un `.deb`. Compresión de las dos partes de mc: control.tar.zst (o .xz) y data.tar.zst (o .xz)**

**Compresión de las dos partes de cowsay: control.tar.zst (o .xz) y data.tar.zst (o .xz).**

**Respuesta correcta:**

`dpkg-deb -I` muestra la parte de control y `dpkg -c`, la de datos

---
**Cuestión E2.8: El campo Provides de mc
Nombre que proporciona: `mcedit`**

**Respuesta correcta:**

Que `mc` se puede instalar con el nombre `mcedit` aunque no exista ningún paquete así.

---
**Cuestión E2.9: Los dibujos de cowsay
Ficheros `.cow` que contiene el paquete: 46 (varía entre 40 y 50 según la versión)**

Propietario y grupo que tendrán los ficheros al instalarse: `root` / `root`

---
### Práctica 5 — Ejercicio 3: Consultar lo instalado

**1. Comandos a ejecutar en la máquina
A continuación se muestran los bloques de comandos del ejercicio con su propósito desglosado:**

**Bloque 1: Estados y recuentos de paquetes**
```bash
# Consultar la cabecera / leyenda del formato de dpkg -l
dpkg -l | head -3

# Contar paquetes instalados correctamente (estado ii) según dpkg
dpkg -l | grep -c '^ii'

# Contar paquetes instalados según la interfaz de APT (incluye cabecera)
apt list --installed 2>/dev/null | wc -l

# Contar paquetes marcados como automáticos desde apt list
apt list --installed 2>/dev/null | grep -c 'automático'

# Contar paquetes marcados explícitamente como automáticos (dependencias)
apt-mark showauto | wc -l

# Contar paquetes instalados de forma manual
apt-mark showmanual | wc -l
```

**Bloque 2: ¿De qué paquete es cada fichero?**
```bash
# Buscar el fichero tar con ruta absoluta consolidada y tradicional
dpkg -S /usr/bin/tar ; dpkg -S /bin/tar ; echo $?

# Buscar patron sin barra inicial
dpkg -S bin/tar

# Comprobar si /bin es un enlace simbólico a usr/bin (usrmerge)
ls -ld /bin

# Buscar paquete propietario de la alternativa awk
dpkg -S /usr/bin/awk

# Averiguar el destino real de la cadena de enlaces simbólicos de awk
readlink -f /usr/bin/awk

# Buscar el paquete propietario del binario real resuelto por readlink
dpkg -S "$(readlink -f /usr/bin/awk)"

# Consultar paquetes propietarios de ficheros de configuración del sistema
dpkg -S /etc/os-release /etc/passwd
```

**Bloque 3: Comparación entre bases de datos de dpkg y APT**
```bash
# Consultar campos de control de un paquete esencial instalado (tar)
dpkg -s tar | grep -E '^(Status|Priority|Essential)'

# Intentar consultar la información disponible en dpkg para un paquete (falla si /var/lib/dpkg/available no se actualiza)
dpkg -p nano ; echo $?

# Consultar el estado y versión en la base de datos local de estado (/var/lib/dpkg/status)
dpkg -s nano | grep -E '^(Status|Version)'

# Consultar un paquete que no está instalado en la base de datos de dpkg (devuelve error)
dpkg -s lynx ; echo $?

# Consultar metadatos del paquete desde los índices de APT (/var/lib/apt/lists)
apt show lynx 2>/dev/null | grep -E '^(Version|Section|APT-Sources)'
```

### 2. Respuestas a las Cuestiones
**Cuestión E3.1: La leyenda de dpkg -l
Letra de la columna «Estado» para un paquete del que solo quedan los ficheros de configuración:** `c (rc)`

**Respuesta correcta:**

Que el estado es anómalo: el paquete necesita atención («Estado,Err: mayúsc.=malo»)

---
**Cuestión E3.2: Los recuentos de paquetes instalados**

**Diferencia entre apt list --installed ... | wc -l y dpkg -l | grep -c '^ii': 1 (debido a la línea de cabecera Listing... que imprime apt list)**

**¿Coinciden los paquetes marcados «automático» en apt list con `apt-mark` showauto?**: Sí

**¿Suman showauto y showmanual el número de paquetes `ii`?**: Sí
---
**Cuestión E3.3: `/usr/bin/tar` y `/bin/tar`
Código de terminación de `dpkg -S /bin/tar`: 1 (falla / no encontrado)**

**Respuesta correcta:**

Porque dpkg -S busca la ruta tal como figura en la lista de ficheros del paquete, /usr/bin/tar, y /bin es un enlace simbólico a usr/bin que dpkg no sigue

---
**Cuestión E3.4: `/usr/bin/awk`
Lo que escribe `readlink -f /usr/bin/awk`: `/usr/bin/mawk` (o /usr/bin/gawk)**

**Paquete al que pertenece: mawk (o gawk)**

**Respuesta correcta:**

Porque el enlace no viene en ningún paquete: lo crea update-alternatives desde el guion de instalación de mawk, y dpkg solo registra los ficheros que contiene el paquete

---
**Cuestión E3.5: `dpkg -S /etc/os-release /etc/passwd`**

**Paquete al que pertenece `/etc/os-release`: base-files**

**Respuesta correcta:**

Porque `/etc/passwd` contiene datos de cada sistema —las cuentas creadas al instalarlo y después—: se genera durante la instalación, y si un paquete lo contuviera, actualizarlo lo sobrescribiría

---
**Cuestión E3.6: Campos de tar en la base de datos de estado**

**Valor del campo Essential:** yes

**Valor del campo Priority:** required

---
**Cuestión E3.7: `dpkg -p nano` frente a `dpkg -s nano`. Código de terminación de `dpkg -p` nano: 1 (error)**

**Respuesta correcta:**

`-p` lee `/var/lib/dpkg/available`, que APT no mantiene, y `-s`, `/var/lib/dpkg/status`, el estado de lo instalado

---
**Cuestión E3.8: lynx, que no está instalado
Código de terminación de dpkg -s lynx: 1 (error, paquete no instalado / no encontrado)**

**Respuesta correcta:**

Porque apt show lee las listas de los repositorios (`/var/lib/apt/lists`), que describen todos los paquetes disponibles, y `dpkg -s` solo la base de datos de lo instalado

---
**Cuestión E3.9: `dpkg -S bin/tar`, sin la barra inicial Líneas que escribe: 2 (o más, según los binarios coincidentes como tar y tarcat)**

**Respuesta correcta:**

Porque un argumento que no empieza por / se interpreta como un patrón, y /usr/sbin/tarcat contiene la cadena bin/tar.