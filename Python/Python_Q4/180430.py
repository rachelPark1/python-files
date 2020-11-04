##fruits = ["Apple", "Banana", "Coconut", "Durian"]
##i = 0
##while i < len(fruits):
##    #looping code
##    print(fruits[i])
##    i = i + 1
##print("End of program")

##fruits = []
##
##while True:
##    print("Do you want to add a fruit to the basket? (y/n)")
##    cont = input()
##    if cont in "Nn":    ## "" in "Nn" --> always true
##        #leave the loop
##        break ## BREAK!!!!!!!!!!!!
##    print("What fruit would you like to add?")
##    newFruit = input()
##    fruits.append(newFruit)

##print(fruits)
##print("End of program")

def printFruitsF():
    ## This fuction takes the list of fruits
    ## and puts a ', ' between each item.
    ## It will attach ', and ' before the last item.
    ## ie. ['A', 'B', 'C'] --> 'A, B,and C'
    s = ""
    for i in range(len(fruits)):  ## range(3) => 0, 1, 2 (not 3)
        if i == 0:
            s = s + fruits[i]
        elif i == (len(fruits) - 1):
            s = s + ", and " + fruits[i]
        else:
            s = s + ", " + fruits[i]
    print(s)

def printFruitsW():
    s = ""
    i = 0
    while i < len(fruits):  ## range(3) => 0, 1, 2 (not 3)
        if i == 0:
            s = s + fruits[i]
        elif i == (len(fruits) - 1):
            s = s + ", and " + fruits[i]
        else:
            s = s + ", " + fruits[i]
        i = i + 1
    print(s)

##printFruitsF()
##printFruitsW()

fruits = []

while True:
    print("Do you want to add a fruit to the basket? (y/n)")
    cont = input()
    if cont in "Nn":    ## "" in "Nn" --> always true
        #leave the loop
        break ## BREAK!!!!!!!!!!!!
    print("What fruit would you like to add?")
    newFruit = input()
    fruits.append(newFruit)
    print("Do you want to see your fruits basket? (y/n)")
    ch = input()
    if ch in "Yy":
        #Option A
        printFruitsF()
        #Option B
##        s = ""
##        for i in range(len(fruits)):  ## range(3) => 0, 1, 2 (not 3)
##            if i == 0:
##                s = s + fruits[i]
##            elif i == (len(fruits) - 1):
##                s = s + ", and " + fruits[i]
##            else:
##                s = s + ", " + fruits[i]
        print(s)
