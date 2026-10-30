# 08- Programación en Shell.Ejecución condicional de órdenes.

## 1. La Estructura Condicional `if-then-else`

Permite la ejecución condicional de órdenes dentro de un shell script. La palabra `if` es una palabra clave reservada del sistema, no un comando externo

### Sintaxis básica:

```bash
if [ condicion ]
then
    # Se ejecuta si la condición es VERDADERA
else
    # Se ejecuta si la condición es FALSA
fi
```

1. **Espacios en los corchetes:** Es obligatorio dejar un espacio en blanco tras el primer corchete `[` y antes del último `]`
   * `if [-d $DIR]` *(Error: `[-d: no se encontró la orden`)*
   * `if [ -d $DIR]`  *(Correcto)*
2. **Ubicación de `then`:** Debe escribirse en una nueva línea o separado por un punto y coma `;` en la misma línea (`if [ ... ]; then`)
3. **Cierre:** Todo bloque condicional iniciado con `if` debe cerrarse obligatoriamente con `fi`

## 2. Operadores de Evaluación
### A. Operadores para Archivos y Directorios
| Operador | Descripción / Condición verdadera |
| :---: | :--- |
| `-e archivo` | El archivo o directorio existe. |
| `-f archivo` | Existe y es un **fichero regular** (no un directorio ni dispositivo). |
| `-d archivo` | Existe y es un **directorio**. |
| `-r archivo` | Existe y tiene permiso de **lectura**. |
| `-x archivo` | Existe y tiene permiso de **ejecución**. |
| `-s archivo` | Existe y **no está vacío** (tamaño > 0 bytes). |
| `-h archivo` | Existe y es un **enlace simbólico**. |
| `-O archivo` | El archivo pertenece al usuario que ejecuta el script. |
| `-G archivo` | El archivo pertenece al grupo del usuario que ejecuta el script. |
| `f1 -nt f2` | El archivo `f1` es **más reciente** (*newer than*) que `f2`. |
| `f1 -ot f2` | El archivo `f1` es **más antiguo** (*older than*) que `f2`. |

### B. Operadores Numéricos (Comparación Entera)
| Operador | Significado | Equivalente |
| :---: | :--- | :---: |
| `-eq` | Igual a (*equal*) | `==` |
| `-ne` | Distinto de (*not equal*) | `!=` |
| `-gt` | Mayor que (*greater than*) | `>` |
| `-ge` | Mayor o igual que (*greater or equal*) | `>=` |
| `-lt` | Menor que (*less than*) | `<` |
| `-le` | Menor o igual que (*less or equal*) | `<=` |



### C. Operadores para Cadenas de Texto
| Operador | Descripción |
| :---: | :--- |
| `-z "cadena"` | La cadena está **vacía** (longitud igual a 0). |
| `-n "cadena"` | La cadena **NO está vacía** (longitud mayor a 0). |
| `str1 = str2` | Las dos cadenas son idénticas. |
| `str1 != str2` | Las cadenas son diferentes. |
| `str1 < str2` | `str1` va antes alfabéticamente (Requiere `[[ ]]`). |
| `str1 > str2` | `str1` va después alfabéticamente (Requiere `[[ ]]`). |


## 3. Condiciones Compuestas y Dobles Corchetes `[[ ]]`

* **Operadores Lógicos:** `&&` (*AND*), `||` (*OR*), `!` (*NOT*).
* **Uso con corchetes simples `[ ]`:**
  ```bash
  if [ -r "$file" ] && [ -x "$file" ]; then ...
  ```
* **Ventajas de Dobles Corchetes `[[ ]]`:**
  * No requieren entrecomillar las variables con espacios.
  * Admiten operadores `<` y `>` sin redireccionar archivos.
  * Permiten **Expresiones Regulares** con `=~` (Ejemplo: `[[ "$var" =~ ^[0-9]+$ ]]` para verificar números).
  * Admiten comodines (Ejemplo: `[[ "abc" == a* ]]`).