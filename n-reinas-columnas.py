import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import time


"""Generar ramas superiores e inferiores para
   verificar si hay alguna reina en las diagonales
   izquierdas."""
def diagCheck(dir, board,i, j):
    N = len(board[0])
    #print(dir + "i:" + str(i) + " j:" + str(j))
    if i < 0 or j < 0 or i > (N-1):
        return False
    elif board[i][j] == 1:
        return True
    elif dir == "up":
        # i-1, j-1
        return diagCheck("up", board,i-1, j-1)
        
    elif dir == "down":
        # i+1, j-1
        return diagCheck("down", board,i+1, j-1)

def diagCheckStart(board, i, j):
    if diagCheck("up", board, i-1, j-1) == True or diagCheck("down", board, i+1, j-1) == True:
        return True
    else:
        return False


"""Verificar el lado izquierdo de la fila"""      
def leftCheck(board, i, j):
    checkFailed = False
    x = 1
    while(j-x >= 0):
        if board[i][j-x] == 1:
            checkFailed = True
            break
        x += 1
    return checkFailed

def checkPos(board, i, j):
    if leftCheck(board, i, j) == True or diagCheckStart(board, i, j) == True:
        return True
    else:
        return False


def backTrack(board, j):
    N = len(board[0])
    if j > (N-1):
        return True

    i = 0
    while (i < N):
        if checkPos(board, i, j) == False:
            board[i][j] = 1

            if backTrack(board, j+1):
                return True
            
            board[i][j] = 0
        i+=1

    return False

def N_Queens(N):
    chessB = np.zeros((N,N)).astype(int)
    backTrack(chessB, 0)
    return chessB


if __name__ == "__main__":
    

    #Ejecución única
    N = 4
    print(N_Queens(N))



    #Ejecución múltiple
    print("Ejecución múltiple: \n")
    timeData = []
    N_arr = []
    #Itera desde N = 4 hasta N = 15
    for x in range(4, 15+1):
        
        
        #Aquí empieza la medición de tiempo
        start_time = time.time()
        N_Queens(x)
        timeData.append(time.time() - start_time)
        N_arr.append(x)
        print("Q para N = " + str(x) + ": ")
    
    print(timeData)
    print(N_arr)
    plt.plot(N_arr, timeData)
    plt.show() 