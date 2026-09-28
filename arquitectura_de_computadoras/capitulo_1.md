# Capitulo 1 del Manual de Ripes - AC

En las prácticas trabajamos con lenguaje ensamblador de la **ISA RISC-V** y sus registros usando el simulador **Ripes**.

ISA (_Intstruction Set Architecture_) es la interfaz que determina cómo (mediante software) se controla el hardware de un microprocesador.

Las partes de **ISA** son:

- El **banco de registros**
- Los **modos de direccionamiento**
- El **conjunto de instrucciones**

## Banco de registros

Los registros son pequeñas porciones de memoria interna cuya finalidad es mantener temporalmente los datos con los que se opera y los resultados que producen las operaciones. En **RV32I** (nuestra arquitectura) contamos con **32 registros** de **32 bits**. Están enumerados de x0 a x31.

Cada uno de estos registros se usa para fines específicos segun una convención para el desarrollo de compiladores para RISC-V, llamada ABI (_Application Binary Interface_)

![tabla de registros](images/registros.png)

#### ¿Cual es el propósito de cada registro?

| Nombre            | Alias    | Uso                                                                     |
| ----------------- | -------- | ----------------------------------------------------------------------- |
| **x0**            | zero     | Siempre contiene el valor 0 (útil para operaciones)                     |
| **x1**            | ra       | (return addres) Es una dirección de retorno                             |
| **x2**            | sp       | (stack pointer) Puntero de pila                                         |
| **x3**            | gp       | (global pointer) Puntero Global                                         |
| **x4**            | tp       | (thread pointer) Puntero de hilo                                        |
| **x5** a **x7**   | t0 a t2  | (Temporary) Guardamos valores temporales                                |
| **x8**            | s0/fp    | (saved register/frame pointer) Registro preservado / Puntero de _frame_ |
| **x9**            | s1       | Registro preservado                                                     |
| **x10**, **x11**  | a0 a a1  | Parámetro de función o Valor de retorno                                 |
| **x12**, **x17**  | a2 a a7  | Parámetro de función                                                    |
| **x18** a **x27** | s2 a s11 | Registro preservado                                                     |
| **x28** a **x31** | t3 a t6  | Valores temporales                                                      |

(falta explicar un poco más los registros, sigo esta tarde)

## Conjunto de instrucciones

El conjunto de instrucciones que necesitamos para escribir programas también cambia según las extensiones de la ISA

![tabla](images/instrucciones.png)
