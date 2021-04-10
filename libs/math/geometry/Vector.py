# -*- coding: utf-8 -*-

from math import sqrt
from Point import *
from tkinter import *


class Vector:
    """
    A class which represents a Vector

    Attributes
        x (float) : The abscissa
        y (float) : The ordinate
        can(Canvas) : The Canvas where the point will be drawn
    Methods

    """

    def __init__(self, application_point: Point, x: float, y: float, can: Canvas):
        """

        :param application_point: the point of application of the vector
        :param x: the abscissa to set
        :param y: The ordinate to set
        :param can: The
        """
        self.__application_point = application_point
        self.__x = None
        self.__y = None
        self.__lenght = None

        self.__image = can
        self.__color = 'black'

        self.set_x(x)
        self.set_y(y)
        self.set_lenght()

    def draw(self, color):
        """
        Draw the vector on the Canvas automatically when there is a click on the Canvas

        :param color: object of the event click
        """
        self.set_color(color)
        self.__image.create_line(self.__application_point.get_x(),
                                 self.__application_point.get_y(),
                                 self.__application_point.get_x() + self.__x,
                                 self.__application_point.get_y() + self.__y,
                                 fill=self.__color, width=2, arrow='last', arrowshape=(10, 10, 10))

    def set_lenght(self):
        """
        calculation of the vector's lenght
        """
        self.__lenght = sqrt(self.__x ** 2 + self.__y ** 2)

    def set_x(self, x):
        """
        :param float x: The abscissa
        """
        self.__x = x

    def set_y(self, y):
        """
        :param float y: The ordinate
        """
        self.__y = y

    def set_color(self, color):
        """
        :param color: color of the point
        """
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
