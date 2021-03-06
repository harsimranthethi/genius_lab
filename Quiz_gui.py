import tkinter
from tkinter import *
import random

questions  = ["The place of origin of an earthquake is called:",
"Who is the english physicist responsible for the Big Bang Theory?",
"The busiest  sea route is:",
"This is a sample ques 4",
"This is a sample ques 5",
"This is a sample ques 6",
"This is a sample ques 7",
"This is a sample ques 8",
"This is a sample ques 9",
"This is a sample ques 10"]



answers_choice = [
["Epicentre","Seismal","Focus","Amphidromic Point"],
["Albert Einstein","Michael Skube","George Gamow","Roger Penrose"],
["The Mediterranean Red-Sea Route","The South Atlantic Route","The North Atlantic Route","The Pacific Route"],
["13","14","15","16"],
["17","18","19","20"],
["21","22","23","24"],
["25","26","27","28"],
["29","30","31","32"],
["33","34","35","36"],
["37","38","39","40"]
]

answers = [2,2,2,1,1,1,1,1,1,1]

user_answer = []

indexes = []
def gen():
    global indexes
    while(len(indexes)<5):
        x = random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)

def bonques():
    labelimage.destroy()




def showresult(score):
    lblquestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(root,background = "#ffffff")
    labelimage.pack(pady=(150,30))
    labelresulttext = Label(root,font = ("Consolas",30),background = "#ffffff")
    labelresulttext.pack()
    bonus = Button(root,text="Bonus",fg = "blue",height = 2,width=7,background = "#ffffff",font = ("Comic sans MS",30),command = bonques)
    bonus.pack(pady = (15,30))
    if score >= 15:
        image = PhotoImage(file = "jk2.gif")
        labelimage.configure(image = image)
        labelimage.image = image
        labelresulttext.configure(text = "Nice Work!\nYour score is:{}".format(score))
    else:
        image = PhotoImage(file = "rm.gif")
        labelimage.configure(image = image)
        labelimage.image = image
        labelresulttext.configure(text = "You can do better\nYour score is: {}".format(score))





def calc():
    global indexes,user_answer,answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    print("Your score is:",score)
    showresult(score)




ques = 1
def selected():
    global radiovar,user_answer
    global lblquestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques<5:
        lblquestion.config(text = questions[indexes[ques]])
        r1["text"] = answers_choice[indexes[ques]][0]
        r2["text"] = answers_choice[indexes[ques]][1]
        r3["text"] = answers_choice[indexes[ques]][2]
        r4["text"] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        print(indexes)
        print(user_answer)
        calc()






def startquiz():
    global lblquestion,r1,r2,r3,r4
    lblquestion = Label(root,text = questions[indexes[0]],font = ("Consolas",25),width = 300,justify = "center",wraplength = 400,background = "#ffffff",foreground = "#FC6C85")
    lblquestion.pack(pady = (30,50))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(root,text = answers_choice[indexes[0]][0],font = ("Times",20),value = 0,variable = radiovar,background = "#ffffff",height = 2,width = 25,foreground = "#E77471",command = selected,)
    r1.pack(pady = (30,50))

    r2 = Radiobutton(root,text = answers_choice[indexes[0]][1],font = ("Times",20),value = 1,variable = radiovar,background = "#ffffff",height = 2,width = 25,foreground = "#E77471",command = selected,)
    r2.pack(pady = (30,50))
    
    r3 = Radiobutton(root,text = answers_choice[indexes[0]][2],font = ("Times",20),value = 2,variable = radiovar,background = "#ffffff",height = 2,width = 25,foreground = "#E77471",command = selected,)
    r3.pack(pady = (30,50))
    
    r4 = Radiobutton(root,text = answers_choice[indexes[0]][3],font = ("Times",20),value = 3,variable = radiovar,background = "#ffffff",height = 2,width = 25,foreground = "#E77471",command = selected,)
    r4.pack(pady = (30,50))
    

def startispressed(): # Start button command
    labelimage.destroy()
    labeltext.destroy()
    instruction.destroy()
    rules.destroy()  
    fm.destroy()
    gen()
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
instruction.pack(pady=(10,40))
rules = Label(root,text = """The quiz consists of 5 questions.Each question in the quiz is of multiple-choice format.
 Read each question carefully,and select a suitable answer for each of the questions. The questions in the quiz are based on general subjects.
  Each correct or incorrect response will result in an appropriate feedback immediately on screen.
After responding to a question, click on the "Next Question" button at the bottom to go to the next question. The total score for the quiz is based on your responses to all questions.
In the end of the quiz, """,width=160,height=15,font = ("Times",15),background = "#48cccd",foreground = "#ffffff")
rules.pack()

root.mainloop() # To run

