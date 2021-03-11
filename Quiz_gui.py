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
answers_choice_bonus = [1]
user_answer = []
user_answerb = []
indexes = []
def gen():
    global user
    global indexes
    while(len(indexes)<user):
        x = random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)

def quit(): # Quit
    root.destroy()



def wrong():
    bonimage.destroy()
    bontext.destroy()
    x1.destroy()
    x2.destroy()
    x3.destroy()
    x4.destroy()
    bonus_image = Label(root,background = "#ffffff")
    bonus_image.pack(pady=(100,80))
    bonus_ques = PhotoImage(file = "bear.gif")
    bonus_image.configure(image = bonus_ques)
    bonus_image.image = bonus_ques
    labelresulttext_bonus = Label(root,font = ("Consolas",30),background = "#ffffff")
    labelresulttext_bonus.pack()
    labelresulttext_bonus.configure(text = "Wrong Answer\nYour score is:{}".format(score),foreground = "#E77471")
    quitwrong = Button(root,text="Quit",fg = "blue",height = 2,width=7,background = "#ffffff",font = ("Comic sans MS",30),command = quit)
    quitwrong.pack(pady = (15,30))

def correct():
    global score
    bonimage.destroy()
    bontext.destroy()
    x1.destroy()
    x2.destroy()
    x3.destroy()
    x4.destroy()
    bonus_image = Label(root,background = "#ffffff")
    bonus_image.pack(pady=(100,80))
    bonus_ques = PhotoImage(file = "download.png")
    bonus_image.configure(image = bonus_ques)
    bonus_image.image = bonus_ques
    labelresulttext_bonus = Label(root,font = ("Consolas",30),background = "#ffffff")
    labelresulttext_bonus.pack()
    score = score + 10
    labelresulttext_bonus.configure(text = "Correct!\nYour score is:{}\nThanks for playing!".format(score),foreground = "#E77471")
    quitcorrect = Button(root,text="Quit",fg = "#ffffff",height = 2,width=7,background = "#FF0000",font = ("Comic sans MS",30),command = quit)
    quitcorrect.pack(pady = (15,30))



def bonround(): #Bonus question
    global bontext
    global bonimage
    global x1,x2,x3,x4
    labelimage.destroy()
    labelresulttext.destroy()
    quitbutton.destroy()
    bonus.destroy()
    bonimage = Label(root,background = "#ffffff")
    bonimage.pack(pady=(50,30))
    boques = PhotoImage(file = "giphy.gif")
    bonimage.configure(image = boques)
    bonimage.image = boques
    bontext = Label(root,text = "Which famous Hollywood\nmovie is this scene from? ",fg = "#2481BE",bg = "#ffffff",font = ("Consolas",25))
    bontext.pack()

    global radiobonus
    radiobonus = IntVar()
    radiobonus.set(-1)

    x1 = Radiobutton(root,text = "Pulp Fiction",font = ("Times",20),value = 0,variable = radiobonus,background = "#ffffff",height = 2,width = 25,foreground = "#54BAD8",command = wrong)
    x1.pack(pady = (15,25))

    x2 = Radiobutton(root,text = "The Shawshank Redemption",font = ("Times",20),value = 1,variable = radiobonus,background = "#ffffff",height = 2,width = 25,foreground = "#54BAD8",command = correct)
    x2.pack(pady = (15,25))
    
    x3 = Radiobutton(root,text = "The Godfather I",font = ("Times",20),value = 2,variable = radiobonus,background = "#ffffff",height = 2,width = 25,foreground = "#54BAD8",command = wrong)
    x3.pack(pady = (15,25))
    
    x4 = Radiobutton(root,text = "The Matrix",font = ("Times",20),value = 3,variable = radiobonus,background = "#ffffff",height = 2,width = 25,foreground = "#54BAD8",command = wrong)
    x4.pack(pady = (15,25))


def showresult(score):
    global user
    global labelimage
    global labelresulttext
    global quitbutton
    global bonus
    lblquestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(root,background = "#ffffff")
    labelimage.pack(pady=(150,30))
    labelresulttext = Label(root,font = ("Consolas",30),background = "#ffffff")
    labelresulttext.pack()
    quitbutton = Button(root,text="Quit",fg = "#ffffff",height = 2,width=7,background = "#FF0000",font = ("Comic sans MS",30),command = quit)
    quitbutton.pack(pady = (15,30))
    bonus = Frame(root)
    bonus.pack(pady=(5,20))
    Button(bonus,text="Bonus",fg = "C68E17",height = 2,width=7,background = "#FFFF00",font = ("Comic sans MS",30),command = bonround).pack()

    if score >= (user*5)//2:
        image = PhotoImage(file = "gif.gif")
        labelimage.configure(image = image)
        labelimage.image = image
        labelresulttext.configure(text = "Nice Work!\nYour score is:{}".format(score),foreground = "#E77471")
    else:
        image = PhotoImage(file = "meme.png")
        labelimage.configure(image = image)
        labelimage.image = image
        labelresulttext.configure(text = "You can do better\nYour score is: {}".format(score))





def calc():
    global score
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
    global user
    global radiovar,user_answer
    global lblquestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques<user:
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



def startquiz(): # Question and MC options
    int_text.destroy()
    int_box.destroy()
    int_button.destroy()
    int_answer.destroy()

    global lblquestion,r1,r2,r3,r4
    lblquestion = Label(root,text = questions[indexes[0]],font = ("Consolas",25),width = 300,justify = "center",wraplength = 400,background = "#E0FFFF",foreground = "#254117")
    lblquestion.pack(pady = (30,50))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(root,text = answers_choice[indexes[0]][0],font = ("Times",20),value = 0,variable = radiovar,background = "#C6DEFF",height = 2,width = 25,foreground = "#151B8D",command = selected,)
    r1.pack(pady = (30,50))

    r2 = Radiobutton(root,text = answers_choice[indexes[0]][1],font = ("Times",20),value = 1,variable = radiovar,background = "#C6DEFF",height = 2,width = 25,foreground = "#151B8D",command = selected,)
    r2.pack(pady = (30,50))
    
    r3 = Radiobutton(root,text = answers_choice[indexes[0]][2],font = ("Times",20),value = 2,variable = radiovar,background = "#C6DEFF",height = 2,width = 25,foreground = "#151B8D",command = selected,)
    r3.pack(pady = (30,50))
    
    r4 = Radiobutton(root,text = answers_choice[indexes[0]][3],font = ("Times",20),value = 3,variable = radiovar,background = "#C6DEFF",height = 2,width = 25,foreground = "#151B8D",command = selected,)
    r4.pack(pady = (30,50))





def number():
    global user
    try:
        user = int(int_box.get())
    except ValueError:
        int_answer.config(text = "Please enter a number between 1-10",bg = "#ffffff",fg = "#C42121")
    if user <= 10 and user >= 1:
        gen()
        startquiz()
    else:
        int_answer.config(text = "Please enter a number between 1-10",bg = "#ffffff",fg = "#C42121")

    # int_text.destroy()
    # int_box.destroy()
    # int_button.destroy()
    # gen()
    # startquiz()

def startispressed(): # Start button command
    global int_text
    global int_box
    global int_button
    global int_answer
    labelimage.destroy()
    labeltext.destroy()
    instruction.destroy()
    rules.destroy()  
    fm.destroy()
    
    int_text = Label(root,text = "How many questions would you like?",fg = "#254117",bg = "#48CCCD",font = ("Consolas",25),width = 40,height = 3)
    int_text.pack()
    int_box = Entry(root)
    int_box.pack(pady = 20)
    int_button = Button(root,text = "Start",height = 2,width = 10,command = number,bg = "#438D80",fg = "#ffffff")
    int_button.pack(pady = (10,20))
    int_answer = Label(root)
    int_answer.pack(pady = (20,26))



    # gen()
    # startquiz()


# Starting point
root = tkinter.Tk()
root.title("Quiz Master")
root.geometry("1200x900")
root.config(background = "#b1fb17")

# First crown image
image1 = PhotoImage(file="crown2.gif")
labelimage = Label(root,image = image1,background = "#ffffff",height = 400,width = 600)
labelimage.pack()

# Quiz Title
labeltext = Label(root,text = "Quiz Master",font = ("Comic sans MS",44),background = "#b1fb17")
labeltext.pack(pady=(5,20))

# Start Button
fm = Frame(root)
fm.pack(pady=(5,20))
Button(fm,text="Start",fg = "ffffff",height = 2,width=7,background = "#ffff00",font = ("Comic sans MS",30),command = startispressed).pack()

# Instructions and rules
instruction = Label(root,text = "Read the rules\nClick once you are ready",background = "#ffffff",font = ("Consolas",14),justify = "center")
instruction.pack(pady=(10,40))
rules = Label(root,text = """The quiz consists of 5 questions.Each question in the quiz is of multiple-choice format.
 Read each question carefully,and select a suitable answer for each of the questions. The questions in the quiz are based on general subjects.
  Each correct or incorrect response will result in an appropriate feedback immediately on screen.
The entered option will be the final and cannot be changed. The total score for the quiz is based on your responses to all questions.
In the end of the quiz, you will be provided with a choice to answer a bonus question. """,width=160,height=15,font = ("Times",15),background = "#fff8c6",foreground = "#000000")
rules.pack()

root.mainloop() # To run

