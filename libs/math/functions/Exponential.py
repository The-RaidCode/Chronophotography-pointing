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

    def __add__(self, other):
        """
        :param Exponential other: Exponential object to add up
        :return Exponential: Result of the Sum
        :raise TypeError: Raised when a non-Exponential object tried to be summed up with this one
        :raise ValueError: Raised if the Exponential Objects do not have the same power
        """

        if type(other) is Exponential:
            if other.get_power() == self.power:
                return Exponential(self.power, self.factor + other.get_factor())
            else:
                raise ValueError("ValueError: can only concatenate Exponential objects with the same power")
        else:
            raise TypeError("can only concatenate Exponential (not \"{}\") to Exponential".format(type(other).__name__))

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

    def __eq__(self, other):
        """
        :param other: Object to compare
        :return bool: Result of the Comparison
        """

        return type(other) == Exponential and self.factor == other.get_factor() and self.power == other.get_power()

    def __str__(self):
        """
        :return str: Character String of the Exponential
        """

        return "({factor})exp({p})".format(factor=self.factor, p=self.power)

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
        :param Polynomial power: Power of the Exponential to set
        :raise TypeError: Raised when power is not a Polynomial object
        """

        if type(power) == Polynomial:
            self.power = power
        else:
            raise TypeError("'power' must be an Polynomial object (not \"{}\")".format(type(power).__name__))

    def set_factor(self, factor: Polynomial):
        """
        :param Polynomial factor: Multiplying Factor of the Exponential
        :raise TypeError: Raised when factor is not a Polynomial object
        """

        if type(factor) == Polynomial:
            self.factor = factor
        else:
            raise TypeError("'factor' must be an Polynomial object (not \"{}\")".format(type(factor).__name__))

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
