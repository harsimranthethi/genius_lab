import random
q1 = """The place of origin of an earthquake is called:
a.Epicentre\nb.Seismal\nc.Focus\nd.Amphidromic Point"""
q2 = """The capital of Columbia is:
a.Bogota\nb.Olympus\nc.Rome\nd.Jakarta"""
q3 = """The busiest  sea route is:
a.The Mediterranean Red-Sea Route\nb.The South Atlantic Route\nc.The North Atlantic Route\nd.The Pacific Route"""

questions = {q1:"c",q2:"a",q3:"c"} # Question-Answer dictionary

score = 0
rand_ques = random.sample(list(questions),2) # To randomly select 2 questions
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
print("Final score is:",score)

