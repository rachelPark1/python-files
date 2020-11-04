def highest(string):
    # This function takes in a string of words.
    # Each alphabet has a point e.g. a = 1, b = 2, c = 3, d = 4
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alpChar = [] # contain alphabets
    alpPoint = [] # contain point of each alphabet
    i = 1
    for char in alphabet:
        # char is 'a',  'b', 'c', etc.
        alpChar.append(char)
        alpPoint.append(i)
        i = i + 1
##    print("alpChar: " + str(alpChar) + "\n")
##    print("alpPoint: " + str(alpPoint) + "\n")
    listStr = string.split(" ") # listStr is a list --> ['man', 'i', 'need', ...]
##    print("listStr: " + str(listStr) + "\n")
    #pointEach = 1
    pStore = []
    for iNum in range(len(listStr)):
##        print("iNum: " + str(iNum)) # iNum is 0, 1, 2, ..., 7
        word = listStr[iNum]
        # word is 'man', 'i', 'need', ... etc.
##        print("word: " + word)
        pointEach = 1
##        for num in range(len(alpChar)):
##            # num is 0, 1, 2, 3, ..., 25
##            i = 0
##            if word[i] == alpChar[num]:
##                print("alpPoint[num]: " + str(alpPoint[num]))
##                pointEach = pointEach * alpPoint[i]
##                i = i + 1
        for num in range(len(word)):
            # num is 0, 1, 2
            i = 0
            while i <=25:
                if word[num] == alpChar[i]:
                    pointEach = pointEach * alpPoint[i]
                i = i + 1
                
##        print("pointEach: " + str(pointEach))
        pStore.append(pointEach)
        print("pStore: " + str(pStore) + "\n")
    while True:
        
    
x = highest("take me to semynak")
print(x)
