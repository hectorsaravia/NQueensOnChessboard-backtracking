import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import time

""" Esta función genera una matriz a partir de
    un arreglo de reinas con sus posiciones desde 
    1 hasta N^2 en el tablero (de izquierda a
    derecha y de arriba hacia abajo). """
def plotMat(Q):
    matLen = len(Q)
    mat = np.zeros((matLen, matLen)).astype(int)

    for i in Q:
        if i != 0:
            h = i-1
            row = int(h / matLen)
            col = int(h % matLen)
            mat[row][col] = 1
    return mat

""" Esta función valida la posición de las reinas
    en el tablero. De ser válida devuelve True, de 
    lo contrario False. Para esto se hacen cuatro 
    comprobaciones:
    1) Ni una reina está intentando usar la misma pos.
    2) La suma por fila <= 1
    3) La suma por columna <= 1
    4) La fila por diagonales <= 1"""

def isValidPos(Q, i):
    #1) Buscar si alguna otra reina tiene esta posición
    for x in range(len(Q)):
        if( x != i and Q[x] == Q[i]):
            #Si la posición está ocupada, return False
            return False
    
    #Checkear matriz
    mat = plotMat(Q)
    #2) Sumar columnas
    matSumCols = mat.sum(axis=0)
    
    #3) Sumar filas
    matSumRows = mat.sum(axis=1)

    #Si hay más de un 1 por fila o columna, retornar False
    if(any(i > 1 for i in (np.concatenate((matSumCols, matSumRows), axis=0)))):
        return False
    
    #4) Sumar las diagonales
    diagSums = []
    for x in range(-len(mat[0])+2, len(mat[0])-1):
        #print(np.trace(mat, offset=x))
        diagSums.append(int(np.trace(mat, offset=x)))
    
    #Suma diagonales matriz invertida
    for x in range(-len(mat[0])+2, len(mat[0])-1):
        #print(np.trace(np.rot90(mat), offset=x))
        diagSums.append(int(np.trace(np.rot90(mat), offset=x)))
    if(any(i > 1 for i in diagSums)):
        return False
    return True

""" Esta función genera el árbol de backtracking 
    a partir de un arreglo de N reinas para un 
    tablero N x N. 
    El arreglo comienza lleno de 0's, y termina
    con una solución factible.
    La i sirve para llevar seguimiento de la reina
    actual sobre la que se está iterando. """
def backtrack(Q, i):
    
    #Si llegamos a la última reina, parar
    if (i+1) > len(Q):
        return True
    
    """ Este ciclo cuenta desde 1 hasta N^2 para la
        reina actual. Se rompe antes si es que la 
        siguiente reina del árbol es válida, de lo
        contrario x +=1 y se genera otra rama. """
    for x in range(1, (len(Q)**2) + 1):
        Q[i] = x
        if isValidPos(Q, i):
            if backtrack(Q, i+1):
                return True
    Q[i] = 0

def N_Queens(N):
    #Arreglo de N reinas (lleno de 0's)
    Q = np.zeros(N).astype(int)
    backtrack(Q, 0)
    return Q

if __name__ == "__main__":

    
    #Para una sola ejecución:
    N = 4
    Q = N_Queens(N)
    print("Ejecución única: \n")
    print("Solución: " + str(Q))
    print("Matriz: ")
    print(plotMat(Q))
    print("\n")


    #Para ejecuciones múltiples y generar graf N v/s tiempo
    print("Ejecución múltiple: \n")
    timeData = []
    N_arr = []
    #Itera desde N = 4 hasta N = 8
    for x in range(4, 8+1):
        
        
        #Aquí empieza la medición de tiempo
        start_time = time.time()
        Q = N_Queens(x)
        timeData.append(time.time() - start_time)
        N_arr.append(x)
        print("Q para N = " + str(x) + ": " + str(Q))
    
    print(timeData)
    print(N_arr)
    plt.plot(N_arr, timeData)
    plt.show() 

    
