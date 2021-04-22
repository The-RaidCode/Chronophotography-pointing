# -*- coding: utf-8 -*-

from libs.gui.Application import Application
from libs.gui.managers.ImageManager import ImageManager
from libs.gui.managers.MenuBarManager import MenuBarManager
from libs.gui.managers.ModeManager import ModeManager
from libs.gui.managers.ToolsBarManager import ToolsBarManager


class ApplicationManager:
    """
    A class managing the main application

    Attributes
        static instance (ApplicationManager) : Instance of the ApplicationManager
        application (Application) : Instance of the main tkinter application
        mode_manager (ModeManager) : Instance of the mode manager
        tools_bar_manager (ToolsBarManager) : Instance of the tools bar manager
        image_manager (ImageManager) : Instance of the image manager
        menu_bar_manager (MenuBarManager) : Instance of the menu bar manager

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

        self.__application = Application("Physique", "1280x720", "resources/icons/icon.ico", True, "#595959")
        self.__application.state("zoomed")

        self.__menu_bar_manager = None

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
        :return list: List containing placed points
        """

        return self.__list_points

    def get_list_scale(self):
        """
        :return list: List containing placed scale points
        """

        return self.__list_scale

    @staticmethod
    def get_instance():
        """
        :return ApplicationManager: ApplicationManager instance
        """

        return ApplicationManager.__instance

    # -*- Setters -*-

    def set_list_points(self, points: list):
        """
        :param points: Array list of the placed points
        """

        self.__list_points = points

    def set_list_scale(self, scale: list):
        """
        :param scale: Array list of the placed scale points
        """

        self.__list_scale = scale
