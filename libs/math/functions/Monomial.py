# -*- coding: utf-8 -*-

class Monomial:
    """
    A class which represents a Monomial (Mathematics)

    Attributes
        degree (int) : Degree of the Monomial
        coefficient (float) : Multiplying Factor of the Monomial

    Methods
        add : Adds up a Monomial object to this one
        calculate : Returns the result of the Monomial's Calculation with a given value
        deepcopy : Returns a new Object with the same arguments
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

    def __str__(self):
        """
        :return str: Character String of the Monomial
        """

        return "{coefficient}x^{p}".format(coefficient=self.coefficient, p=self.degree)

    def add(self, other):
        """
        Adds up a Monomial object to this one

        :param Monomial other:
        :raise TypeError: Raised when a non-Monomial object tried to be summed up with this one
        :raise ValueError: Raised if the Monomial Objects do not have the same degree
        """

        if type(other) is Monomial:
            if other.get_degree() == self.degree:
                self.coefficient += other.get_coefficient()
            else:
                raise ValueError("ValueError: can only concatenate Monomial objects with the same degree")
        else:
            raise TypeError("can only concatenate Monomial (not \"{}\") to Monomial".format(type(other).__name__))

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

    def deepcopy(self):
        """
        Returns a new Object with the same arguments

        :return Monomial: Same Object that self
        """

        return Monomial(self.degree, self.coefficient)
    
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
