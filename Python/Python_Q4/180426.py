##for i in range(6):  ## i represent each item in range(6).
##    print(i)
##print("End of program")



fruits = ["Apple", "Banana", "Coconut", "Durian"]
fruits.append("Mango")
fruits.append("Melon")
fruits.append("Watermelon")
##s = ""
##
##for i in range(len(fruits)): ## 4 --> how many times do you want to loop
##    if i == (len(fruits) - 1):
##        s = s + ", and " + fruits[i]
##    elif i == 0:
##        s = s + fruits[i]
##    else:
##        s = s + ", " + fruits[i]
##print(s)
##print("End of program")

## control + c

##i = 0
##
##while i < (len(fruits)):
##    print(fruits[i])
##    i = i + 1
##print("End of program")

userInput = ""
password = "CS is my favorite class."

while userInput != password: # same as not (userInput == password)
    print("Please type in the password.")
    userInput = input()
    if userInput == password:
        print("That is the corrct password.")
    else:
        print("That is incorrect. Try again.")

print("Rest of program starts here.")
