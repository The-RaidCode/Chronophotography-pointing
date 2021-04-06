from math import *

class Point:
    def __init__(self, x: float, y: float):
        self.setX(x)
        self.setY(y)

    def distance_to(self, otherPoint: Point):
        x = otherPoint.getX()
        y = otherPoint.getY()

        return sqrt((self.__x - x)**2 + (self.__y - y)**2)


    def setX(self, x):
        if x >= 0:
            self.__x = x
        else :
            self.__x = 0

    def setY(self, y):
        if y >= 0:
            self.__y = y
        else:
            self.__y = 0

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

