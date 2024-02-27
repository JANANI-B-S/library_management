from tkinter import *
from tkinter import Canvas
import PIL
from tkinter import *
from tkinter import Canvas
import PIL
import mysql_connector
from PIL import ImageTk, Image

# Designing the window
root = Tk()
img = PhotoImage(file="bit.png")
root.title("Library")
root.minsize(width=400, height=400)
root.geometry("1020x735")
root.iconphoto(False,img)

# Add Background Image
bg = Image.open("Lib.jpg")

def resize_image(event):
    width = event.width
    height = event.height
    image = bg.resize((width,height),Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0,0,image=photo,anchor='nw')
    canvas.image = photo

# create a canvas
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()

# Create a canvas
canvas = Canvas(root, width=windowWidth, height=windowHeight)
canvas.pack(fill="both", expand=True)
canvas.bind('<Configure>', resize_image)

root.mainloop()