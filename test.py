import numpy as np
import time
N = 22

chessB = np.zeros((N,N)).astype(int)

sol = [0] * N
#chessB[1][2] = 1
#chessB[0][0] = 1
""" def printBoard(board):
    for i in board:
        for j in i:
            print(j, end = " ")
        print() """


"""Generar ramas superiores e inferiores para
   verificar si hay alguna reina en las diagonales
   izquierdas."""
def diagCheck(dir, board,i, j):
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

if __name__ == "__main__":
    #print(chessB)
    #checkPos(1,3,chessB)
    start_time = time.time()
    #print(diagCheckStart(chessB, 3, 3))
    #print(checkPos(chessB, 0, 0))
    backTrack(chessB, 0)
    print(chessB)
    print(chessB.sum())
    print(time.time() - start_time)