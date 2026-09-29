# Capitulo 2: Bucles y Condicionales

La posibilidad de ejecutar o salir de cierto bloque de instrucciones según que se cumpla una determinada condición la haremos con bucles if o else con ensamblador mediante la **alteración del flujo del programa** que permite cambiar el contenido del **contador de programa**.

## Instrucciones de salto
modifican `pc` asingandole un valor general que será simbolizado por `etiquetas` sin tener que calcular manualmente las distintas direcciones

A las instrucciones anteriores de la tabla le añadiremos otras 8 más que serán las instrucciones de salto

| Instrucción | Condición | 
| -- | -- |
| `beq` rs11,rs2,imm | salta si rs1=rs2 | 
| `bne` rs1,rs2,imm | salta si rs1 $!=$ rs2 |
| `bge` rs1,rs2,imm | salta si rs1 $>=$ rs2 |
| `bgeu` rs1,rs2,imm | igual que `bge` pero sin signo |
| `blt` rs1,rs2,imm | salta si rs1 < rs2 |
| `bltu` rs1,rs2,imm | Igual que la anterior pero sin signo |

El valor inmediato determina a donde debe saltar `pc` en el caso que se cumpla la condición sobre ambos registros 

también se definen otras seudoinstruccinoes como `bgt`, `bgtu`, `ble` y `bleu`,
que toman los mismos argumentos que las instrucciones previas, y `beqz`, `bnez`,
`bgez`, `blez` y `bgtz` en las que rs2= `zero` **SIEMPRE** 

La seudoinstrución `bnez` compara el contenido de `a0` con el registro `zero` y si no coinciden , ejecuta el salto de forma que el bcucle se repeitŕa hasta que `a0` contenga `0`

## Saltos Incondicionales

* `jal` rd, imm : Es de tipo U que cuenta con 2 operandos. En rd se guarda el contenido de `pc`y después se actualizará asignandole la suma de `rs + imm` 

Como primer parámetro podemos usar el registro `ra` (`x1`) para la seudoinstrucción `jal` imm -> `jal` x1,imm de forma q no es obligatorio expresar de forma explicita elr egistro de destino. o también lo podemos hacer a otros puntos como `jal x0, imm` 

**Diferencias entre `jal` y `jalr`** 

* `jalr` no suma el desplazamiento a `pc` sino que se asgina con `rs + imm` . 

## Llamadas a Subrutinas
`call` prepara en el registro `ra` la dirección base que será la de `pc` y salta al punto indicado

`ret` toma a `ra` la dirección de rentorno, enviando a `x0` el actual valor de `pc`

## Otras instrucciones

### Instrucciones Lógicas
* se usan las que hemos visto anteriormente: `and`, `andi`.... Y se añaden otras

| Instrucción | Funcionamiento | 
| -- | -- | 
| `sll` rd,rs1,rs2 | Desplaza el valor en rs1 hacia la izquierda tantos bits como rs2 y guarda en rd | 
| `slli` rd,rs1,imm |  Igual pero con un valor inmediato |
| `srl` rd,rs1,rs2 | desplaza el ocntenido de rs1 hacia la derecha tantos bits indique `rs2` y guarda en rd | 
| `srli` | igual pero conn inmediato |
| `sra` rd, rs1,rs2 | desplaza el contenido de `rs1` hacia la der tantos bits como indique `rs2` y tomando el bit de signo |


### Instrucciones de comparación 
**Estas no alteran el valor de `pc`** se limitan a almacenar `0` o `1` 

*(son las instrucciones anteriores con la siguiente consideración)*

> El valor de `rs1` debe ser siempre menor que el de `rs2` o `imm`

### Otras seudoinstrucciones

* `not` rd,rs: complemento a uno de rs y almacena en rd
* `neg` rd,rs: complemento a 2 de rs y almacena en rd
* `nop` no hace nada solo consume uno o más ciclos de reljo

### ---Recordatorio---

**complemento a uno**: invierte todos los bits 
**complemento a dos**: invirtiendo todos los bits y sumando 1

## Almacenamiento temporal de datos en la pila

Una función puedem odificar cualquiera de sus registros temporales: `t0` a `t6` o registros `a0` a `a7` . Si el codigo tiene interés en el contenido de alguno de estos registros se debe preservar y ser conservados . Como esta necesidad es teporal solo pse precisa mientras dura la ejecución -> serán almacenados en la pila (`sp`)

**Pasos**
**1. Reservar en la pila el espacio necesario**: como crece hacia **abajo** tenemos q restar el valor a `sp` y siempre ha de ser un múltiplo de 16

**2. Guardar el contenido en registros apropiados**: Se usa el registro sp y un desplazamiento

**3. Realizar la tarea que la función tenga encomendada**

**4. Restaurar el contenido de los registros del paso 2 en `sp`**

**5. Ajustar el registro `sp` para liberar el espacio del paso 1**

----
Poner ejemplo más claro que en apuntes y explicar
---

## La pila para tranferir parámetros a funciones
El núm de registros de la CPu es limitado por lo que será preciso recurrir a la memoria para almacenar datos, (se usará en funciones con muchos parámetros)

Hasta 8 registros de `a0` a `a7` están destinados a facilitar la transferencia de parámetros al invocar a una función . **SE USAN EN ORDEN**; si solo necesitamos 2 -> `a0` y `a1`

----
IGUAL
----

## Funciones recursivas y la pila
Cuando escribimos una función de lenguaje de alto nivel , el compilador se ocupa de generar en cada llamada a la misma lo que se conoce como `stack frame`, estas funciones serán escritas sobre todo en `C` debido a la complejidad , por ejemplo para calcular un factorial

```c
int factorial(int n){
    if(n==1)
        return n;
    else
        return n*factorial(n-1)
}
```

![alt text](/images/factorial.png)

Un compilador en C produce el código ensamblador preciso para ir ajustando el registro `sp`, almacenar y extraer datos de la pila. Y se tendrá que implementar de forma manual:

![alt text](/images/imfacto.png)

Las tres primeras líneas hacen `stack frame` y gaurdan en la pila la dirección de retorno y valor actual del parámetro de entrada. Después se actualiza ese parámetro y con un condicional se determina si ha alcanzado el caso base. Se produce una nueva llamada a la misma función si no se da el caso. Al llegar al caso base se recupera de la pila el parámetro y se hace la operación correspondiente

