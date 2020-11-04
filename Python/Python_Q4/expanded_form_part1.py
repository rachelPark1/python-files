def expanded_form_whole(wholeNum):
    # This function takes in an integer number bigger than 0
    # Make an empty list so that I can append expanded form of number
    ans = []
    listNum = list(str(wholeNum))
    # Loop as the same number as the number of characters in the wholeNum
    for i in range(len(listNum)):
        # i is 0, 1, 2, 3, 4, 5
        # Unless listNum[i] is 0, append expanded form number to ans
        if int(listNum[i]) != 0:
            # Add 0 (len(listNum) - i - 1) times to listNum[i]
            ans.append(str(listNum[i]) + "0" * (len(listNum) - i - 1))
        #print("ans: " + str(ans) + "\n")
    finalAns = " + ".join(ans)
    return finalAns
    

m = expanded_form_whole(703040)
print(m)
