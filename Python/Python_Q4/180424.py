##iterable = ["Apple", "Banana", "Coconut"]
##
##for var_name in iterable: ## "var_name" can be anything you want
##    print(var_name) ## "var_name" represents "each item" in the iterable"
##print("End of program")
##
##
##
##fruits = ["Apple", "Banana", "Coconut", "Durian"]
##
##for i in range(4): ## Here, i is an integer from 0 to 3
##    print("i = " + str(i))
##    print(fruits[i])
##
##
##
##fruits = ["Apple", "Banana", "Coconut", "Durian"]
##s = ""
##for i in range(4):
##    if i == 3: ## The biggest index in fruits is 3
##        # ATTACH and TO s
##        # A, B, C, and D
##        s = s + ", and " + fruits[i]
##    elif i == 0:
##        # ATTACH fruits[i] TO s
##        s = s + fruits[i]
##    else:
##        # ATTACH ", " + fruits[i] TO s
##        s = s + ", " + fruits[i]
##print(s)
##
##
##
##fruits = ["Apple", "Banana", "Coconut", "Durian"]
##fruits.append("Orange")
##fruits.append("Mango")
##fruits.append("Watermelon")
##s = ""
##for i in range(len(fruits)):
##    if i == (len(fruits)-1): ## The biggest index in fruits is 3
##        # ATTACH and TO s
##        # A, B, C, and D
##        s = s + ", and " + fruits[i]
##    elif i == 0:
##        # ATTACH fruits[i] TO s
##        s = s + fruits[i]
##    else:
##        # ATTACH ", " + fruits[i] TO s
##        s = s + ", " + fruits[i]
##print(s)
##
##
##
##grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]
##gradesThreshold = [97, 93, 90, 87, 83, 80, 77, 73, 70, 67, 63, 60, 0]
##
##for i in range(len(grades)):
##    print("If you have " + str(gradesThreshold[i] + " or higher , you have a(n) " + grades[i]))
##
##
##
##print("Type in your grade: ")
##userInput = int(input())
##grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]
##gradesThreshold = [97, 93, 90, 87, 83, 80, 77, 73, 70, 67, 63, 60, 0]
##gradesIndex = 0
##
##for i in range(len(grades)): # i is 0 to 12
##    if userInput < gradesThreshold[i]:
##        gradesIndex = gradesIndex + 1
##
##print("You have a(n) " + grades[gradesIndex])

print("Type in your grade: ")
Input = int(input())
grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]
scores = [97, 93, 90, 87, 83, 80, 77, 73, 70, 67, 63, 60, 0]
i = 0
for a in range(len(grades)):
    if Input < scores[i]:
        i = i + 1
    else:
        break
print("You have a(n) " + grades[i])

##fruits = ["Apple", "Banana", "Coconut", "Durian"]
##s = ""
##for i in range(len(fruits)):
##    if i == 0:
##        s = s + fruits[i]
##    elif i == (len(fruits) - 1):
##        s = s + ", and " + fruits[len(fruits) - 1]
##    else:
##        s = s + ", " + fruits[i]
##print(s)
