from libs.gui.Application import Application
from tkinter import *
from PIL import Image, ImageTk


window = Application("Chronophotograph", "1400x800", "logo.ico", True, "#595959")


'''cadre = LabelFrame(window, text='cest un bouton', bg='#595959')
boutton = Button(cadre, text="coucou")
echelle = Scale(window, orient='horizontal', from_=0, to=10, troughcolor='#ff00ff', bg='#595959',
      resolution=0.1, tickinterval=2, length=350,
      label='Volume (db)')
echelle.grid()
boutton.grid()
cadre.grid()'''
#osef c'est juste pour créer les variables
x_mouse,y_mouse=0,0
im_height,im_width=0,0

def origine(event):
    """fixe l'origine du clic de la souris"""
    global x_mouse,y_mouse
    x_mouse, y_mouse = event.x,event.y

def slide(event):
    global photo
    global id_photo
    global x_mouse, y_mouse
    photo.move(id_photo, event.x - x_mouse, event.y -y_mouse)
    x_mouse, y_mouse = event.x, event.y

def zoom(event):
    global photo
    global id_photo
    global drapeau
    global drapeau2
    global im_height,im_width
    print(im_height,im_width)
    im_height, im_width = int(im_height*(1+event.delta/1000)),int(im_width*(1+event.delta/1000))
    print(im_height, im_width)
    drapeau=drapeau.resize((im_height, im_width))
    drapeau2 = ImageTk.PhotoImage(drapeau)
    photo.delete(id_photo)
    id_photo = photo.create_image(x_mouse, y_mouse, image=drapeau2)
    print("zzz")


longueur_fenetre, largeur_fenetre = window.get_geometry().split("x")
longueur_ecran, largeur_ecran = window.winfo_screenwidth(), window.winfo_screenheight()
longueur_fenetre = int(longueur_fenetre)
largeur_fenetre =int(largeur_fenetre)


barre_outils = LabelFrame(window, height=largeur_fenetre, width=50, bg="blue")
photo = Canvas(window, height=largeur_fenetre//4*3, width=(longueur_fenetre-50)//4*3)
recap = Button(window, text="recap")
instruction = Button(window, text="instruction")

boutton5 = Button(barre_outils, text="outil 1")
boutton6 = Button(barre_outils, text="outil 2")
boutton7 = Button(barre_outils, text="outil 3")

box=drapeau.getbbox()
im_height,im_width = box[2]-box[0],box[3]-box[1]


drapeau = Image.open("image test.jpg")
drapeau2 = ImageTk.PhotoImage(drapeau)
id_photo = photo.create_image(318, 159, image=drapeau2)

barre_outils.grid(column=0, row=0, rowspan=2)
photo.grid(column=1, row=0)
recap.grid(column=2, row=0)
instruction.grid(column=1, row=1, columnspan=2)

boutton5.grid(column=0, row=0)
boutton6.grid(column=0, row=1)
boutton7.grid(column=0, row=2)

photo.bind("<B1-Motion>", slide)
photo.bind("<Button-1>", origine)
photo.bind("<MouseWheel>", zoom)

window.mainloop()
