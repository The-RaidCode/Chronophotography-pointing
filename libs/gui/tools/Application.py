# -*- coding: utf-8 -*-

import re
import threading
import tkinter


class Application(threading.Thread):
    """
    A class which represents a Tkinter window application

    Attributes
        name (str) : Name of the window
        geometry (str) : Geometry of the window
        icon (str) : Path to the icon of the window
        resizable (bool) : Window resizable with the mouse or not
        background (str) : Default hexadecimal background color code

    Methods
        destroy : Stops the window
        run : Overridden method from Threading that creates window and new thread
    """

    ERR_NAME = "Name"
    ERR_RESOLUTION = "Resolution"
    ERR_ICON = "Icon"
    ERR_RESIZABLE = "Resizable"
    ERR_BACKGROUND = "Background"

    def __init__(self, name: str, geometry: str, icon: str, resizable=True, background="#ffffff"):
        """
        Creates a tkinter window with parameters and starts a thread

        :param str name: Name of the window
        :param str geometry: Width and height of the default window, ex: 1920x1080
        :param str icon: Path to the icon of the window, must be a .ico file
        :param bool resizable: Define if the window will be resizable or not
        :param str background: Default hexadecimal background color code
        """

        self._window = None
        self._appName = None
        self._geometry = None
        self._icon = None
        self._resizable = None
        self._background = None
        self._is_fullscreen = None

        self.set_app_name(name)
        self.set_geometry(geometry)
        self.set_icon(icon)
        self.set_resizable(resizable)
        self.set_background(background)

        threading.Thread.__init__(self)
        self.start()

    def __set_fullscreen(self, event=None):
        """
        Set or unset fullscreen mode on the window
        """

        if self._is_fullscreen:
            self._window.attributes("-fullscreen", False)
            self._is_fullscreen = False
        else:
            self._window.attributes("-fullscreen", True)
            self._is_fullscreen = True

    def destroy(self):
        """
        Stops and exits current window
        """

        self._window.quit()

    def run(self):
        self._window = tkinter.Tk()
        self._window.protocol("WM_DELETE_WINDOW", self.destroy)

        self.__buildApp()

        self._window.mainloop()

    def __buildApp(self):
        """
        Builds application and applies parameters to tkinter window
        """

        self._window.resizable(self._resizable, self._resizable)
        self._window.title(self._appName)
        if self._geometry == "fullscreen":
            self.set_geometry("{0}x{1}+0+0".format(self._window.winfo_screenwidth(), self._window.winfo_screenheight()))
            self.__set_fullscreen()
        self._window.geometry(self._geometry)
        self._window.iconbitmap(self._icon)
        self._window.config(bg=self._background)

        self._window.bind("<F11>", self.__set_fullscreen)

    # -*- Setter -*-

    def set_app_name(self, name: str):
        """
        :param str name: Name of the window
        """

        if 3 <= len(name) <= 16:
            self._appName = str(name)
        else:
            raise ValueError("This value must be between 3 and 16 chars", self.ERR_NAME)

    def set_geometry(self, geometry: str):
        """
        :param str geometry: Geometry of the window
        """

        if geometry == "fullscreen":
            self._geometry = geometry
            self._is_fullscreen = False
        elif re.match(r"^\d{1,5}x\d{1,5}", geometry):
            self._geometry = geometry
        else:
            raise ValueError("This value doesn't respect the format", self.ERR_RESOLUTION)

    def set_icon(self, icon: str = " "):
        """
        :param str icon: Path to the icon of the window
        """

        if re.match(r"^(\w+\\)*\w+.ico$", icon):
            try:
                with open(icon, "r"):
                    self._icon = icon
            except FileNotFoundError:
                raise ValueError("This value doesn't lead to any file", self.ERR_ICON)
        else:
            raise ValueError("This value doesn't respect the format", self.ERR_ICON)

    def set_resizable(self, resizable: bool):
        """
        :param bool resizable: Window resizable or not
        """

        if isinstance(resizable, bool):
            self._resizable = resizable
        else:
            raise ValueError("This value must be a boolean", self.ERR_RESIZABLE)

    def set_background(self, background: str):
        """
        :param str background: Hexadecimal code of the background of the window
        """

        if re.match(r"^#[a-zA-Z0-9]{6}$", background):
            self._background = background
        else:
            raise ValueError("This value must be an hexadecimal color code", self.ERR_BACKGROUND)

    # -*- Getters -*-

    def get_app_name(self):
        """
        :return str: Application name
        """

        return self._appName

    def get_geometry(self):
        """
        :return str: Current geometry of the application
        """

        return self._geometry

    def get_icon(self):
        """
        :return str: Path to the icon of the application
        """

        return self._icon

    def get_resizable(self):
        """
        :return bool: If the window is resizable or not
        """

        return self._resizable

    def get_background(self):
        """
        :return str: Background color of the window (hexadecimal code)
        """

        return self._background

    def get_window(self):
        """
        :return Tk: Current window
        """

        return self._window
