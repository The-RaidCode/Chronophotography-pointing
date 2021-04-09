# -*- coding: utf-8 -*-

from math import *
from Point import *
from tkinter import *


class Vector:
    """
    A class which represents a Vector

    Attributes
        x (float) : The abscissa
        y (float) : The ordinate

    Methods

    """

    def __init__(self, image: Canvas, application_point: Point, x: float, y: float):
        self.__x = None
        self.__y = None
        self.__lenght = None

        self.__image = image
        self.__application_point = application_point

        self.set_x(x)
        self.set_y(y)
        self.set_lenght()

    def draw(self, color):
        self.set_color(color)
        self.__image.create_line(self.__application_point.get_x(),
                                 self.__application_point.get_y(),
                                 self.__application_point.get_x() + self.__x,
                                 self.__application_point.get_y() + self.__y,
                                 fill=self.__color, width=2, arrow='last', arrowshape=(10, 10, 10))


    def set_lenght(self):
        self.__lenght = sqrt(self.__x ** 2 + self.__y ** 2)

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y
    def set_color(self, color):
        self.__color = color

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

