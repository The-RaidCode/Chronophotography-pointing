# -*- coding: utf-8 -*-

class Monomial:
    """
    A class which represents a Monomial (Mathematics)

    Attributes
        degree (int) : Degree of the Monomial
        coefficient (float) : Multiplying Factor of the Monomial
        var_name (str) : Name of the used Variable when converted to str (must be a unique character)

    Methods
        add : Add up a Monomial object to this one
        deepcopy : Return a new Object with the same arguments
        derive : Returns the Derivative as an other Monomial Instance
    """

    def __init__(self, degree: int, coefficient: float, var_name: str = "x"):
        """
        :param int degree: Degree to set
        :param float coefficient: Multiplying Factor to set
        :param str var_name: Name of the used Variable when converted to str (must a unique character)
        :raise TypeError: Raised when degree is not a integer
        :raise TypeError: Raised when coefficient is not a integer
        :raise TypeError: Raised when var_name is not a integer
        :raise ValueError: Raised when var_name is more than one character
        """

        if type(degree) == int:
            self.degree = degree if degree >= 0 else 0  # Check if the degree is positive or zero
        else:
            raise TypeError("'degree' must be an integer (not \"{}\"".format(type(degree).__name__))

        if type(coefficient) == float:
            self.coefficient = coefficient
        else:
            raise TypeError("'coefficient' must be a float (not \"{}\"".format(type(coefficient).__name__))

        if type(var_name) == str:
            if len(var_name) == 1:
                self.var_name = var_name
            else:
                raise ValueError("var_name must be a unique character")
        else:
            raise TypeError("'var_name' must be a string (not \"{}\"".format(type(var_name).__name__))

    def __str__(self):
        """
        :return str: Character String of the Monomial
        """

        return "{coefficient}{var}^{p}".format(coefficient=self.coefficient, p=self.degree, var=self.var_name)

    def add(self, other):
        """
        Add up a Monomial object to this one

        :param Monomial other:
        :raise TypeError: Raised when a non-Monomial object tried to be summed up with this one
        :raise ValueError: Raised if the Monomial Objects do not have the same variable
        :raise ValueError: Raised if the Monomial Objects do not have the same degree
        """

        if type(other) is Monomial:
            if other.get_var_name() == self.var_name:
                if other.get_degree() == self.degree:
                    self.coefficient += other.get_coefficient()
                else:
                    raise ValueError("ValueError: can only concatenate Monomial objects with the same degree")
            else:
                raise ValueError("ValueError: can only concatenate Monomial objects with the same variable")
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

    def get_var_name(self):
        """
        :return str: Name of the used Variable when converted to str
        """

        return self.var_name

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

    def set_var_name(self, var_name: str):
        """
        :param str var_name: Name of the used Variable when converted to str to set
        """

        self.var_name = var_name

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

        return Monomial(self.degree, self.coefficient, self.var_name)
