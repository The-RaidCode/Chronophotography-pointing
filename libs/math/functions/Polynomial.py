# -*- coding: utf-8 -*-

from libs.math.functions.Monomial import Monomial


class Polynomial:
    """
    A class which represents a Polynomial (Mathematics)

    Attributes
        terms (list) : List of the Monomial objects making the Polynomial

    Methods
        add_term : Adds one or several new Monomial object(s) to the Polynomial
        calculate : Returns the result of the Polynomial's Calculation with a given value
        derive : Returns the Derivative as an other Polynomial Instance
        simplify : Simplifies this Polynomial by adding up Monomial objects with the same degree
    """

    def __init__(self, *monomials: Monomial, array=None):
        """
        :param Monomial monomials: Monomial object(s) to set
        :param list array: Array of Monomial object(s) to set
        :raise TypeError: Raised if a non-Monomial object tried to be add to this Polynomial
        """
        if array is None:
            array = []
        self.__terms = []

        for item in monomials:
            if type(item) == Monomial:  # Checks if all the elements of monomials are Monomial Objects
                self.__terms.append(item)
            else:
                raise TypeError("can only contain Monomial object (not \"{}\")".format(type(item).__name__))

        for term in array:  # Same that above, but with array
            if type(term) == Monomial:
                self.__terms.append(term)
            else:
                raise TypeError("can only contain Monomial object (not \"{}\")".format(type(term).__name__))

        self.simplify()

    def __add__(self, other):
        """
        :param Polynomial other: Polynomial object to add to this one
        :return Polynomial: Result of the Sum
        :raise TypeError: Raised when a non-Polynomial object tried to be summed up with this one
        """

        if type(other) == Polynomial:
            return Polynomial(array=self.__terms + other.get_terms())
        else:
            raise TypeError('can only concatenate Polynomial (not "{}") to Polynomial'.format(type(other).__name__))

    def __mul__(self, other):
        """
        :param Polynomial other: Polynomial object to multiply
        :return Polynomial: Result of the Multiplication
        :raise TypeError: Raised when a non-Polynomial object tried to be multiplied with this one
        """

        if type(other) == Polynomial:
            final_terms = []

            for self_term in self.__terms:
                for other_term in other.get_terms():
                    final_terms.append(self_term * other_term)

            return Polynomial(array=final_terms)
        else:
            raise TypeError('can only concatenate Polynomial (not "{}") to Polynomial'.format(type(other).__name__))

    def __eq__(self, other):
        """
        :param other: Object to compare
        :return bool: Result of the comparison
        """

        if type(other) == Polynomial:
            other_terms = other.get_terms()
            i_max = len(self.__terms)
            j_max = len(other_terms)

            i = 0
            same = i_max == j_max

            while same and i < i_max:
                j = 0
                found = False

                while not found and j < j_max:
                    found = self.__terms[i] == other_terms[j]
                    j += 1

                same = found
                i += 1
            return same
        else:
            return False

    def __str__(self):
        """
        :return str string: Character String of the Polynomial
        """

        string = str(self.__terms[0])

        for monomial in self.__terms[1:]:
            if monomial.get_coefficient() >= 0:
                string += "+"

            string += str(monomial)

        return string

    def get_terms(self):
        """
        :return list: List of the Polynomial's terms
        """

        return self.__terms

    def add_term(self, *new_terms: Monomial):
        """
        Adds one or several new Monomial object(s) to the Polynomial

        :param Monomial new_terms: Monomial object(s) to add
        :raise TypeError: Raised when new_term is not a Monomial Object
        """

        for new in new_terms:
            if type(new) == Monomial:
                self.__terms.append(new)
            else:
                raise TypeError("can only add a Monomial object (not \"{}\")".format(type(new).__name__))

            self.simplify()

    def derive(self):
        """
        Derives this Polynomial

        :return Polynomial: Derivative of the Polynomial
        """

        return Polynomial(array=[n.derive() for n in self.__terms])

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

            for monomial in self.__terms:
                result += monomial.calculate(value)

            return result
        else:
            raise TypeError("value must be an integer or a float (not \"{}\")".format(type(value).__name__))

    def simplify(self):
        """
        Simplifies this Polynomial by adding up Monomial objects with the same degree
        """

        i = 0

        while i < len(self.__terms):
            j = i + 1
            while j < len(self.__terms):
                if self.__terms[i].get_degree() == self.__terms[j].get_degree():
                    self.__terms[i] += self.__terms[j]
                    self.__terms.pop(j)
                    # No incrementation because self.terms[j] is a new object
                else:
                    j += 1
            i += 1

        i = 0

        while i < len(self.__terms):
            if self.__terms[i].get_coefficient() == 0:
                self.__terms.pop(i)
            else:
                i += 1
