from tkinter import *
from Point import *
from Vector import *

top = Tk()
test = Canvas(top, background='red', height=700, width=1000)

oval =test.create_oval(100, 105, 105, 100)
instance = []
def suppr():
    test.delete(top, oval)


button1 = Button(top, text='vector', command=suppr).pack(side='left')


def recherche(x,y):
    for point in instance:
        if (point.get_x() - x <= 5 or point.get_x() + x <= 5) and (point.get_y() - y <= 5 or point.get_y() + y <= 5):
            print('oui')

instance.append(Point(100, 100))
instance.append(Point(300, 100))
instance.append(Point(400, 100))
instance.append(Point(100, 200))

recherche(110, 100)
test.pack()
top.mainloop()
