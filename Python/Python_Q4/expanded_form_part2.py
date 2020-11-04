
def expanded_form_whole_list(wholeNum):
    # This function takes in an integer number bigger than 0
    # Make an empty list so that I can append expanded form of number
    ans1 = []
    listNum = list(str(wholeNum))
    #print("listNum: " + str(listNum))
    # Loop as the same number as the number of characters in the wholeNum
    for i in range(len(listNum)):
        # i is 0, 1, 2, 3
        # Unless listNum[i] is 0, append expanded form number to ans
        #listNum[i]: 7, 0, 9, 0
        #print("listNum[i]: " + str(listNum[i]))
        # Unless listNum[i] is 0, append expanded form number to ans
        if int(listNum[i]) != 0:
            # Add 0 (len(listNum) - i - 1) times to listNum[i]
            ans1.append(str(listNum[i]) + "0" * (len(listNum) - i - 1))
        #print("ans: " + str(ans) + "\n")
    return ans1

def expanded_form(dec):
    # This function takes in decimal
    # Make an empty list so that I can append expanded form of number
    ans = []
    listDec= list(str(dec))
    #print(listDec)
    #print("listDec: " + str(listDec))
    # Make a loop that finds where is a decimal point
    for i in range(len(listDec)):
        # i is 0, 1, 2, 3
        if listDec[i] == ".":
            listNum = listDec[0 : i]
            #print("listNum: " + str(listNum))
            listDec = listDec[(i + 1) : len(listDec)]
            #print("listDec: " + str(listDec))
            wholeNum = "".join(listNum)
            #print("wholeNum: " + str(wholeNum) + "\n")
            break
    # Make a loop that append expanded form of number
    for i in range(len(listDec)):
        # i is 0, 1
        #print("listDec: " + str(listDec))
        if int(listDec[i]) != 0:
            ans.append(str(listDec[i]) + "/1" + "0" * (i + 1))
        #print("ans: " + str(ans) + "\n")
    #print(str(expanded_form_whole_list(wholeNum)) + "\n")
    ans = expanded_form_whole_list(wholeNum) + ans
    ans = " + ".join(ans)
    return ans

k = expanded_form(01.03040)
print(k)
