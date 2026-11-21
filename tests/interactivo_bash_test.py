#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TEST INTERACTIVO: Acerca del Shell BASH (Practicas 7, 8, 9)
Formato: opciones con letras a, b, c, d
"""

PREGUNTAS = [
    # ============= LECCION 7: Shell Script ----------
    {
        "num": 7,
        "tema": "Lección 7: Shell Script",
        "preguntas": [
            {
                "q": "¿Qué indica la línea shebang '#!/bin/bash' al iniciar un script?",
                "opciones": {
                    "a": "Que el script debe compilar con gcc",
                    "b": "Que el intérprete (shell) a usar es /bin/bash",
                    "c": "Que el script requiere espacio en /bin",
                    "d": "Que el script es un programa en C"
                },
                "respuesta": "b"
            },
            {
                "q": "¿Qué hace echo -e \"hola\\nmundo\"?",
                "opciones": {
                    "a": "Imprime 'hola mundo' sin saltos de línea",
                    "b": "Imprime 'hola' seguido de un salto de línea y 'mundo'",
                    "c": "Da un error de sintaxis",
                    "d": "Solo imprime la palabra 'hola'"
                },
                "respuesta": "b"
            },
            {
                "q": "¿Cuál es la diferencia entre 'var=5' y 'var = 5'?",
                "opciones": {
                    "a": "Ninguna, hacen lo mismo",
                    "b": "var=5 asigna el valor; var = 5 intenta ejecutar el comando '=5'",
                    "c": "var=5 es un comentario",
                    "d": "var = 5 hace una suma"
                },
                "respuesta": "b"
            },
            {
                "q": "¿Qué representa el parámetro especial $# en un script?",
                "opciones": {
                    "a": "El nombre del script",
                    "b": "El PID de la shell",
                    "c": "El número total de argumentos posicionales",
                    "d": "El último argumento"
                },
                "respuesta": "c"
            },
            {
                "q": "¿Qué hace echo \"${var1} ${var2}\" cuando var1=3 y var2=hola?",
                "opciones": {
                    "a": "Error de sintaxis",
                    "b": "Imprime: 3 hola",
                    "c": "Solo imprime el valor de var1",
                    "d": "Imprime: hola 3"
                },
                "respuesta": "b"
            },
            {
                "q": "¿Qué sucede si ejecutamos unset var1 y luego echo ${var1}?",
                "opciones": {
                    "a": "Da un error de 'variable no definida'",
                    "b": "Imprime el nombre 'var1'",
                    "c": "Imprime una cadena vacía",
                    "d": "Se cierra el script"
                },
                "respuesta": "c"
            },
            {
                "q": "¿Qué opción de grep devuelve SOLO las coincidencias, no la línea completa?",
                "opciones": {
                    "a": "-n",
                    "b": "-c",
                    "c": "-o",
                    "d": "-i"
                },
                "respuesta": "c"
            },
            {
                "q": "¿Qué hace el comando read?",
                "opciones": {
                    "a": "Lee el contenido de un fichero",
                    "b": "Lee el valor introducido por el usuario y lo guarda en una variable",
                    "c": "Imprime el contenido de una variable",
                    "d": "Limpia la terminal"
                },
                "respuesta": "b"
            },
            {
                "q": "¿Qué hace bash -n mi_script.sh?",
                "opciones": {
                    "a": "Ejecuta el script",
                    "b": "Compila el script",
                    "c": "Comprueba solo la sintaxis sin ejecutarlo",
                    "d": "Limpia la terminal"
                },
                "respuesta": "c"
            },
            {
                "q": "¿Cómo se ejecuta un script bash desde el directorio actual?",
                "opciones": {
                    "a": "script.sh (sin prefijo)",
                    "b": "./script.sh",
                    "c": "/script.sh",
                    "d": "sh script.sh"
                },
                "respuesta": "b"
            },
            # ============= LECCION 8: Condicional ----------
            {
                "q": "¿Qué verifica [ -f archivo ]?",
                "opciones": {
                    "a": "Que el archivo existe y es un directorio",
                    "b": "Que el archivo existe y es un fichero regular",
                    "c": "Que el archivo está vacío",
                    "d": "Que el archivo tiene permisos de escritura"
                },
                "respuesta": "b"
            },
            {
                "q": "¿Qué verifica [ -d directorio ]?",
                "opciones": {
                    "a": "Que el directorio existe y es un directorio",
                    "b": "Que el directorio contiene ficheros",
                    "c": "Que el directorio está vacío",
                    "d": "Que el directorio tiene permisos de lectura"
                },
                "respuesta": "a"
            },
            {
                "q": "¿Qué hace [ $a -eq $b ]?",
                "opciones": {
                    "a": "Compara cadenas",
                    "b": "Compara si $a es mayor que $b",
                    "c": "Compara si $a es igual a $b (entero)",
                    "d": "Compara si $a es diferente de $b"
                },
                "respuesta": "c"
            },
            {
                "q": "¿Qué hace [ -z \"$var\" ]?",
                "opciones": {
                    "a": "Verifica que la variable NO esté vacía",
                    "b": "Verifica que la variable esté vacía",
                    "c": "Verifica que la variable contenga '0'",
                    "d": "Verifica la longitud de la variable"
                },
                "respuesta": "b"
            },
            {
                "q": "En 'if [ -d $DIR ]', ¿cuál es el problema?",
                "opciones": {
                    "a": "Falta el then",
                    "b": "Faltan los espacios alrededor del corchete",
                    "c": "Falta el fi",
                    "d": "No se puede usar con directorios"
                },
                "respuesta": "b"
            },
            {
                "q": "En un if-then-else, ¿qué cierra el bloque?",
                "opciones": {
                    "a": "end",
                    "b": "done",
                    "c": "fi",
                    "d": "close"
                },
                "respuesta": "c"
            },
            {
                "q": "¿Cuál es una ventaja de los dobles corchetes [[ ]] sobre [ ]?",
                "opciones": {
                    "a": "Requieren comillas alrededor de las variables",
                    "b": "No necesitan espacio después de [",
                    "c": "Admite expresiones regulares con =~ y comparación < > sin redireccionar",
                    "d": "Son más rápidos en todos los casos"
                },
                "respuesta": "c"
            },
            {
                "q": "¿Qué hace [[ \"$var\" =~ ^[0-9]+$ ]]?",
                "opciones": {
                    "a": "Verifica si var contiene solo dígitos",
                    "b": "Asigna la expresión regular a var",
                    "c": "Verifica si var empieza con un número",
                    "d": "Da un error"
                },
                "respuesta": "a"
            },
            {
                "q": "En la condición if [ -r \"$file\" ] && [ -x \"$file\" ]; then, ¿qué significa &&?",
                "opciones": {
                    "a": "OR: al menos una condición verdadera",
                    "b": "AND: ambas condiciones deben ser verdaderas",
                    "c": "NOT: invierte el resultado",
                    "d": "XOR: solamente una falsa"
                },
                "respuesta": "b"
            },
            {
                "q": "¿Qué operador negaría el resultado de una condición?",
                "opciones": {
                    "a": "-not",
                    "b": "!",
                    "c": "!!",
                    "d": "neg"
                },
                "respuesta": "b"
            },
            # ============= LECCION 9: Listas y bucles ----------
            {
                "q": "¿Cómo se define un array en Bash?",
                "opciones": {
                    "a": "array = (a b c)",
                    "b": "array = a b c",
                    "c": "array=(a b c)",
                    "d": "array[0]=a; array[1]=b; array[2]=c"
                },
                "respuesta": "c"
            },
            {
                "q": "Dado animales=(gato perro loro), ¿qué devuelve echo ${animales[1]}?",
                "opciones": {
                    "a": "gato",
                    "b": "perro",
                    "c": "loro",
                    "d": "0"
                },
                "respuesta": "b"
            },
            {
                "q": "En un array de 3 elementos, ¿qué devuelve ${#animales[*]}?",
                "opciones": {
                    "a": "El número total de elementos (3)",
                    "b": "La longitud de la primera palabra",
                    "c": "Un error",
                    "d": "La longitud de la cadena completa"
                },
                "respuesta": "a"
            },
            {
                "q": "Dado array=(uno dos tres), ¿qué imprime echo \"${array[@]}\"?",
                "opciones": {
                    "a": "unodostres",
                    "b": "uno dos tres",
                    "c": "solo 'uno'",
                    "d": "2"
                },
                "respuesta": "b"
            },
            {
                "q": "Dado array=(uno dos tres cuatro), ¿qué imprime echo \"${array[@]:1:2}\"?",
                "opciones": {
                    "a": "uno dos",
                    "b": "dos tres",
                    "c": "tres cuatro",
                    "d": "dos cuatro"
                },
                "respuesta": "b"
            },
            {
                "q": "Dado cadena=\"hola mundo\", ¿qué imprime echo ${#cadena}?",
                "opciones": {
                    "a": "9",
                    "b": "10",
                    "c": "4",
                    "d": "5"
                },
                "respuesta": "b"
            },
            {
                "q": "¿Qué hace for i in {1..5}?",
                "opciones": {
                    "a": "Recorre i = 1, 2, 3, 4, 5",
                    "b": "Recorre i = 1, 2, 3, 4",
                    "c": "Da error de sintaxis",
                    "d": "Solo recorre el número 5"
                },
                "respuesta": "a"
            },
            {
                "q": "¿Qué es IFS (Internal Field Separator) en Bash?",
                "opciones": {
                    "a": "Una variable que indica el separador de campos internos (espacio, tabulador, salto de línea)",
                    "b": "Una variable de configuración del sistema",
                    "c": "Una orden de bash",
                    "d": "Una variable de entorno"
                },
                "respuesta": "a"
            },
            {
                "q": "En 'for f in \"${array[@]}\"', ¿por qué se usan comillas dobles y @?",
                "opciones": {
                    "a": "Para que cada elemento del array se trate como una palabra separada",
                    "b": "Para juntar todos los elementos en una sola cadena",
                    "c": "Para que el array se convierta en un string",
                    "d": "Para evitar usar comillas al definir el array"
                },
                "respuesta": "a"
            },
        ]
    },
]

def run_test():
    puntuacion = 0
    total = 0
    idx = 0

    for leccion in PREGUNTAS:
        print(f"\n{'='*60}")
        print(f"  LECCION {leccion['num']}: {leccion['tema']}")
        print(f"{'='*60}")
        for pregunta in leccion["preguntas"]:
            total += 1
            idx += 1
            print(f"\n  Pregunta {idx}: {pregunta['q']}")
            for letra, opcion in pregunta["opciones"].items():
                print(f"    {letra}). {opcion}")

            while True:
                try:
                    respuesta = input("\n  Tu respuesta (a/b/c/d): ").strip().lower()
                except EOFError:
                    print("\n  [Entrada no disponible]")
                    respuesta = ""
                if respuesta in ("a", "b", "c", "d"):
                    break
                print("  ✗ Respuesta no válida. Usa una de las opciones a/b/c/d.")

            correcta = pregunta["respuesta"]
            if respuesta == correcta:
                print(f"  ✓ ¡Correcta! ({correcta})")
                puntuacion += 1
            else:
                print(f"  ✗ Incorrecta. Tu elección: {respuesta}. La correcta es: {correcta}")
            print()

    print("=" * 60)
    print(f"  RESULTADO FINAL: {puntuacion}/{total}")
    porcentaje = puntuacion / total * 100 if total else 0
    print(f"  Porcentaje: {porcentaje:.1f}%")
    if porcentaje == 100:
        print("  ¡Excelente! Dominas el material.")
    elif porcentaje >= 80:
        print("  Muy bien. Solo a falta de pequeños detalles.")
    elif porcentaje >= 60:
        print("  Aprobado. Repasa los temas con más puntuación menor.")
    else:
        print("  No llegado. Haz la prueba de nuevo.")
    print("=" * 60)

if __name__ == "__main__":
    run_test()
