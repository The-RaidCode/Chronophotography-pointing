# -*- coding: utf-8 -*-

import tkinter

from PIL import Image, ImageTk

from libs.gui.managers import ApplicationManager
from libs.math.geometry.Point import Point


class ImageManager:
    """
    Class managing image on the canvas area

    Attributes
        application_manager (ApplicationManager) : Instance of the application manager
        canvas (Canvas) : Tkinter canvas representing draw zone
        image (PIL.Image.Image) : Current image on canvas
        tk_image (PIL.ImageTK.PhotoImage) : Current photo image on canvas
        id_photo (PhotoImage) : Tkinter image representation and identifier
        x_mouse (int) : X mouse position
        y_mouse (int) : Y mouse position
        im_height (int) : Image's height (pixel)
        im_width (int) : Image's width (pixel)
        canvas_height (int) : Canvas's height (pixel)
        canvas_width (int) : Canvas's width (pixel)

    Methods
        load_image : Loads an image on the canvas from his path and bind events
        origin : Event triggered on left click
        slide : Event triggered on mouse slide to slide image
        zoom : Event triggered on mousewheel roll to zoom image
    """

    def __init__(self):
        """
        Creates an instance of ImageManager and prepare canvas for images
        """

        self.__image = None
        self.__tk_image = None
        self.__id_photo = None

        self.__x_mouse = 0
        self.__y_mouse = 0
        self.__im_height = 0
        self.__im_width = 0

        self.__application_manager = ApplicationManager.ApplicationManager.get_instance()
        screen__height = self.__application_manager.get_application().winfo_screenheight()
        screen_width = self.__application_manager.get_application().winfo_screenwidth()

        self.__canvas_height = screen__height // 4 * 3
        self.__canvas_width = screen_width // 4 * 3

        self.__canvas = tkinter.Canvas(self.__application_manager.get_application(), bg="#E2FADB",
                                       height=self.__canvas_height, width=self.__canvas_width)

        self.__canvas.grid(column=1, row=0)

    def load_image(self, path: str):
        """
        Loads an image on the canvas from his path and bind events

        :param str path: Path to the chosen image
        """
        application = self.__application_manager.get_application()
        application.set_app_name(application.get_main_title() + " - " + path)

        self.__image = Image.open(path)
        image_width, image_height = self.__image.size
        if image_width / image_height < self.__canvas_width / self.__canvas_height:
            nw = int(image_width * (self.__canvas_height / image_height))
            nh = self.__canvas_height
        else:
            nw = self.__canvas_width
            nh = int(image_height * (self.__canvas_width / image_width))
        self.__image = self.__image.resize((nw, nh), Image.ANTIALIAS)
        self.__tk_image = ImageTk.PhotoImage(self.__image)
        self.__id_photo = self.__canvas.create_image(self.__canvas_width // 2, self.__canvas_height // 2,
                                                     image=self.__tk_image)

        box = self.__image.getbbox()
        self.__im_height = box[2] - box[0]
        self.__im_width = box[3] - box[1]

        self.__canvas.bind("<Button-1>", self.__left_click)

    def clear_canvas(self):
        """
        Clears the canvas and reset data
        """

        self.__canvas.delete("all")

        self.__image = None
        self.__tk_image = None
        self.__id_photo = None

        self.__x_mouse = 0
        self.__y_mouse = 0
        self.__im_height = 0
        self.__im_width = 0

    def __left_click(self, event):
        """
        Triggered on left click

        :param event: Event triggered by Tkinter
        """

        x = event.x
        y = event.y

        mode = self.__application_manager.get_mode_manager().get_current_mode()
        if mode == 0:
            Point(x, y).draw(self.__application_manager.get_application(),
                             self.__application_manager.get_image_manager().get_canvas())
        elif mode == 1:
            point = Point.research(x, y)
            if point:
                point.remove()
        elif mode == 2:
            pass
        else:
            pass

    def __slide(self, event):
        """
        Triggered on left slide click
        Moves image on new coordinates

        :param event: Event triggered by Tkinter
        """

        self.__canvas.move(self.__id_photo, event.x - self.__x_mouse, event.y - self.__y_mouse)
        self.__x_mouse = event.x
        self.__y_mouse = event.y

    def __zoom(self, event):
        """
        Triggered on mousewheel roll
        Zoom on the image

        :param event: Event triggered by Tkinter
        """

        x_coordinates, y_coordinates = [int(s) for s in self.__canvas.coords(self.__id_photo)]
        self.__im_height = int(self.__im_height * (1 + event.delta / 1000))
        self.__im_width = int(self.__im_width * (1 + event.delta / 1000))
        self.__image = self.__image.resize((self.__im_height, self.__im_width))
        self.__tk_image = ImageTk.PhotoImage(self.__image)
        self.__canvas.delete(self.__id_photo)
        self.__id_photo = self.__canvas.create_image(x_coordinates, y_coordinates, image=self.__tk_image)

    # -*- Getters -*-

    def get_canvas(self):
        """
        :return Canvas: Tkinter canvas object
        """

        return self.__canvas

    def get_id_photo(self):
        """
        :return int: Photo identifier
        """

        return self.__id_photo

    def get_canvas_width(self):
        """
        :return int: Current canvas width
        """

        return self.__canvas_width

    def get_canvas_height(self):
        """
        :return int: Current canvas height
        """

        return self.__canvas_height
