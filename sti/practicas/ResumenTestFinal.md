## Apuntes de Prácticas de Seguridad

**Aviso**: Esto es un resumen general de los guiones con lo que se puede considerar lo más relevante, es decir, en est resumen **NO** está todo. Se recomiendo leer también los guiones para ampliar un poco más y, al menos, conocer que más hay en esos guiones.

[Guiones explicados](https://github.com/valentinVilla05/Guias-Basicas/tree/master/sti/practicas/ExplicacionesPracticas)

### 1. Fuentes de información y estándares de vulnerabilidades

- **Listas de divulgación (SecLists.org)**:
  - **Full Disclosure**: Lista activa donde se publican abiertamente detalles técnicos de vulnerabilidades.
  - **Bugtraq**: Lista histórica de divulgación creada en 1993 (su archivo en SecLists llega hasta 2021 y fue relanzada posteriormente en securityfocus.com bajo gestión comunitaria).
  - **Open Source Security (oss-security)**: Lista enfocada en fallos de seguridad en software libre y Linux.

- **Catálogos, bases de datos y organismos**:
  - **CVE (Common Vulnerabilities and Exposures)**: Catálogo oficial de identificadores únicos de vulnerabilidades gestionado por MITRE.
  - **NVD (National Vulnerability Database)**: Base de datos del NIST que amplía cada CVE con su puntuación de gravedad CVSS (una métrica estandarizada donde un valor de 7.0 o superior indica severidad Alta o Crítica, calculada a partir de un vector de ataque e impacto), el tipo de debilidad (CWE, clasificación del error de diseño o programación) y los productos o versiones afectados (CPE).
  - **EUVD (European Vulnerability Database)**: Base de datos europea gestionada por ENISA (creada en 2025 bajo la Directiva NIS2) que aporta información sobre mitigaciones y estado de explotación.
  - **Catálogo KEV (Known Exploited Vulnerabilities)**: Registro de la agencia estadounidense CISA que reúne vulnerabilidades con constancia de explotación activa en entornos reales.
  - **INCIBE-CERT**: Organismo español que ofrece avisos de seguridad y una base de datos de vulnerabilidades en castellano.
  - **CCE (Common Configuration Enumeration)**: Estándar de identificadores para configuraciones inseguras en sistemas.
  - **Exploit Database**: Archivo público de exploits y pruebas de concepto (PoC), indexados por su identificador CVE.

---

### 2. Criptografía Asimétrica e Infraestructura PKI con OpenPGP y GnuPG

- **2.1. Estándar OpenPGP y la Herramienta GnuPG**:
  - Desarrollado originalmente por Phil Zimmermann en la década de 1990 bajo el nombre PGP (_Pretty Good Privacy_), el protocolo evolucionó hasta convertirse en un estándar abierto documentado en la **RFC 9580 (OpenPGP)**.
  - **GnuPG (GPG)** representa la implementación libre estándar en sistemas Linux.
  - PGP/GnuPG combina criptografía simétrica, asimétrica y funciones hash, gestionando las claves en archivos llamados anillos (_keyrings_).

- **2.2. Generación, Formatos e Identificadores de Claves**:
  - El comando `gpg --full-gen-key` permite configurar el par de claves.
  - **Certificado de Revocación**: Al generar el par de claves, GnuPG crea automáticamente un archivo de revocación en `~/.gnupg/openpgp-revocs.d/`. Este certificado permite invalidar la clave pública en los servidores si la clave privada se compromete o se olvida la frase de paso (_passphrase_).
  - **Identificadores**:
    - **Huella Dactilar (_Fingerprint_)**: Cadena de 40 caracteres hexadecimales que identifica la clave de manera unívoca.
    - **Identificador Largo**: Formado por los últimos 16 caracteres hexadecimales de la huella dactilar (ejemplo del profesor: `97404C7A6627F766`).
    - **Identificador Corto**: Los últimos 8 caracteres hexadecimales. Su uso está explícitamente desaconsejado por la facilidad computacional de generar claves falsas colisionantes.

- **2.3. Resumen de Operaciones Principales en GnuPG**:

| Operación                         | Comando GnuPG                                                        | Descripción / Observaciones                                                            |
| --------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Comprobación de instalación       | `gpg --version`                                                      | Muestra versión y algoritmos soportados (simétricos, asimétricos, hashes, compresión). |
| Generación completa               | `gpg --full-gen-key`                                                 | Solicita algoritmo (ECC/RSA), validez (ej. 2y), UID (nombre, correo) y _passphrase_.   |
| Listar claves públicas            | `gpg --list-keys`                                                    | Consulta el anillo público local.                                                      |
| Listar claves privadas            | `gpg --list-secret-keys`                                             | Consulta el anillo de claves secretas local.                                           |
| Exportar clave pública ASCII      | `gpg -a --export <id>`                                               | Genera bloque de texto armado ASCII (_Armor_).                                         |
| Exportar clave privada ASCII      | `gpg -a -o priv.asc --export-secret-keys <id>`                       | Exporta la clave secreta solicitando la frase de paso.                                 |
| Importar clave                    | `gpg --import <archivo>`                                             | Incorpora claves externas al anillo.                                                   |
| Servidor de claves (Envío)        | `gpg --keyserver hkps://keyserver.ubuntu.com --send-keys <huella>`   | Publica la clave pública en el servidor remoto.                                        |
| Servidor de claves (Búsqueda)     | `gpg --keyserver hkps://keyserver.ubuntu.com --search-keys <patrón>` | Localiza claves por nombre o correo en el servidor.                                    |
| Servidor de claves (Descarga)     | `gpg --keyserver hkps://keyserver.ubuntu.com --recv-keys <huella>`   | Descarga una clave específica por huella.                                              |
| Actualizar anillo                 | `gpg --keyserver hkps://keyserver.ubuntu.com --refresh-keys`         | Descarga nuevas firmas para las claves existentes. No sube firmas locales.             |
| Cifrar archivo binario            | `gpg -e -r <destinatario> <fichero>`                                 | Cifrado asimétrico destinado al receptor indicado.                                     |
| Cifrar texto ASCII                | `gpg -ea -r <destinatario> <fichero>`                                | Genera salida formateada en `.asc`.                                                    |
| Descifrar archivo                 | `gpg -d <fichero_cifrado>`                                           | Descifra usando la clave privada y solicitando la clave de paso.                       |
| Firma binaria combinada           | `gpg -s <fichero>`                                                   | Integra el contenido original y la firma digital.                                      |
| Firma separada (_Detached_)       | `gpg -b <fichero>`                                                   | Genera un archivo `.sig` independiente manteniendo el original intacto.                |
| Firma en modo texto               | `gpg --clear-sign <fichero>`                                         | Añade el bloque de firma legible al documento de texto (_clearsign_).                  |
| Verificar firma                   | `gpg --verify <fichero>`                                             | Comprueba la integridad del archivo y la validez del firmante.                         |
| Firmar clave pública (Local)      | `gpg --lsign-key <id>`                                               | Marca la clave como válida únicamente en el equipo local sin exportar la firma.        |
| Firmar clave pública (Exportable) | `gpg --sign-key <id>`                                                | Certifica la autenticidad de la clave ajena tras verificar físicamente su huella.      |
| Eliminación total                 | `gpg --delete-secret-and-public-key <huella>`                        | Borra definitivamente la clave secreta y pública del anillo local.                     |

---

### 3. Criptografía Clásica y Máquinas de Cifrado Históricas

- **3.1. Algoritmos de Sustitución y Transposición**:
  - Las herramientas _criptoclasicos v2.1_ y _CrypTool_ integran modelos teóricos y prácticos de la criptografía previa a la era computacional moderna.
  - **Sustitución**:
    - **Monoalfabética**: Desplazamiento puro (César), Decimación pura, Adición y Afín.
    - **Polialfabética**: Gronsfeld, Vigenère, Beaufort, Variante de Beaufort, Clave continua.
    - **Poligráfica**: Hill (matricial), Playfair.
  - **Transposición (Permutación)**: Transposición por filas (con/sin clave), columnas (con/sin clave), vallas (_rail fence_), por series, por escítala y Cifra de Vernam binario.
  - **Cuerpos de Cifra (Alfabéticos)**:
    - Inglés Mayúsculas ($\text{mod } 26$).
    - Inglés Mayúsculas y Dígitos ($\text{mod } 36$).
    - Castellano Mayúsculas ($\text{mod } 27$, incluye la Ñ).
    - Castellano Mayúsculas y Dígitos ($\text{mod } 37$).
    - Subconjunto ASCII Imprimible ($\text{mod } 191$).

- **3.2. Criptoanálisis del Cifrado Vigenère: El Ataque de Kasiski**:
  - El cifrado Vigenère aplica desplazamientos variables basados en una palabra clave repetida. Su vulnerabilidad fundamental reside en la repetición periódica de la clave sobre el texto plano.
  - **Funcionamiento del Test de Kasiski**:
    - **Localización de Patrones**: Se buscan cadenas de caracteres idénticas (trigramas o n-gramas) repetidas en el criptograma.
    - **Cálculo de Distancias**: Se mide la cantidad de caracteres que separan la posición inicial de cada repetición.
    - **Máximo Común Divisor (MCD)**: Se calcula el MCD de todas las distancias obtenidas. El valor del MCD coincide o es un múltiplo de la longitud de la clave.
  - **Nota sobre caracteres especiales y números**: Si el texto original contiene dígitos (como el número 600) y el algoritmo se ejecuta bajo un alfabeto estricto de letras ($\text{mod } 26$ o $\text{mod } 27$), dichos elementos no alfabéticos son omitidos o alterados durante el cifrado. Al procesar el texto bajo el cuerpo ASCII 191, los números y símbolos se incluyen en el módulo aritmético de desplazamiento, modificando completamente la salida cifrada y preservando la totalidad de los datos.

---

### 4. La Máquina Enigma

- **Historia**: Patentada en 1918 por la empresa Scherbius y Ritter (cofundada por Arthur Scherbius a partir de una patente neerlandesa), la máquina Enigma se comercializó en 1923 y fue adoptada por la Armada Alemana en 1926, extendiéndose su uso a todas las fuerzas armadas alemanas antes y durante la Segunda Guerra Mundial.

- **Componentes Mecánicos y Configuración**:
  - **Rotores**: Discos giratorios con cableado interno que realizan sustituciones monoalfabéticas cambiantes con cada pulsación de tecla.
  - **Ring Settings**: Configuración del anillo de graduación de los rotores.
  - **Reflector (UKW - _Umkehrwalze_, ej. UKW-B)**: Desvía la corriente eléctrica de vuelta a través de los rotores por un camino alternativo.
  - **Clavijero (_Plugboard_ / _Steckerbrett_)**: Permite intercambiar parejas de letras mediante cables (típicamente 10 pares conectados), añadiendo una capa masiva de permutación antes y después del paso por los rotores.

- **Propiedad de Reciprocidad**:
  - La presencia del reflector impide matemáticamente que una letra se cifre como sí misma.
  - Asimismo, otorga a la máquina un comportamiento estrictamente recíproco: si una máquina ajustada con una configuración determinada $C$ transforma el carácter A en el carácter Z, introducir Z en otra máquina con la misma configuración $C$ devolverá de forma automática el carácter original A.

---

### 5. Cifrado Simétrico Moderno y Funciones Hash

- **5.1. Cifrado Simétrico: Advanced Encryption Standard (AES)**:
  - Basado en el algoritmo Rijndael, AES opera sobre bloques de datos de 128 bits utilizando claves de 128, 192 o 256 bits. Opera iterativamente sobre una matriz de $4 \times 4$ bytes denominada el **Estado** (_State_).
  - **Módulos Internos de AES**:
    - **SubBytes**: Sustitución no lineal individual de cada byte del estado empleando la Caja-S (_S-Box_) de Rijndael, derivada de operaciones matemáticas sobre el Campo de Galois $GF(2^8)$.
    - **ShiftRows**: Desplazamiento circular hacia la izquierda en las filas de la matriz del estado: la fila 0 no se desplaza, la fila 1 rota 1 byte, la fila 2 rota 2 bytes y la fila 3 rota 3 bytes.
    - **AddRoundKey**: Operación binaria XOR byte a byte entre el estado actual y la subclave de ronda correspondiente, obtenida mediante el algoritmo de expansión de claves de Rijndael.
    - **MixColumns**: Transformación lineal de alta complejidad donde cada columna del estado se trata como un polinomio y se multiplica por una matriz fija sobre el campo $GF(2^8)$. Otorga difusión cruzando los bytes de una misma columna.
  - **Modo ECB (Electronic Codebook)**: En el modo ECB, cada bloque de texto plano se cifra de forma independiente con la misma clave. Si el texto plano contiene patrones repetidos, los bloques cifrados resultantes serán idénticos, revelando la estructura subyacente del archivo y comprometiendo la confidencialidad.

- **5.2. Obsolescencia de MD5 y SHA-1**:
  - Las funciones hash son algoritmos deterministas unidireccionales sin clave. Se consideran obsoletas e inseguras debido al descubrimiento de colisiones prácticas (dos entradas distintas que producen el mismo hash):
    - **MD5**: Primeras colisiones prácticas demostradas en 2004. Demostración con binarios colisionantes ejecutables distintos (ejemplos: `hello` y `erase`).
    - **SHA-1**: Ataque **SHAttered** publicado en 2017, produciendo dos documentos PDF funcionalmente distintos (`shattered-1.pdf` y `shattered-2.pdf`) que generan exactamente el mismo hash SHA-1.

- **5.3. Funciones Hash Actuales: SHA-2 y SHA-3**:
  - **Estructura Estándar SHA-256 vs. SHA-3-256**
  - **Efecto Avalancha e Impacto de la Codificación**:
    - **Efecto Avalancha**: Propiedad deseable según la cual la modificación de un único bit en el mensaje plano de entrada provoca una variación drástica e impredecible en aproximadamente el 50% de los bits del resumen resultante.
    - **Codificación (UTF-8 vs. Latin-1)**: Las funciones hash procesan cadenas de bytes primarias. Caracteres acentuados (como la 'ó') se representan mediante un solo byte en Latin-1 (`0xF3`) y mediante dos bytes en UTF-8 (`0xC3 0xB3`). Por consiguiente, la misma frase generará resúmenes SHA-256 completamente inconexos si cambia la codificación del archivo de texto.

---

### 6. Ingeniería Inversa de Binarios Ejecutables

- **6.1. Análisis Estático y Dinámico con OllyDbg**:
  - La ingeniería inversa analiza el comportamiento interno de programas ejecutables compilar sin disponer del código fuente original.
  - **OllyDbg** es un depurador/desensamblador de nivel de código máquina de 32 bits para ejecutables de Windows.

- **6.2. Metodología de Análisis de Código Máquina**:
  - **Identificación de Cadenas**: Se escanean las referencias de texto (_Search for all referenced strings_) para aislar mensajes de error, nombres de usuario de prueba (ej. "Robin Banks") o avisos de licencias (_nag-screens_).
  - **Seguimiento del Flujo de Control**: Se localiza la llamada de comparación de cadenas de la API de Windows, típicamente `KERNEL32.lstrcmp`.
  - **Comprobación de Banderas**: Posterior a la comparación, la instrucción `OR EAX, EAX` evalúa el resultado devuelto por la función (donde `EAX = 0` indica igualdad).
  - **Bifurcación Condicional**: La instrucción `JNE SHORT...` (_Jump if Not Equal_) desvía el flujo del programa hacia la rutina de autenticación fallida cuando las credenciales no coinciden.
  - **Parcheo (_Patching_) de Código**: Reemplazando la instrucción de salto condicional `JNE` por instrucciones `NOP` (_No Operation_, opcode `0x90`), el salto se inactiva por completo, forzando al programa a continuar hacia la rutina de acceso concedido independientemente de los datos introducidos.

---

### 7. Seguridad de Contraseñas y Generación de Números Pseudoaleatorios

- **7.1. Generación de Números Pseudoaleatorios (PRNG vs. CSPRNG)**:
  - **Generadores Deterministas (PRNG)**: Basados en relaciones de recurrencia deterministas partiendo de una semilla ($x_0$).
    - **Generador Congruencial Lineal (LCG)**: Definido por la fórmula: $x_{n+1} = (a \cdot x_n + c) \bmod m$
      - **Parámetros Degenerados**: Si $a=0$, la secuencia se vuelve constante ($c \bmod m$). Si $a=1$, se convierte en un contador lineal.
      - **Ciclo**: Cantidad de valores únicos generados antes de que la secuencia empiece a repetirse. Un ciclo corto permite predecir los números futuros.
    - **Función `rand()` en C**: Sembrada habitualmente mediante `srand(semilla)`. Si se utiliza la hora del sistema (`time(NULL)`) como semilla, la secuencia es completamente reproducible por un atacante que conozca la ventana temporal aproximada de ejecución.
    - **Uso adecuado**: Videojuegos, simulaciones científicas, depuración. Completamente inadecuados para seguridad.
  - **Generadores Criptográficamente Seguros (CSPRNG)**: Diseñados de forma que, aun conociendo parte de la secuencia de salida, resulte imposible computacionalmente predecir los bits siguientes o reconstruir el estado interno.
    - **Pool de Entropía del Sistema Operativo**: Alimentado por eventos físicos impredecibles del equipo (temporización de pulsaciones de teclado, interrupciones de disco, tráfico de red).
    - En Linux, se accede mediante la llamada al sistema `getrandom()`, el dispositivo `/dev/urandom` (equivalente en los núcleos modernos a `/dev/random`) o la utilidad `openssl rand`.

- **7.2. Almacenamiento de Contraseñas y Sales Criptográficas**:
  - Las contraseñas nunca deben almacenarse en claro. La protección reside en guardar el hash del valor. Sin embargo, los hashes sin sal son vulnerables a **Tablas Arcoíris** (_Rainbow Tables_), que almacenan hashes precalculados de millones de contraseñas comerciales.
  - **Función de la Sal (_Salt_)**: Una sal es una cadena de bytes aleatoria generada al crear la cuenta que se concatena con la contraseña antes de aplicar la función hash: $\text{hash}(\text{sal} + \text{contraseña})$.
    - **Propósito**: Garantizar que el hash almacenado sea único para cada usuario, incluso si dos usuarios eligen exactamente la misma contraseña. Esto obliga al atacante a recalcular el ataque de fuerza bruta usuario por usuario, anulando el uso de tablas precalculadas.
    - **Visibilidad**: La sal no es secreta; se almacena en texto claro en la base de datos junto con el hash.

- **7.3. Evolución del Almacenamiento de Contraseñas (De V1 a V5)**:
  - **Vector 1 (V1): MD5 sin sal**: Vulnerable a ataques directos de diccionario y tablas arcoíris debido a la ausencia de sal y a la extrema velocidad del algoritmo.
  - **Vector 2 (V2): SHA-256 sin sal**: SHA-256 es seguro frente a colisiones pero inadecuado para almacenar contraseñas. Su alta velocidad computacional permite realizar miles de millones de intentos por segundo mediante herramientas como Hashcat.
  - **Vector 3 (V3): Sal predecible**: Si la sal se genera mediante un PRNG inseguro sembrado con la hora (`srand(time(NULL))`), un atacante que conozca la hora aproximada de creación de la cuenta puede calcular en pocos segundos todas las semillas posibles en ese rango horario, reconstruyendo la sal exacta y anulando la protección.
  - **Vector 4 (V4): Sal Criptográficamente Segura**: Generada mediante un CSPRNG (ej. `openssl rand -hex 16`). Impide la reconstrucción de la sal. No obstante, si el hash subyacente sigue siendo un algoritmo rápido (SHA-256), los ataques de diccionario por fuerza bruta individualizados siguen siendo factibles.
  - **Vector 5 (V5): Algoritmos Lentos Diseñados para Contraseñas**: Se emplean funciones de derivación de clave lentas e iterativas, parametrizables en tiempo (iteraciones), memoria y paralelismo:
    - **bcrypt**: Requiere coste mínimo de rondas recomendado por OWASP de 10 (ejemplo: `--rounds=12` vía `mkpasswd`).
    - **Argon2id**: Ganador de la _Password Hashing Competition_. Parámetros de referencia OWASP: `-t 2` (iteraciones), `-m 16` (memoria en KiB, $2^{16} = 64\text{ MiB}$), `-p 1` (paralelismo).
    - **yescrypt**: Algoritmo predeterminado utilizado en el archivo `/etc/shadow` en distribuciones modernas como Debian/Kali Linux.
  - **Incompatibilidad Fundamental de Diseño**: Una función hash de integridad (SHA-256) exige ser lo más rápida posible para procesar archivos grandes eficientemente. Por el contrario, una función de derivación de contraseñas (bcrypt/Argon2id) requiere ser computacionalmente costosa y lenta para penalizar los intentos masivos de fuerza bruta. Ambas propiedades son conceptualmente incompatibles en un mismo algoritmo.

- **7.4. Auditorías de Contraseñas con Hashcat**:
  - **Modos de Hash y Estructuras de Ataque**:
    - **Modos de Algoritmo (`-m`)**:
      - `-m 0`: MD5.
      - `-m 1400`: SHA-256.
      - `-m 3200`: bcrypt.
    - **Modos de Ataque (`-a`)**:
      - `-a 0`: Ataque de Diccionario Directo.
      - `-a 3`: Ataque de Máscara (fuerza bruta estructurada según patrones).
      - `-a 1`: Ataque Combinador (combina palabras de dos diccionarios).
    - **Reglas de Transformación (`-r`)**: Permiten modificar dinámicamente palabras de un diccionario (ejemplo: la regla `best64.rule` añade dígitos o altera mayúsculas, permitiendo romper credenciales como `Password1` partiendo del término básico `Password`).

- **7.5. Selección Segura, Entropía y Estándares NIST**:
  - **Metodología Diceware**: Generación de contraseñas aleatorias seleccionando palabras de listas predefinidas mediante tiradas de dados:
    - **Listas de Referencia**: Lista de 7776 palabras en español (Manuel Palao) o lista larga oficial de la EFF (inglés).
    - **Entropía**: Cada palabra extraída de una lista de 7776 términos aporta $\log_2(7776) \approx 12,92$ bits de entropía.
    - **Cálculo de Entropía Objetivo**: Para superar los 70 bits de entropía recomendados, se requiere un mínimo de 6 palabras: $6 \times \log_2(7776) \approx 6 \times 12,92 = 77,54 \text{ bits}$
  - **Verificación de Filtraciones e API k-Anonymity**: La plataforma _Have I Been Pwned_ permite comprobar si una credencial ha sido filtrada sin comprometer la contraseña original:
    - Se calcula el hash SHA-1 de la contraseña.
    - Se extraen los 5 primeros caracteres del hash hexadecimal (Prefijo).
    - Se envía el prefijo a la API (`https://api.pwnedpasswords.com/range/$PREFIX`).
    - El servidor devuelve la lista de sufijos coincidentes observados en filtraciones reales, permitiendo la verificación local en el cliente de forma anónima.
  - **Pautas Actualizadas del NIST (SP 800-63B)**:
    - **Longitud Mínima**: Prioriza la longitud (mínimo de 8 a 64 caracteres) por encima de la complejidad sintáctica.
    - **Reglas de Composición**: Desaconseja la imposición forzada de reglas de composición complejas (combinación obligatoria de mayúsculas, símbolos y números), dado que inducen a patrones predecibles en los usuarios.
    - **Rotación de Contraseñas**: Elimina la exigencia de cambios periódicos forzados de contraseña a menos que exista evidencia explícita de un compromiso de seguridad.

---

### 8. Sistemas de Detección de Intrusiones (IDS)

- **Finalidad**: Permiten saber si se ha producido (o se está produciendo) una intrusión en un sistema informático.

- **Funcionamiento**: Analizan distintas fuentes de información (archivos de registro, configuración del sistema, tráfico de red, etc.) y, mediante un mecanismo de decisión usualmente basado en reglas, avisan si detectan alguna anomalía.

- **8.1. Detección basada en archivos de registro: Fail2ban**:
  - **Método de detección**: Supervisa archivos de registro del sistema operativo (como `/var/log/auth.log`, que en Linux registra las entradas al sistema e intentos de login por ssh) y detecta actividades sospechosas mediante expresiones regulares.
  - **Acciones contra intrusos**: Aplica medidas sobre las IP sospechosas, como su inclusión en el fichero `/etc/hosts.deny` o su bloqueo en el cortafuegos (mediante `nftables`).
  - **Ficheros de configuración**:
    - **`jail.conf`**: Mecanismo configurable donde se definen los filtros (_jails_) y se especifica por cuánto tiempo se aplicará la acción correspondiente sobre una IP tras detectarse un comportamiento anómalo. Por convención no se modifica para evitar que se sobrescriba al actualizar el paquete.
    - **`jail.local`**: Se lee después de `jail.conf` y sus valores prevalecen sobre este. Aquí se escriben los cambios propios y se activan los filtros mediante la directiva `enabled = true` (por ejemplo, en la sección `[sshd]`).
    - **Otros ficheros y rutas**: Los filtros se ubican en `/etc/fail2ban/filter.d` (ej. `sshd.conf`), las acciones en `/etc/fail2ban/action.d/`, la configuración general en `/etc/fail2ban/fail2ban.conf` y el registro de actividad del servicio en `/var/log/fail2ban.log`.
  - **Comandos de consulta y gestión**:
    - `sudo fail2ban-client status`: Permite ver qué filtros (_jails_) están activos y configurarlos.
    - `sudo fail2ban-client status sshd`: Muestra información relativa al estado del filtro SSH (el nombre del filtro es `sshd`, no `ssh`).

- **8.2. Comprobación de la integridad de ficheros ejecutables**:
  - **Generación de firmas de referencia**: En UNIX se calculan las sumas criptográficas de los ejecutables y se guardan en un archivo: `find /usr/bin/ -type f -exec sha256sum {} \; > fichero.txt`
  - **Detección de anomalías**: Ejecutar periódicamente `sha256sum -c fichero.txt` compara los archivos actuales con el registro guardado y emite una advertencia si alguno ha sido alterado (la opción `-c` es la que permite detectar las anomalías).

- **8.3. Detección basada en la integridad del sistema: Rootkit Hunter**:
  - **Tipo de detección**: Se basa en la integridad del sistema (no en archivos de registro ni en el tráfico de red).
  - **Funcionamiento**: Mantiene una base de datos de posibles indicios de la presencia de algunos de los rootkits más comunes en un sistema UNIX.
  - **Ejecución y registro**: Se lanza con `sudo rkhunter --check` (añadiendo `--sk` no se detiene entre pruebas) y guarda el registro completo en `/var/log/rkhunter.log`.

- **8.4. Detección basada en el tráfico de red: Suricata**:
  - **Tipo de detección**: Monitoriza el tráfico de red de una computadora (escuchando en una interfaz de red, como `eth1`) para detectar y avisar de situaciones anómalas.
  - **Mecanismo de decisión**: Utiliza un conjunto de reglas (como _Emerging Threats Open_, con más de 50.000 reglas).
  - **Visor, análisis y registros**:
    - `sudo ids-alerts -f`: Muestra las alertas en tiempo real (hora, prioridad, regla activada y direcciones origen y destino).
    - `ids-replay <fichero.pcap>`: Permite analizar un archivo de captura sin necesidad de reproducirlo en la red (a diferencia de `tcpreplay`, que sí reinyecta el tráfico en la interfaz de red).
    - **Registros detallados**: Los detalles completos de cada alerta (paquete, reglas, protocolo, etc.) se almacenan en `/var/log/suricata/eve.json` y `/var/log/suricata/fast.log`.
