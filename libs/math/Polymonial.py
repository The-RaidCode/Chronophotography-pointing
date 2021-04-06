# -*- coding: utf-8 -*-

class Polynomial:
    """
    A class which represents a Polynomial (Mathematics)

    Attributes
        terms (list) : List of the Monomials making the Polynomial

    Methods
        derive : Returns the Derivative as an other Polynomial Instance
    """

    def __init__(self, monomials: list):
        """
        :param list monomials: List of the Monomials to set
        """

        self.terms = monomials

    def __str__(self, var: str = "x"):
        """
        :param var: Name of the Variable to use
        :return str: Character String of the Polynomial
        """

        return "+".join([m.__str__(var) for m in self.terms])

    def derive(self):
        """
        Derives the Polynomial

        :return Polynomial: Derivative of the Monomial
        """

        return Polynomial([n.derive() for n in self.terms], self.variable)
