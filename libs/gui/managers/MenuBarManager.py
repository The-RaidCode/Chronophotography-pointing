# -*- coding: utf-8 -*-

import tkinter.filedialog

from libs.gui.managers import ApplicationManager


class MenuBarManager:
    """
    Class managing the menu bar on the top of the window

    Attributes
        application_manager (ApplicationManager) : Instance of the application manager
        main_menu_bar (Menu) : Main Tkinter menu bar
        menu_file (Menu) : File Tkinter menu bar
        import_media_icon (PhotoImage) : Import media function icon
        delete_media_icon (PhotoImage) : Delete media function icon
        export_csv_icon (PhotoImage) : Export CSV function icon
        quit_icon (PhotoImage) : Quit function icon

    Methods
        load_menu_file : Loads file menu bar
        open_file_explorer : Opens file explorer, triggered on 'Import media' button
        clear_canvas : Clears media from canvas area
    """

    def __init__(self):
        """
        Creates an instance of MenuBarManager and loads menus bar
        """

        self.__application_manager = ApplicationManager.ApplicationManager.get_instance()
        self.__application = self.__application_manager.get_application()

        self.__main_menu_bar = tkinter.Menu(self.__application)
        self.__menu_file = tkinter.Menu(self.__main_menu_bar, tearoff=0)

        self.__import_media_icon = tkinter.PhotoImage(file="resources/icons/menu/import_media_16.png")
        self.__delete_media_icon = tkinter.PhotoImage(file="resources/icons/menu/delete_media_16.png")
        self.__export_csv_icon = tkinter.PhotoImage(file="resources/icons/menu/export_csv_16.png")
        self.__quit_icon = tkinter.PhotoImage(file="resources/icons/menu/quit_16.png")

        self.__load_menu_file()

        self.__application.config(menu=self.__main_menu_bar)
        self.__application.mainloop()

    def __load_menu_file(self):
        """
        Loads file menu bar with all components
        """

        self.__menu_file.add_command(label="Nouveau projet", command=None)
        self.__menu_file.add_command(label="Enregistrer le projet", command=None)
        self.__menu_file.add_command(label="Ouvrir un projet", command=None)
        self.__menu_file.add_separator()
        self.__menu_file.add_command(label="Importer un média (Ctrl+I)", compound="left",
                                     image=self.__import_media_icon, command=self.open_file_explorer)
        self.__menu_file.add_command(label="Supprimer le média (Ctrl+D)", compound="left",
                                     image=self.__delete_media_icon, command=self.clear_canvas)
        self.__menu_file.add_separator()
        self.__menu_file.add_command(label="Exporter en CSV", compound="left",
                                     image=self.__export_csv_icon, command=None)
        self.__menu_file.add_separator()
        self.__menu_file.add_command(label="Quitter (Ctrl+Q)", compound="left",
                                     image=self.__quit_icon, command=self.__application.destroy)

        # Temporary code while functionalities are not fully implemented
        self.__menu_file.entryconfig("Nouveau projet", state="disabled")
        self.__menu_file.entryconfig("Enregistrer le projet", state="disabled")
        self.__menu_file.entryconfig("Ouvrir un projet", state="disabled")

        self.__application_manager.get_application().bind("<Control-i>", self.open_file_explorer)
        self.__application_manager.get_application().bind("<Control-d>", self.clear_canvas)
        self.__application_manager.get_application().bind("<Control-q>", lambda p: self.__application.destroy())

        self.__main_menu_bar.add_cascade(label="Fichier", menu=self.__menu_file)

    @staticmethod
    def open_file_explorer(event=None):
        """
        Triggered on 'Import media' button
        Opens file explorer
        Used to import file into canvas area

        :param event: Event triggered by Tkinter
        """

        filename = tkinter.filedialog.askopenfilename(initialdir="/",
                                                      title="Sélectionner un fichier",
                                                      filetypes=(("Images", ["*.png", "*.jpg", "*.jpeg"]),
                                                                 ("Tous les fichiers", "*.*")))
        if filename:
            ApplicationManager.ApplicationManager.get_instance().get_image_manager().load_image(filename)

    @staticmethod
    def clear_canvas(event=None):
        """
        Triggered on 'Delete media' button
        Delete current media in the canvas area

        :param event: Event triggered by Tkinter
        """

        application_manager = ApplicationManager.ApplicationManager.get_instance()
        application_manager.get_image_manager().clear_canvas()
        application_manager.get_instance().get_application().set_app_name(
            application_manager.get_application().get_main_title())
        application_manager.get_image_manager().get_canvas().unbind("<Button-1>")
