print("Welcom to the divisible program!")
print("Type in a whole number: ")
first = input()
if float(first) / int(float(first)) != 1.0:
    print("=====================================")
    print("I'm sorry, but " + first + " is not a whole number.")
elif float(first) / int(float(first)) == 1.0:
    print("Type in a whole number: ")
    second = input()
    if float(second) / int(float(second)) != 1.0:
        print("=====================================")
        print("I'm sorry, but " + second + " is not a whole number.")
    elif float(second) / int(float(second)) == 1.0:
        print("Type in a whole number: ")
        third = input()
        if float(third) / int(float(third)) != 1.0:
            print("=====================================")
            print("I'm sorry, but " + third + " is not a whole number.")
        else:
            print("Thank you")
            print("=====================================")
            if float(first) % 2 == 0.0:
                print(first + " is an even number.")
            else:
                print(first + " is an odd number.")
            if float(second) % 2 == 0.0:
                print(second + " is an even number.")
            else:
                print(second + " is an odd number.")
            if float(third) % 2 == 0.0:
                print(third + " is an even number.")
            else:
                print(third + " is an odd number.")
            print("=====================================")
            combined = first + second + third
            print(first + second + third + " combined maked " + combined + ".")
            if float(combined) % 3 == 0.0:
                print(combined + " is divisible by 3.")
            else:
                print(combined + " is not divisible by 3.")
            if float(combined) % 4 == 0.0:
                print(combined + " is divisible by 4.")
            else:
                print(combined + " is not divisible by 4.")
            if float(combined) % 5 == 0.0:
                print(combined + " is divisible by 5.")
            else:
                print(combined + " is not divisible by 5.")
            if float(combined) % 7 == 0.0:
                print(combined + " is divisible by 7.")
            else:
                print(combined + " is not divisible by 7.")
print("=====================================")
print("That is all for now. Have a nice day!\nEnd of program")
