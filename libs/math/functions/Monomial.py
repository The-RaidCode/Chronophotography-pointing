# -*- coding: utf-8 -*-

class Monomial:
    """
    A class which represents a Monomial (Mathematics)

    Attributes
        degree (int) : Degree of the Monomial
        coefficient (float) : Multiplying Factor of the Monomial

    Methods
        calculate : Returns the result of the Monomial's Calculation with a given value
        derive : Returns the Derivative as an other Monomial Instance
    """

    def __init__(self, degree: int, coefficient: float):
        """
        :param int degree: Degree to set
        :param float coefficient: Multiplying Factor to set
        :raise TypeError: Raised when degree is not a integer
        :raise TypeError: Raised when coefficient is not a float or an integer
        """

        if type(degree) == int:
            self.degree = degree if degree >= 0 else 0  # Check if the degree is positive or zero
        else:
            raise TypeError("'degree' must be an integer (not \"{}\"".format(type(degree).__name__))

        if type(coefficient) == float:
            self.coefficient = coefficient
        elif type(coefficient) == int:
            self.coefficient = float(coefficient)
        else:
            raise TypeError("'coefficient' must be a float (not \"{}\"".format(type(coefficient).__name__))

    def __add__(self, other):
        """
        :param Monomial other: Monomial object to add up
        :return Monomial: Result of the Sum
        :raise TypeError: Raised when a non-Monomial object tried to be summed up with this one
        :raise ValueError: Raised if the Monomial Objects do not have the same degree
        """

        if type(other) is Monomial:
            if other.get_degree() == self.degree:
                return Monomial(self.degree, self.coefficient + other.get_coefficient())
            else:
                raise ValueError("ValueError: can only concatenate Monomial objects with the same degree")
        else:
            raise TypeError("can only concatenate Monomial (not \"{}\") to Monomial".format(type(other).__name__))

    def __mul__(self, other):
        """
        :param Monomial other: Monomial object to multiply
        :return Monomial: Result of the Multiplication
        :raise TypeError: Raised when a non-Monomial object tried to be multiplied with this one
        """

        if type(other) is Monomial:
            return Monomial(self.degree + other.get_degree(), self.coefficient * other.get_coefficient())
        else:
            raise TypeError("can only multiply Monomial by Monomial (not \"{}\")".format(type(other).__name__))

    def __str__(self):
        """
        :return str string: Character String of the Monomial
        """

        string = ""

        if self.coefficient != 1 or self.degree == 0:
            string += str(self.coefficient)

        if self.degree != 0:
            string += "x^{}".format(self.degree)

        return string

    def get_degree(self):
        """
        :return int: Degree of the Monomial
        """

        return self.degree

    def get_coefficient(self):
        """
        :return float: Multiplying Factor of the Monomial
        """

        return self.coefficient

    def set_degree(self, degree: int):
        """
        :param int degree: Degree of the Monomial to set
        """

        self.degree = degree if degree >= 0 else 0

    def set_coefficient(self, coefficient: float):
        """
        :param float coefficient: Multiplying Factor of the Monomial
        """

        self.coefficient = coefficient

    def derive(self):
        """
        Derives the Monomial

        :return Monomial: Derivative of the Monomial
        """

        return Monomial(self.degree - 1, self.coefficient * self.degree)
    
    def calculate(self, value: float):
        """
        Returns the result of the Monomial's Calculation with a given value

        :param float value: Value to use for the calculation of the Monomial (integers can be used)
        :return float: Result of the Calculation
        :raise TypeError: Raised when 'value' is not a float or an integer
        """

        if type(value) == int:
            value = float(value)

        if type(value) == float:
            return self.coefficient * value ** self.degree
        else:
            raise TypeError("value must be an integer or a float (not \"{}\")".format(type(value).__name__))
