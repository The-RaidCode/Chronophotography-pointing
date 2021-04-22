class ModeManager:
    """
    Class managing draw modes

    Attributes
        current_mode (int) : Selected draw mode
    """

    def __init__(self):
        """
        Creates an instance of ModeManager and set default mode to 0
        """
        self.__current_mode = 0

    # -*- Getters -*-

    def get_current_mode(self):
        """
        :return int: Current draw mode
        """

        return self.__current_mode

    # -*- Setters -*-

    def set_current_mode(self, mode: int):
        """
        :param mode: Draw mode
        """
        if 0 <= mode <= 3:
            self.__current_mode = mode
