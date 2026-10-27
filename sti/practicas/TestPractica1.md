## Preguntas Obtenidas de la práctica 1

> Metasploit es una de las herramientas más conocidas para comprobar si nuestro sistema presenta vulnerabilidades.

- **Verdadero**
- _Motivo: Metasploit Framework es un estándar en el ámbito de la ciberseguridad y las pruebas de penetración (pentesting), utilizado tanto para auditorías de seguridad como para verificar y validar la presencia de vulnerabilidades en sistemas mediante la ejecución de exploits._

----------------------------

> En la versión vsftpd 2.3.4, la vulnerabilidad reside en una mala configuración por defecto del archivo /etc/vsftpd.conf.

- **Falso**
- _Motivo: no se trata de un fallo de configuración. La vulnerabilidad (CVE-2011-2523) es una puerta trasera (backdoor) introducida maliciosamente en el propio código fuente de la aplicación, la cual se activa al recibir una secuencia de caracteres específica en el nombre de usuario._

----------------------------

> La aplicación de un parche de seguridad o actualización consiste en bloquear el puerto afectado mediante un firewall.

- **Falso**
- _Motivo: el filtrado de puertos con un firewall (iptables) es una medida de mitigación a nivel de red. Un parche o actualización consiste en modificar o reemplazar el código binario ejecutable (vsftpd >= 2.3.5) para corregir o eliminar la vulnerabilidad manteniendo la funcionalidad del servicio._

----------------------------

> Al bloquear únicamente el puerto 6200/TCP mediante iptables, el servicio FTP legítimo en el puerto 21/TCP sigue funcionando, pero el atacante no logra obtener la consola de comandos.

- **Verdadero**
- _Motivo: el puerto 21 permanece abierto y responde a los usuarios FTP. Aunque la secuencia maliciosa active el listener del puerto 6200 internamente, la regla de iptables en el puerto 6200 bloquea la conexión de retorno de Metasploit, impidiendo la apertura de la sesión de root._

----------------------------

> La imposibilidad de actualizar vsftpd mediante apt-get en Metasploitable 2 se debe a un error de sintaxis en el comando ejecutado.

- **Falso**
- _Motivo: la imposibilidad de actualizar se debe a que Metasploitable 2 se basa en Ubuntu 8.04 LTS (versión obsoleta fuera de soporte cuyos repositorios fueron retirados, devolviendo errores 404 Not Found) y al aislamiento de red del propio laboratorio._

----------------------------