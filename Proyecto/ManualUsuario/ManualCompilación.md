## Proyecto: Flow Free
**Integrantes:**
- María Camila Aguirre Collante
- Jessica Tatiana Naizaque Guevara
### Manual de compilación
#### Librerías adicionales:
- Colorama: pip install colorama (Windows o Linux)
#### Interacción con el usuario:
- El jugador puede elegir el tamaño del tablero y el nivel aparecerá de manera aleatoria.
    - Los movimientos se realizan casilla por casilla.
        - Si se ingresa una casilla que ya ha sido llenada previamente:
            - Si el color de la casilla coincide con la casilla ingresada, se mantiene el camino hasta esa casilla.
            - Si el color de la casilla no coincide con la casilla ingresada, se elimina completamente el camino correspondiente a ese color y se le asigna el valor y color de la casilla ingresada.
        - Si se ingresa una casilla adyacente a uno de los valores iniciales (extremo) de un color, y ya existe un camino correspondiente a ese color. Se elimina el camino existente y se agrega la casilla ingresada.
