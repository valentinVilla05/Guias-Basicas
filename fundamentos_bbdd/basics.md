## Introducción

#### ¿Qué es una base de datos?

Una **Base de Datos (BD)** es una colección de datos estructurados junto con sus metadatos (esquema) orientada a representar la realidad de una organización.

**No confundir** con un **Sistema Gestor de Bases de Datos (SGBD / DBMS)**, el cual es el software especializado que actúa como interfaz entre la base de datos, las aplicaciones y los usuarios para gestionar el acceso, almacenamiento y control.

---

### ¿Por qué utilizar un SGBD y no un sistema de ficheros tradicional?

Guardar la información en archivos independientes (archivos de texto, hojas de cálculo, etc.) tiene varios inconvenientes:

* **Redundancia e inconsistencia**: Duplicación innecesaria de información en distintos archivos, lo que provoca que los datos no coincidan entre sí.
* **Dificultad de acceso y aislamiento**: Múltiples archivos con formatos diferentes que obligan a escribir código específico para cada nueva consulta.
* **Problemas de integridad**: En los ficheros, las reglas de validación (ej. `saldo > 0`) se tienen que programar dentro de la aplicación. En un SGBD, las reglas se definen centralizadamente en la BD.
* **Falta de atomicidad**: Si ocurre cualquier fallo eléctrico o del sistema a mitad de una transacción, los ficheros quedan en un estado corrupto o incompleto.
* **Concurrencia insegura**: Accesos simultáneos sin control provocan la pérdida de actualizaciones (dos usuarios editando lo mismo a la vez).
* **Seguridad reducida**: Dificultad para restringir qué partes del archivo puede ver o editar cada usuario.

---

### Niveles de abstracción

El SGBD oculta la complejidad del almacenamiento físico mediante tres niveles:

1. **Nivel físico**: Describe en detalle *cómo* se almacenan físicamente los datos en los soportes de almacenamiento (bloques de disco, estructuras de archivos, índices B-Tree/Hash).
2. **Nivel lógico**: Describe *qué* datos se guardan y las relaciones existentes entre ellos (esquema conceptual de la base de datos).
3. **Nivel de vistas**: Muestra únicamente la porción de información relevante para cada perfil de usuario u operación, ocultando el resto por sencillez o seguridad.

#### Ejemplos prácticos:

* **Nivel Físico**: Cómo se organizan los sectores en el disco duro o los punteros de memoria donde residen los datos.
* **Nivel Lógico**: La definición de tablas y campos. Por ejemplo, la tabla `Alumno` (`id`, `nombre`, `dni`) relacionada con la tabla `Calificaciones` (`idAlumno`, `nota`). Relación 1:N (*"Un alumno tiene varias calificaciones"*). El código SQL DDL (`CREATE TABLE`) opera en este nivel.
* **Nivel de Vistas**: En una plataforma de comercio (Amazon), el cliente ve una vista con el catálogo y sus compras; el vendedor ve una vista del inventario; y el administrador tiene acceso a paneles globales de facturación.

---

### Roles en una Base de Datos

* **Usuarios finales**: Interactúan con la BD a través de aplicaciones sin necesidad de conocer su estructura interna.
* **Programadores de aplicaciones**: Escriben el código de las aplicaciones que realizan operaciones sobre la BD.
* **DBA (Database Administrator)**: Responsable de la seguridad, control de accesos, rendimiento, diseño físico/lógico y procesos de recuperación ante fallos.

---

### Lenguajes y Componentes del SGBD

* **DDL (Data Definition Language)**: Permite definir y modificar la estructura de los objetos de la BD (`CREATE`, `ALTER`, `DROP`).
* **DML (Data Management Language)**: Permite consultar, insertar, modificar y eliminar los datos (`SELECT`, `INSERT`, `UPDATE`, `DELETE`).
* **DCL (Data Control Language)**: Gestiona la seguridad, permisos y privilegios de acceso (`GRANT`, `REVOKE`).
* **Diccionario de datos**: Repositorio central del SGBD que almacena los metadatos (información sobre las tablas, tipos de datos, usuarios y restricciones).

---

### Clasificación de las Bases de Datos

* **Según el modelo de datos**: Jerárquico, En Red, Relacional (el más usado), Orientado a Objetos y NoSQL.
* **Según la ubicación**: Local, Distribuida, Federada y En la nube (Virtual Machine / As a Service).