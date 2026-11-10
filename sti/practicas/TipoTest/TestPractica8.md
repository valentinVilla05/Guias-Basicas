## Bloque 1: Generación de Números Aleatorios y Criptografía

> La entropía de una contraseña es inversamente proporcional a la población de caracteres utilizados en la contraseña.

- **Falso**
- _Motivo: Es directamente proporcional. Cuanto mayor es la población o conjunto de caracteres disponibles, mayor es la entropía y la seguridad._

---

> Si el test chi-cuadrado del software ENT, aplicado a una posible secuencia de números aleatorios, nos devuelve un porcentaje del 99%, la secuencia puede ser considerada con total seguridad aleatoria.

- **Falso**
- _Motivo: Ningún test estadístico garantiza la aleatoriedad con total seguridad. Un resultado extremo del 99% resulta muy sospechoso de sesgo o falta de aleatoriedad._

---

> La página web random.org nos permite obtener números realmente aleatorios.

- **Verdadero**
- _Motivo: Utiliza el ruido atmosférico (un fenómeno físico e impredecible) para generar aleatoriedad real (TRNG)._

---

> Existen diversas listas de palabras disponibles en diferentes idiomas para el método de generación de contraseñas Diceware. Cada lista tiene un número diferente de símbolos.

- **Falso**
- _Motivo: En el estándar Diceware, las listas de cualquier idioma contienen exactamente 7776 palabras o símbolos (6^5 = 7776)._

---

> La entropía se calcula realizando el logaritmo en base 2 de la cantidad de elementos de la población por la longitud de la contraseña.

- **Verdadero**
- _Motivo: Aplica la fórmula E = L × log₂(N), multiplicando la longitud (L) por el logaritmo en base 2 del tamaño del alfabeto (N)._

---

> El valor de la semilla debe ser modificada en tiempo de ejecución.

- **Falso**
- _Motivo: La semilla se establece al inicializar el PRNG; modificarla continuamente rompe la determinación y el comportamiento esperado del algoritmo._

---

> Los números pseudoaleatorios deben usarse en aplicaciones críticas, como la criptografía.

- **Falso**
- _Motivo: La criptografía requiere números aleatorios reales (TRNG) o generadores pseudoaleatorios criptográficamente seguros (CSPRNG)._

---

> Un ordenador es capaz de generar números realmente aleatorios.

- **Falso**
- _Motivo: Los ordenadores convencionales son máquinas deterministas; solo generan números pseudoaleatorios mediante algoritmos._

---

> Las características de la aleatoriedad dependen de una serie de números y no de un número en sí.

- **Verdadero**
- _Motivo: La aleatoriedad evalúa el comportamiento de una secuencia o conjunto, no la propiedad de un único número aislado._

---

> La sucesión de estados en un generador de números pseudoaleatorios no es periódica porque trabaja con un conjunto infinito de estados.

- **Falso**
- _Motivo: La memoria de un ordenador es finita, por lo que los estados de un PRNG son finitos y la secuencia termina repitiéndose (es periódica)._

---

## Bloque 2: Seguridad en Sistemas y Herramientas (Fail2Ban y Rootkit Hunter)

> Al ejecutar el siguiente código (`find /usr/bin/ -type f -exec sha1sum {} \;`) en una terminal UNIX y redireccionar su salida a un fichero, se podrían detectar anomalías con `-c`.

- **Verdadero**
- _Motivo: Genera los hashes de los ejecutables. Posteriormente, `sha1sum -c <fichero>` verifica el estado de cada archivo contra ese registro para detectar alteraciones._

---

> Fail2Ban posee un mecanismo configurable (`/etc/hosts.deny`) donde se especifica por cuánto tiempo se aplicará la actualización correspondiente a una IP.

- **Falso**
- _Motivo: El tiempo de baneo (bantime) se configura en los archivos propios de Fail2Ban (`jail.conf` o `jail.local`), no en `/etc/hosts.deny`._

---

> En Fail2Ban, con el comando (`sudo fail2ban-client status ssh`), se muestra información relativa al estado del filtro SSH.

- **Verdadero**
- _Motivo: Al indicar la jaula concreta (ssh), muestra sus métricas particulares: fallos detectados e IP bloqueadas._

---

> En Fail2Ban, con el comando (`sudo fail2ban-client status ssh`), podemos ver los filtros (jails) que están activos.

- **Falso**
- _Motivo: Con `status ssh` solo vemos el estado de la jaula SSH. Para listar todos los filtros activos se utiliza `sudo fail2ban-client status` sin especificar ninguna jaula._

---

> En Fail2Ban, con el comando (`sudo fail2ban-client status`), podemos ver los filtros (jails) que están activos y configurarlos.

- **Falso**
- _Motivo: El comando `status` es únicamente informativo (de lectura); no permite editar ni aplicar configuraciones._

---

> Fail2Ban posee un mecanismo configurable (`jail.conf`) donde se especifica por cuánto tiempo se aplicará la acción correspondiente sobre una IP tras detectarse un comportamiento anómalo.

- **Verdadero**
- _Motivo: En `jail.conf` se configura el parámetro `bantime`, que establece la duración del bloqueo a las IP atacantes._

---

> Rootkit Hunter realiza la detección de intrusiones basándose en archivos de registro.

- **Falso**
- _Motivo: `rkhunter` es una herramienta de auditoría sobre el sistema de archivos (binarios, hashes y permisos), no analiza archivos de log o registro._

---

> Rootkit Hunter es un programa de detección de intrusiones basada en archivos de registro.

- **Falso**
- _Motivo: Su análisis se basa en la comprobación de integridad y firmas de rootkits en los archivos del sistema, no en archivos de registro (logs)._

---

> En Fail2Ban se aplican restricciones de acceso contra las IP intrusoras mediante reglas que provocan la inclusión de las intrusoras en el fichero `/etc/hosts.deny`.

- **Falso**
- _Motivo: Por defecto, las acciones de bloqueo se aplican directamente en las tablas del cortafuegos (iptables, nftables o ufw)._

---

> Fail2Ban supervisa (entre otros) el archivo `/var/log/auth.log` y, mediante expresiones regulares, detecta actividades sospechosas y aplica acciones contra las IP correspondientes.

- **Verdadero**
- _Motivo: Lee archivos de registro del sistema como `/var/log/auth.log`, buscando patrones sospechosos (failregex) para bloquear las IP atacantes._

---

> En Fail2Ban, con el comando (`sudo fail2ban-client status`), podemos ver los filtros (jails) que están activos.

- **Verdadero**
- _Motivo: Sin parámetros adicionales ni la parte de configurarlos, el comando `status` devuelve el listado con todas las jaulas o filtros activos._

---

> Fail2Ban posee un mecanismo configurable (`/etc/hosts.deny`) donde se especifica por cuánto tiempo se aplicará la actualización correspondiente a una IP.

- **Falso**
- _Motivo: El archivo `/etc/hosts.deny` no controla los tiempos de expiración de baneo de Fail2Ban; estos se especifican en la configuración propia del servicio (`jail.conf`)._

---

> En Fail2Ban, con el comando (`sudo fail2ban-client status ssh`), se muestra información relativa al estado del filtro SSH.

- **Verdadero**
- _Motivo: Muestra el detalle de la jaula SSH, especificando el estado de sus reglas e IP bloqueadas._

---

> En Fail2Ban se aplican restricciones de acceso contra las IP intrusoras mediante reglas que provocan la inclusión de las intrusoras en el fichero `/etc/host.deny`.

- **Falso**
- _Motivo: Las restricciones se gestionan aplicando reglas de cortafuegos a nivel de red, no modificando `/etc/host.deny`._

---

> Fail2Ban supervisa (entre otros) el archivo `/var/log/auth.log` y, mediante expresiones regulares, detecta actividades sospechosas y aplica acciones contra las IP correspondientes.

- **Verdadero**
- _Motivo: Es una de las funciones principales de Fail2Ban: analizar archivos de registro mediante expresiones regulares para aplicar bloqueos automáticos._

---

> Fail2Ban posee un mecanismo configurable (`jail.conf`) donde se especifica por cuánto tiempo se aplicará la acción correspondiente sobre una IP tras detectarse un comportamiento anómalo.

- **Verdadero**
- _Motivo: En `jail.conf` se establece la variable `bantime` para determinar el tiempo de restricción._

---

> Rootkit Hunter realiza la detección de intrusiones basándose en archivos de registro.

- **Falso**
- _Motivo: Audita el sistema de archivos buscando cambios en los binarios del sistema, no procesando archivos de registro (logs)._

---

> Rootkit Hunter es un programa de detección de intrusiones basada en archivos de registro.

- **Falso**
- _Motivo: Es un analizador de integridad y buscador de firmas de rootkits en ejecutables, no una herramienta basada en archivos de registro (logs)._