# -*- coding: utf-8 -*-

from Monomial import Monomial


class Polynomial:
    """
    A class which represents a Polynomial (Mathematics)

    Attributes
        terms (list) : List of the Monomial objects making the Polynomial

    Methods
        add : Adds up a Polynomial object to this one
        add_term : Adds a new Monomial to the Polynomial
        calculate : Returns the result of the Polynomial's Calculation with a given value
        derive : Returns the Derivative as an other Polynomial Instance
    """

    def __init__(self, monomials: list):
        """
        :param list monomials: List of the Monomials to set
        :raise TypeError: Raised if the argument 'monomials' is not a list
        :raise TypeError: Raised if a non-Monomial object tried to be add to this Polynomial
        """

        if type(monomials) == list:
            self.terms = []

            for term in monomials:
                if type(term) == Monomial:  # Checks if all the elements of monomials are Monomial Objects
                    self.terms.append(term)
                else:
                    raise TypeError("can only contain Monomial object (not \"{}\")".format(type(term).__name__))
        else:
            raise TypeError("argument 'monomials' must be a list (not\"{}\"".format(type(monomials).__name__))

    def __str__(self):
        """
        :return str: Character String of the Polynomial
        """

        return "+".join([str(m) for m in self.terms])

    def add(self, other):
        """
        Adds up a Polynomial object to this one

        :param Polynomial other: Polynomial object to add to this one
        :raise TypeError: Raised when a non-Polynomial object tried to be summed up with this one
        """

        if type(other) == Polynomial:
            for term in other.get_terms():
                self.add_term(term)
        else:
            raise TypeError('can only concatenate Polynomial (not "{}") to Polynomial'.format(type(other).__name__))

    def get_terms(self):
        """
        :return list: List of the Polynomial's terms
        """

        return self.terms

    def add_term(self, new_term: Monomial):
        """
        Adds a new Monomial object to the Polynomial

        :param Monomial new_term: Monomial object to add
        :raise TypeError: Raised when new_term is not a Monomial Object
        """

        if type(new_term) == Monomial:
            added = False

            for i in range(len(self.terms)):  # Try to add, by adding coefficient with a Monomial of the same degree
                if new_term.get_degree() == self.terms[i].get_degree():
                    self.terms[i].add(new_term)
                    added = True

                    if self.terms[i].get_coefficient() == 0:  # If the coefficient is zero; remove the Monomial
                        self.terms.pop(i)

                    break

            if not added:  # If a Monomial of the same degree doesn't exist or with a different variable
                self.terms.append(new_term.deepcopy())
        else:
            raise TypeError("can only add a Monomial object (not \"{}\"".format(type(new_term).__name__))

    def derive(self):
        """
        Derives this Polynomial

        :return Polynomial: Derivative of the Monomial
        """

        return Polynomial([n.derive() for n in self.terms])

    def calculate(self, value: float):
        """
        Returns the result of the Polynomial's Calculation with a given value

        :param float value: Value to use for the calculation of the Polynomial (integers can be used)
        :return float: Result of the Calculation
        :raise TypeError: Raised when 'value' is not a float or an integer
        """

        if type(value) == int:
            value = float(value)

        if type(value) == float:
            result = 0

            for monomial in self.terms:
                result += monomial.calculate(value)

            return result
        else:
            raise TypeError("value must be an integer or a float (not \"{}\")".format(type(value).__name__))
