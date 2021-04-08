# -*- coding: utf-8 -*-

import tkinter

from libs.gui.Application import Application


class ApplicationManager:
    """
    A class managing the main application

    Attributes
        application (Application) : Instance of the main tkinter application

    Methods
        build_menu_bar : Builds tkinter menu bar, this method must be executed in last position
        run_application : Starts tkinter application
    """

    def __init__(self):
        """
        Creates instance of a new tkinter Application and configures the app

        """
        self.__application = Application("Physique", "1280x720", "resources/icons/icon.ico", True, "#595959")
        self.__application.state("zoomed")

        self.__build_menu_bar()

    def __build_menu_bar(self):
        """
        Builds tkinter menu bar with all the components

        """
        main_menu_bar = tkinter.Menu(self.__application)

        export_csv_icon = tkinter.PhotoImage(file="resources/icons/menu/export_csv.png")
        import_media_icon = tkinter.PhotoImage(file="resources/icons/menu/import_media.png")

        menu_file = tkinter.Menu(main_menu_bar, tearoff=0)
        menu_file.add_command(label="Nouveau projet", command=None)
        menu_file.add_command(label="Enregistrer le projet", command=None)
        menu_file.add_command(label="Ouvrir un projet", command=None)
        menu_file.add_separator()
        menu_file.add_command(label="Importer un média", compound='left', image=export_csv_icon, command=None)
        menu_file.add_separator()
        menu_file.add_command(label="Exporter en CSV", compound='left', image=import_media_icon, command=None)

        # Temporary code while functionalities are not fully implemented
        menu_file.entryconfig("Nouveau projet", state="disabled")
        menu_file.entryconfig("Enregistrer le projet", state="disabled")
        menu_file.entryconfig("Ouvrir un projet", state="disabled")

        main_menu_bar.add_cascade(label="Fichier", menu=menu_file)

        self.__application.config(menu=main_menu_bar)
        self.__application.mainloop()

    def run_application(self):
        """
        Starts tkinter application

        """
        self.__application.mainloop()
