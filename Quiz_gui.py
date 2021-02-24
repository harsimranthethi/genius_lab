import tkinter
from tkinter import *

root = tkinter.Tk()
root.title("Quiz Master")
root.geometry("800x700")

image1 = PhotoImage(file="butterfly.gif")

labelimage = Label(root,image = image1)
labelimage.pack()

root.mainloop()
