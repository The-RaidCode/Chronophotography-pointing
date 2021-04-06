# -*- coding: utf-8 -*-

class Monomial:
    """
    A class which represents a Monomial (Mathematics)

    Attributes
        degree (int) : degree of the Monomial
        coefficient (float) : Multiplying Factor of the Monomial

    Methods
        deepcopy : Return a new Object with the same arguments
        derive : Returns the Derivative as an other Monomial Instance
    """

    def __init__(self, degree: int, coefficient: float):
        """
        :param int degree: degree to set
        :param float coefficient: Multiplying Factor to set
        """

        self.degree = degree if degree >= 0 else 0  # Check if the degree is positive or zero
        self.coefficient = coefficient

    def __str__(self, var: str = "x"):
        """
        :param str var: Name of the Variable to use
        :return str: Character String of the Monomial
        """

        return "{coeff}{var}^{p}".format(coeff=self.coefficient, p=self.degree, var=var)

    def __add__(self, other):
        if type(other) is Monomial:
            if other.get_degree() == self.degree:
                self.coefficient += other.get_coefficient()
            else:
                raise ValueError("ValueError: can only concatenate Monomial objects with the same degree")
        else:
            raise TypeError('TypeError: can only concatenate Monomial (not "{}") to Monomial'.format(type(other).__name__))

    def get_degree(self):
        """
        :return int: degree of the Monomial
        """

        return self.degree

    def get_coefficient(self):
        """
        :return float: Multiplying Factor of the Monomial
        """

        return self.coefficient

    def set_degree(self, degree: int):
        """
        :param int degree: degree of the Monomial to set
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
        Return a new Object with the same arguments

        :return Monomial: Same Object that self
        """

        return Monomial(self.degree, self.coefficient)
