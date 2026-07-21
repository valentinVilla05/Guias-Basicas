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

``` bash 
#!/bin/bash <br>
rm -rf mi_primer_script/ 

echo "Iniciando script" 

mkdir mi_primer_script 

touch mi_primer_script/mensaje_del_script.txt 

echo "Hola, estoy creando mi primer script chachi-piruli" >> mi_primer_script mensaje_del_script.txt' 

cd mi_primer_script/ 

pwd 

cat mensaje_del_script.txt

mkdir segunda_carpeta

mv mensaje_del_script.txt segunda_carpeta/

ls

echo "Fin del script"

```

---

Tambien podemos guardar variables de la siguiente manera:

> `variable="Esto es una variable"`

y luego la podemos usar como por ejemplo de la siguiente manera:

``` bash

#!/bin/bash

nombre="Me llamo Valentin"

echo "Hola, $nombre"
```
Importante que al asignar una variable **no podemos dejar espacios entre el `=`**

Evidentemente también podemos interactuar con el usuario en cuestión de la siguiente manera:

> `read <variable>`

Y esto se puede usar para cualquier cosa y no solamente en mensajes, por ejemplo, vamos a hacer un pequeño programa que te pregunte tu nombre y cree una carpeta con ese nombre:

``` bash
#!/bin/bash
echo "¿Como te llamas?"

read nombre

echo "Creando carpeta llamada: \"carpeta_de_$nombre \""

mkdir $nombre
```
---

#### Condicionales en bash.

Al igual que en cualquier lenguaje de programación en bash también podemos usar condicionales, bucles...

Para hacer un condicional en bash usamos lo siguiente:  

*(Programa que verifica si eres mayor de edad)*

``` bash
#!/bin/bash

echo "¿Qué edad tienes?"
read edad

if [ "$edad" -ge 18 ]; then
    echo "Eres mayor de edad"
else
    echo "Eres menor de edad"
fi

```

Vemos que la estructura para un condicional es:

``` bash
if [ condicion ]; then
    accion
else
    accion
fi
```

Es importante **el espacio entre los corchetes** para que funcione.
También es importante saber que aquí no se usan los operadores lógicos como '>', '<'... Sino que usamos:

* **`-ge`** = Greater or Equal (Mayor o igual que)

* **`-gt`** = Greater Than (Mayor que)

* **`-le`** = Less or Equal (Menor o igual que)

* **`-lt`** = Less Than (Menor que)

En caso de que queramos usar los operadores lógicos los podemos usar usando `(( ))` en vez de corchetes:

Vemos que la estructura para un condicional es:

``` bash
if (( edad >= 18 )); then
    accion
else
    accion
fi
```

Si queremos comprobar que una respuesta no esté vacia usamos el flag `-n` (not Empty)

> `[ -n "$respuesta" ]`

Otros flags utiles son:
* **`-f`** archivo: Comprueba si físicamente existe un archivo.

* **`-d`** directorio: Comprueba si existe un directorio.

[Más información del `if`](https://cheat.sh/if)

#### Bucles en bash.

La estructura para hacer un bucle `for` en bash es la siguiente:

*(Programa que crea 5 carpetas enumeradas)*
``` bash 
for NUMERO in {1..5} do
    echo "Creando la carpeta Carpeta_$NUMERO..."
    mkdir -p "Carpeta_$NUMERO"
done
```
[Más información del `for`](https://cheat.sh/for)

También tenemos el bucle `while`:

*(Programa que cuenta hasta llegar al 3)*
``` bash
CONTADOR=1

while [ $CONTADOR -le 3 ]; do
    echo "Contador en: $CONTADOR"
    CONTADOR=$((CONTADOR + 1))
done 
```

[Más información del `while`](https://cheat.sh/while)

---

### Argumentos en la linea de comandos

Cuando usamos sccripts lo normal es pasar los paramétros en la propia linea de comandos y no ir parando para preguntar al usuario.

Para capturar y usar esos datos dentro del script, Bash reserva unas **variables especiales**:

* **`$0`**: Guarda el nombre de tu propio script.
* **`$1`, `$2`, `$3`...**: Representan el primer, segundo, tercer parámetro que le hemos pasado.
* **`$#`**: Nos dice el **número total** de argumentos que se han introducido.
* **`$@`**: Contiene **todos** los argumentos pasados juntos en una lista.

¿Cómo se usa?

*(Ejemplo de script para hacer copias de seguridad rápidas)*

``` bash
#!/bin/bash

#Primero comprobamos que el usuario nos haya pasado 2 parámetros
if [ $# -lt 2 ]; then
    echo "Debes indicar ORIGEN y DESTINO"
    echo "Uso correcto: $0 <archivo_origen> <carpeta_destino>"
    exit 1
fi

# Asignamos las variables
ORIGEN=$1
DESTINO=$2

echo "Moviendo $ORIGEN a $DESTINO"
mv "$ORIGEN" "$DESTINO"
```
*(Pro tip: poner las variables en los comandos entre comillas por si hay algún archivo con espacios en el nombre, el script no fallará)*

### Switch case

Si tenemos que evaluar diferentes opciones usaremos un `case` :

``` bash
echo "1) Actualizar sistema"
echo "2) Limpiar papelera y temporales"
echo "3) Salir"

read OPCION

case $OPCION in
    1)
        echo "Actualizando"
        ;;
    2)
        echo "Limpiando archivos temporales"
        rm -rf /tmp/*
        ;;
    3)
        echo "Saliendo"
        ;;
    *) 
        echo "Opcion no válida"
        ;;
esac
```

[Más información del `case`](https://cheat.sh/case)

### Funciones en Bash

``` bash

#!/bin/bash

# Definimos la función
mostrar_header() {
    echo "=================================="
    echo "   $1"  # $1 aquí es el argumento que recibe LA FUNCIÓN, no el script
    echo "=================================="
}

mostrar_header "INICIANDO PROCESO"
mkdir -p test_dir

mostrar_header "PROCESO FINALIZADO"

```

### Control de errores

``` bash
#!/bin/bash

# Intentamos entrar a una carpeta
cd ~/CarpetaQueNoExiste 2>/dev/null

# Comprobamos si el comando anterior falló ($? diferente de 0)
if [ $? -ne 0 ]; then
    echo "Error: La carpeta no existe, no se puede continuar."
    exit 1
fi
```