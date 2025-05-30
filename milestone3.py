questions = ("When was Red Dead Redemption 2 released?",
             "When was the first God Of War game released?",
             "How many games are in the God Of War franchise?",
             "Is Marvel Rivals overrated?")

choices = (("A) 2018", "B) 2019", "C) 2017", "D) 2020"), 
           ("A) 2008", "B) 2001", "C) 2005", "D) 2002"), 
           ("A) 11", "B) 10", "C) 9", "D) 7"), 
           ("A) No", "B) Hell no", "C) Absolutely not", "D) Yes")) 

answers = ("A", "C", "B", "D")
score = 0
question_num = 0

for question in questions:
    print("------------------")
    print(question)
    for choice in choices[question_num]:
        print(choice)


    guess = input("Enter (A, B, C, D) ").upper()

    if guess == answers[question_num]:
        print("CORRECT")
        score += 1
    else:
        print("INCORRECT")
        print("------------------")
        print(f"THE CORRECT ANSWER WAS {answers[question_num]}")

    question_num += 1 

if question_num > 3:
    print("===========================")
    print("---------------------------")
    print(f"YOUR SCORE IS {score}/{question_num}")
    print("---------------------------")
    print("===========================")
