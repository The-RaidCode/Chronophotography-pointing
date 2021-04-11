# -*- coding: utf-8 -*-

import tkinter

from libs.gui.managers import ApplicationManager


class ToolsBarManager:
    """
    Class managing tools/button

    Attributes

    Methods

    """
    def __init__(self):
        self.__import_media_icon = tkinter.PhotoImage(file="resources/icons/toolbar/import_media_32.png")
        self.__delete_media_icon = tkinter.PhotoImage(file="resources/icons/toolbar/delete_media_32.png")
        self.__calibration_icon = tkinter.PhotoImage(file="resources/icons/toolbar/calibration_32.png")
        self.__pointing_icon = tkinter.PhotoImage(file="resources/icons/toolbar/pointing_32.png")
        self.__unpointing_icon = tkinter.PhotoImage(file="resources/icons/toolbar/unpointing_32.png")
        self.__zoom_in_icon = tkinter.PhotoImage(file="resources/icons/toolbar/zoom_in_32.png")
        self.__zoom_out_icon = tkinter.PhotoImage(file="resources/icons/toolbar/zoom_out_32.png")
        self.__move_icon = tkinter.PhotoImage(file="resources/icons/toolbar/move_32.png")

        self.__application_manager = ApplicationManager.ApplicationManager.get_instance()
        self.__application = self.__application_manager.get_application()

        self.__frame = tkinter.Frame(self.__application, bg="#7584F2")
        self.__frame.grid(column=0, row=0)

        self.__fichier = tkinter.LabelFrame(self.__frame, bg="#7584F2", pady=30)
        self.__fichier.grid(column=0, row=0)
        self.__point = tkinter.LabelFrame(self.__frame, bg="#7584F2", pady=30)
        self.__point.grid(column=0, row=1)
        self.__deplacement = tkinter.LabelFrame(self.__frame, bg="#7584F2", pady=30)
        self.__deplacement.grid(column=0, row=2)

        self.__ouvrir = tkinter.Button(self.__fichier, image=self.__import_media_icon, bg="#7584F2", relief="flat")
        self.__ouvrir.grid(column=0, row=0)
        self.__fermer = tkinter.Button(self.__fichier, image=self.__delete_media_icon, bg="#7584F2", relief="flat")
        self.__fermer.grid(column=0, row=1)

        self.__placement = tkinter.Button(self.__point, image=self.__pointing_icon, bg="#7584F2", relief="flat")
        self.__placement.grid(column=0, row=0)
        self.__suppression = tkinter.Button(self.__point, image=self.__unpointing_icon, bg="#7584F2", relief="flat")
        self.__suppression.grid(column=0, row=1)
        self.__echelle = tkinter.Button(self.__point, image=self.__calibration_icon, bg="#7584F2", relief="flat")
        self.__echelle.grid(column=0, row=2)

        self.__zoom = tkinter.Button(self.__deplacement, image=self.__zoom_in_icon, bg="#7584F2", relief="flat")
        self.__zoom.grid(column=0, row=0)
        self.__dezoom = tkinter.Button(self.__deplacement, image=self.__zoom_out_icon, bg="#7584F2", relief="flat")
        self.__dezoom.grid(column=0, row=1)
        self.__translation = tkinter.Button(self.__deplacement, image=self.__move_icon, bg="#7584F2", relief="flat")
        self.__translation.grid(column=0, row=2)

        print(self.__application_manager.get_image_manager().get_canvas_height())
        print(self.__frame.size())
        self.__frame.config(pady=(
                                         self.__application_manager.get_image_manager().get_canvas_height() - self.__frame.winfo_reqheight()) // 2)
