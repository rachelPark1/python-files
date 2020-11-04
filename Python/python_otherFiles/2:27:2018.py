## This program will ask the user to input a name
## If the name is "Mary", then the program will ask
## for a password.
## If the password is correct, then it will allow access
## to the computer.
## If the user is not "Mary", it will say that user
## does not exist.

print("Hello! What is your name?")
name = input()
password = "swordfish"

if name == "Mary":
    print("What is the password?")
    userInput = input()
    if userInput == password:
        print("Access granted.")
        print("Welcome, Mary.")
    else:
        print("That password is incorrect.")
        print("Intruder alert.")
        print("SECURITY!!!!")
    print("Example")
else:
    print(name + " is not a user in this computer.")

print("End of Program")
