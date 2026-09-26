# Practica 2
> Recordatorio : En esta práctica sobre todo hay que aprender como funciona el ejecutor de ordenes **Nano** y otra serie de comandos necesarios para obtener información sobre hilos y demás

## Formas para programar en la terminal
Para programar desde la terminal se pueden usar **Tres métodos principales**. Cada uno tiene funciones distintas como editar archivos, probar código linea a linea o generar código mediante IA, como en la práctica lo más relevante y lo único que usaremos de momento es Nano solo profundizaremos en este

## Ordenes Útiles
| Orden | Uso | 
| -- | -- |
| **pwd** | muestra el directorio de trabajo |
| **cd [dir]** | sirve para desplazarse al directorio que queramos |
| **more fichero** | muestra el contenido de un fichero de texto pantalla por pantalla (paginado) |
| **cat fichero** | muestra todo el contenido de un fichero de golpe en la terminal |
| **cp** | sirve para copiar ficheros | 
| **mv** | sirve para desplazar ficheros | 
| **rm** | sirve para borrar ficheros
| **man orden** | es un manual que nos premite consultar que hacen las órdenes **Es muy importante saber usarlo** |
| **touch** | sirve para crear un fichero desde 0 | 
| **whatis orden/es** | se puede obtener una descripción breve sobre lo que hace cualquier orden |
| **whereis orden/es** | se usa para localziar los archivos binarios de código fuente y de manual de un comando | 
| **whoami** | muestra la identidad del usuario | 
| **hostname** | muestra el nombre de la computadora a la q nos hemos conectado |
| **uname** | muesra info relacionada al SO |
| **wc** | Sirve para contar, si ponemos `wc -c` cuenta bytes, `wc -m`cuenta caracteres, `wc -w` cuenta palabras y `wc -l` cuenta lineas |
| **echo** | mostrar una línea de texto / cadena de una salida estandar|


## Nano (Para crear y editar archivos)
Es un programa que ejecutamos directamente desde la consola, sin necesitar el ratón ya q todo es por combinación de teclas
> Esta es de las más importantes y las que más usaremos

**1. Crear o abrir un archivo**:
nano programa.cpp

**2. Escribir Código**: escribimos como lo haríamos normalmente en CLion y VisualStudio 

**3. Menú de funciones en Nano**:
![nano](imagenes/nano.png)

Las funciones que más usaremos són la de Guardar: `^ O`y Salir: `^ X` 

### Ejemplo de Programa en nano

Voy a crear un ejemplo en Nano para poder ver como podemos guardarlo y cargarlo desde la terminal hasta que compile correctamente

**Paso 1**: nano ejemplo.cpp 
![ejemplo 1](image-1.png)
**Paso 2**: Como ya he escritor mi código hago `Control O` , `Enter`para volver al menú y finalmente `Control X`.

**Paso 3**: Hemos vuelto a la terminal y hemos guardado nuestro código 

**Paso 4: COMPILAR**: Como vamos a usar c++ para programar tenemos que poner el siguiente comando:
> g++ ejemplo.cpp -o ejemplo

**¿Qué es -o?**: Es un parámetro que significa *output* o *salida* para indicarle el nombre del ejecutable que queremos crear 

**Paso 5: Ejecutar como programa final**: Para ejecutar el programa tenemos que poner `./`y el nombre del ejecutable

![ejemplo terminao](image.png)

Como podemos ver, en tan solo **3 comandos** hemos creado, compilado y ejecutado nuestro código

## Operadores de redrección 
| Operador | Tipo | Qué hace | Ejemplo |
| :---: | :--- | :--- | :--- |
| `>` | Salida (`stdout`) | **Sobrescribe** archivo con la salida normal | `ls -l > lista.txt` |
| `>>` | Salida (`stdout`) | **Añade** la salida normal al final | `ps -ef >> procesos.txt` |
| `2>` | Errores (`stderr`) | **Sobrescribe** archivo solo con errores | `g++ main.cpp 2> errores.log` |
| `2>>` | Errores (`stderr`) | **Añade** los errores al final | `g++ main.cpp 2>> errores.log` |
| `&>` | Todo (`stdout` + `stderr`) | **Sobrescribe** con salida normal y errores | `g++ main.cpp &> todo.log` |
| `<` | Entrada (`stdin`) | Usa un archivo como entrada del comando | `sort < lista.txt` |
| `<<` | Entrada (`stdin`) | Lee texto introducido hasta llegar a un delimitador | `cat << FIN` |
| `<>` | Entrada y Salida | Usa un archivo como entrada y salida a la vez | `cmd <> archivo.txt` |


## Interconexiones (Pipes)
Un **pipe** o **tubería** (`|`) permite **conectar comandos en cadena**: La salida de un comando se convierte en la entrada de otro

### Flujo de datos Continuo
Sin tuberías, si quieres procesar datos en varios pasos, tienes que guardar archivos intermedios en el disco. Con tuberías, la información fluye por la memoria de un comando a otro sin guardar nada en medio

**Sin tubería**
```text
Comando 1  --->  Guarda en archivo.txt  --->  Comando 2 lee archivo.txt
```

**Con Tubería**
```text
Comando 1  ===[ tubería | ]===>  Comando 2  ===[ tubería | ]===>  Comando 3
```


## Resolución de los Ejercicios y Explicación

### EJERCICIO 1
Si ejecutamos los códigos que nos pone haciendo lo que hemos comentado previamente de nano quedaría algo así
![alt text](image-2.png)

> fork() lo que hace es duplicar el proceso actual para crear un **proceso hijo** idéntico que se ejecuta en paralelo al proceso padre

Para hacer el ejercicio que nos piden tenemos que crear un código similar a este:

![alt text](image-3.png)

Nos dará un resultado similar a este: 

![sol](image-4.png)

### EJERCICIO 2
Nos pide hacer un programa que actue como la función `echo` que lo que hace es mostrar una línea de texto

![alt text](image-6.png)

**Explicación**
* Le tenemos que pasar por la cabecera `argc` que indica el número de elementos de un array y luego char* `argv[]` que actua como un vector

* Empezamos por i=1 ya que i=0 siempre será el nombre de nuestro programa


**Resultado**
![alt text](image-7.png)

* Como podemos ver en el primer caso si le pasamos `./eco a b` hace un simple cout con a y b 

* Si hacemos un `./eco *` muestra todos los archivos dentro de ese directorio 

* Por otro lado si hacemos `./eco \*` si se muestra el `*` ya que la barra invertida sirve como un **carácer de escape** que le dice a la terminal que no haga caso al significado especial del caracter que pongamos y lo trate como un texto normal

### EJERCICIO 3
Nos pregunta por los valores de ejecutar cat a b>x

* argc=3 ya que es el número total de elementos
* argv contiene: 
    * argv[0]="cat"
    * argv[1]="a"
    * argv[2]="b"

**Por qué no se incluyen ni `>` ni `x`?**

El operador `>` es una redirección de la terminal, no un argumento

1. Si escribimos cat a b>x la terminal capta el `>` antes de lanzar el programa
2. La terminal abre o crea el archivo `x`
3. La terminal ejecuta cat solo pasandole los nombres a y b

![](image-8.png)

como no tenemos nada pues no tenemos nada como a o b pues simplemente nos dice que no existe, pero si nos metemos con **cat x** si nos muestra que están dentro de este

### EJERCICIO 4
![](image-9.png)

**Explicación**:
La shell procesa la redirección `>` antes de ejecutar la orden, woh no es un comando que exista pero crea el fichero en disco `usuarios` y luego ejecuta la orden


**Demostración de los 0 bytes**

![alt text](image-10.png)

Podemos ver que el fichero existe y también podemos ver los permisos que tiene este, pero el tamaño es `0`

### EJERCICIO 5

En este ejercicio nos piden que conectemos el comando `head` y `tail` para ello tenemos que utilizar `|`

Como nos piden mostrar las 3 primeras líneas tenemos que ejecutar `head -n 3` ya que por defecto mostraría las 10 primeras

```bash
head -n 3 /etc/passwd | tail -n 1
```

**Explicación**
* `head -n 3 /etc/passwd`: lee el archivo `/etc/passwd` y extrae las 3 lineas 
* `|` en lugar de imprimir las 3 las envia directamente como entrada 
* `tail -n 1`: recibe las 3 primeras lineas y se queda con la última