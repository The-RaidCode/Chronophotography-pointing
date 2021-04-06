# -*- coding: utf-8 -*-

class Monomial:
    """
    A class which represents a Monomial (Mathematics)

    Attributes
        power (int) : Power of the Monomial
        coefficient (float) : Multiplying Factor of the Coefficient

    Methods
        derive : Returns the Derivative as an other Monomial Instance
    """

    def __init__(self, power: int, c: float):
        """
        :param int power: Power to set
        :param int c: Multiplying Factor to set
        """

        self.power = power if power >= 0 else 0  # Check if the power is positive or zero
        self.coefficient = c

    def __str__(self, var: str = "x"):
        """
        :param str var: Name of the Variable to use
        :return str: Character String of the Monomial
        """

        return "{coeff}*{var}**{p}".format(coeff=self.coefficient, p=self.power, var=var)

    def derive(self):
        """
        Derives the Monomial

        :return Monomial: Derivative of the Monomial
        """

        return Monomial(self.power - 1, self.coefficient * self.power)
