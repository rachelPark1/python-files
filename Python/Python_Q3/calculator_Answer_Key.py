print("Welcome to the calculator program!")
print("Which mathematical operation would you like to perform?")
print("Your choices are: addition, subtraction, multiplication, division, power, remainder, and quotient")
operation = input()

if operation == "addition": # did user type in addition?
    print("You want me to add two numbers")
    print("Please input the first number")
    num1_str = input()
    print("Please input the second number")
    num2_str = input()
    num1_int = int(num1_str) # change it to a number we can manipulate
                             # but still leave the string so we can print easily
                             # with sentences
    num2_int = int(num2_str)
    answer_int = num1_int + num2_int # this line does the actual math the lines
                                     # before were just data type manipulation
                                     # so we could use this line easily
    answer_str = str(answer_int)
    print("Good job!")
    print(num1_str + " plus " + num2_str + " equals " + answer_str)
    # At this point, I can copy and paste this if block and change to elif.
    # The data type manipulation section is all the same and I just need to change
    # the answer_int = num1_int + num2_int line
    # along with some grammar.
elif operation == "subtraction": # otherwise, did user type in subtraction?
    print("You want me to subtract two numbers!")
    print("Please input the first number")
    num1_str = input()
    print("Please input the second number")
    num2_str = input()
    num1_int = int(num1_str)
    num2_int = int(num2_str)
    answer_int = num1_int - num2_int
    answer_str = str(answer_int)
    print("Good job!")
    print(num1_str + " minus " + num2_str + " equals " + answer_str)
elif operation == "multiplication": # otherwise, did user type in multiplication?
    print("You want me to multiply two numbers!")
    print("Please input the first number")
    num1_str = input()
    print("Please input the second number")
    num2_str = input()
    num1_int = int(num1_str)
    num2_int = int(num2_str)
    answer_int = num1_int * num2_int
    answer_str = str(answer_int)
    print("Good job!")
    print(num1_str + " times " + num2_str + " equals " + answer_str)
elif operation == "division": # otherwise, did user type in division?
    print("You want me to divide one number by another!")
    print("Please input the numerator")
    num1_str = input()
    print("Please input the denominator")
    num2_str = input()
    num1_int = int(num1_str)
    num2_int = int(num2_str)
    answer_int = num1_int / num2_int
    answer_str = str(answer_int)
    print("Good job!")
    print(num1_str + " divided by " + num2_str + " equals " + answer_str)
elif operation == "power": # otherwise, did user type in power?
    print("You want me to get the result of the power of one number to the other!")
    print("Please input the base")
    num1_str = input()
    print("Please input the exponent")
    num2_str = input()
    num1_int = int(num1_str)
    num2_int = int(num2_str)
    answer_int = num1_int ** num2_int
    answer_str = str(answer_int)
    print("Good job!")
    print(num1_str + " to the power of " + num2_str + " equals " + answer_str)
elif operation == "remainder": # otherwise, did user type in remainder?
    print("You want me to divide two numbers and return the remainder!")
    print("Please input the numerator")
    num1_str = input()
    print("Please input the denominator")
    num2_str = input()
    num1_int = int(num1_str)
    num2_int = int(num2_str)
    answer_int = num1_int % num2_int
    answer_str = str(answer_int)
    print("Good job!")
    print(num1_str + " divided by " + num2_str + " has a remainder of " + answer_str)
elif operation == "quotient": # otherwise, did user type in quotient?
    print("You want me to divide two numbers and return the quotient!")
    print("Please input the numerator")
    num1_str = input()
    print("Please input the denominator")
    num2_str = input()
    num1_int = int(num1_str)
    num2_int = int(num2_str)
    answer_int = num1_int // num2_int
    answer_str = str(answer_int)
    print("Good job!")
    print(num1_str + " divided by " + num2_str + " has a quotient of " + answer_str)
else: # if none of the above conditions were met, it means the user did not type any of the seven optionss
    print("I'm sorry, I don't recognize that operation.")
print("Thank you for using the calculator program!")
print("End of program")
