# -*- coding: utf-8 -*-

import re
import tkinter


class Application(tkinter.Tk):
    """
    A class which represents a Tkinter window application

    Attributes
        app_name (str) : Name of the window
        geometry (str) : Geometry of the window
        icon (str) : Path to the icon of the window
        resizable (bool) : Window resizable with the mouse or not
        background (str) : Default hexadecimal background color code
        fullscreen_mode (bool) : Window fullscreen mode

    Methods
        change_fullscreen_mode : Change window's fullscreen mode
    """

    def __init__(self, app_name: str, geometry: str, icon: str, resizable: bool, background: str):
        """
        Creates a tkinter window with parameters and starts a thread

        :param str app_name: Name of the window
        :param str geometry: Width and height of the default window, ex: 1920x1080
        :param str icon: Path to the icon of the window, must be a .ico file
        :param bool resizable: Define if the window will be resizable or not
        :param str background: Default hexadecimal background color code
        """

        self.__app_name = None
        self.__geometry = None
        self.__icon = None
        self.__resizable = None
        self.__background = None
        self.__fullscreen_mode = None

        tkinter.Tk.__init__(self)

        self.set_app_name(app_name)
        self.set_geometry(geometry)
        self.set_icon(icon)
        self.set_resizable(resizable)
        self.set_background(background)

        self.__build_app()

    def __change_fullscreen_mode(self):
        """
        Change window's fullscreen mode
        """

        self.attributes("-fullscreen", self.__fullscreen_mode)

    def __build_app(self):
        """
        Builds application and applies parameters to tkinter window
        """

        self.protocol("WM_DELETE_WINDOW", self.destroy)
        self.resizable(self.__resizable, self.__resizable)
        self.title(self.__app_name)
        self.iconbitmap(self.__icon)
        self.config(bg=self.__background)
        self.bind("<F11>", lambda p: self.set_fullscreen_mode(not self.__fullscreen_mode))

        if self.__geometry == "fullscreen":
            self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
            self.set_fullscreen_mode(True)
        else:
            self.geometry(self.__geometry)
            self.set_fullscreen_mode(False)

    # -*- Setters -*-

    def set_app_name(self, app_name: str):
        """
        :param str app_name: Name of the window
        """

        if 3 <= len(app_name) <= 16:
            self.__app_name = str(app_name)
        else:
            raise ValueError("this value must be between 3 and 16 chars (not {})".format(len(app_name)))

    def set_geometry(self, geometry: str):
        """
        :param str geometry: Geometry of the window
        """

        if geometry == "fullscreen":
            self.__geometry = geometry
            self.__fullscreen_mode = True
        elif re.match(r"^\d{1,5}x\d{1,5}", geometry):
            self.__geometry = geometry
        else:
            raise ValueError("this value doesn't respects the format '0000x000' or 'fullscreen'")

    def set_icon(self, icon: str = " "):
        """
        :param str icon: Path to the icon of the window
        """

        if re.match(r"^(\w+\\)*\w+.ico$", icon):
            try:
                with open(icon, "r"):
                    self.__icon = icon
            except FileNotFoundError:
                raise ValueError("this path doesn't lead to any file")
        else:
            raise ValueError("this path doesn't respect the format")

    def set_resizable(self, resizable: bool):
        """
        :param bool resizable: Window resizable or not
        """

        if isinstance(resizable, bool):
            self.__resizable = resizable
        else:
            raise ValueError("this value must be a boolean")

    def set_background(self, background: str):
        """
        :param str background: Hexadecimal code of the background of the window
        """

        if re.match(r"^#[a-zA-Z0-9]{6}$", background):
            self.__background = background
        else:
            raise ValueError("this value must be an hexadecimal color code")

    def set_fullscreen_mode(self, fullscreen_mode: bool):
        """
        :param fullscreen_mode: Fullscreen mode
        """

        if isinstance(fullscreen_mode, bool):
            self.__fullscreen_mode = fullscreen_mode
            self.__change_fullscreen_mode()
        else:
            raise ValueError("this value must be a boolean")

    # -*- Getters -*-

    def get_app_name(self):
        """
        :return str: Application name
        """

        return self.__appName

    def get_geometry(self):
        """
        :return str: Current geometry of the application
        """

        return self.__geometry

    def get_icon(self):
        """
        :return str: Path to the icon of the application
        """

        return self.__icon

    def get_resizable(self):
        """
        :return bool: If the window is resizable or not
        """

        return self.__resizable

    def get_background(self):
        """
        :return str: Background color of the window (hexadecimal code)
        """

        return self.__background

    def get_fullscreen_mode(self):
        """
        :return: Current fullscreen mode
        """

        return self.__fullscreen_mode
