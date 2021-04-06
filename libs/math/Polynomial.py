# -*- coding: utf-8 -*-

from Monomial import Monomial


class Polynomial:
    """
    A class which represents a Polynomial (Mathematics)

    Attributes
        terms (list) : List of the Monomials making the Polynomial

    Methods
        add : Add up to Polynomials
        add_term : Adds a new Monomial to the Polynomial
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

    def add(self, other):
        """
        :param Polynomial other: Polynomial to add to this one
        """

        if type(other) == Polynomial:
            for term in other.get_terms():
                self.add_term(term)
        else:
            raise TypeError('TypeError: can only concatenate Polynomial (not "{}") to Polynomial'.format(type(other).__name__))

    def get_terms(self):
        """
        :return list: List of the Polynomial's terms
        """

        return self.terms

    def add_term(self, new_term: Monomial):
        """
        Adds a new Monomial to the Polynomial

        :param Monomial new_term: Monomial to add
        """

        print(self, new_term)

        added = False

        for i in range(len(self.terms)):  # Try to add, by adding coefficient with a Monomial of the same degree
            if new_term.get_degree() == self.terms[i].get_degree():
                self.terms[i].__add__(new_term)
                added = True
                break

        if not added:  # If a Monomial of the same degree doesn't exist
            self.terms.append(new_term.deepcopy())

    def derive(self):
        """
        Derives the Polynomial

        :return Polynomial: Derivative of the Monomial
        """

        return Polynomial([n.derive() for n in self.terms], self.variable)
