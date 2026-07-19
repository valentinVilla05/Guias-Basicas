# Introducción a scripting 

Un **script** es un archivo de texto que contiene una lista de comandos de linux ordenados.

Muy útil para automaztizar tareas, copias de seguridad 

### ¿Cómo creamos un script?

Para crear un script tenemos que crear un archivo de extensión `.sh`. Por ejemplo:

> `touch primer_script.sh`

**Lo primero** que debemos escribir al crear un sript es la siguiente linea:

> `#!/bin/bash`

*(Esto es lo que le dice al sistema que lo que va debajo es un script)*

Para poner comentarios en un script ponemos: `#`

Si queremos que nos devuelva un mensaje usamos: `echo ""`

Vamos a practicar haciendo nuestro primer script que haga lo siguiente:
* a) Nos muestre un mensaje de iniciación
* b) Cree una carpeta llamada "mi_primer_script"
* c) Cree un archivo en esa carpeta llamado "mensaje_del_script.txt"
* **d) Meteremos el texto: "Hola, estoy creando mi primer script chachi-piruli" en el archivo creado en el apartado anterior**
* e) Entramos a la carpeta "mi_primer_script" y mostramos en que carpeta estamos 
* f) Mostramos el contenido del archivo
* g) Creamos una segunda carpeta llamada "segunda_carpeta"
* h) Movemos el archivo creado anteriormente a la nueva carpeta
* i) Listamos los archivos de la primera carpeta para confirmar que el archivo se ha movido 

*(Realizar ejercicio con los comandos básicos que hemos visto antes)*

#### ¿Cómo lo ejecutamos?

* Primero debemos darle al archivo los permisos de ejecución:

> `chmod +x primer_script.sh`

Una vez tenga los permisos necesarios lo ejecutamos "abriendolo":

> `./primer_script.sh`

El código debe quedar algo así:

> `#!/bin/bash` <br>
`rm -rf mi_primer_script/` <br>
`echo "Iniciando script"` <br>
`mkdir mi_primer_script` <br>
`touch mi_primer_script/mensaje_del_script.txt` <br>
`echo "Hola, estoy creando mi primer script chachi-piruli" >> mi_primer_script mensaje_del_script.txt'` <br>
`cd mi_primer_script/` <br>
`pwd` <br>
`cat mensaje_del_script.txt`<br>
`mkdir segunda_carpeta`<br>
`mv mensaje_del_script.txt segunda_carpeta/`<br>
`ls`<br>
`echo "Fin del script"`