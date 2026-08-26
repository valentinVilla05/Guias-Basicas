## Álgebra relacional

Las bases de datos **relacionales** se basan en un sistema compuesto por tablas (formadas por filas y columnas) que se conectan entre sí mediante **claves**.

- La **terminología** que se usa es la siguiente:
  - **Relación**: Equivale a una tablas.
  - **Tupla**: Equivale a una fila/registro
  - **Atributo**: Equivale a una columna/campo
  - **Grado o aridad**: Número total de atributos que tiene la tabla
  - **Dominio**: Rango de valores permitidos para un atributo (pueden ser discretos o contínuos).
  - **Clave**: Atributo/s que identifican de forma única cada tupla.

Este modelo tiene algunas restricciones como:

- Todos los datos de una misma columna deben ser del mismo tipo
- Cada columna debe tener un nombre único
- No se permiten filas duplicadas en una relación
- Todos los valores deben ser atómicos

# Operaciones sobre las tablas

Las operaciones se dividen en **operaciones primitivas** (fundamentales e irreducibles) y **operaciones derivadas** (combinaciones de las primitivas para simplificar consultas complejas).

- ## Operaciones primitivas:

### Selección ($\sigma$):

La idea clave de esta operación es filtrar información de una tabla sin modificar nada de la misma:

- La formula usada: $$\sigma_{\text{condición}}(\text{Tabla})$$
  - Donde $\sigma$ (S en griego) significa Selección
  - _condicion_ : Es la regla que ponemos para filtrar los datos (se pueden aplicar varias). Por ejemplo: edad >= 18
  - Tabla : La tabla de la que queremos obtener los datos.

- Efecto que tiene en la tabla esta operaión:
  - El **grado** se mantiene intacto ya que como hemos dicho la "selección" no modifica nada en la tabla.
  - La **cardinalidad** disminuye o se queda igual, lo cual es evidente ya que si de una tabla de 100 registros queremos conseguir los que cumplen X condición pues la cardinalidad que obtendremos será menor (o incluso 0 sin ningun registro la cumple)

- Demostraciones algebráica:
  - **Conmutatividad**: Es decir, el orden no altera el resultado, da igual la condición que pongas primero:

  $$\sigma_{\text{Ciudad}=\text{'Madrid'}}(\sigma_{\text{Edad}\ge 18}(\text{Usuarios})) = \sigma_{\text{Edad}\ge 18}(\sigma_{\text{Ciudad}=\text{'Madrid'}}(\text{Usuarios}))$$
  - **Unificación de condiciones**: Puedes unir 2 selecciones en una sola con operadores lógicos:
    $$\sigma_{\text{Edad}\ge 18 \land \text{Ciudad}=\text{'Madrid'}}(\text{Usuarios})$$

### Proyección ($\pi$):

La idea clave de esta operación es filtrar **columnas**. Es decir, quedarnos solo con la columna que queramos a diferencia de la seleccion que filtramos por información específica de una tabla manteniendo la tabla igual

- La formula usada: $$\pi_{A_1, A_2, \dots, A_k}(\text{Tabla})$$
  - Donde $\pi$ (P en griego) significa Proyección
  - $A_1, A_2, \dots, A_k$: La lista de columnas que queremos conseguir.
  - Tabla : La tabla de la que queremos obtener los datos.

- Efecto que tiene en la tabla esta operaión:
  - El **grado** se reduce al número de columnas que hayamos especificado. (Si solo queremos la columna de "nombre" y "dni" pues el grado será 2).
  - La **cardinalidad** Puede disminuir o quedarse igual. En álgebra relacional, el resultado de cualquier operación es un conjunto matemático, y los conjuntos no permiten elementos repetidos. Si al eliminar columnas desaparece la clave primaria y dos filas resultan ser idénticas en los datos restantes, la proyección las fusiona en una sola fila.

- Demostraciones algebráica:
  - Anidación de proyecciones: Si hacemos una proyección sobre otra, la más externa mandará: $$\pi_{\text{Nombre}}(\pi_{\text{Nombre, Email}}(\text{Usuarios})) = \pi_{\text{Nombre}}(\text{Usuarios})$$

  Es decir:, si primero te quedas con 'Nombre y Email' y de ahí seleccionas solo 'Nombre', el resultado es exactamente el mismo que si desde el principio te hubieras quedado únicamente con 'Nombre'.
  - Intercambio con la Selección: ¿Se puede filtrar por filas ($\sigma$) antes o después de elegir columnas ($\pi$)?$$\pi_L(\sigma_P(\text{Tabla})) = \sigma_P(\pi_L(\text{Tabla}))$$Condición obligatoria: Solo se pueden intercambiar si la condición $P$ usa únicamente columnas que están dentro de la lista $L$. Si la condición necesita una columna que la proyección va a eliminar, estás obligado a hacer la selección ($\sigma$) primero.

  Ejemplo: No puedes pedir el $\text{Nombre}$ de los mayores de $18$ si antes proyectaste solo la columna $\text{Nombre}$, porque habrás perdido el dato de la $\text{Edad}$ para poder evaluar la regla.

### Renombrado y Asignación ($\rho$)

La idea clave es que esto es el equivalente a **renombrar** un archivo, es decir, no modifica los datos de la tabla sino que solamente cambia la "etiqueta" con la que nos referimos a la tabla o sus columnas

- La formula usada: $$\rho_{S}(\text{Tabla})$$
  - La tabla pasa a llamarse $S$. Sus columnas mantienen exactamente sus nombres originales.

- Cambiar el nombre de la tabla Y de sus columnas:$$\rho_{S(B_1, B_2, \dots, B_n)}(\text{Tabla})$$
  - La tabla pasa a llamarse $S$, y sus columnas cambian en orden a $B_1, B_2$...

- Guardar un resultado intermedio (Asignación):$$\text{VarTemporal} \gets \text{ExpresiónAlgebraica}$$
  Funciona exactamente como crear una variable en programación para no tener que escribir una fórmula gigante de una sola vez.

- Efecto que tiene en la tabla esta operaión:
  - El **grado** se mantiene igual.
  - La **cardinalidad** se mantiene igual.
  - El **contenido** no cambia.

- ¿Para qué se usa?
  - Para evitar la ambigüedad (Self-Join): Imagina que tienes una tabla Empleado con las columnas ID*Emp y ID_Jefe. Como el jefe también es un empleado, si quieres juntar la tabla consigo misma para ver el nombre del jefe de cada persona, el álgebra relacional se confundirá si ambas tablas se llaman Empleado. Usamos renombrado para crear un duplicado virtual:$$\rho*{\text{Jefe}}(\text{Empleado})$$

  - Para simplificar fórmulas largas: Si una consulta requiere 5 pasos, puedes ir asignando resultados intermedios:
    $$\text{Paso1} \gets \sigma_{\text{Ciudad}=\text{'Madrid'}}(\text{Usuarios})$$

  $$\text{ResultadoFinal} \gets \pi_{\text{Nombre, Email}}(\text{Paso1})$$

- ## Operaciones primitivas:

  Antes de sumar, restar o buscar coincidencias entre tablas, deben cumplir una condición obligatoriamente: **ser compatbiles de unión**.
  - Idea clave: Unir columnas que signifiquen lo mismo. Ejemplo: No puedes unir una lista de "Clientes" con una de "Vehiculos" porque no significan lo mismo. ("Comparar peras con peras y manzanas con manzanas").

  - Las dos reglas de compatibilidad que hay son las siguientes:
    - **Mismo grado**: Las 2 tablas deben tener excatamente el mismo número de columnas. ($G(R) = G(S)$).
    - **Mismos dominios**: El tipo de dato de la columna de una tabla deber ser el mismo que de la otra tabla. Es decir si la columna 1 de la primera tabla es "text" la columna 1 de la tabla 2 debe ser "text" y así sucesivamente.

**1. Unión ($\cup$):**

**Idea clave**: Juntar 2 listas en una. Ejemplo: Tenemos una lista de "alumnos mañana" y "alumnos tarde" y la juntamos en una lista "alumnos".

- Explicación de la fórmula:$$R \cup S = \{ t \mid t \in R \lor t \in S \}$$
  - $R \cup S$: La relación $R$ UNIDA a la relación $S$.
  - $t \in R \lor t \in S$: La fila final $t$ pertenece al resultado si está en $R$ O está en $S$ (o en ambas).

- Efecto en la estructura:
  - **Grado**: Se mantiene igual al de cualquiera de las dos tablas.
  - **Cardinalidad**: Elimina los duplicados automáticamente. Ejemplo: si un alumno cursa una misma asignatura en tanto en grupo mañanas como en grupo de tardes, solo aparecerá una vez al final.
    $$\max(C(R), C(S)) \le C(R \cup S) \le C(R) + C(S)$$

- Propiedades algebraicas:
  - **Conmutatividad**: $R \cup S = S \cup R$ (da igual el orden en el que untes las listas)
  - **Asociatividad**: $(R \cup S) \cup T = R \cup (S \cup T)$. (da igual juntar lista A y B y luego con C que A con B y C).

**2. Diferencia ($-$):**

**Idea clave**: Quitar de la primera lista los que aparezcan en la segunda. Ejemplo: Queremos ver los alumnos matriculados este año que NO estuvieran el año pasado.

- Explicación de la fórmula:
  $$R - S = \{ t \mid t \in R \land t \notin S \}$$
  - $R - S$: La relación $R$ MENOS la relación $S$.
  - $t \in R \land t \notin S$: La fila $t$ estará en el resultado si está en $R$ Y ADEMÁS NO está en $S$.

- Efecto en la estructura:
  - **Grado** se mantiene igual.
  - **Cardinalidad** En el mejor de los casos (ninguna fila de $S$ está en $R$) obtienes todas las filas de $R$. En el peor (todas las filas de $R$ están en $S$), obtienes 0 filas:$$0 \le C(R - S) \le C(R)$$

- **NO** es conmutativa.

**3. Intersección ($\cap$):**

**Idea clave:** Quedarse solo con los elementos comúnes. Ejemplo: quedarse con los alumnos que han estado matriculados los dos años.

- Explicación de la formula:
  $$R \cap S = \{ t \mid t \in R \land t \in S \}$$
  - $R \cap S$: La relación $R$ INTERSECTADA con $S$.
  - $t \in R \land t \in S$: La fila $t$ solo pasa el corte si existe en $R$ Y también en $S$.

- Demostración algebraica:
  La interseccion no es una operación primitiva porque se puede demostrar y construir usando una sola diferencia.
  $$R \cap S = R - (R - S)$$

- Efecto de la estructura:
  - **Grado** se mantiene igual.
  - **Cardinalidad**: Como máximo será igual a la tabla que menos fila tenga:
    $$0 \le C(R \cap S) \le \min(C(R), C(S))$$

- Propiedades algebraicas:
  - Es Conmutativa ($R \cap S = S \cap R$) y Asociativa.

**4. Producto Cartesiano ($\times$)**

**Idea clave**: Combinar absolutamente todo con todo. Es decir, coge cada una de las filas de la primera tabla y la pega individualmente con todas y cada una de las filas de la segunda tabla.

La diferencia fundamental entre la unión, diferencia e intersección:

- No requiere **compatibilidad de unión**

* Explicación de la formula:
  $$R \times S = \{ t_r \cdot t_s \mid t_r \in R \land t_s \in S \}$$
  - $R \times S$: La relación $R$ multiplicada cartesianamente por la relación $S$.
  - $t_r \cdot t_s$: Representa una fila resultante formada al encadenar/pegar los datos de la fila $t_r$ con los datos de la fila $t_s$.
  - $\mid t_r \in R \land t_s \in S$: Condición matemática que se lee: "tal que la fila $t_r$ pertenezca a la tabla $R$ Y la fila $t_s$ pertenezca a la tabla $S$".

* Efecto en la estructura de los datos:
  - **Grado**: Se **suman**. Si la tabla R tiene 3 columnas y la tabla S tiene 2, el producto tendrá 5 columnas.
    $$G(R \times S) = G(R) + G(S)$$

  - **Cardinalidad**: Se **multiplican**.ç
    $$C(R \times S) = C(R) \times C(S)$$

* Resolución de ambigüedades (Columnas con el mismo nombre):
  - Si la tabla Clientes tiene una columna llamada ID y la tabla Pedidos también tiene una columna llamada ID, el resultado no puede tener dos columnas idénticas.

Solución: Se añade el nombre de la tabla origen seguido de un punto antes del nombre del atributo: $\text{Clientes.ID}$ y $\text{Pedidos.ID}$.

- ¿Qué sentido tiene hacer esto?
  - Si multiplicas Alumnos $\times$ Asignaturas, el cartesiano conectará a cada alumno con todas las asignaturas del centro, incluso las que no cursa.
  - A primera vista parece inútil, pero es el bloque fundamental sobre el que se construye el Join / Reunión ($\bowtie$). La estrategia es:
    1. Haces el Producto Cartesiano para tener todas las combinaciones posibles.

    2. Aplican inmediatamente una Selección ($\sigma$) para filtrar y quedarte solo con las filas donde el ID del alumno coincide con el ID de la asignatura en la que está matriculado.

- Propiedades algebraicas:
  - Conmutatividad (salvo por el orden visual de las columnas): $R \times S \equiv S \times R$. La cantidad de filas y las combinaciones de datos son idénticas; solo cambia qué datos aparecen primero a la izquierda.
  - Asociatividad: $(R \times S) \times T = R \times (S \times T)$.

___ 
**5. Join ($\bowtie$)**:

La **idea clave** del join es pegar datos de dos tablas relacionadas mediante una regla

* Explicación de la fórmula y demostración:
        $$R \bowtie_{\theta} S = \sigma_{\theta}(R \times S)$$

    - $R \bowtie_{\theta} S$: Representa el Join entre la tabla $R$ y la tabla $S$ bajo la condición $\theta$.
    - $\theta$: Es cualquier condición lógica que utilice operadores de comparación ($=, \ne, <, \le, >, \ge$).
    - Demostración: No es una operación primitiva. El símbolo $\bowtie$ es simplemente una forma abreviada de escribir un Producto Cartesiano ($\times$) seguido inmediatamente de una Selección ($\sigma$).

* Efecto en la estructura de los datos:
    - **Grado**: Se suman las columnas de ambas tablas.
    $$G(R \bowtie_{\theta} S) = G(R) + G(S)$$
    - **Cardinalidad**: Depende de cuantas combinaciones cumplan la condición.


**6. Equi-Join ($\bowtie_{A=B}$)**:

La **idea clave** es que es un tipo específico de Join donde la condición utiliza unicamente el =.

- Explicación de la fórmula:$$R \bowtie_{R.A = S.B} S = \sigma_{R.A = S.B}(R \times S)$$


**7. Reunión Natural / Natural Join ($\bowtie$)**:

Es el Join más utilizado. Detecta automáticamente cuáles son los atributos que tienen el mismo nombre en ambas tablas, hace el Equi-Join por esa coincidencia y elimina la columna duplicada del resultado final.

- Explicación de la fórmula y demostración:Si $R(A, B, C)$ y $S(B, D)$ comparten la columna $B$:$$R \bowtie S = \pi_{A, R.B, C, D}(\sigma_{R.B = S.B}(R \times S))$$

  - Paso 1 ($R \times S$): Multiplica todas las filas.
  - Paso 2 ($\sigma$): Filtra dejando solo las filas donde la columna común $B$ valga lo mismo en ambos lados.
  - Paso 3 ($\pi$): Proyecta todas las columnas descartando la columna repetida ($S.B$), dejando solo $R.B$.

- Efecto en la estructura de los datos:
  - **Grado**: La suma de las columnas menos las columnas repetidas que se han unificado:
  $$G(R \bowtie S) = G(R) + G(S) - \text{Nº de columnas comunes}$$

- Propiedades algebráicas del Join:

  - **Conmutatividad**: $R \bowtie S = S \bowtie S$ (da igual qué tabla pongas a la izquierda o a la derecha; el resultado en datos es el mismo).

  - **Asociatividad**: $(R \bowtie S) \bowtie T = R \bowtie (S \bowtie T)$ (puedes unir 3 tablas en el orden que prefieras sin alterar el resultado).

**8. Division ($\div$)**:

**Idea clave**: Sirve para responder a consultas del tipo "para todo" o "encontrar quiénes han interactuado con TODOS los elementos de una lista". Por ejemplo: "Obtener los alumnos que se han matriculado de TODAS las asignaturas" o "Clientes que han comprado TODOS los productos del catálogo".

* Explicación de las tablas de origen:
  - Para aplicar $R \div S$, la relación $R$ debe contener dos tipos de atributos $R(X, Y)$ y la relación $S$ debe contener únicamente el tipo de atributo $S(Y)$. El resultado devolverá únicamente los valores de $X$.
    
* Explicación de la fórmula y demostración paso a paso:$$R \div S = \pi_X(R) - \pi_X((\pi_X(R) \times S) - R)$$

  - Para entender de dónde sale esta fórmula formal sin memorizarla a ciegas, se sigue esta lógica inversa:
  
  1. $\pi_X(R)$ (Todos los candidatos posibles): Extraes la lista de todos los alumnos que han cursado al menos alguna asignatura.
  
  2. $\pi_X(R) \times S$ (El escenario ideal perfecto): Creas una combinación teórica de cada alumno con absolutamente todas las asignaturas que existen en $S$.
  
  3. $(\pi_X(R) \times S) - R$ (Detectar lo que falta): A la combinación teórica perfecta le restas la realidad ($R$). El resultado son las asignaturas que a cada alumno le han faltado por cursar.
  
  4. $\pi_X(\dots)$ (Lista de alumnos incompletos): Proyectas los IDs de los alumnos que aparecieron en el paso anterior. Son los alumnos imperfectos (les falta al menos una asignatura).Resta final 
  
  5. $\pi_X(R) - \text{Imperfectos}$: A la lista de todos los alumnos posibles le quitas la lista de los alumnos incompletos. Lo único que queda son los alumnos que han cursado TODAS las asignaturas de $S$.

* Efecto en la estructura de datos:

  - **Grado**: La diferencia entre el número de columnas de R y S: $$G(R \div S) = G(R) - G(S)$$

  - **Cardinalidad**: Como máximo será igual a la cantidad de elementos distintos en X

  $$0 \le C(R \div S) \le C(\pi_X(R))$$

**9. Reuniones Externas (Outer Joins)**:

  * 1. **Left Outer Join (⟕)**:
  Mantiene todas las filas de la izquierda independientemente de si tienen coincidencia en la derecha o no.
    - Explicación de la fórmula:
    Explicación de la fórmula:$$R ⟕ S = (R \bowtie S) \cup \left( (R - \pi_{\text{Atributos}_R}(R \bowtie S)) \times \{\text{NULL}_S\} \right)$$

    - Ejemplo: "Obtener un listado de TODOS los clientes y sus compras (si un cliente nunca ha comprado nada, aparecerá en la lista con su información de cliente y las columnas de la compra vacías)".

  * 2. **Right Outer Join (⟖)**:
  Lo mismo que el Left Outer Join pero con las filas de la derecha.

  * 3. **Full Outer Join (⟗)**:
  No pierde información de ninguna de las dos tablas.
    - Explicación de la fórmula:
    $$R \text{ ⟗ } S = (R ⟕ S) \cup (R ⟖ S)$$

  Combina los resultados de conservar los elementos de la izquierda y los de la derecha. Si hay pareja, la muestra completa; si alguna fila de $R$ o de $S$ no tiene pareja en el otro lado, se conserva rellenando el lado opuesto con $\text{NULL}$.