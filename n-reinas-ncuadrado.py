import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import time

""" Esta función genera una matriz a partir de
    un arreglo de reinas con sus posiciones desde 
    1 hasta N^2 """
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
    lo contrario False. """
def isValidPos(Q, i):
    #Buscar si alguna otra reina tiene esta posición
    for x in range(len(Q)):
        if( x != i and Q[x] == Q[i]):
            #Si la posición está ocupada, return False
            return False
    
    #Checkear matriz
    mat = plotMat(Q)
    #Sumar columnas
    matSumCols = mat.sum(axis=0)
    
    #Sumar filas
    matSumRows = mat.sum(axis=1)

    #Si hay más de un 1 por fila o columna, retornar False
    if(any(i > 1 for i in (np.concatenate((matSumCols, matSumRows), axis=0)))):
        return False
    
    #Sumar las diagonales
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
    tablero N x N """
def backtrack(Q, i):
    #print(Q)
    #Si llegamos a la última reina, parar
    if (i+1) > len(Q):
        return True
    
    for x in range(1, (len(Q)**2) + 1):
        Q[i] = x
        if isValidPos(Q, i):
            if backtrack(Q, i+1):
                return True
    Q[i] = 0
    

if __name__ == "__main__":
    Q = [0,0,0,0,0,0]
    
    
    start_time = time.time()
    
    backtrack(Q, 0)
    print(plotMat(Q))
    print(Q)

    print("--- %s seconds ---" % (time.time() - start_time))