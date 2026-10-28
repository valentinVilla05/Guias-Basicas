# Expresiones Regulares

Las expresiones regulares son una herramienta que usamos para encontrar cadenas de texto que corresponden a un patrón de caracteres. Estas las utilizamos mucho cuando trabajamos en una terminal ya sea para buscar archivos tanto en la terminal como en aplicaciones...

Una sola expresión regular puede representar múltiples cadenas de texto.

Mediante regex podemos representar tanto **literales** (un carácter se corresponde a sí mismo) como **carácteres especiales** (Representan conjuntos de caracteres o llevan a cabo ciertas funciones).

---

### Cuantificadores

| Cuantificador | Nº Caracteres | Correspondencia                               | Ejemplo                                       |
| ------------- | ------------- | --------------------------------------------- | --------------------------------------------- |
| ?             | 0 ó 1         | Carácter opcional (0 o 1 veces)               | 'las?'' corresponde a 'la' o 'las'            |
| +             | 1 ó más       | Ocurre al menos 1 vez                         | 'al+' corresponde a 'al', 'all', 'allllll'... |
| {x}           | Nº exacto     | El caracter aparece un número exacto de veces | 'al{2}' corresponde a 'all'                   |
| {x, y}        | Intervalo     | Un caracter aparece entre x e y veces         | 'er{1,2}' corresponde a 'er' y 'erer'         |
| \*            | 0 o más       | 0 o más veces                                 | 'be\*' corresponde a 'b' y a 'be'             |

### Clases de caracteres

Para representar un conjunto de caracteres lo hacemos mediante []. Ejemplo: [aeoiuáéíóú].

Formas abreviadas:

| Abreviacion | Representacion                                                                               |
| ----------- | -------------------------------------------------------------------------------------------- |
| \s          | Tabulaciones, espacios y saltos de linea                                                     |
| \d          | Numeros                                                                                      |
| \w          | Caracter de palabra                                                                          |
| \W          | De todo menos caracteres de palabra                                                          |
| \D          | Todo menos un digito                                                                         |
| ^           | Sirve para negar una clase. Ejemplo: [^aeiou] encuentra de todo menos las vocales sin acento |
| \t          | Tabulacion                                                                                   |
| \n          | Salto de línea                                                                               |
| \r          | Retorno de carro                                                                             |
| .           | Corresponde a casi cualquier caracter (excepto los saltos de linea). Es el "comodin"         |

> ^\d es igual a \D y ^\s es igual a \S

### Anclas

| Simbolo | Representación                                                        |
| ------- | --------------------------------------------------------------------- |
| ^       | Principio de linea (dentro de una clase ([]) actua como una negacion) |
| $       | Final de linea                                                        |
| \b      | Ancla para el principio o final de una palabra                        |
| \<      | Principio de una palabra                                              |
| \\>     | Final de una palabra                                                  |

No corresponden a un patrón, pero indican la posición donde debe ser encontrado el patrón, con respecto al principio/fin de las palabras

### Alternancias

Sirve para poner alternativas en la busqueda, por ejemplo, 'ao|oa' encontrará correspondencia en 'ao' y 'oa'.

### Paginas para probar regex

[regexpal.com](regexpal.com)

[regex101.com](regex101.com)

[regexr.com](regexr.com)
