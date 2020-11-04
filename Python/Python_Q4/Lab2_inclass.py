def findNumberWord(wList, n):
    # Takes in a list of words, and a number
    # Finds the word w/ the number inside it
    # Returns that word
    for word in wList: # word represents each word in
    #wList
        # Ask the question, is str(n) in word?
        if str(n) in word:
            # If it is, return that word
            return word
        

def sortString(s):
    # Takes a string and reorders the words in the string
    # according to the Arabic numbers attached to each word
    # returns the reordered string
    # s: the string passed into this function

    #1) Divide the string into a list of words
    wordsList = s.split()

    #2) Create a new empty list, call newList
    newList = []

    #3) Loop as many times as there are items in the list
    #-> Loop w/ somethinglike for i in range(len(listWords))
    #-> then check if i + 1 is in the word
    for i in range(len(wordsList)): # i stands for the current
        # nubmer we're searching for
        #4) Find the word w/ 1 in it (i + 1)
        curWord = findNumberWord(wordsList, i + 1)
        ##print(curWord)
        #After find the word w/ a 1,
        #Append it to a the new list
        newList.append(curWord)
        #5) Find the word w/ 2 in it, etc.
    ##print(newList)
    #6) After getting the new list, joing all the words
    #back together as a sentence
    newSent = " ".join(newList)
    #7) Return that new sentence
    return newSent

    

#Example Strings
a = sortString("So4uth 5Korea wor2ld fro3m hel1lo")
print(a)
["So4uth", "5Korea", "wor2ld", "fro3m", "hel1lo"]
