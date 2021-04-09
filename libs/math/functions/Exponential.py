# -*- coding: utf-8 -*-

from Polynomial import Polynomial
from math import exp


class Exponential:
    """
    A class which represents a Exponential Function (Mathematics)

    Attributes
        power (Polynomial) : Power of the Exponential
        factor (Polynomial) : Multiplying Factor of the Exponential

    Methods
        calculate : Returns the result of the Calculation with a given value
        derive : Returns the Derivative as an other Exponential Instance
    """

    def __init__(self, power: Polynomial, factor: Polynomial):
        """
        :param Polynomial power: Power to set
        :param Polynomial factor: Multiplying Factor to set
        """

        self.power = power
        self.factor = factor

    def __str__(self):
        """
        :return str: Character String of the Exponential
        """

        return "({factor})exp({p})".format(factor=self.factor, p=self.power)

    def __mul__(self, other):
        """
        :param Exponential other: Exponential object to multiply
        :return Exponential: Result of the Multiplication
        :raise TypeError: Raised when a non-Exponential object tried to be multiplied with this one
        """

        if type(other) is Exponential:
            return Exponential(self.power + other.get_power(), self.factor * other.get_factor())
        else:
            raise TypeError("can only multiply Exponential by Exponential (not \"{}\")".format(type(other).__name__))

    def get_power(self):
        """
        :return Polynomial: Power of the Exponential
        """

        return self.power

    def get_factor(self):
        """
        :return Polynomial: Multiplying Factor of the Exponential
        """

        return self.factor

    def set_power(self, power: Polynomial):
        """
        :param Polynomial power: Degree of the Exponential to set
        """

        self.power = power

    def set_factor(self, factor: Polynomial):
        """
        :param Polynomial factor: Multiplying Factor of the Exponential
        """

        self.factor = factor

    def derive(self):
        """
        Derives the Exponential

        :return Exponential: Derivative of the Exponential
        """

        return Exponential(self.power, self.factor.derive() + (self.factor * self.power.derive()))
        # (v * exp(u))' = (v' * vu')exp(u)

    def calculate(self, value: float):
        """
        Returns the result of the Calculation with a given value

        :param float value: Value to use for the calculation of the Exponential (integers can be used)
        :return float: Result of the Calculation
        :raise TypeError: Raised when 'value' is not a float or an integer
        """

        if type(value) == int:
            value = float(value)

        if type(value) == float:
            return self.factor.calculate(value) * exp(self.power.calculate(value))
        else:
            raise TypeError("value must be an integer or a float (not \"{}\")".format(type(value).__name__))
