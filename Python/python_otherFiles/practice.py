choice = input()
if choice == "addition":  ## !!!!!!!!!!!It must be a string since chocie, which is input, is always a string
    print("Type in the first number")
    num1 = input()
    print("Type in the second number")
    num2 = input()
    answer = float(num1) + float(num2)
    print(num1 + " plus " + num2 + " equals to " + str(answer))
elif choice == "subtraction":
    print("Type in the first number")
    num1 = input()
    print("Type in the second number")
    num2 = input()
    answer = float(num1) - float(num2)
    print(num1 + " minus " + num2 + " equals to " + str(answer))
elif choice == "multiplication":
    print("Type in the first number")
    num1 = input()
    print("Type in the second number")
    num2 = input()
    answer = float(num1) * float(num2)
    print(num1 + " times " + num2 + " equals to " + str(answer))
elif choice == "division":
    print("Type in the numerator number")
    num1 = input()
    print("Type in the denominator number")
    num2 = input()
    answer = float(num1) / float(num2)
    print(num1 + " divided by " + num2 + " equals to " + str(answer))
elif choice == "power":
    print("Type in the base")
    num1 = input()
    print("Type in the exponent")
    num2 = input()
    answer = float(num1) ** float(num2)
    print(num1 + " power of " + num2 + " equals to " + str(answer))
elif choice == "remainder":
    print("Type in the numerator number")
    num1 = input()
    print("Type in the denominator number")
    num2 = input()
    answer = float(num1) % float(num2)
    print(num1 + " divided by " + num2 + " has a remainder of " + str(answer))
elif choice == "quotient":
    print("Type in the numerator number")
    num1 = input()
    print("Type in the denominator number")
    num2 = input()
    answer = float(num1) // float(num2)
    print(num1 + " divided by " + num2 + " has a quotient of " + str(answer))
else:
    print("I'm sorry, I don't recognize that operation.")
print("Thank you\nEnd of program")



