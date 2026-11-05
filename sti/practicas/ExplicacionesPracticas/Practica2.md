## Práctica 2: Criptografía Asimétrica, Firmas Digitales y GnuPG (OpenPGP)

### 1. Fundamentos de PGP y OpenPGP

- **PGP (Pretty Good Privacy)**: Creado por Phil Zimmermann en los años 90. **NO es un algoritmo de cifrado**, sino un programa/protocolo.
- **Criptografía Híbrida**: PGP/GnuPG combina técnicas simétricas y asimétricas:
  - **Simétrica**: Cifra el contenido del archivo o mensaje de forma rápida y eficiente mediante una clave de sesión aleatoria.
  - **Asimétrica**: Cifra la clave de sesión simétrica utilizando la clave pública del destinatario (y se usa para las firmas digitales con la clave privada).
- **Estándar Abierto OpenPGP**: Es el protocolo estandarizado (RFC 9580) derivado de PGP. **GnuPG (GPG)** es la implementación libre y estándar más utilizada en entornos Linux.

---

### 2. Gestión e Identificación de Claves (Anillos de Claves)

GnuPG organiza las llaves en dos estructuras de almacenamiento llamadas **anillos de claves** (*keyrings*):

- **Listado de Claves**:
  - `gpg --list-keys`: Muestra únicamente las **claves públicas** guardadas en el anillo.
  - `gpg --list-secret-keys`: Muestra únicamente las **claves privadas** almacenadas.

- **Identificadores de Clave**:
  - **Huella dactilar (*Fingerprint*)**: Cadena hexadecimal de **40 caracteres** que identifica de forma unívoca a una clave. Es la única forma 100% segura de validar la autenticidad de una clave recibida.
  - **Identificador Largo**: Formado por los **últimos 16 caracteres** de la huella dactilar.
  - **Identificador Corto (8 caracteres)**: **INSEGURO**. No debe utilizarse debido a que es técnicamente trivial generar colisiones y claves falsas que compartan esos 8 caracteres.

- **Creación de Claves**:
  - Se utiliza el comando interactivo `gpg --full-gen-key`.
  - **Algoritmos**: Por defecto utiliza curvas elípticas (ECC, Curve 25519) por su alta seguridad y rapidez; opcionalmente admite RSA (longitudes típicas de 3072 a 4096 bits).
  - **Certificado de Revocación**: Se genera automáticamente en el directorio `~/.gnupg/openpgp-revocs.d/` para invalidar la clave si se pierde la contraseña o se compromete la clave privada.

---

### 3. Operaciones Principales: Cifrado, Descifrado y Exportación

| Operación | Comando GPG | Clave Requerida / Solicita Contraseña | Notas |
|---|---|---|---|
| **Cifrar (Binario)** | `gpg -e -r <destinatario> <fichero>` | Clave **pública** del destinatario | No pide contraseña del emisor. |
| **Cifrar (Texto/ASCII)** | `gpg -ea -r <destinatario> <fichero>` | Clave **pública** del destinatario | Crea un archivo con armadura ASCII (`.asc`). |
| **Descifrar** | `gpg -d <fichero_cifrado>` | Clave **privada** del receptor | **GnuPG solicitará obligatoriamente la contraseña** para desbloquear la clave privada. |
| **Exportar PÚBLICA** | `gpg -a -o <pub.asc> --export <id>` | Ninguna | Exporta el bloque de clave pública en formato ASCII. |
| **Exportar PRIVADA** | `gpg -a -o <priv.asc> --export-secret-keys <id>` | Requiere contraseña | Utiliza obligatoriamente `--export-secret-keys` (la opción `--export` falla para claves privadas). |

---

### 4. Firmas Digitales en GnuPG

La firma digital garantiza la **autenticidad**, la **integridad** del mensaje y el **no repudio** (firmada siempre con la propia **clave privada** del emisor).

- **Tipos de Firma**:
  - **Firma Empaquetada (`gpg -s <fichero>`)**: Empaqueta el contenido original junto con la firma en un nuevo fichero binario.
  - **Firma Separada / Detached (`gpg -b <fichero>`)**: Genera un archivo de firma independiente (extensión `.sig`), **dejando el archivo original totalmente intacto**.
  - **Firma en Modo Texto (`gpg --clear-sign <fichero>`)**: Mantiene el texto plano legible e incluye la firma ASCII rodeando el contenido (ideal para correos o documentos legibles).
- **Verificación**: `gpg --verify <fichero>` comprueba la validez de la firma usando la clave pública correspondiente.

---

### 5. Servidores de Claves y Red de Confianza (*Web of Trust*)

- **Protocolos y Conexión**:
  - El estándar seguro para comunicarse con los servidores de claves es mediante **HKPS** (`hkps://keyserver.ubuntu.com`). El antiguo uso de `hkp://` en el puerto `:80` está en desuso por carecer de cifrado en la transmisión.
- **Intercambio en Servidores**:
  - `gpg --keyserver <servidor> --send-keys <huella>`: Sube o actualiza la clave pública en el servidor.
  - `gpg --keyserver <servidor> --recv-keys <huella>`: Descarga una clave pública específica.
  - `gpg --keyserver <servidor> --search-keys <patron>`: Busca claves por nombre o correo.
- **Firmar Claves de Terceros y Actualización**:
  - `gpg --sign-key <id>`: Firma la clave pública de otra persona para certificar públicamente su autenticidad tras verificar su huella.
  - `gpg --refresh-keys`: Actualiza las claves de nuestro anillo local descargando las **nuevas firmas externas** que otros hayan subido al servidor.
  - **Diferencia Crítica**: Las órdenes de refresco (`--refresh-keys` o `--recv-keys`) **únicamente descargan información del servidor**; jamás suben de forma automática las firmas que nosotros hayamos realizado localmente (para subir nuestras firmas locales hay que hacer `--send-keys`).