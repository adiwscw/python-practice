start_or_no = input("Hello, welcome to this quiz. Do you wish to play? y or n: ").lower()
points = 0
if start_or_no == "n":
    exit
elif start_or_no == "y":
    question_1 = input("What is 2+2: ")
    if question_1 == 4:
      points += 1
      question_2 = input("What is 4 x 4: ")
    elif question_2 == 16:
      
else:
    print("Invalid Text")