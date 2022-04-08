#clase que controla los atributos de las reinas y donde pueden ver
class queen:

    #definiciones de variables
    def __init__(self):
        self.__upperLeftDiag = None
        self.__upperRightDiag = None
        self.__downLeftDiag = None
        self.__downRightDiag = None

    #setters para diagonales
    def setUpperLeftDiag (self, upperLeftDiag):
        self.__upperLeftDiag = upperLeftDiag

    def setUpperRightDiag (self, upperRightDiag):
        self.__upperRightDiag = upperRightDiag

    def setDownLeftDiag (self, downLeftDiag):
        self.__downLeftDiag = downLeftDiag

    def setDownRightDiag (self, downRightDiag):
        self.__downRightDiag = downRightDiag

    #getters para diagonales
    def getUpperLeftDiag (self):
        return self.__upperLeftDiag
    
    def getUpperRightDiag (self):
        return self.__upperRightDiag

    def getDownLeftDiag (self):
        return self.__downLeftDiag

    def getDownRightDiag (self):
        return self.__downRightDiag