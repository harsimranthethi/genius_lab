import random
q1 = """The place of origin of an earthquake is called:
a.Epicentre\nb.Seismal\nc.Focus\nd.Amphidromic Point"""
q2 = """Who is the english physicist responsible for the "Big Bang Theory"?:
a.Albert Einstein\nb.Michael Skube\nc.George Gamow\nd.Roger Penrose"""
q3 = """The busiest  sea route is:
a.The Mediterranean Red-Sea Route\nb.The South Atlantic Route\nc.The North Atlantic Route\nd.The Pacific Route"""
q4 = """Who is known as the 'Nightingale of India'?
a.Indira Gandhi\nb.Kittur Rani Chennamma\nc.Savithri Bai Phule\nd.Sarojini Naidu"""
<<<<<<< HEAD
q5 = """Which of the following has no skeleton at all?
a.Starfish\nb.Sponge\nc.Jellyfish\nd.Silver Fish"""
=======
q5 = """Who coined the term 'Supermoon'?
a.Richard Nolle\nb.Michael Gauquelin\nc.Shawn Carlson\nd.None of the above"""
>>>>>>> 6bf93c16f256a5cf83a6b80cb5ad5cf8a7573f3d
q6 = """Where is the headquarters of SAARC?
a.Dhaka\nb.Jakarta\nc.Kathmandu\nd.Manila"""
q7 = """Who was the first president of Russia?
a.Boris Yeltsin\nb.Vladimir Putin\nc.Dmitry Medvedev\nd.Kokichi"""
q8 = """Which two calender months are named after Roman Emperors?
a.July and June\nb.December and May\nc.July and August\nc.March and April"""
q9 = """The world's most populated country is:
a.USA\nb.Russia\nc.India\nd.China"""
<<<<<<< HEAD
q10 = """The capital of Philippines is:
a.Dili\nb.Manila\nc.Marawi\nd.Jakarta"""
questions = {q1:"c",q2:"c",q3:"c",q4:"d",q5:"c",q6:"c",q7:"a",q8:"c",q9:"d",q10:"b"} # Question-Answer dictionary

score = 0
#a = input("How many questions would you like?: ")

rand_ques = random.sample(list(questions),5) # To randomly select 5 questions.
=======
q10 = """The capital of philipines is:
a.Dili\nb.Manila\c.Marawi\nd.Jakarta"""
questions = {q1:"c",q2:"a",q3:"c",q4:"d",q5:"a",q6:"c",q7:"a",q8:"c",q9:"d",q10:"b"} # Question-Answer dictionary

score = 0
rand_ques = random.sample(list(questions),5) # To randomly select 5 questions
>>>>>>> 6bf93c16f256a5cf83a6b80cb5ad5cf8a7573f3d
for i in rand_ques:
    print(i)
    print()
    answer = input("Enter your answer: ")
    print()
    if answer == questions[i]:
        print("Well done! You get one point.")
        score = score + 1    
    else:
        print("Sorry, wrong answer")
        print("The correct answer was:",questions[i])
        print()
print("Final score is:",score,"/ 5")


