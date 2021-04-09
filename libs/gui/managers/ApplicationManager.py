# -*- coding: utf-8 -*-

from libs.gui.Application import Application
from libs.gui.managers.ImageManager import ImageManager
from libs.gui.managers.MenuBarManager import MenuBarManager


class ApplicationManager:
    """
    A class managing the main application

    Attributes
        static instance (ApplicationManager) : Instance of the ApplicationManager
        application (Application) : Instance of the main tkinter application
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

        self.__application = Application("Physique", "1280x720", "resources/icons/icon.ico", True, "#595959")
        self.__application.state("zoomed")

        self.__image_manager = ImageManager()
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

    def get_menu_bar_manager(self):
        """
        :return MenuBarManager: Menu bar manager instance
        """

        return self.__menu_bar_manager

    @staticmethod
    def get_instance():
        """
        :return ApplicationManager: ApplicationManager instance
        """

        return ApplicationManager.__instance
