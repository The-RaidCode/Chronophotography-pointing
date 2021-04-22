from tkinter import *
from Point import *
from Vector import *

top = Tk()
test = Canvas(top, background='red', height=700, width=1000)




def point_manager(event):
    Point(event.x, event.y).draw(top, test, 'blue')

def vector_manager():
    for point in Point.instances[:-1]:
        Vector(point, 50, 50).draw(top, test)

def suppretion():
    # test.delete(top, Point.instances[-1].image)
    # Point.instances.pop(-1)
    if Point.get_last()!= None :
        Point.get_last().remove()



def click(event):
    point = Point.research(event.x, event.y)
    if point != None:
        point.remove()


button1 = Button(top, text='vector', command=vector_manager).pack(side='left')
button2 = Button(top, text='back', command=suppretion).pack(side='left')

test.bind("<Button-1>", point_manager)
test.bind("<Button-3>", click)
test.pack()
top.mainloop()
