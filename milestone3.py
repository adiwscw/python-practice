questions = ("What is 2 + 2:",
             "What is 4 x 4:",
             "What is 17 / 5:",
             "What is 5 x 19:")

choices = (("A) 9", "B) 5", "C) 4", "D) 10"),
           ("A) 20", "B) 17", "C) 16", "D) 10"),
           ("A) 3.4", "B) 5.8", "C) 7.9", "D) 10"),
           ("A) 125", "B) 95", "C) 78", "D) 88"))

answers = ("C", "C", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------")
    print(question)
    for choice in choices[question_num]:
        print(choice)


    guess = input("Enter (A, B, C, D) ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("CORRECT")
        score += 1
    elif guess not == "a", 
    else:
        

    question_num += 1 

if question_num > 3:
    print("===========================")
    print("---------------------------")
    print(f"YOUR SCORE IS {score}")
    print("---------------------------")
    print("===========================")
