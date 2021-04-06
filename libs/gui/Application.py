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

        self.setAppName(name)
        self.setGeometry(geometry)
        self.setIcon(icon)
        self.setResizable(resizable)
        self.setBackground(background)

        threading.Thread.__init__(self)
        self.start()

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
        self._window.geometry(self._geometry)
        self._window.iconbitmap(self._icon)
        self._window.config(bg=self._background)

    # -*- Setter -*-

    def setAppName(self, name: str):
        """
        :param str name: Name of the window
        """

        if 3 <= len(name) <= 16:
            self._appName = str(name)
        else:
            raise ValueError("This value must be between 3 and 16 chars", self.ERR_NAME)

    def setGeometry(self, geometry: str):
        """
        :param str geometry: Geometry of the window
        """

        if re.match(r"^\d{1,5}x\d{1,5}$", geometry):
            self._geometry = geometry
        else:
            raise ValueError("This value doesn't respect the format", self.ERR_RESOLUTION)

    def setIcon(self, icon: str = " "):
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

    def setResizable(self, resizable: bool):
        """
        :param bool resizable: Window resizable or not
        """

        if isinstance(resizable, bool):
            self._resizable = resizable
        else:
            raise ValueError("This value must be a boolean", self.ERR_RESIZABLE)

    def setBackground(self, background: str):
        """
        :param str background: Hexadecimal code of the background of the window
        """

        if re.match(r"^#[a-zA-Z0-9]{6}$", background):
            self._background = background
        else:
            raise ValueError("This value must be an hexadecimal color code", self.ERR_BACKGROUND)

    # -*- Getters -*-

    def getAppName(self):
        """
        :return str: Application name
        """

        return self._appName

    def getGeometry(self):
        """
        :return str: Current geometry of the application
        """

        return self._geometry

    def getIcon(self):
        """
        :return str: Path to the icon of the application
        """

        return self._icon

    def getResizable(self):
        """
        :return bool: If the window is resizable or not
        """

        return self._resizable

    def getBackground(self):
        """
        :return str: Background color of the window (hexadecimal code)
        """

        return self._background

    def getWindow(self):
        """
        :return Tk: Current window
        """

        return self._window
