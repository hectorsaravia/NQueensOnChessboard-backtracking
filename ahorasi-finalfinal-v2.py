import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import time

def plotMat(Q):
    matLen = len(Q)
    mat = np.zeros((matLen, matLen)).astype(int)

    for i in Q:
        h = i-1
        row = int(h / matLen)
        col = int(h % matLen)
        mat[row][col] = 1
    print(mat)

def isValid(Q):
    if ( 0 in Q ):
        return False
    elif (len(Q) == len(set(Q))):
        return False
    elif ():
        pass
    return True


def newQueen(Q, pos):
    Q[pos] = 1
    if (isValid(Q)):
        return True
    return False



if __name__ == "__main__":
    Q = [5,7,13,16, 8]
    #Q = np.zeros(N).astype(int)
    #backTrack(np.zeros(N).astype(int))
    start_time = time.time()
    plotMat(Q)
    print("--- %s seconds ---" % (time.time() - start_time))