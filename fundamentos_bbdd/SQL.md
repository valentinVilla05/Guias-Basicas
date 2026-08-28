# SQL

Aquí vamos a ver la sintaxis de estándar de SQL que podemos dividir en cuatro bloques (como se vió en [basics.md](https://github.com/valentinVilla05/Guias-Basicas/blob/master/fundamentos_bbdd/basics.md)): `DDL`, `DML`, `DCL` y tipos de datos.

### DDL (Data definition language)

---

Aquí se encuentran los comandos para crear, modificar o eliminar la estructura en la base de datos (`CREATE`, `ALTER` y `DROP` respectivamente). Además tenemos las **restricciones**. Vamos a verlo:

Vamos a crear por ejemplo la tabla "Persona", este debe contar con los campos `id`, `nombre`, `apellidos`, `edad`, `email`.

```sql
CREATE TABLE persona (
    id NUMBER PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellidos TEXT,
    edad NUMBER,
    email TEXT UNIQUE
)
```

Así sería la estructura para crear una tabla, vamos a ver que es cada cosa.

CREATE TABLA "nombre_tabla" (--> para crear la tabla

columna + "tipo de dato" + [restricciones]

...

)

Para modificar una tabla usariamos `ALTER TABLE persona (...)` y para eliminarla usariamos `DROP TABLE persona;`

### Tipos de restricciones y qué hacen

- `PRIMARY KEY`: Define la **clave primaria** (implica `NOT NULL` y valores únicos, es decir, este campo será único para cada registro y nunca podrá estar vacía, por lo general este campo suele ser el `id`)

- `FOREIGN KEY (columna) REFERENCES tablaPadre(columna)`: Enlaza con la clave primaria de otra tabla.

Por ejemplo, imaginemos la tabla Alumno y la tabla Profesor: la clave primaria del **profesor** será su `id` y la tabla alumno tendrá su clave primaria `id` pero, ¿como relacionamos un curso con su profesor? para eso tenemos las `FOREIGN KEY`, añadimos una columna `profesor_id` en la tabla curso y de esta manera cada curso tendrá su profesor asignado.

- `UNIQUE`: Evita valores duplicados en una columna o conjunto de columnas.
- `NOT NULL`: Impide dejar la columna sin valor.
- `CHECK (condicion)`: Exige que el dato introducido cumpla una condición. Ejemplo: `CHECK (edad > 18)`
- `DEFAULT valor`: Asigna un valor por defecto a una columna

### Reglas de integridad

---

- `CASCADE` Si se borra o modifica la fila en una tabla padre se borran/modifican automáticamente sus filas asocidas en la tabla hija. ç

Ejemplo: volviendo a la relacion entre tabla `Alumno` y `Profesor` si al crear la tabla ponemos la regla `ON DELETE CASCADE` al eliminar un profesor (clase padre) se borrará su correspondiente id de la columna `profesor_id` de la tabla Curso (tabla hija).

- `SET NULL` : Si se borra en la tabla padre, la clave foránea en la tabla hija se pone a NULL.

- `RESTRICT`: Impide borrar o modificar la fila padre si tiene filas hijas vinculadas.

---

### DML (Data Manipulation Lenguage)

Aquí tenemos:

- `INSERT INTO tabla (columna1, columna2...) VALUES (valor1, valor2...)`

Ejemplo (una vez creada la tabla Persona): `INSERT INTO persona (id, nombre, apellidos, edad, email) VALUES (1, 'pepe', 'gomez', 21, 'pepe@gmail.com')`

- `UPDATE tabla SET columna1 = valor1, columna2 = valor2... WHERE condicion`. **Importante**: Si no ponemos el `WHERE` se actualizan todas las filas de la tabla.

- `DELETE FROM tabla WHERE condicion`: Eliminamos todas las columnas que cumplan una condicion.

### Consultas básicas (`SELECT`) y filtrados.

---

- `SELECT columnas FROM tabla WHERE condicion ORDER BY columna [ASC|DESC]`
  - Los operadores de filtrado en el `WHERE` son:
    - Comparación: `=`, `<>`, `<`, `>`, `<=`, `>=`
    - Rangos: `BETWEEN valor_min AND valor_max`
    - Lista de valores: `IN ('valor1, valor2', ...)`
    - Patrones de texto: `LIKE 'A%'` (empieza por A) o `LIKE '_B%'` (seguna letra B)
    - Nulos: `IS NULL`, `IS NOT NULL`
    - Lógicos: `OR`, `AND`, `NOT`

- Agregacion y agrupamiento:

  Podemos calcular un único valor a partir de un cojunto de filas: `COUNT(*)`, `SUM(col)`, `AVG(col)`, `MAX(col)`, `MIN(col)`.

  Podemos agrupar los datos de las siguientes maneras:
  - `GROUP BY columna`: Agrupa las filas con el mismo valor para poder aplicarles funciones de agregación.

  - `HAVING condicion`: Filtra los grupos resultantes.

  - ¿En qué se diferencia wl `WHERE` del `HAVING`?:
    - `WHERE` filtra filas individuales antes de realizar la agrupación.
    - `HAVING` filtra **grupos completos** después de aplicar el `GROUP BY` (acepta funciones de agregación)

* Consultas avanzadas: Join, Subconsultas y Conjuntos
  - Combinacion de tablas (Joins):
    - **Implícito**: `SELECT * FROM TablaA, TablaB WHERE TablaA.id = TablaB.id;`
    - **Explícito**: `SELECT * FROM TablaA JOIN TablaB ON TablaA.id = TablaB.id;`

* Subconsultas (Consultas anidadas):
  - Independientes: La subconsulta interior se ejecuta una sola vez y su resultado se entrega a la consulta principal.

  - Correlacionadas: La subconsulta utiliza una variable de la consulta exterior, por lo que debe ejecutarse de forma iterativa fila por fila.

  - Operador `[NOT] EXISTS`: Comprueba si la subconsulta devuelve alguna fila. Devuelve verdadero o falso y es la herramienta estándaren SQL para implementar la operación de **division**.

* Operaciones con conjuntos:
  - `UNION`: Combina resultados eliminados duplicados.
  - `INTERSECT`: Devuelve solo los registros comunes en ambas consultas.
  - `MINUS` (o `EXCEPT`): Devuelve los registros de la primera consulta que no están en la segunda.

* Vistas, Índices y DCL:
  - **Vistas (`CREATE VIEW`)**: Tablas virtuales definidas por una consulta `SELECT`. Simplifican consultas complejas y aportan seguridad restrigiendo el acceso directo a las tablas base.

  - **Ïndices (`CREATE INDEX`)**: Estructuras físicas auxiliares creadas sobre columnas para acelerar la velocidad de búsqueda y consulta.

  - Control de permisos (DCL):
    - `GRANT permiso ON objeto TO usuario;` (concede privilegios como `SELECT`, `INSERT`, etc)
    - `REVOKE permiso ON objeto FROM usuario`; (retira privilegios previamente concedidos)

---

Vamos con un ejemplo práctico, haremos una gestión de un centro de estudios que tendrá tres tablas:

- Tabla principal: _Profesor_

```sql
    CREATE TABLE profesor (
        id NUMBER PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL,
        departamento VARCHAR(50)
    );
```

En esta tabla hemos asignado `id` de tipo número y será la clave primaria de nuestra tabla, `nombre` y `departamento` son de tipo `VARCHAR` que es lo mismo que texto solo que en `VARCHAR` especificamos el número máximo de caracteres que tendrá, ademaś hemos añadido la restricción de `NOT NULL`.

- Tabla hija (con FK y regla de integridad): _curso_

```sql
    CREATE TABLE curso (
        id NUMBER PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL,
        precio NUMBER CHECK (precio >= 0),
        profesor_id NUMBER,

        CONSTRAINT fk_profesor FOREIGN KEY (profesor_id) REFERENCES profesor(id) ON DELETE SET NULL
    )
```

En esta tabla ponemos el `id` del curso como clave primaria y establecemos que `profesor_id` sea la clave foránea para relacionar esta tabla con la tabla `profesor`, asdemás añadimos `ON DELETE SET NULL` para que cuando se elimine un profesor el campo `profesor_id` se ponga en NULL.

- Tabla con una relacion N:M: _matrícula_

```sql
  CREATE TABLE matricula (
    alumno_id NUMBER,
    curso_id NUMBER,
    fecha_inscripcion DATE DEFAULT CURRENT_DATE,

    PRIMARY KEY (alumno_id, curso_id),
    CONSTRAINT fk_curso FOREIGN KEY (curso_id) REFERENCES curso(id) ON DELETE CASCADE
  )
```

Esta tabla es lo que se suele llamar "tabla pivote" que se utiliza para las relaciones N:M (muchos a muchos), en este caso sería: "Un alumno puede estar matriculado de muchos cursos y un curso puede tener muchos alumnos" entonces para eso usamos una tabla intermedia que relaciona ambas. Las claves de esta tabla son: `id` del alumno matriculado, `id` del curso al que se matricula y la fecha en la que se inscribe. Por otro lado al poner `ON DELETE CASCADE` al borrar algún alumno o curso se eliminará esa matricula que lo contenga.

Ahora vamos a probar a insertar datos en estas tablas (DML):

```sql
INSERT INTO profesor (id, nombre, departamento) VALUES (1, 'Paco Sanz', 'Informática');
INSERT INTO profesor (id, nombre, departament) VALUES (2, 'Raúl Beckham', 'Matemáticas');


INSERT INTO curso (id, nombre, precio, profesor_id) VALUES (101, 'Bases de datos', 120, 1);
INSERT INTO curso (id, nombre, precio, profesor_id) VALUES (102, 'Álgebra', 90, 2);
INSERT INTO curso (id, nombre, precio, profesor_id) VALUES (103, 'Programación SQL', 150, 1);


INSERT INTO matricula (alumno_id, curso_id) VALUES (501, 101);
INSERT INTO matricula (alumno_id, curso_id) VALUES (501, 103);
INSERT INTO matricula (alumno_id, curso_id) VALUES (502, 101);
```

Ahora probamos a hacer unas consultas (`SELECT`) para obtener datos:

Obtenemos el nombre de cada curso junto con el nombre del profesor que lo imparte.

```sql
SELECT c.nombre AS curso, p.nombre AS profesor
FROM curso c
JOIN profesor p ON c.profesor_id = p.id;
```

Como curso y profesor tienen una fila con el mismo nombre usamos c. o p. para especificar de que tabla estamos obteniendo el dato.

Obtenemos los profesores que imparten más de 1 curso, mostrando cuántos imparten y la suma total del precio.

```sql
SELECT p.nombre, COUNT(c.id) AS total_cursos, SUM(c.precio) AS precio_total
FROM profesor p
JOIN curso c ON p.id = c.profesor_id
GROUP BY p.id, p.nombre
HAVING COUNT(c.id) > 1;
```

Obtenemos los profesores que tienen asignado al menos un curso.

```sql
SELECT p.nombre
FROM profesor p
WHERE EXISTS (
    SELECT 1
    FROM curso c
    WHERE c.profesor_id = p.id
);
```

Ahora probamos a hacer una vista e índice:

```sql
-- Creamos una vista para simplificar la consulta del catálogo de cursos
CREATE VIEW vista_catalogo AS
SELECT c.nombre AS curso, c.precio, p.nombre AS profesor
FROM curso c
LEFT JOIN profesor p ON c.profesor_id = p.id;

-- Creamos un índice sobre la columna departamento para acelerar las búsquedas
CREATE INDEX idx_prof_dpto ON profesor(departamento);

-- Concedemos permiso de lectura sobre la vista a un rol o usuario llamado 'estudiante'
GRANT SELECT ON vista_catalogo TO estudiante;
``
```
