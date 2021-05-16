# -*- coding: utf-8 -*-
import tkinter

from libs.gui.managers import ApplicationManager


class InstructionManager:
    """
    Class managing instructions frames and labels

    Attributes
        scale (DoubleVar) : Current entry
        application_manager (ApplicationManager) : Instance of the application manager
        application (Application) : Instance of the main application
        instructions_frame (Frame) : Main instructions frame
        scale_frame (Frame) : Scale frame
        entry_scale_frame (Frame) : Entry scale frame

    Methods
        load_label : Loads pointing labels
        load_scale_frame : Loads scale frame
    """

    def __init__(self):
        """

        """

        self.__scale = tkinter.DoubleVar()

        self.__application_manager = ApplicationManager.ApplicationManager.get_instance()
        self.__application = self.__application_manager.get_application()

        self.__instructions_frame = tkinter.Frame(self.__application, bg="#ffffff")
        self.__instructions_frame.config()
        self.__instructions_frame.grid(column=0, row=1, columnspan=2)

        self.__scale_frame = tkinter.Frame(self.__instructions_frame)
        self.__scale_frame.grid(column=1, row=0, rowspan=2)

        self.__entry_scale_frame = tkinter.LabelFrame(self.__scale_frame, text="Distance réelle pour étalonnage")
        self.__entry_scale_frame.grid(row=2)

        self.__load_label()
        self.__load_scale_frame()

    def __load_label(self):
        tkinter.Label(self.__instructions_frame, text="Pointage:").grid(column=0, row=0)
        tkinter.Label(self.__instructions_frame, text="Cliquez sur les points de la trajectoire dans l'ordre "
                                                      "chronologique").grid(column=0, row=1)

    def __load_scale_frame(self):
        tkinter.Label(self.__scale_frame, text="Etalonnage:").grid(row=0)
        tkinter.Label(self.__scale_frame, text="Cliquez sur les deux extremités d'un objet").grid(row=1)
        tkinter.Entry(self.__entry_scale_frame, textvariable=self.__scale).grid()

    # -*- Getters -*-

    def get_scale(self):
        """
        :return float: Scale entry
        """

        return self.__scale.get()
