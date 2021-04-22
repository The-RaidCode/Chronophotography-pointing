# -*- coding: utf-8 -*-

from math import *
from tkinter import *


class Point:
    """
        A class which represents a Point

        Attributes
            x (float) : The abscissa
            y (float) : The ordinate
            can(Canvas) : The Canvas where the point will be drawn
            color(str) :

        Methods
            distance_to : Returns the distance between this point and an other point
            draw : Draw the point on the Canvas
        """
    instances = []

    @classmethod
    def get_last(cls):
        """

        :return: The last point that have been created or None if no point has been created
        """
        if cls.instances:
            return cls.instances[-1]
        return None

    @classmethod
    def research(cls, x: float, y: float):
        """
        Research if there is a point on the abscissa x and the ordinate y

        :param x: The abscissa
        :param y: The ordinate
        :return: The point that is at this place and None if there is no point at this place
        """
        for point in cls.instances:
            if sqrt((point.get_x() - x) ** 2 + (point.get_y() - y) ** 2) <= 5:
                return point
        return None

    def __init__(self, x: float, y: float):
        """
        :param float x: The abscissa to set
        :param float y: The ordinate to set
        """

        self.__x = None
        self.__y = None

        self.__color = 'black'
        self.__drawing = False
        self.tk = None
        self.can = None
        self.image = None

        self.set_x(x)
        self.set_y(y)
        self.instances.append(self)

    def remove(self, instance_remove=True):
        """
        Erase Point from the Canvas if the point have been drawn
        Delete the point from instances
        :return:
        """
        if self.__drawing:
            self.can.delete(self.tk, self.image)
        if instance_remove:
            Point.instances.remove(self)

    def distance_to(self, other_point):
        """
        :param Point other_point: the point whose distance we want to know
        :return float: distance between this point and the other point
        """
        x = other_point.get_x()
        y = other_point.get_y()

        return sqrt((self.__x - x) ** 2 + (self.__y - y) ** 2)

    def draw(self, tk: Tk, can: Canvas, color='black'):
        """
        Draw the point

        :param tk: The window where the point is drawn
        :param can: The Canvas Where the point is drawn
        :param color: The color of the point
        :return:
        """
        self.tk = tk
        self.can = can
        self.__color = color
        self.__drawing = True
        self.image = self.can.create_oval(self.__x - 5, self.__y - 5, self.__x + 5, self.__y + 5, fill=self.__color,
                                          outline=self.__color)

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
