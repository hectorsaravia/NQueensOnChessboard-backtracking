#importación del archivo con la clase queen
from chessBoard import chessBoard
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import time

#definiciones de variables
#N representa el tamaño del tablero NxN
N = 4
#chessBoard representa el tablero de ajedrez
chessB = np.zeros((N,N)).astype(int)

#sección main del código
if __name__ == "__main__":

    start_time = time.time()
    myChessBoard = chessBoard(N)
    print( myChessBoard )
    print( time.time() - start_time )
    


    # for i in range (0, N-1):
    #     for j in range (0, N-1):
    #         print( chessBoard[i][j] )

