#se importan las clases de las posiciones y las reinas
from pos import pos
from queen import queen

#definicion de la clase chessboard que contiene los atributos de orden y que los objetos de las posiciones
class chessBoard (object):

    #definicion de variables
    def __init__(self, N, pos):
        self.__N = N
        self.__queensNum = 0

        self.__pos = [ [] for i in range (0,N) ]

        for i in range (0, N):
            for j in range (0, N):
                self.__pos.append[i]( pos(i* self.__N + j) )

        

    #get del orden del tablero
    def getN(self):
        return self.__N
    
    #get de todos los objetos posiciones
    def getAllPos(self):
        return self.__pos
    
    #se obtiene el numero total de reinas
    def getQueensNum(self):
        return self.__queensNum
    
    #se modifica el numero de reinas
    def setQueensNum(self, queensNum):
        self.__queensNum = queensNum
    
    #se obtiene el objeto de posicion de un indice en especifico
    def getPos(self, pos):
        return self.__pos[pos]
    
    #se modifica el objeto de posicion de un indice en especifico
    def setPos(self, pos, newPos):
        self.__pos[pos] = newPos
    
    #se obtiene la reina de una posicion en especifico a partir de un indice
    def getQueenOnPos(self, pos):
        return self.__pos[pos].getQueen()
    
    #se setea una nueva reina en una posicion en especifico
    def setQueenOnPos(self, pos):
        
        self.__pos[pos].setQueen( queen() )
        self.__pos[pos].setIsOnQueenSight(True)
        N = self.__N

        if ( pos % N == 1 ):
            if (pos / N > 1):
                self.__pos[pos - (N+1)].setIsOnQueenSight(True)
            elif (pos / N < N*N - N):
                self.__pos[pos + (N-1)].setIsOnQueenSight(True)
            else:
                self.__pos[pos - (N+1)].setIsOnQueenSight(True)
                self.__pos[pos + (N-1)].setIsOnQueenSight(True)

    #se verifica si la posicion esta a la vista de la reina
    def getPosIsOnQueenSight(self, pos):
        return self.__pos[pos].getIsOnQueenSight()
    
    def setPosIsOnQueenSight(self, pos, newIsOnQueenSight):
        self.__pos[pos].setIsOnQueenSight(newIsOnQueenSight)

    def getIfAllPosAreOnQueenSight(self):
        for pos in self.__pos:
            if pos.getIsOnQueenSight() == False:
                return False
        return True
        