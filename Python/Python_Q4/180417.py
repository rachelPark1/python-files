fruits = ["Apple", "Banana", "Coconut", "Durian", "Mango"]

if "Apple" in fruits:
    print("Apple is in the list: " + "True")
else:
    print("Apple is in the list: " + "False")
if "Dragon" in fruits:
    print("Dragon is in the list: " + "True")
else:
    print("Dragon is in the list: " + "False")

appleInFruits = "Apple" in fruits
print("Apple is in the list: " + str(appleInFruits))
dragonInFruits = "Dragon" in fruits
print("Dragon is in the list: " + str(dragonInFruits))

print("Apple is in the list: " + str("Apple" in fruits))
print("Dragon is in the list: " + str("Dragon" in fruits))

fruits = ["Apple", "Banana", "Coconut", "Durian", "Mango"]
lenFruits = len(fruits)
print("lenFruits has " + str(lenFruits) + " items in it.")
fruits.append(1)
fruits.append(1.5)
fruits.append(True)
fruits.append("Haha")
fruits.append("Yay")
fruits.append(2)
fruits.append(3.982)
fruits.append(False)
fruits.append("Matthew")
fruits.append("Computers")
fruits.append(3)
fruits.append(5.8729)
fruits.append(True)
fruits.append("Glasses")
fruits.append("Uniform")
lenFruits = len(fruits)
print("lenFruits has " + str(lenFruits) + " items in it.")



selfIntro = "Hello my name is Bobby Kim. I am from South Korea. My favorite suject is Computer Science. He is very nice. Wink Wink"
lenIntro = len(selfIntro)
print("lenIntro has " + str(lenIntro) + " characters in it.")



hello = "Hello World"
hList = list(hello)
print(hello)
print(hList)
del hList[5]
print(hList)
hello2 = str(hList) + "This is proof that hello2 is a string."
hello2 = str(hList)
hello2Len = len(hello2)
print("hello2 has " + str(hello2Len) + " items in it.")
hello2 = "".join(hList)
print(hello2)
hello3 = " ".join(hList)
print(hello3)
hello4 = "XXXXX".join(hList)
print(hello4)



selfIntro = "Hello my name is Bobby Kim. I am from South Korea. I go to a school called Seoul Scholar International. We are an awesome school. My favorite teacher is the Computer Science teacher. He is very nice. Wink Wink"
listIntro = selfIntro.split()
##print(selfIntro)
print(listIntro)
##listIntro = selfIntro.split(" ")
##print(listIntro)
listIntro = selfIntro.split(". ")
print(listIntro)
