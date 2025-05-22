#Asking for numbers and operators
num_1 = int(input("What is your first number? "))
op = input("What operator do you want to use +, -, *, /, **? ")
num_2 = int(input("What is your second number? "))

#Checking the operators
if op == "+":
    print("Your answer is {}".format(num_1 + num_2))
elif op == "-":
    print("Your answer is {}".format(num_1 - num_2))
elif op == "*":
    print("Your answer is {}".format(num_1 * num_2))
elif op == "/":
    print("Your answer is {}".format(num_1 / num_2))
elif op == "**":
    print("Your answer is {}".format(num_1 ** num_2))
else:
    print("Invalid Operator")