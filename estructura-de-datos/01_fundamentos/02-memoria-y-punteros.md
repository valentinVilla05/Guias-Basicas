# Memoria y Punteros en C++

### La Memoria RAM
Es necesario entender el funcionamiento de la memoria ram para poder manejar correctamente punteros y memoria dinámica-

* La memoria RAM se divide en celdas donde se almacenan los distintos valores con su tipo de dato correspondiente, *int, float, double, char, string..*
* Cada casillero tiene un número de dirección único (por ejemplo, `0x7ffc82`).
* Cuando creas una variable, el sistema reserva uno de esos casilleros y le asigna el nombre de tu variable.

```text
  Dirección de Memoria       Variable      Valor Guardado
  ┌──────────────────┐      ┌─────────┐    ┌──────────┐
  │     0x7ffc81     │ ---> │  edad   │ -->│    20    │
  ├──────────────────┤      └─────────┐    └──────────┘
  │     0x7ffc82     │ ---> │  precio │ -->│   15.99  │
  └──────────────────┘      └─────────┘    └──────────┘
```

También es importante entender que no todos los tipos de dato ocupan el mismo espacio en memoria.

### Tipos de datos y memoria

| Tipo de dato | ¿Qué almacena? | Memoria |
|--------------|----------------|---------|
| `int` | Números enteros | 4 bytes |
| `long` | Números enteros grandes | 8 bytes |
| `float` | Números decimales | 4 bytes |
| `double` | Números decimales con mayor precisión | 8 bytes |
| `char` | Un carácter Unicode | 2 bytes |
| `bool` | `true` o `false` | 1 bit |
| `string` | Texto | Variable |


### Operadores

Operador dirección (&): Se coloca delante de una variable existente para obtener su dirección de memoria en formato hexadecimal. Significa "¿dónde está guardada esta variable?".
* **Operador de desreferencia (`*`):** Se coloca delante de un puntero para acceder al dato que hay dentro de la dirección que guarda. Significa *"¿qué valor hay dentro de esa dirección?"*.

---