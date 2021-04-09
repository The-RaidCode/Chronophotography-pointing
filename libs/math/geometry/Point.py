# -*- coding: utf-8 -*-

from math import *
from tkinter import *

class Point:
    """
        A class which represents a Point

        Attributes
            x (float) : The abscissa
            y (float) : The ordinate

        Methods
            distance_to : Returns the distance between this point and an other point
        """
    def __init__(self, x: float, y: float):
        """
        :param float x: The abscissa to set
        :param float y: The ordinate to set
        """

        self.__x = None
        self.__y = None


        self.set_x(x)
        self.set_y(y)

    def distance_to(self, other_point):
        """
        :param Point other_point: the point whose distance we want to know
        :return float: distance between this point and the other point
        """
        x = other_point.get_x()
        y = other_point.get_y()

        return sqrt((self.__x - x) ** 2 + (self.__y - y) ** 2)

    #def draw(self, ):
    #    self.set_color(color)
    #    image.create_oval(self.__x-5, self.__y-5, self.__x+5, self.__y+5, fill=self.__color, outline=self.__color)

    def set_x(self, x):
        """
        :param float x: The abscissa
        """
        if x >= 0:
            self.__x = x
        else:
            self.__x = 0

    def set_y(self, y):
        """
        :param float y: The ordinate
        """
        if y >= 0:
            self.__y = y
        else:
            self.__y = 0

    def set_color(self, color: str):
        self.__color = color
    def get_x(self):
        """
        :return float: The abscissa
        """
        return self.__x

    def get_y(self):
        """
        :return float: The ordinate
        """
        return self.__y
