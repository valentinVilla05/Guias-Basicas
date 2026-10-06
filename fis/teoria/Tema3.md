
# TEMA 3 **Análisis de Requisitos**

## **Importancia de la definición de Requisitos:** 

* Son la **base** para el **diseño** y la **implementación** en la ingeniería del software   
* Son una **lista completa** de las **propiedades** específicas y la **funcionalidad** que debe tener la aplicación expresada con **todo detalle**  
* Estos requisitos se **enumeran, etiquetan** y se **registra su traza** durante la implementación  
* Los **errores** más **numerosos**, **costosos** de reparar y que más tiempo consumen se dan **en esta fase** por lo que constituye una etapa fundamental para el éxito del proyecto

## **Marco de Referencia normativo** 

**ISO/IEC/IEEE 29148:2018**  
`System and software engineering - Life cycle processes - Requires engineering`. Es el **estándar de referencia para la ingeniería de requisitos y sustituye a normas más antiguas** (IEEE 830\) como marco habitual para especificar requisitos software (ERS/SRS)

**SWEBOK v4.0a — Área Software Requirements**  
Estructura la disciplina en cinco subáreas: 
    
1. Fundamentos de requisitos
2. Obtención 
3. Análisis
4. Especificación 
5. Validación de requisitos

### **Ingeniería De requisitos**  
Proceso para establecer los servicios que el cliente requiere de un sistema junto con las restricciones de funcionamiento bajo las que será desarrollado 

### **Requisito:** 

* Conjunto de **propiedades** o **restricciones** definidas con precisión, que un sistema software debe satisfacer  
* Puede estar definido como un **requisito de alto nivel** que se irá concentrando a lo largo del proceso o puede ser una función matemática perfectamente definida 

### **Características de un buen requisitos**

* **Necesario**: su eliminación causaría una carencia que ningún otro requisito cumple  
* **Libre de solución:** describe que debe hacer el sistema, nunca como construirse   
* **No ambiguo:** admite una única interpretación  
* **Completo:** no necesita información adicional para entenderse  
* **Singular**: Expresa una única idea, no varias mezcladas en la misma frase  
* **Factible**: puede implementarse con la tecnología, presupuesto y plazo disponibles   
* **Verificable**: existe alguna forma de comprobar que se ha cumplido 


### **Análisis de requisitos**

* Podemos definirlo como el **proceso de entender y documentar** que es lo que debe hacer un sistema  
* No se refiere al como debe hacerse algo en un sistema, sino al **que debe hacerse**

### **Especificación de requisitos:**  
**Documento final entregable** donde deben quedar perfectamente numerados, especificados y detallados **todos y cada uno de los requisitos** que debe reunir un sistema 

### **Características del listado de requisitos**  
Además de que cada requisito individualmente sea bueno , el conjunto (especificación) debe cumplir estas propiedades:

* **Completo**: recoge todos los requisitos relevantes , funcionales y no funcionales  
* **Consistente**: ningún requisito contradice a otro   
* **Correlacionable (traceable):** cada requisito se vincula hacia atrás (su origen) y hacia delante (diseño,código,prueba)  
* **Asequible:** el conjunto puede desarrollarse con los recursos y el presupuesto disponibles  
* **Priorizado**: se distingue que requisitos son esenciales de cuales son deseables  
* **Comprensible**: redactado a un nivel de detalle y lenguaje asequible

> Ejemplo del qué (requisito)  
El sistema permite que el cliente pueda consultar los vuelos en una fecha concreta entre dos ciudades

> Ejemplo del cómo (no requisito)  
Los vuelos se almacenan en una tabla llamada vuelos en una base de datos de Oracle 

## **Tipos de requisitos:** 

* **Requisitos funcionales:** describen lo que hace un sistema o lo que se espera que haga: **funcionalidad**  
* **Requisitos no funcionales:** relacionados con el grado de cumplimiento de los funcionales  
* **Requisitos de facilidad de uso:** permiten asegurar que existe un buen acoplamiento del sistema desarrollado con usuarios del sistema y con las tareas que deben realizar cuando lo utilizan

Los requisitos funcionales y no funcionales son categorías convencionales en el análisis y diseño de sistemas. La facilidad de uso es ignorada en proyectos de desarrollo de sistemas 

### **Expresión de requisitos funcionales:**

* **Lenguaje natural no estructurado**: sin plantilla fija. Forma más habitual pero la más expuesta a la ambigüedad  
* **Lenguaje natural estructurado:** sigue una plantilla fija , reduce ambigüedad y facilita comparar y gestionar los requisitos. Es la más extendida

**El formato ágil de expresar un requisito funcional**
> Como \<rol\>, quiero \<acción\> para \<beneficio\>

* Forma más extendida de **RF en lenguaje natural estructurado:** sigue siempre la misma plantilla propia   
* **Complementada:** no sustituye a la especificación formal (ERS/SRS)   
* Cada historia se completa con **criterios de aceptación**   
* El **prototipado** es también una técnica de búsqueda de requisitos : un prototipo interactivo ayuda a validarlas con cliente 

### **Plantilla EARS:**  
La plantilla **EARS** (`Easy Approach to Requirements Syntax`) fija unos pocos esquemas según el tipo de comportamiento que se describe:

* Ubico: “El \<sistema\> deberá \<respuesta\>”  
* Dirigido por evento: “Cuando \<evento\>, el \<sistema\> deberá \<respuesta\>”  
* Dirigido por estado: “Mientras \<estado\> , el \<sistema\> deberá \<respuesta\>”

### **Requisitos no funcionales:**  
Habitualmente están relacionados con restricciones a tener en cuenta en relación con los requisitos del sistema

* **Criterios de rendimiento:** tiempos de respuesta deseados para la actualización de datos en el sistema o para la obtención de datos del sistema  
* **Previsión del volumen de datos:** bien en términos de circulación de datos o de los que deben almacenarse  
* **Consideraciones de seguridad** 

### **Medidas para requisitos no funcionales:**

* **Velocidad**: Tiempo de respuesta, transacciones por segundo..  
* **Tamaño**: Megabytes..  
* **Facilidad de uso:** Tiempo de entrenamiento..  
* **Confiabilidad**: Frecuencia de fallo , ratio de disponibilidad..  
* **Robustez**: tiempo para recuperarse de un fallo, porcentaje de eventos que pueden causar fallo..  
* **Portabilidad**: Porcentaje de sentencias dependientes de un sistema  
* **Seguridad**: confidencialidad, integridad y disponibilidad…  
* **Privacidad y protección de datos.** Cumplimiento del RGPD / GDPR en el contexto europeo, si bien fuera de la Unión Europea es necesario estudiar la normativa específica de protección de datos de cada país  
* **Accesibilidad**: Cumplimiento de pautas WCAG (Web Content Accessibility Guidelines) cada vez más exigidas por normativa  
* **Sostenibilidad y eficiencia energética:** requisito no funcional emergente cada vez más presente en el desarrollo software actual 

## **Definición de facilidad de uso dada por ISO**  
Grado en que usuarios específicos pueden conseguir objetivos específicos dentro de un entorno determinado de forma eficaz, eficiente , confortable y aceptable

**Debemos reunir:**

* **Características de los usuarios** que usarán el sistema  
* **Tareas que realizarán los usuarios** : objetivos que tratan de conseguir..  
* **Factores situacionales:** que describen las situaciones que pueden surgir durante la utilización del sistema  
* **Criterios de aceptación** mediante los cuales el usuario valorará el sistema entregado

La facilidad de uso no es un aspecto aislado: conviven con ella otras dos familias de requisitos:

* **Requisitos tecnológicos:** compatibilidad con distintos navegadores o sistemas operativos   
* **Requisitos de calidad de servicio:** Rendimiento (t de respuesta) , disponibilidad o fiabilidad


**Técnicas de búsqueda de requisitos:**

Qué debe hacerse con cada requisito:

    * Expresarse de modo adecuado  
    * Ser de acceso sencillo  
    * Numerarse  
    * Acompañarse con pruebas que lo verifiquen  
    * Tomarse en cuenta en el diseño  
    * Tomarse en cuenta en el código  
    * Probarse de forma aislada  
    * Probarse junto con otros requisitos  
    * Validarse con las pruebas después de construirse la aplicación

**Técnicas de búsqueda de requisitos:**

    1. Lecturas preparatorias  
    2. Entrevistas  
    3. Observación  
    4. Muestreo de documentos  
    5. Cuestionarios

\> Son denominadas :`SQIRO (Sampling, Questionnaires, Interviewing, Reading and Observation`) 

**1. Lecturas preparatorias:**

**Objetivo** : Entender bien la organización así como los objetivos de negocio  
**Incluye:**

* Informes de la empresa  
* Gráficos de la organización  
* Manuales de normativas  
* Descripciones de trabajos  
* Informes  
* Documentación de los sistemas existentes

**Ventajas:**

* Ayudar a conocer la organización antes de reunirse con las personas que trabajan en ella  
* Permiten preparar otro tipo de búsqueda de hechos  
* La documentación del sistema existente puede ayudar a identificar requisitos para funcionalidades del nuevo sistema

## **Entrevistas:**

> **Objetivo:** Obtener un profundo conocimiento de los objetivos de la organización, los requisitos de los usuarios y los roles de cada persona  
* Permite obtener información:  
  * De la dirección sobre los objetivos de la organización del nuevo sistema  
  * De la plantilla sobre sus trabajos actuales y sus necesidades de información  
  * Del público los compradores como posibles usuarios del sistema

**Directrices:** Requieren una buena planificación, buenas habilidades para las relaciones interpersonales y una mente abierta y ágil. Se debe tener en cuenta:

* Antes de la entrevista  
* Al principio de la entrevista  
* Durante la entrevista  
* Después de la entrevista

**Antes de la entrevista:**

* Citar a los entrevistados con antelación  
* Informar sobre la duración aproximada y temática  
* Preparar un calendario de entrevistas en términos de puestos de trabajo   
* Deberá ser el director quien decida que personas intervienen por puesto de trabajo en cada entrevista  
* Planificar, seleccionar y escribir las preguntas

**Al llegar a la entrevista:**

* Llegar temprano y no excederse del horario programado  
* Pedir permisos al entrevistado antes de grabar o tomar notas  
* Tomar notas incluso si utiliza grabadora

**Durante la entrevista:** 

* El entrevistador debe controlar la entrevista  
* Si el entrevistado se desvía del tema debe hacerle volver con sutileza  
* Utilizar distintos tipos de preguntas según el tipo de información \-\> abiertas o cerradas  
* Mantener un enfoque positivo y animar al entrevistado en sus explicaciones de puntos clave  
* Ser sensible sobre la utilización de la información obtenida en otras entrevistas , especialmente si hay comentarios negativos o críticos  
* Aprovechar para obtener ejemplos de documentos  
* Agradecer al entrevistador el tiempo concebido  
* Enviar una copia con las anotaciones al entrevistado para comprobar las notas  
* Transcribir las grabaciones y pasar a limpio las notas lo antes posible  
* Actualizar las anotaciones utilizando los comentarios del entrevistado

**Ventajas:**

* Permite al analista adaptarse a lo que dice el usuario. Generan información de gran calidad  
* Permiten al analista indagar con gran profundidad sobre el trabajo de cada persona implicada

**Desventajas:**

* Requieren bastante tiempo y son costosas de preparar  
* Es necesario transcribir las grabaciones o pasar a limpio las notas  
* El entrevistado puede sentirse presionado  
* Puede convertirse en info conflictiva

### Observación:  
>Objetivo: Permite observar qué realmente sucede y no sólo quçé se dice en las entrevistas que sucede

**Incluye:**

* Observar como las personas realizan sus tareas  
* Observar que documentos se utilizan realmente  
* Obtener datos cuantitativos como base para mejoras en el nuevo sistema  
* Observar las posibles relaciones entre distintas tareas  
* Calcular el tiempo que se invierte en una tarea  
* Comprobar el número de errores que se cometen con el sistema actual como base para el diseño de la facilidad de uso

**Ventajas:**

* Ofrece una idea real de cómo funciona el sistema  
* Permite obtener un alto nivel de validación de los datos  
* Permite verificar información de otras fuentes  
* Permite obtener datos básicos sobre el funcionamiento del sistema existente y de los usuarios

**Desventajas:**

* A la gente no le gusta ser observada  
* Requiere entrenamiento y capacitación por parte del observador  
* Problemas logísticos si el equipo trabaja a turnos o tiene que desplazarse grandes distancias para hacer su trabajo  
* Problemas éticos: si el trabajador maneja datos personales o privados o trabaja con el público

### Muestreo de documentos:  
**Objetivo:**

* Determinar la información que realmente utiliza el personal en su trabajo  
* Realizar análisis estadístico de los documentos para localizar patrones de datos

**Incluye:**

* Obtener copias de documentos vacíos y rellenos  
* Conocer la distribución de las líneas en una orden de pedido  
* Capturas de pantalla del sistema existente

**Ventajas:**

* Obtener datos cuantitativos como el número medio de líneas de una factura o el rango de valores   
* Permite calcular porcentajes de error en documentos en papel

**Desventajas:**

* No ayuda si el sistema va a cambiar drásticamente

### Cuestionarios:  
**Objetivo:**

* Obtener el punto de vista de un gran número de personas de manera que permitan su análisis estadístico

**Incluye:**

* Cuestionarios por correo, en web o email  
* Cuestiones de abierto y cerrado  
* Recogida de opiniones y hechos

**Ventajas:**

* Recogida económica de datos a partir de un número elevado de personas  
* Forma efectiva de recogida de información de gente geográficamente dispersa   
* Análisis automático de resultados si el cuestionario está bien diseñado

**Desventajas:**

* Los buenos cuestionarios son difíciles de diseñar  
* No existe un mecanismo automático para profundizar en los resultados aunq esto puede hacerse mediante entrevistas posteriores personales o telefónicas  
* La respuesta a cuestionarios postales puede ser lenta

## Técnicas ágiles y complementarias:  
>Las técnicas SQIRO siguen siendo necesarias pero no suficientes en un contexto ágil y de producto digital. Se combinan hoy con:

* User story mapping: mapa visual de historias de usuario  
* Talleres colaborativos / Design Thinking: dinámicas de definición de producto centradas en el usuario  
* Prototipado: Como técnica de búsqueda de requisitos  
* Analítica de datos y A/B testing: requisitos derivados del uso real del sistema  
* Búsqueda de requisitos asistida por IA generativa

### User story mapping:  
Técnica que organiza las historias de usuario en un **mapa visual de dos dimensiones**, muy útil para planificar qué incluir en cada incremento del producto:

* En la `fila superior` se colocan las **grandes actividades** del usuario en el orden en que ocurren  
* `Bajo cada actividad` se colocan sus **historias de usuario ordenadas** de arriba abajo por prioridad  
* `Trazando una línea horizontal` se define **qué historias entran** en el primer incremento (release) y **cuales quedan** para incrementos posteriores

### Talleres colaborativos y Design Thinking:  
Es una metodología de **resolución de problemas centrada en el usuario** que se organiza típicamente en 5 fases:
```text
1. Empatizar (entender al usuario) 
2. Definir (delimitar el problema) 
3. Idear (generar posibles soluciones) 
4. prototipar 
5. Testear (validar con usuarios reales)
```

* se aplica en **talleres colaborativos (workshops)** de definición de producto  
* Suelen apoyarse en **pizarras digitales colaborativas** : Miro, Mural , Fig JAm

### Prototipado como técnica de búsqueda de requisitos:  
**Validar un prototipo interactivo con usuarios reales, antes de construir el sistema**, permite descubrir y corregir requisitos mal entendidos a muy bajo coste

**Herramientas habituales de prototipado**

* `Figma y Adobe XD`: prototipos de alta fidelidad , navegables e interactivos  
* `Balsamiq`: prototipos de baja fidelidad (wireframes útiles en las primeras conversaciones con el cliente  
* `Pen Pot`: alternativa de código abierto a figma

**Analítica de datos y A/B testing**  
Cuando el sistema ya existe , su propio uso real es una fuente de requisitos: la analítica de datos revela que funcionalidades se usan (o no) en el A/B testing compara dos variantes del sistema con usuarios reales para decidir cual cumple mejor un objetivo

**Búsqueda de requisitos asistidas por IA generativa:**

* Generación de borradores de historias de usuario o de preguntas de entrevista a partir de documentación existente  
* Apoyo en la síntesis de resultados de cuestionarios o de sesiones de observación  
* Sigue siendo imprescindible la validación humana

**Gestión y trazabilidad de requisitos**

Numerar y registrar la traza de un requisito ya no es solo una anotación manual \-\> se apoya en herramientas de gestión de requisitos 

* `Jira y Azure DevOps`: Vinculan requisito \-\> historia de usuario / tarea \-\>  commit de código \-\> caso de prueba  
* `Herramientas específicas de gestión de requisitos`: IBM DOORS, Jama connect  
* `Cierran el ciclo de trazabilidad de extremo a extremo`: La gestión puramente documental solo contemplaba de forma conceptual 
