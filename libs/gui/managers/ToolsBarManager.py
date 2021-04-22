# -*- coding: utf-8 -*-

import math
import tkinter

from libs.gui.managers import ApplicationManager
from libs.gui.managers.MenuBarManager import MenuBarManager


class ToolsBarManager:
    """
    Class managing the tools bar on the left side of the window

    Attributes
        application_manager (ApplicationManager) : Instance of the application manager
        application (Application) : Instance of the main application
        mode_manager (ModeManager) : Instance of the mode manager
        menu_bar_manager (MenuBarManager) : Instance of the menu bar manager
        main_frame (Frame) : Main tools bar frame
        file_frame (LabelFrame) : File frame
        point_frame (LabelFrame) : Point frame
        movement_frame (LabelFrame) Movement frame

    Methods
        load_file_frame : Loads file frame
        load_point_frame : Loads point frame
        load_movement_frame : Loads movement frame
    """

    def __init__(self):
        """
        Creates an instance of ToolsBarManager and loads label frames
        """

        self.__application_manager = ApplicationManager.ApplicationManager.get_instance()
        self.__application = self.__application_manager.get_application()
        self.__mode_manager = self.__application_manager.get_mode_manager()
        self.__menu_bar_manager = self.__application_manager.get_menu_bar_manager()

        self.__main_frame = tkinter.Frame(self.__application, bg="#7584F2")
        self.__main_frame.grid(column=0, row=0)

        self.__file_frame = tkinter.LabelFrame(self.__main_frame, bg="#7584F2", pady=30)
        self.__file_frame.grid(column=0, row=0)
        self.__point_frame = tkinter.LabelFrame(self.__main_frame, bg="#7584F2", pady=30)
        self.__point_frame.grid(column=0, row=1)
        self.__movement_frame = tkinter.LabelFrame(self.__main_frame, bg="#7584F2", pady=30)
        self.__movement_frame.grid(column=0, row=2)

        self.__import_media_icon = tkinter.PhotoImage(file="resources/icons/toolbar/import_media_32.png")
        self.__delete_media_icon = tkinter.PhotoImage(file="resources/icons/toolbar/delete_media_32.png")
        self.__calibration_icon = tkinter.PhotoImage(file="resources/icons/toolbar/calibration_32.png")
        self.__pointing_icon = tkinter.PhotoImage(file="resources/icons/toolbar/pointing_32.png")
        self.__erase_icon = tkinter.PhotoImage(file="resources/icons/toolbar/erase_32.png")
        self.__zoom_in_icon = tkinter.PhotoImage(file="resources/icons/toolbar/zoom_in_32.png")
        self.__zoom_out_icon = tkinter.PhotoImage(file="resources/icons/toolbar/zoom_out_32.png")
        self.__move_icon = tkinter.PhotoImage(file="resources/icons/toolbar/move_32.png")

        self.__load_file_frame()
        self.__load_point_frame()
        self.__load_movement_frame()

        self.__application.update_idletasks()

        self.__main_frame.config(pady=(math.ceil(self.__application_manager.get_image_manager().get_canvas_height() -
                                                 self.__main_frame.winfo_reqheight()) / 2) + 2)

    def __load_file_frame(self):
        """
        Loads file frame with all components
        """

        self.__open_file = tkinter.Button(self.__file_frame, image=self.__import_media_icon, bg="#7584F2",
                                          relief="flat", command=MenuBarManager.open_file_explorer)
        self.__open_file.grid(column=0, row=0)
        self.__close_file = tkinter.Button(self.__file_frame, image=self.__delete_media_icon, bg="#7584F2",
                                           relief="flat", command=MenuBarManager.clear_canvas)
        self.__close_file.grid(column=0, row=1)

    def __load_point_frame(self):
        """
        Loads point frame with all components
        """

        self.__placement = tkinter.Button(self.__point_frame, image=self.__pointing_icon, bg="#7584F2", relief="flat",
                                          command=lambda: self.__mode_manager.set_current_mode(0))
        self.__placement.grid(column=0, row=0)
        self.__suppression = tkinter.Button(self.__point_frame, image=self.__erase_icon, bg="#7584F2", relief="flat",
                                            command=lambda: self.__mode_manager.set_current_mode(1))
        self.__suppression.grid(column=0, row=1)
        self.__scale = tkinter.Button(self.__point_frame, image=self.__calibration_icon, bg="#7584F2", relief="flat",
                                      command=lambda: self.__mode_manager.set_current_mode(2))
        self.__scale.grid(column=0, row=2)

    def __load_movement_frame(self):
        """
        Loads movement frame with all components
        """

        self.__zoom_in = tkinter.Button(self.__movement_frame, image=self.__zoom_in_icon, bg="#7584F2", relief="flat")
        self.__zoom_in.grid(column=0, row=0)
        self.__zoom_out = tkinter.Button(self.__movement_frame, image=self.__zoom_out_icon, bg="#7584F2", relief="flat")
        self.__zoom_out.grid(column=0, row=1)
        self.__translation = tkinter.Button(self.__movement_frame, image=self.__move_icon, bg="#7584F2", relief="flat",
                                            command=lambda: self.__mode_manager.set_current_mode(3))
        self.__translation.grid(column=0, row=2)
