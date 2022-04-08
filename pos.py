class pos (object):
    def __init__(self, numb):
        self.__queen = None
        self.__isOnQueenSight = False
        self.__numb = numb
    
    def getNumb(self):
        return self.__numb

    def setQueen(self, queen):
        self.__queen = queen
    
    def getQueen(self):
        return self.__queen

    def setIsOnQueenSight(self):
        self.__isOnQueenSight = True
    
    def setIsNotOnQueenSight(self):
        self.__isOnQueenSight = False
    
    def getIsOnQueenSight(self):
        return self.__isOnQueenSight