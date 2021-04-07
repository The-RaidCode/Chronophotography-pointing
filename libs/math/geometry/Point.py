# -*- coding: utf-8 -*-

from math import *


class Point:
    def __init__(self, x: float, y: float):
        self.__x = None
        self.__y = None

        self.set_x(x)
        self.set_y(y)

    def distance_to(self, otherPoint):
        x = otherPoint.getX()
        y = otherPoint.getY()

        return sqrt((self.__x - x) ** 2 + (self.__y - y) ** 2)

    def set_x(self, x):
        if x >= 0:
            self.__x = x
        else:
            self.__x = 0

    def set_y(self, y):
        if y >= 0:
            self.__y = y
        else:
            self.__y = 0

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y
