def count_duplicates(strAlpha):
    # This function takes in strAlpha which is made of lowercase alphabets and
    #numberic digits.
    #1) Cast the strAlpha into a new list and assign it
    listAlpha = list(strAlpha) # e.g. listAlpha is ['a', 'a', 'b', 'b']
    #2) Make a new empty list that can be appended when any characters are
    #reapeated
    dupChar = []
    #3) Loop until the iNum is the last index of the listAlpha
    for iNum in range(len(listAlpha)): # iNum is 0, 1, 2, 3
        #print("iNum: " + str(iNum))
        newListAlpha = listAlpha[0 : iNum] + listAlpha[(iNum + 1) : (len(listAlpha) + 1)]
        #print("newListAlpha: " + str(newListAlpha))
        if listAlpha[iNum] in newListAlpha:
            # As long as there is the same character as the listAlpha[iNum]
            #remove listAlpha[iNum] from the listAlpha
            if not (listAlpha[iNum] in dupChar):
                dupChar.append(listAlpha[iNum])
                #print("dupChar: " + str(dupChar))
                newListAlpha.remove(listAlpha[iNum])
        #print("dupChar: " + str(dupChar) + "\n")
    return len(dupChar)
        
    
p = count_duplicates("investigate")
print(p)
