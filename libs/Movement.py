from libs.math.functions import Monomial, Polynomial
from libs.math.geometry import Point, Vector
from scipy.optimize import curve_fit


class Movement:
    """
    A Class which represents a movement described by two functions (abscissa & ordinate).
    The functions are determined with a collection of points given at the instantiation.

    Class Attributes
        FUNCTIONS : Array of functions : linear function and Polynomial from 1st to 3rd degree

    Class Methods
        equ_determinate : Determines the equations of the Movement with the collection of Point

    Attributes
        points (list<Point>) : Collection of Point Objects used to determined the movement's equations
        abs_equation (Polynomial) : Movement's Equations on Abscissa Axis
        ord_equation (Polynomial) : Movement's Equations on Ordinate Axis
        delta_t (float) : Duration between each points
        time (list) : List of the value of time

    Methods
        hydrate : Extracts data from the collection of Points to determined the functions
        speed_vectors : Returns a collection of Vector Objects for each points, representing the Speed Vectors of the
                        movement
        acceleration_vectors : Returns a collection of Vectors Objects for each points, representing the Acceleration
                               Vectors of the movement.
    """

    FUNCTIONS = [lambda x, a: a * x,  # Linear Function
                 lambda x, a, b: a*x + b,  # 1st Degree Polynomial
                 lambda x, a, b, c: a*x**2 + b*x + c,  # 2nd Degree Polynomial
                 lambda x, a, b, c, d: a*x**3 + b*x**2 + c*x + d]  # 3rd Degree Polynomial

    def __init__(self, points: list, delta_t: float, abs_degree: int, ord_degree: int):
        """
        :param list points: List of Point objects, constituting the movement
        :param float delta_t: Duration between each points
        :param int abs_degree: Degree of Polynomial for the Abscissa component of the Movement
        :param int ord_degree: Degree of Polynomial for the Ordinate component of the Movement

        :raise TypeError: Raised when delta_t is not a float or an integer
        :raise ValueError: Raise when delta_t is zero or negative
        :raise TypeError: Raised when points is not a list
        :raise ValueError: Raised when points has less than two elements
        :raise TypeError: Raised when an element of points is not a Point object
        """

        if type(delta_t) == int:
            delta_t = float(delta_t)

        if type(delta_t) == float:
            if delta_t > 0:
                self.__delta_t = delta_t
            else:
                raise ValueError("'delta_t' can not be zero or negative")
        else:
            raise TypeError("'delta_t' must be a float or an integer (not \"{}\")".format(type(delta_t).__name__))

        if type(points) == list:
            if len(points) >= 2:
                i = len(points) - 1
                type_check = True

                while type_check and i >= 0:  # Checks if all the elements of points are Point Objects
                    type_check = type(points[i]) == Point
                    i -= 1

                if type_check:
                    self.__points = points
                else:
                    raise ValueError("all elements of 'points' must be Point object (not \"{}\")".format(type(points[i + 1]).__name__))
            else:
                raise ValueError("'points' must contain several objects (not {})".format(len(points)))
        else:
            raise TypeError("'points' must be list (not \"{}\")".format(type(points).__name__))

        # Determination of the movement's equations

        self.__time, x_data, y_data = [], [], []
        i = 0
        i_max = len(self.__points)

        while i < i_max:
            self.__time.append(self.__delta_t * i)
            x_data.append(self.__points[i].get_x())
            y_data.append(self.__points[i].get_y())

            i += 1

        self.__abs_equation = self.equ_determinate(self.__time, x_data, abs_degree)
        self.__ord_equation = self.equ_determinate(self.__time, y_data, ord_degree)

    @classmethod
    def equ_determinate(cls, x_array: list, y_array: list, degree: int):
        """
        Class method which can determined the function linking the elements of y_array to the ones of x_array

        :param list x_array: List of Floats which are the Inputs of the searched Function
        :param list y_array: List of Floats which are the Outputs of the searched Function
        :param int degree: Degree of the searched Polynomial Function (1 to 3, with linear function as degree 0)

        :raise TypeError: Raised when degree is not an integer
        :raise ValueError: Raised if degree is not 0 (linear function), 1, 2 or 3
        """

        if type(degree) == int:
            if degree > 3 or degree < 0:
                raise ValueError("degree must be 0 (linear function), 1, 2 or 3 (not {})".format(degree))
        else:
            raise TypeError("'degree must be an integer")

        params, covariance = curve_fit(cls.FUNCTIONS[degree], x_array, y_array)

        if degree == 0:
            return Polynomial(Monomial(1, params[0]))
        else:
            return Polynomial(array=[Monomial(i, round(float(params[degree - i]), 6)) for i in range(degree, -1, -1)])

    def speed_vectors(self):
        """
        Returns a collection of Vector Objects for each points, representing the Speed Vectors of the movement

        :return list vectors: List of the Speed Vectors
        """

        vectors = []
        abs_vector = self.__abs_equation.derive()
        ord_vector = self.__ord_equation.derive()

        for i in range(len(self.__points)):
            vectors.append(Vector(self.__points[i], abs_vector.calculate(self.__time[i]), ord_vector.calculate(self.__time[i])))

        return vectors

    def acceleration_vector(self):
        """
        Returns a collection of Vector Objects for each points, representing the Acceleration Vectors of the movement

        :return list vectors: List of the Acceleration Vectors
        """

        vectors = []
        abs_vector = self.__abs_equation.derive().derive()
        ord_vector = self.__ord_equation.derive().derive()

        for i in range(len(self.__points)):
            vectors.append(
                Vector(self.__points[i], abs_vector.calculate(self.__time[i]), ord_vector.calculate(self.__time[i])))

        return vectors

