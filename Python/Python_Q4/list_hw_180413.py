fruits1 = [] #1
fruits1.append("Apple") #2
fruits1.append("Banana")
fruits1.append("Coconut")
fruits1.append("Durian")
fruits1.append("Mango")
fruits1.insert(4, "Grape") #3
print(fruits1[2:5]) #4
del fruits1[2] #5
fruits1.append("Coconut") #6
del fruits1[3] ##Grape  #7

print("Apple is in the list: " + str("Apple" in fruits1)) #8
print("Banana is in the list: " + str("Banana" in fruits1))     #"Banana in fruits1" is a boolean, not a string. So, you should put str()
print("Coconut is in the list: " + str("Coconut" in fruits1))
print("Durian is in the list: " + str("Durian" in fruits1))
print("Grape is in the list: " + str("Grape" in fruits1))
print("Mango is in the list: " + str("Mango" in fruits1))


##if "Apple" in fruits1:
##    print("Apple is in the list: " + "True")
##else:
##    print("Apple is in the list: " + "False")
##if "Banana" in fruits1:
##    print("Banana is in the list: " + "True")
##else:
##    print("Banana is in the list: " + "False")
##if "Coconut" in fruits1:
##    print("Coconut is in the list: " + "True")
##else:
##    print("Coconut is in the list: " + "False")
##if "Durian" in fruits1:
##    print("Durian is in the list: " + "True")
##else:
##    print("Durian is in the list: " + "False")
##if "Grape" in fruits1:
##    print("Grape is in the list: " + "True")
##else:
##    print("Grape is in the list: " + "False")
##
##if "Mango" in fruits1:
##    print("Mango is in the list: " + "True")
##else:
##    print("Mango is in the list: " + "False")
dislikes = ["Asparagus", "Broccoli", "Cucumber", "Eggplant", "Ginger", "Leek"] #9
final = fruits1 + dislikes #10
print(final) #11
