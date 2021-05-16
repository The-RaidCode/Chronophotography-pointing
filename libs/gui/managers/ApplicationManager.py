# -*- coding: utf-8 -*-

from libs.gui.Application import Application
from libs.gui.managers.ImageManager import ImageManager
from libs.gui.managers.InstructionManager import InstructionManager
from libs.gui.managers.MenuBarManager import MenuBarManager
from libs.gui.managers.ModeManager import ModeManager
from libs.gui.managers.ToolsBarManager import ToolsBarManager


class ApplicationManager:
    """
    A class managing the main application

    Attributes
        static instance (ApplicationManager) : Instance of the ApplicationManager
        application (Application) : Instance of the main tkinter application
        instruction_manager (InstructionManager) : Instance of the instruction manager
        mode_manager (ModeManager) : Instance of the mode manager
        tools_bar_manager (ToolsBarManager) : Instance of the tools bar manager
        image_manager (ImageManager) : Instance of the image manager
        menu_bar_manager (MenuBarManager) : Instance of the menu bar manager
        list_points (list: Point) : List containing placed points
        scale_points (list: Point) : List containing placed scale points
        speed_vectors (list: Vector) : List containing speed vectors
        acceleration_vectors (list: Vector) : List containing acceleration vectors

    Methods
        build_menu_bar : Builds tkinter menu bar, this method must be executed in last position
        run_application : Starts tkinter application
    """

    __instance = None

    def __init__(self):
        """
        Creates instance of a new tkinter Application and configures the app
        """

        ApplicationManager.__instance = self

        self.__list_points = []
        self.__list_scale = []

        self.__speed_vectors = []
        self.__acceleration_vectors = []

        self.__application = Application("Physique", "1280x720", "resources/icons/icon.ico", True, "#595959")
        self.__application.state("zoomed")

        self.__menu_bar_manager = None

        self.__instruction_manager = InstructionManager()
        self.__mode_manager = ModeManager()
        self.__image_manager = ImageManager()
        self.__tools_bar_manager = ToolsBarManager()
        self.__menu_bar_manager = MenuBarManager()

    def run_application(self):
        """
        Starts tkinter application
        """

        self.__application.mainloop()

    # -*- Getters -*-

    def get_application(self):
        """
        :return Application: Main application instance
        """

        return self.__application

    def get_instruction_manager(self):
        """
        :return InstructionManager: Instruction manager instance
        """

        return self.__instruction_manager

    def get_image_manager(self):
        """
        :return ImageManager: Image manager instance
        """

        return self.__image_manager

    def get_mode_manager(self):
        """
        :return ModeManager: Mode manager instance 
        """
        return self.__mode_manager

    def get_menu_bar_manager(self):
        """
        :return MenuBarManager: Menu bar manager instance
        """

        return self.__menu_bar_manager

    def get_list_points(self):
        """
        :return list: Point: List containing placed points
        """

        return self.__list_points

    def get_list_scale(self):
        """
        :return list: Point: List containing placed scale points
        """

        return self.__list_scale

    def get_speed_vectors(self):
        """
        :return list: Vector: List containing speed vectors
        """

        return self.__speed_vectors

    def get_acceleration_vectors(self):
        """
        :return list: Vector: List containing acceleration vectors
        """

        return self.__acceleration_vectors

    # -*- Setters -*-

    def set_list_points(self, list_points: list):
        """
        :param list_points: List of points
        """

        self.__list_points = list_points

    def set_list_scale(self, list_scale: list):
        """
        :param list_scale: List of scale points
        """

        self.__list_scale = list_scale

    def set_speed_vectors(self, speed_vectors: list):
        """
        :param speed_vectors: List of speed vectors
        """

        self.__speed_vectors = speed_vectors

    def set_acceleration_vectors(self, acceleration_vectors: list):
        """
        :param acceleration_vectors: List of acceleration vectors
        """

        self.__acceleration_vectors = acceleration_vectors

    @staticmethod
    def get_instance():
        """
        :return ApplicationManager: ApplicationManager instance
        """

        return ApplicationManager.__instance
