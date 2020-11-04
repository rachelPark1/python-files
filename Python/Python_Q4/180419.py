##fruits = ["Apple", "Banana", "Coconut", "Durian", "Mango"]
##fruits.append(1)
##fruits.append(1.5)
##fruits.append("Hello")
##
##print(len(fruits))

selfIntro = "Hello my name is Bobby Kim. I will now make a very short introduction of myself. Good Bye"

##print(list(selfIntro))
##print(len(selfIntro))

#print(selfIntro.split(". "))   ##". " --> separating string
listIntro = selfIntro.split(". ")

listIntro.insert(2, "I go to SSI")

newIntro = ". ".join(listIntro) ## ". " is inserted between every single item.
print(newIntro)

fruits = ["Apple", "Banana", "Coconut", "Durian", "Mango"]
vowels = "AEIOUaeiou"

if fruits[0][0] in vowels:
    print("An " + fruits[0])
else:
    print("A " + fruits[0])
if fruits[1][0] in vowels:
    print("An " + fruits[1])
else:
    print("A " + fruits[1])
if fruits[2][0] in vowels:
    print("An " + fruits[2])
else:
    print("A " + fruits[2])
if fruits[3][0] in vowels:
    print("An " + fruits[3])
else:
    print("A " + fruits[3])
if fruits[4][0] in vowels:
    print("An " + fruits[4])
else:
    print("A " + fruits[4])

print("End of Program")

fruits = ["Apple", "Banana", "Coconut", "Durian", "Mango"]
vowels = "AEIOUaeiou"
fruits.append("Orange")
fruits.append("Eggplant")
fruits.append("Watermelon")
fruits.append("Grapes")
fruits.append("Melon")
fruits.append("Lemon")
addedFruits = ["Orange", "Eggplant", "Watermelon", "Grapes", "Melon", "Lemon"]
fruits = fruits + addedFruits
for newFruits in addedFruits:
    fruits.append(newFruits)

for cp in fruits:
    if cp[0] in vowels:
        print("An " + cp)
    else:
        print("A " + cp)

print("End of Program")
