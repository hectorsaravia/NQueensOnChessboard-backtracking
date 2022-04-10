# NQueensOnChessboard-backtracking


## n-reinas-ncuadrado.py:
Este acercamiento considera como variables cada una de las reinas, las cuales se encuentran almacenadas en un arreglo de tamaño N, donde cada una tiene su posición en el tablero, siendo estas desde 1 hasta N^2. Dado que se verifica cada una de las posiciones en cada iteración, la complejidad de este algoritmo es muy elevada (N^2?), por lo que no es el acercamiento más óptimo. 

## n-reinas-columnas.py:
En éste caso, se considera que cada una de las columnas puede tener solamente 1 reina, por lo que ya no se verifica cada una de las casillas del tablero. Esto disminuye el espacio de búsqueda considerablemente, por lo que el algoritmo es capaz de llegar a matrices de un orden más elevado. Por otra parte, en este script se consideró una función recursiva para verificar las diagonales de cada reina, lo cuál evita tener que implementar algunos ciclos que empeoran el tiempo de ejecución.
