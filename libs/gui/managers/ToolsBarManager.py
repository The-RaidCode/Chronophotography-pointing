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
        self.__import_media_icon = tkinter.PhotoImage(file="resources/icons/menu/import_media.png")
        self.__delete_media_icon = tkinter.PhotoImage(file="resources/icons/menu/delete_media.png")

        self.__application_manager = ApplicationManager.ApplicationManager.get_instance()
        self.__application = self.__application_manager.get_application()

        self.__frame = tkinter.Frame(self.__application, bg="#7584F2", pady=258)
        self.__frame.grid(column=0, row=0)

        self.__fichier = tkinter.LabelFrame(self.__frame, text="Fichier", bg="#7584F2")
        self.__fichier.grid(column=0, row=0)
        self.__point = tkinter.LabelFrame(self.__frame, text="Points", bg="#7584F2")
        self.__point.grid(column=0, row=1)
        self.__deplacement = tkinter.LabelFrame(self.__frame, text="Déplacement", bg="#7584F2")
        self.__deplacement.grid(column=0, row=2)

        self.__ouvrir = tkinter.Button(self.__fichier, image=self.__import_media_icon, bg="#7584F2", relief="flat")
        self.__ouvrir.grid(column=0, row=0)
        self.__fermer = tkinter.Button(self.__fichier, image=self.__delete_media_icon, bg="#7584F2", relief="flat")
        self.__fermer.grid(column=0, row=1)

        self.__placement = tkinter.Button(self.__point, bg="#7584F2", relief="flat")
        self.__placement.grid(column=0, row=0)
        self.__suppression = tkinter.Button(self.__point, bg="#7584F2", relief="flat")
        self.__suppression.grid(column=0, row=1)
        self.__echelle = tkinter.Button(self.__point, bg="#7584F2", relief="flat")
        self.__echelle.grid(column=0, row=2)

        self.__zoom = tkinter.Button(self.__deplacement, bg="#7584F2", relief="flat")
        self.__zoom.grid(column=0, row=0)
        self.__dezoom = tkinter.Button(self.__deplacement, bg="#7584F2", relief="flat")
        self.__dezoom.grid(column=0, row=1)
        self.__translation = tkinter.Button(self.__deplacement, bg="#7584F2", relief="flat")
        self.__translation.grid(column=0, row=2)
