## Preguntas Obtenidas de la práctica 2

> Para descargar las claves públicas de otras personas conociendo su identificador hexadecimal basta con ejecutar gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys <id>.

- **Verdadero (con matices)**
- _Motivo: conceptualmente el comando funciona en GnuPG para descargar una clave por su ID o huella. Sin embargo, en el documento de la práctica se exige usar el protocolo seguro hkps:// (sin especificador de puerto :80) y la huella o ID largo._

----------------------------

> Cada clave lleva asociado un código hexadecimal de 8 dígitos, que sirve de identificador.

- **Falso**
- _Motivo: no deben usarse identificadores cortos de 8 caracteres porque son inseguros y fáciles de falsificar. Las claves se identifican unívocamente mediante la huella dactilar de 40 caracteres o los 16 últimos caracteres (identificador largo)._

----------------------------

> Para exportar la clave privada generada y usarla en otro computador utilizaremos la orden gpg -a -ea --export.

- **Falso**
- _Motivo: la opción --export solo sirve para la clave pública. Para la clave privada se debe usar obligatoriamente --export-secret-keys y guardar el resultado en un fichero (gpg -a -o <fichero> --export-secret-keys <id>)._

----------------------------

> El comando gpg --list-keys listará todas las claves privadas instaladas en el anillo de claves.

- **Falso**
- _Motivo: gpg --list-keys lista únicamente las claves públicas. Para ver las claves privadas se debe utilizar gpg --list-secret-keys._

----------------------------

> PGP (Pretty Good Privacy) es un programa que permite cifrar nuestra información utilizando solamente técnicas criptográficas asimétricas.

- **Falso**
- _Motivo: PGP es un sistema híbrido que utiliza criptografía tanto simétrica como asimétrica, además de firmas digitales._

----------------------------

> Para crear una firma digital separada del fichero original, el cual queda intacto utilizamos gpg -s.

- **Falso**
- _Motivo: el comando gpg -s crea un archivo que empaqueta el contenido junto con la firma. Para crear una firma separada (detached signature) dejando el archivo original intacto se usa gpg -b._

----------------------------

> Utilizaremos el siguiente comando gpg -d para cifrar un archivo binario.

- **Falso**
- _Motivo: el comando gpg -d sirve para descifrar. Para cifrar un archivo binario se utiliza gpg -e -r <destinatario> <fichero>._

----------------------------

> Para descifrar, GnuPG únicamente te solicitará tu contraseña.

- **Verdadero**
- _Motivo: para cifrar solo se necesita la clave pública del destinatario, pero para descifrar se requiere la clave privada, por lo que GnuPG te solicitará la contraseña para desbloquearla._

----------------------------

> Para crear nuestro propio par de claves públicas y privadas deberemos ejecutar gpg --full-gen-key.

- **Verdadero**
- _Motivo: es la orden indicada en la práctica para iniciar el proceso interactivo de creación de claves (tipo de algoritmo, validez, datos de usuario y contraseña)._

----------------------------

> Mediante la orden gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys, se actualiza las claves públicas de nuestro anillo con todas las nuevas firmas que haya en el servidor, y subo las firmas que nosotros hayamos añadido.

- **Falso**
- _Motivo: para actualizar las firmas del anillo se usa gpg --refresh-keys (no --recv-keys). Además, las órdenes de actualización solo descargan información del servidor y nunca suben las firmas que hayamos añadido nosotros (para subirlas hay que usar --send-keys)._

----------------------------