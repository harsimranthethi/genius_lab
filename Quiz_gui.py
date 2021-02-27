import tkinter
from tkinter import *

def startquiz():
    lblquestion = Label(root,text = "This is a sample question",font = ("Consolas",25),width = 300,justify = "center",wraplength = 400,background = "#ffffff",foreground = "#FC6C85")
    lblquestion.pack(pady = (30,50))

    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(root,text = "sample choice 1",font = ("Times",20),value = 0,variable = radiovar,background = "#ffffff",height = 2,width = 15,foreground = "#E77471")
    r1.pack(pady = (30,50))

    r2 = Radiobutton(root,text = "sample choice 2",font = ("Times",20),value = 1,variable = radiovar,background = "#ffffff",height = 2,width = 15,foreground = "#E77471")
    r2.pack(pady = (30,50))
    
    r3 = Radiobutton(root,text = "sample choice 3",font = ("Times",20),value = 2,variable = radiovar,background = "#ffffff",height = 2,width = 15,foreground = "#E77471")
    r3.pack(pady = (30,50))
    
    r4 = Radiobutton(root,text = "sample choice 4",font = ("Times",20),value = 3,variable = radiovar,background = "#ffffff",height = 2,width = 15,foreground = "#E77471")
    r4.pack(pady = (30,50))
    

def startispressed(): # Start button command
    labelimage.destroy()
    labeltext.destroy()
    instruction.destroy()
    rules.destroy()  
    fm.destroy()
    startquiz()


# Starting point
root = tkinter.Tk()
root.title("Quiz Master")
root.geometry("1200x900")
root.config(background = "#ffffff")

# First crown image
image1 = PhotoImage(file="crown2.gif")
labelimage = Label(root,image = image1,background = "#ffffff",height = 400,width = 600)
labelimage.pack()

# Quiz Title
labeltext = Label(root,text = "Title",font = ("Comic sans MS",44),background = "#ffffff")
labeltext.pack(pady=(5,20))

# Start Button
fm = Frame(root)
fm.pack(pady=(5,20))
Button(fm,text="Start",fg = "green",height = 2,width=7,background = "#ffffff",font = ("Comic sans MS",30),command = startispressed).pack()

# Instructions and rules
instruction = Label(root,text = "Read the rules\nClick once you are ready",background = "#ffffff",font = ("Consolas",14),justify = "center")
instruction.pack(pady=(10,90))
rules = Label(root,text = """Instructions here""",width=120,height=10,font = ("Times",15),background = "#48cccd",foreground = "#ffffff")
rules.pack()

root.mainloop() # To run

