import random
q1 = """The place of origin of an earthquake is called:
a.Epicentre\nb.Seismal\nc.Focus\nd.Amphidromic Point"""
q2 = """Who is the english physicist responsible for the "Big Bang Theory"?:
a.Albert Einstein\nb.Michael Skube\nc.George Gamow\nd.Roger Penrose"""
q3 = """The busiest  sea route is:
a.The Mediterranean Red-Sea Route\nb.The South Atlantic Route\nc.The North Atlantic Route\nd.The Pacific Route"""
q4 = """Who is known as the 'Nightingale of India'?
a.Indira Gandhi\nb.Kittur Rani Chennamma\nc.Savithri Bai Phule\nd.Sarojini Naidu"""
q5 = """Which of the following has no skeleton at all?
a.Starfish\nb.Sponge\nc.Jellyfish\nd.Silver Fish"""
q6 = """Where is the headquarters of SAARC?
a.Dhaka\nb.Jakarta\nc.Kathmandu\nd.Manila"""
q7 = """Who was the first president of Russia?
a.Boris Yeltsin\nb.Vladimir Putin\nc.Dmitry Medvedev\nd.Kokichi"""
q8 = """Which two calender months are named after Roman Emperors?
a.July and June\nb.December and May\nc.July and August\nc.March and April"""
q9 = """The world's most populated country is:
a.USA\nb.Russia\nc.India\nd.China"""
q10 = """The capital of Philippines is:
a.Dili\nb.Manila\nc.Marawi\nd.Jakarta"""
q11 = """The Great Barrier Reef is off the coast of which country?
a.Fiji\nb.Australia\nc.New Zealand\nd.South africa"""
q12 = """What is the world's smallest country?
a.Monaco\nb.Lichtenstein\nc.Vatican city\nd.Luxembourg"""
q13 = """In which country is Mount Fuji located?
a.China\nb.Peru\nc.North Korea\nd.Japan"""
q14 = """Which of these cities is not a national capital?
a.Sydney\nb.Prague\nc.Cairo\nd.Bangkok"""
q15 = """Which was the first newspaper of India?
a.The Hindu\nb.Bengal gazette\nc.Amrit Bazar Patrika\nd.The Bombay Chronicle"""
q16 = """Who is the prime minister of Chandragupta Maurya?
a.Saktar\nb.Birbal\nc.Kautilya\nd.Chavundaraya"""
q17 = """when the state of Mysore renamed as Karnataka?
a.1947\nb.1960\nc.1970\nd.1956"""
q18 = """which of the following is a 'classical' dance form?
a.Kalaripayattu\nb.kathakali\nc.Chhobia\nd.Bhawai"""
q19 = """Dr.MS.Subbalakshmi has distinguished herself in the field of?
a.Kathak\nb.Bharath Natyam\nc.Playing Violin\nd.Vocal Music"""
q20 = """ The correct abbreviation of 'BEL' is:
a.Bharath Electronics Limited\nb.Bangalore Electronics Limited\nc.Belagaum Electronics Limited\nd.Bellary Electronics Limited"""
q21 = """Who is the odd one out?
a.Indira Gandhi\nb.R.K.Narayan\nc.Dr.Rajendra Prasad\nd.Smt Prathibha Patil"""
q22 = """Rama is an avathara of which god?
a.Brahma\nb.Indra\nc.Shiva\nd.vishnu"""
q23 = """who was the wife of Dhritarashtra?
a.Sita\nb.Gandhari\nc.Satarupa\d.Kunti"""
q24 = """who is the writer of Ramayana?
a.valmiki\nb.ved vyas\nc.Shri krishna\nd.Rama"""
q25 = """what was the true name of Bhishma?
a.Karna\nb.Arjuna\nc.Devabrata\nd.Pallove"""
questions = {q1:"c",q2:"c",q3:"c",q4:"d",q5:"c",q6:"c",q7:"a",q8:"c",q9:"d",q10:"b",q11:"b",q12:"c",q13:"d",q14:"a",q15:"b",q16:"c",q17:"d",q18:"b",q19:"d",q20:"a",q21:"b",q22:"d",q23:"b",q24:"a",q25:"c"} # Question-Answ,er dictionary

score = 0
#a = input("How many questions would you like?: ")
rand_ques = random.sample(list(questions),5) # To randomly select 5 questions

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

if score >= 3:
    #print("You get a bonus question!")
    response = input("Would you like a bonus question?: ")
    if response == 


